#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
if '.' not in sys.path:
    sys.path.append('.')
from swordfish_api import strategy_engine
from swordfish_api.client_api import CLIENT_API_NOTIFY_LEVEL_GENERAL, ClientApiMsgTypeT
from swordfish_api.mds_struct import eMdsMsgTypeT, eMdsExchangeIdT
from swordfish_api.oes_struct import eOesMarketIdT, eOesBuySellTypeT, eOesMsgTypeT


MSG_TYPE_L1_SNAPSHOT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                       eMdsMsgTypeT.MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH.value
MSG_TYPE_L2_SNAPSHOT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                       eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT.value
MSG_TYPE_ORDER_INSERT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                        eOesMsgTypeT.OESMSG_RPT_ORDER_INSERT.value


class P(object):
    msg_count = 0


def handle(msg):
    msg_id = msg.msg_head.msg_id
    if msg_id == MSG_TYPE_L1_SNAPSHOT or msg_id == MSG_TYPE_L2_SNAPSHOT:
        P.msg_count += 1
        if P.msg_count > 10000:
            rc = strategy_engine.quit()
            print(f"发送策略主动退出消息, 设置退出标志且返回-1 rc: {rc}")
            return -1
        data = msg.msg_body.mkt_data_snapshot
        if P.msg_count % 50 == 0:
            if data.head.exchId == eMdsExchangeIdT.MDS_EXCH_SSE.value:
                mkt_id = eOesMarketIdT.OES_MKT_SH_ASHARE.value
            else:
                mkt_id = eOesMarketIdT.OES_MKT_SZ_ASHARE.value
            rc = strategy_engine.send_order(data.union.stock.SecurityID.decode(), mkt_id,
                                            eOesBuySellTypeT.OES_BS_TYPE_BUY.value, 100,
                                            data.union.stock.TradePx)
            print(f"发送委托信息 rc: {rc}")
    elif msg_id == MSG_TYPE_ORDER_INSERT:
        strategy_engine.send_notify_msg(f"{strategy_engine.Engine.strategy_name} 收到交易数据", CLIENT_API_NOTIFY_LEVEL_GENERAL)
    return 0


def main():
    strategy_engine.init(handle)
    strategy_engine.do()


if __name__ == '__main__':
    main()

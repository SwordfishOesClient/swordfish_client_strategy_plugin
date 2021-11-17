#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
if '.' not in sys.path:
    sys.path.append('.')
from ctypes import cast, POINTER
from swordfish_api import strategy_engine
from swordfish_api.client_api import CLIENT_API_NOTIFY_LEVEL_GENERAL
from swordfish_api.mds_struct import eMdsMsgTypeT, eMdsExchangeIdT, MdsMktDataSnapshotT
from swordfish_api.oes_struct import eOesMarketIdT, eOesBuySellTypeT, eOesMsgTypeT


class P(object):
    md_msg_count = 0


def handle_md(msg_head, msg_item, callback_params):
    P.md_msg_count += 1
    if P.md_msg_count > 100000:
        rc = strategy_engine.quit()
        print(f"发送策略主动退出消息, 设置退出标志且返回-1 rc: {rc}")
        return -1
    else:
        msg_id = msg_head.contents.msg_id
        if msg_id == eMdsMsgTypeT.MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH.value or \
                msg_id == eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT.value:

            data = cast(msg_item, POINTER(MdsMktDataSnapshotT))[0]
            if 0 == (P.md_msg_count % 50):
                if data.head.exchId == eMdsExchangeIdT.MDS_EXCH_SSE.value:
                    mkt_id = eOesMarketIdT.OES_MKT_SH_ASHARE.value
                else:
                    mkt_id = eOesMarketIdT.OES_MKT_SZ_ASHARE.value
                rc = strategy_engine.send_order(data.union.stock.SecurityID.decode(), mkt_id,
                                                eOesBuySellTypeT.OES_BS_TYPE_BUY.value, 100,
                                                data.union.stock.TradePx)
                print(f"发送委托信息 rc: {rc}")
    return 0


def handle_trd(msg_head, msg_item, callback_params):
    if msg_head.contents.msg_id == eOesMsgTypeT.OESMSG_RPT_ORDER_INSERT.value:
        strategy_engine.send_notify_msg(f"{strategy_engine.Engine.strategy_name} 收到交易数据", CLIENT_API_NOTIFY_LEVEL_GENERAL)
    return 0


def main():
    strategy_engine.init(handle_trd, handle_md)
    strategy_engine.do()


if __name__ == '__main__':
    main()

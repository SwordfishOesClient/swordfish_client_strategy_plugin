#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
if '.' not in sys.path:
    sys.path.append('.')
from swordfish_api import strategy_engine
from swordfish_api.strategy_base import StrategyBase, do
from swordfish_api.client_api import CLIENT_API_NOTIFY_LEVEL_GENERAL
from swordfish_api.mds_struct import eMdsExchangeIdT
from swordfish_api.oes_struct import eOesMarketIdT, eOesBuySellTypeT, eOesOrdTypeT


class MyStrategy(StrategyBase):
    def __init__(self):
        self.msg_count = 0

    def on_snapshot(self, head, body):
        self.msg_count += 1
        if self.msg_count > 10000:
            rc = strategy_engine.quit()
            print(f"发送策略主动退出消息, 设置退出标志且返回-1 rc: {rc}")
            return -1
        if self.msg_count % 50 == 0:
            if head.exchId == eMdsExchangeIdT.MDS_EXCH_SSE.value:
                mkt_id = eOesMarketIdT.OES_MKT_SH_ASHARE.value
            else:
                mkt_id = eOesMarketIdT.OES_MKT_SZ_ASHARE.value
            rc = strategy_engine.send_order(body.SecurityID.decode(), mkt_id,
                                            eOesBuySellTypeT.OES_BS_TYPE_BUY.value,
                                            eOesOrdTypeT.OES_ORD_TYPE_LMT.value, 100,
                                            body.TradePx)
            print(f"发送委托信息 rc: {rc}")

    def on_l1_snapshot(self, head, body):
        print("on_l1_snapshot")
        self.on_snapshot(head, body)

    def on_l2_snapshot(self, head, body):
        print("on_l2_snapshot")
        self.on_snapshot(head, body)

    def on_l2_trade(self, data):
        print("on_l2_trade")

    def on_l2_order(self, data):
        print("on_l2_order")

    def on_business_reject(self, head, body):
        print("on_business_reject")

    def on_order_insert(self, head, body):
        print("on_order_insert")
        strategy_engine.send_notify_msg(f"{strategy_engine.Engine.strategy_name} 收到交易数据",
                                        CLIENT_API_NOTIFY_LEVEL_GENERAL)

    def on_order_report(self, head, body):
        print("on_order_report")

    def on_trade_report(self, head, body):
        print("on_trade_report")

    def on_cash_variation(self, head, body):
        print("on_cash_variation")

    def on_stock_holding_variation(self, head, body):
        print("on_stock_holding_variation")


if __name__ == '__main__':
    do(MyStrategy())

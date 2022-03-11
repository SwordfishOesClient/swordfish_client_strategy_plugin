# -*- coding: utf-8 -*-
import sys
if '.' not in sys.path:
    sys.path.append('.')
from ctypes import Structure, POINTER, cast, byref, c_int32
from . import strategy_engine
from .client_api import ClientApiMsgTypeT
from .mds_struct import eMdsMsgTypeT
from .oes_struct import eOesMsgTypeT


class P(object):
    strategy = None


MSG_TYPE_L1_SNAPSHOT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                       eMdsMsgTypeT.MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH.value
MSG_TYPE_L2_SNAPSHOT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                       eMdsMsgTypeT.MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT.value
MSG_TYPE_L2_TRADE = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                    eMdsMsgTypeT.MDS_MSGTYPE_L2_TRADE.value
MSG_TYPE_L2_ORDER = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
                    eMdsMsgTypeT.MDS_MSGTYPE_L2_ORDER.value
# MSG_TYPE_L2_SSE_ORDER = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_MDS_START.value + \
#                         eMdsMsgTypeT.MDS_MSGTYPE_L2_SSE_ORDER.value
MSG_TYPE_BUSINESS_REJECT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                           eOesMsgTypeT.OESMSG_RPT_BUSINESS_REJECT.value
MSG_TYPE_ORDER_INSERT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                        eOesMsgTypeT.OESMSG_RPT_ORDER_INSERT.value
MSG_TYPE_ORDER_REPORT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                        eOesMsgTypeT.OESMSG_RPT_ORDER_REPORT.value
MSG_TYPE_TRADE_REPORT = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                        eOesMsgTypeT.OESMSG_RPT_TRADE_REPORT.value
MSG_TYPE_CASH_ASSET_VARIATION = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                                eOesMsgTypeT.OESMSG_RPT_CASH_ASSET_VARIATION.value
MSG_TYPE_STOCK_HOLDING_VARIATION = ClientApiMsgTypeT.CLIENT_API_MSG_BASE_COUNTER_START.value + \
                                   eOesMsgTypeT.OESMSG_RPT_STOCK_HOLDING_VARIATION.value
CLIENT_API_MSG_QRY_ASSET = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_ASSET.value
CLIENT_API_MSG_QRY_HOLD = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_HOLD.value
CLIENT_API_MSG_QRY_ORD = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_ORD.value
CLIENT_API_MSG_QRY_TRD = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_TRD.value
CLIENT_API_MSG_QRY_STOCK = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_STOCK.value
CLIENT_API_MSG_QRY_FINISHED = ClientApiMsgTypeT.CLIENT_API_MSG_QRY_FINISHED.value
CLIENT_API_MSG_CLIENT_QUIT = ClientApiMsgTypeT.CLIENT_API_MSG_CLIENT_QUIT.value
CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN = ClientApiMsgTypeT.CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN.value
CLIENT_API_MSG_STRATEGY_EXE_QUITTED = ClientApiMsgTypeT.CLIENT_API_MSG_STRATEGY_EXE_QUITTED.value


def parse_l1_snapshot(msg):
    tmp = msg.msg_body.mkt_data_snapshot
    head = tmp.head
    body = tmp.union.stock
    return head, body


def parse_l2_snapshot(msg):
    tmp = msg.msg_body.mkt_data_snapshot
    head = tmp.head
    body = tmp.union.l2Stock
    return head, body


def parse_l2_trade(msg):
    return msg.msg_body.trade,


def parse_l2_order(msg):
    return msg.msg_body.md_order,


# def parse_l2_sse_order(msg):
#     return msg.msg_body.md_order,


def parse_business_reject(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.ordRejectRsp
    return head, body


def parse_order_insert(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.ordInsertRsp
    return head, body


def parse_order_report(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.ordCnfm
    return head, body


def parse_trade_report(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.trdCnfm
    return head, body


def parse_cash_asset_variation(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.cashAssetRpt
    return head, body


def parse_stock_holding_variation(msg):
    tmp = msg.msg_body.trd_rpt
    head = tmp.rptHead
    body = tmp.rptBody.stkHoldingRpt
    return head, body


def parse_sync_asset(msg):
    return msg.msg_body.cashAssetRsp,


def parse_sync_hold(msg):
    return msg.msg_body.stkHoldingRsp,


def parse_sync_ord(msg):
    return msg.msg_body.ordRsp,


def parse_sync_trd(msg):
    return msg.msg_body.trdRsp,


def parse_sync_stock(msg):
    return msg.msg_body.stockRsp,


FUNC_MAP = {
    MSG_TYPE_L1_SNAPSHOT: ('on_l1_snapshot', parse_l1_snapshot),
    MSG_TYPE_L2_SNAPSHOT: ('on_l2_snapshot', parse_l2_snapshot),
    MSG_TYPE_L2_TRADE: ('on_l2_trade', parse_l2_trade),
    MSG_TYPE_L2_ORDER: ('on_l2_order', parse_l2_order),
    MSG_TYPE_BUSINESS_REJECT: ('on_business_reject', parse_business_reject),
    MSG_TYPE_ORDER_INSERT: ('on_order_insert', parse_order_insert),
    MSG_TYPE_ORDER_REPORT: ('on_order_report', parse_order_report),
    MSG_TYPE_TRADE_REPORT: ('on_trade_report', parse_trade_report),
    MSG_TYPE_CASH_ASSET_VARIATION: ('on_cash_variation', parse_cash_asset_variation),
    MSG_TYPE_STOCK_HOLDING_VARIATION: ('on_stock_holding_variation', parse_stock_holding_variation),
    CLIENT_API_MSG_QRY_ASSET: ('on_sync_asset', parse_sync_asset),
    CLIENT_API_MSG_QRY_HOLD: ('on_sync_hold', parse_sync_hold),
    CLIENT_API_MSG_QRY_ORD: ('on_sync_ord', parse_sync_ord),
    CLIENT_API_MSG_QRY_TRD: ('on_sync_trd', parse_sync_trd),
    CLIENT_API_MSG_QRY_STOCK: ('on_sync_stock', parse_sync_stock),
    CLIENT_API_MSG_QRY_FINISHED: ('on_sync_finish', None),
    CLIENT_API_MSG_CLIENT_QUIT: ('on_quit', None),
    CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN: ('on_quit', None),
    CLIENT_API_MSG_STRATEGY_EXE_QUITTED: ('on_quit', None),
}


class StrategyBase(object):

    def on_sync_asset(self, data):
        pass

    def on_sync_hold(self, data):
        pass

    def on_sync_ord(self, data):
        pass

    def on_sync_trd(self, data):
        pass

    def on_sync_stock(self, data):
        pass

    def on_sync_finish(self):
        pass

    def on_l1_snapshot(self, head, body):
        pass

    def on_l2_snapshot(self, head, body):
        pass

    def on_l2_trade(self, data):
        pass

    def on_l2_order(self, data):
        pass

    def on_business_reject(self, head, body):
        pass

    def on_order_insert(self, head, body):
        pass

    def on_order_report(self, head, body):
        pass

    def on_trade_report(self, head, body):
        pass

    def on_cash_variation(self, head, body):
        pass

    def on_stock_holding_variation(self, head, body):
        pass

    def on_quit(self):
        pass


def handle(msg):
    msg_id = msg.msg_head.msg_id
    func = FUNC_MAP.get(msg_id)
    if func is not None:
        func_name, parser = func
        if parser is None:
            getattr(P.strategy, func_name)()
        else:
            getattr(P.strategy, func_name)(*parser(msg))
    return 0


def do(strategy):
    P.strategy = strategy
    strategy_engine.init(handle)
    strategy_engine.do()


class _UserInfo(Structure):
    _fields_ = [
        ('strategy_id', c_int32),
        ('strategy_order_id', c_int32),
    ]


def get_strategy_order_id(userinfo):
    data = cast(byref(userinfo), POINTER(_UserInfo))[0]
    return data.strategy_order_id

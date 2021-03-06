# -*- coding: utf-8 -*-
from enum import Enum
from ctypes import CDLL, CFUNCTYPE, POINTER, byref, Structure, Union
from ctypes import c_bool, c_char, c_char_p, c_uint8, c_int32, c_uint32, c_int64, c_void_p
from .oes_struct import OES_INV_ACCT_ID_MAX_LEN, OES_SECURITY_ID_MAX_LEN
from .oes_struct import OesRptMsgT, OesOrdItemT, OesTrdItemT, OesCashAssetItemT, OesStockItemT, OesStkHoldingItemT
from .mds_struct import MdsMktDataSnapshotT, MdsL2TradeT, MdsL2OrderT


# 日志级别
CLIENT_API_LOG_LEVEL_TRACE = 0
CLIENT_API_LOG_LEVEL_DEBUG = 1
CLIENT_API_LOG_LEVEL_INFO = 2
CLIENT_API_LOG_LEVEL_ERR = 3
CLIENT_API_LOG_LEVEL_CRITICAL = 4
CLIENT_API_LOG_LEVEL_OFF = 5

# 通知消息等级
CLIENT_API_NOTIFY_LEVEL_UNDEFINE = 0   # 未定义
CLIENT_API_NOTIFY_LEVEL_LOW = 1        # 较低
CLIENT_API_NOTIFY_LEVEL_GENERAL = 2    # 一般
CLIENT_API_NOTIFY_LEVEL_IMPORTANT = 3  # 重要
CLIENT_API_NOTIFY_LEVEL_URGENT = 4     # 紧急


# 通信消息的消息类型定义
class ClientApiMsgTypeT(Enum):
    CLIENTMSG_MIN = 0  # 0
    CLIENT_API_MSG_BASE_COUNTER_START = 0x00010000  # 65536
    CLIENT_API_MSG_BASE_COUNTER_END = CLIENT_API_MSG_BASE_COUNTER_START + 0x1000  # 69632
    CLIENT_API_MSG_BASE_MDS_START = CLIENT_API_MSG_BASE_COUNTER_END + 1  # 69633
    CLIENT_API_MSG_BASE_MDS_END = CLIENT_API_MSG_BASE_MDS_START + 0x1000  # 73729
    CLIENT_API_MSG_BASE_COUNTER_FINISHED_START = CLIENT_API_MSG_BASE_MDS_END + 1  # 73730
    CLIENT_API_MSG_BASE_COUNTER_FINISHED_END = CLIENT_API_MSG_BASE_COUNTER_FINISHED_START + 0x1000  # 77826

    CLIENT_API_MSG_BASE_MDS_FINISHED_START = CLIENT_API_MSG_BASE_COUNTER_FINISHED_END + 1  # 77827
    CLIENT_API_MSG_BASE_MDS_FINISHED_END = CLIENT_API_MSG_BASE_MDS_FINISHED_START + 0x1000  # 81923

    CLIENT_API_MSG_MERGE_MAX = CLIENT_API_MSG_BASE_MDS_FINISHED_END + 1  # 81924

    # 添加策略
    CLIENT_API_MSG_STRATEGY_ADD = CLIENT_API_MSG_MERGE_MAX + 1  # 81925
    # 策略心跳
    CLIENT_API_MSG_STRATEGY_EXE_LIVING = CLIENT_API_MSG_STRATEGY_ADD + 1  # 81926
    # 策略被动退出
    CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN = CLIENT_API_MSG_STRATEGY_EXE_LIVING + 1  # 81927
    # 策略主动退出
    CLIENT_API_MSG_STRATEGY_EXE_QUITTED = CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN + 1  # 81928
    # 客户端退出
    CLIENT_API_MSG_CLIENT_QUIT = CLIENT_API_MSG_STRATEGY_EXE_QUITTED + 1  # 81929

    # 策略通知
    CLIENT_API_MSG_STRATEGY_NOTIFY = CLIENT_API_MSG_CLIENT_QUIT + 1  # 81930
    # 策略委托
    CLIENT_API_MSG_STRATEGY_ORDER = CLIENT_API_MSG_STRATEGY_NOTIFY + 1  # 81931

    CLIENT_API_MSG_QRY_ASSET = CLIENT_API_MSG_STRATEGY_ORDER + 1  # 81932
    CLIENT_API_MSG_QRY_HOLD = CLIENT_API_MSG_QRY_ASSET + 1  # 81933
    CLIENT_API_MSG_QRY_ORD = CLIENT_API_MSG_QRY_HOLD + 1  # 81934
    CLIENT_API_MSG_QRY_TRD = CLIENT_API_MSG_QRY_ORD + 1  # 81935
    CLIENT_API_MSG_QRY_STOCK = CLIENT_API_MSG_QRY_TRD + 1  # 81936
    CLIENT_API_MSG_QRY_FINISHED = CLIENT_API_MSG_QRY_STOCK + 1  # 81937

    CLIENT_API_MSG_MAX = CLIENT_API_MSG_QRY_FINISHED + 1  # 81938


CLIENT_STRATEGY_INFO_NAME_MAX_LEN = 64
CLIENT_STRATEGY_INFO_PATH_MAX_LEN = 1024
CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN = 2048


# 消息头
class ClientApiMsgHeadT(Structure):
    _fields_ = [
        ('msg_flag', c_uint8),  # 消息标志
        ('status', c_uint8),  # 状态码
        ('detail_status', c_uint8),  # 明细状态代码
        ('__fillter1', c_uint8),
        ('msg_size', c_uint32),  # 消息大小
        ('msg_id', c_int32),  # 消息代码
        ('msg_seq_num', c_int32),  # 消息序号
    ]


class ClientStrategyInfoItemT(Structure):
    _fields_ = [
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
        ('path', c_char * CLIENT_STRATEGY_INFO_PATH_MAX_LEN),
        ('notifymsg', c_char * CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN),
        ('execSts', c_uint8),
        ('isSelect', c_uint8),
        ('disuse', c_uint8),
        ('__fillter', c_uint8),
        ('timestampId', c_int32),  # 精确到毫秒的时间戳,添加的时候获取,作为主键,用于交易数据匹配
        ('pid', c_int64),
        ('lastLiveTime', c_int64),
    ]


class ClientStrategyLivingItemT(Structure):
    _fields_ = [
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
    ]


class ClientStrategyQuitItemT(Structure):
    _fields_ = [
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
    ]


class ClientStrategyShutdownItemT(Structure):
    _fields_ = [
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
    ]


class ClientStrategyNotifyItemT(Structure):
    _fields_ = [
        ('notify_id', c_int32),
        ('notify_level', c_uint8),
        ('__fillter', c_uint8 * 3),
        ('notify_time', c_int32),
        ('__fillter2', c_uint8 * 4),
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
        ('notify_msg', c_char * CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN),
    ]


class ClientStrategyOrdItemT(Structure):
    _fields_ = [
        ('strategy_ord_id', c_int32),
        ('strategy_timestamp_id', c_int32),
        ('mkt_id', c_uint8),
        ('ord_type', c_uint8),
        ('bs_type', c_uint8),
        ('ord_status', c_uint8),
        ('is_auto_send', c_uint8),
        ('__filler', c_uint8 * 3),
        ('ord_rej_reason', c_int32),
        ('exch_err_code', c_int32),
        ('ord_qty', c_int32),
        ('ord_price', c_int32),
        ('trd_price', c_int32),
        ('__filler2', c_int32),
        ('cnfm_qty', c_int32),
        ('canceled_qty', c_int32),
        ('trd_qty', c_int64),
        ('trd_amt', c_int64),
        ('trd_fee', c_int64),
        ('__ord_timestamp', c_int64),
        ('inv_acct_id', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('security_id', c_char * OES_SECURITY_ID_MAX_LEN),
        ('name', c_char * CLIENT_STRATEGY_INFO_NAME_MAX_LEN),
    ]


# 流消息体完整定义
class ClientApiMsgBodyT(Union):
    _fields_ = [
        # 请求应答流数据
        ('living', ClientStrategyLivingItemT),
        ('quit', ClientStrategyQuitItemT),
        ('shutdown', ClientStrategyShutdownItemT),
        ('notify', ClientStrategyNotifyItemT),
        ('order', ClientStrategyOrdItemT),
        # 交易流数据
        ('trd_rpt', OesRptMsgT),
        # 行情流数据
        ('mkt_data_snapshot', MdsMktDataSnapshotT),
        ('trade', MdsL2TradeT),
        ('md_order', MdsL2OrderT),

        ('ordRsp', OesOrdItemT),  # 查询委托信息应答
        ('trdRsp', OesTrdItemT),  # 查询成交信息应答
        ('cashAssetRsp', OesCashAssetItemT),  # 查询客户资金信息应答
        ('stockRsp', OesStockItemT),  # 查询现货产品信息应答
        ('stkHoldingRsp', OesStkHoldingItemT),  # 查询股票持仓信息应答

        ('_strategyItem', ClientStrategyInfoItemT),
        ('__data', c_char * 1),
    ]


# 流消息完整定义
class ClientApiStreamMsgT(Structure):
    _fields_ = [
        ('msg_head', ClientApiMsgHeadT),
        ('msg_body', ClientApiMsgBodyT),
    ]


class ClientAPI(object):
    def __init__(self, filename):
        self.dll = CDLL(filename)
        self.async_ctx = 0

        self._F_CLIENTAPI_ON_STREAM_MSG_T = CFUNCTYPE(c_int32, POINTER(ClientApiMsgHeadT), c_void_p, c_void_p)

        self._ClientAsyncApi_Init = self.dll.ClientAsyncApi_Init
        self._ClientAsyncApi_Init.restype = c_void_p
        self._ClientAsyncApi_Init.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                                              c_int32, c_int32, c_int32, c_int32, c_int32,
                                              self._F_CLIENTAPI_ON_STREAM_MSG_T,
                                              self._F_CLIENTAPI_ON_STREAM_MSG_T,
                                              c_void_p, c_void_p, c_uint8]

        self._ClientAsyncApi_Run = self.dll.ClientAsyncApi_RunWithOutCallBack
        self._ClientAsyncApi_Run.restype = c_int32
        self._ClientAsyncApi_Run.argtypes = [c_void_p]

        self._ClientAsyncApi_Destory = self.dll.ClientAsyncApi_Destory
        self._ClientAsyncApi_Destory.restype = c_int32
        self._ClientAsyncApi_Destory.argtypes = [c_void_p]

        self._ClientAsyncApi_SendOrderReq = self.dll.ClientAsyncApi_SendOrderReq
        self._ClientAsyncApi_SendOrderReq.restype = c_int32
        self._ClientAsyncApi_SendOrderReq.argtypes = [c_void_p, c_char_p, c_uint8, c_uint8, c_uint8,
                                                      c_int32, c_int32, c_int32, c_uint8]

        self._ClientAsyncApi_SendNotifyMsg = self.dll.ClientAsyncApi_SendNotifyMsg
        self._ClientAsyncApi_SendNotifyMsg.restype = c_int32
        self._ClientAsyncApi_SendNotifyMsg.argtypes = [c_void_p, c_char_p, c_uint8]

        self._ClientAsyncApi_SendQuitedMsg = self.dll.ClientAsyncApi_SendQuitedMsg
        self._ClientAsyncApi_SendQuitedMsg.restype = c_int32
        self._ClientAsyncApi_SendQuitedMsg.argtypes = [c_void_p]

        self._ClientAsyncApi_WaitTrdMsg = self.dll.ClientAsyncApi_WaitTrdMsg
        self._ClientAsyncApi_WaitTrdMsg.restype = c_bool
        self._ClientAsyncApi_WaitTrdMsg.argtypes = [POINTER(ClientApiStreamMsgT), c_int32]

        self._ClientAsyncApi_WaitMdMsg = self.dll.ClientAsyncApi_WaitMdMsg
        self._ClientAsyncApi_WaitMdMsg.restype = c_bool
        self._ClientAsyncApi_WaitMdMsg.argtypes = [POINTER(ClientApiStreamMsgT), c_int32]

        self._ClientAsyncApi_IsOwnedByStrategy = self.dll.ClientAsyncApi_IsOwnedByStrategy
        self._ClientAsyncApi_IsOwnedByStrategy.restype = c_bool
        self._ClientAsyncApi_IsOwnedByStrategy.argtypes = [c_int64, c_int32]

        self._ClientAsyncApi_AddStrategy = self.dll.ClientAsyncApi_AddStrategy
        self._ClientAsyncApi_AddStrategy.restype = c_int32
        self._ClientAsyncApi_AddStrategy.argtypes = [c_void_p]

    def client_async_api_init(self, trd_stream, mkt_stream, req_stream, strategy_name, strategy_path, strategy_id,
                              strategy_ord_id, timeout_ms, heart_bt_int, level=CLIENT_API_LOG_LEVEL_DEBUG):
        self.async_ctx = self._ClientAsyncApi_Init(c_char_p(trd_stream.encode()),
                                                   c_char_p(mkt_stream.encode()),
                                                   c_char_p(req_stream.encode()),
                                                   c_char_p(strategy_name.encode()),
                                                   c_char_p(strategy_path.encode()),
                                                   c_int32(strategy_id),
                                                   c_int32(strategy_ord_id),
                                                   c_int32(timeout_ms),
                                                   c_int32(0),
                                                   c_int32(heart_bt_int),
                                                   self._F_CLIENTAPI_ON_STREAM_MSG_T(0),
                                                   self._F_CLIENTAPI_ON_STREAM_MSG_T(0),
                                                   c_void_p(0),
                                                   c_void_p(0),
                                                   c_uint8(level))
        return self.async_ctx

    def client_async_api_run(self):
        return self._ClientAsyncApi_Run(self.async_ctx)

    def client_async_api_destory(self):
        return self._ClientAsyncApi_Destory(self.async_ctx)

    def client_async_api_send_order_req(self, security_id, mkt_id, bs_type, ord_type,
                                        strategy_ord_id, ord_qty, ord_price, is_auto_send):
        return self._ClientAsyncApi_SendOrderReq(self.async_ctx, c_char_p(security_id.encode()),
                                                 c_uint8(mkt_id), c_uint8(bs_type), c_uint8(ord_type),
                                                 c_int32(strategy_ord_id), c_int32(ord_qty),
                                                 c_int32(ord_price), c_uint8(is_auto_send))

    def client_async_api_send_notify_msg(self, msg, msg_level):
        return self._ClientAsyncApi_SendNotifyMsg(self.async_ctx,
                                                  c_char_p(msg.encode()), c_uint8(msg_level))

    def client_async_api_send_quited_msg(self):
        return self._ClientAsyncApi_SendQuitedMsg(self.async_ctx)

    def client_async_api_wait_trd_msg(self, msg, timeout_ms):
        return self._ClientAsyncApi_WaitTrdMsg(byref(msg), c_int32(timeout_ms))

    def client_async_api_wait_md_msg(self, msg, timeout_ms):
        return self._ClientAsyncApi_WaitMdMsg(byref(msg), c_int32(timeout_ms))

    def client_is_owned_by_strategy(self, user_info, strategy_id):
        return self._ClientAsyncApi_IsOwnedByStrategy(c_int64(user_info), c_int32(strategy_id))

    def client_async_api_add_strategy(self):
        return self._ClientAsyncApi_AddStrategy(self.async_ctx)


def debug():
    for i in ClientApiMsgTypeT.__dict__:
        # print(i)
        if i.startswith("CLIENT"):
            print(i, getattr(ClientApiMsgTypeT, i).value)


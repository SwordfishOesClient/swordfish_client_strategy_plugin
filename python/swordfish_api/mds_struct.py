# -*- coding: utf-8 -*-
from enum import Enum
from ctypes import Structure, Union
from ctypes import sizeof, POINTER
from ctypes import c_char, c_char_p, c_void_p
from ctypes import c_int8, c_int16, c_int32, c_int64
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64


MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE = 4000  # 每次的行情订阅请求中可以同时指定的最大订阅产品数量 (可以通过追加订阅的方式订阅更多的产品)
MDS_MAX_OPTION_CNT_TOTAL_SUBSCRIBED = 2000  # 对于沪/深两市的期权产品, 限制对每个市场最多允许同时订阅 2000 只产品
MDS_MAX_USERNAME_LEN = 32  # 用户名最大长度
MDS_MAX_PASSWORD_LEN = 40  # 密码最大长度
MDS_CLIENT_TAG_MAX_LEN = 32  # 客户端标签最大长度
MDS_VER_ID_MAX_LEN = 32  # 协议版本号的最大长度
MDS_MAX_TEST_REQ_ID_LEN = 32  # 测试请求标识符的最大长度
MDS_MAX_IP_LEN = 16  # 点分十进制的IPv4, 字符串的最大长度
MDS_MAX_MAC_LEN = 20  # MAC地址字符串的最大长度
MDS_MAX_MAC_ALGIN_LEN = 24  # MAC地址字符串的最大长度(按64位对齐的长度)
MDS_MAX_DRIVER_ID_LEN = 21  # 设备序列号字符串的最大长度
MDS_MAX_DRIVER_ID_ALGIN_LEN = 24  # 设备序列号字符串的最大长度(按64位对齐的长度)
MDS_MAX_INSTR_CODE_LEN = 9  # 证券代码长度(C6/C8)
MDS_REAL_STOCK_CODE_LEN = 6  # 实际的股票产品代码长度
MDS_REAL_OPTION_CODE_LEN = 8  # 实际的期权产品代码长度
MDS_MAX_POSTFIXED_INSTR_CODE_LEN = 12  # 允许带.SH/.SZ后缀的产品代码的最大长度
MDS_MAX_SECURITY_NAME_LEN = 40  # 证券名称最大长度
MDS_MAX_SECURITY_LONG_NAME_LEN = 80  # 证券长名称长度
MDS_MAX_SECURITY_ENGLISH_NAME_LEN = 48  # 证券英文名称长度
MDS_MAX_SECURITY_ISIN_CODE_LEN = 16  # 证券ISIN代码长度
MDS_MAX_CONTRACT_EXCH_ID_LEN = 24  # 期权合约交易代码长度
MDS_REAL_CONTRACT_EXCH_ID_LEN = 19  # 期权合约交易代码实际长度
MDS_MAX_SENDING_TIME_LEN = 22  # 发送时间字段(YYYYMMDD-HH:mm:SS.sss (*C21))的最大长度
MDS_REAL_SENDING_TIME_LEN = 21  # 发送时间字段(YYYYMMDD-HH:mm:SS.sss (*C21))的实际有效数据长度
MDS_MAX_TRADE_DATE_LEN = 9  # 交易日期字段(YYYYMMDD (*C8))的最大长度
MDS_REAL_TRADE_DATE_LEN = 8  # 交易日期字段(YYYYMMDD (*C8))的实际有效数据长度
MDS_MAX_UPDATE_TIME_LEN = 9  # 最新更新时间字段(HHMMSSss (*C8))的最大长度
MDS_REAL_UPDATE_TIME_LEN = 8  # 最新更新时间字段(HHMMSSss (*C8))的实际有效数据长度
MDS_MAX_TRADING_SESSION_ID_LEN = 9  # 全市场行情状态字段(*C8)的最大长度
MDS_REAL_TRADING_SESSION_ID_LEN = 8  # 全市场行情状态字段(*C8)的实际有效数据长度
MDS_MAX_TRADING_PHASE_CODE_LEN = 9  # 产品实时阶段及标志(C8/C4)的最大长度
MDS_REAL_TRADING_PHASE_CODE_LEN = 8  # 产品实时阶段及标志(C8/C4)的实际有效数据长度
MDS_MAX_FINANCIAL_STATUS_LEN = 9  # 证券状态字段(深交所证券实时状态消息 C8)的最大长度
MDS_REAL_FINANCIAL_STATUS_LEN = 8  # 证券状态字段(深交所证券实时状态消息 C8)的实际有效数据长度
MDS_MAX_SECURITY_SWITCH_CNT = 40  # 证券业务开关的最大数量(深交所证券实时状态消息)
MDS_UNIFIED_PRICE_UNIT = 10000  # 统一的价格单位
MDS_UNIFIED_MONEY_UNIT = 10000  # 统一的金额单位
MDS_TOTAL_VALUE_TRADED_UNIT = MDS_UNIFIED_MONEY_UNIT  # 总成交金额的金额单位 (上交所的总成交金额精度原本为2位, 但在此统一整合为4位精度)
MDS_INDEX_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT  # 指数的价格单位
MDS_STOCK_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT  # 股票的价格单位 (上交所的股票价格精度原本为3位, 但在此统一整合为4位精度)
MDS_OPTION_PRICE_UNIT = MDS_UNIFIED_PRICE_UNIT  # 期权的价格单位
MDS_MAX_ORDER_PRICE = 1999999999  # 逐笔委托中委托价格的最大值 (如果逐笔委托中的委托价格超出该值, 则将赋值为该值)
MDS_MAX_STOCK_ID_SCOPE = 1000000  # 股票代码的最大范围
MDS_MAX_OPTION_ID_SCOPE = 100000000  # 期权代码的最大范围
MDS_MAX_COMP_ID_LEN = 32  # 发送方/接收方代码的最大长度
MDS_APPL_DISCARD_VERSION_MAX_COUNT = 5  # 周边应用废弃版本数目的最大个数
MDS_APPL_UPGRADE_PROTOCOL_MAX_LEN = 32  # 周边应用升级协议名称的最大长度
MDS_MAX_L2_PRICE_LEVEL_INCREMENTS = 40  # Level2增量更新的价位列表最大数量
MDS_MAX_L2_DISCLOSE_ORDERS_CNT = 50  # Level2披露的买一／卖一委托明细最大数量
MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS = 152  # Level2增量更新的委托明细最大数量

MDS_QRYRSP_MAX_STOCK_CNT = 100  # 查询应答报文中的最大证券静态信息数量
MDS_APPL_VER_ID = "0.17.4.3"  # 当前采用的协议版本号
MDS_APPL_VER_VALUE = 1001704031
MDS_MIN_APPL_VER_ID = "0.15.5"  # 兼容的最低协议版本号
MDS_APPL_NAME = "MDS"  # 应用名称

# 最大路径长度
SPK_MAX_PATH_LEN = 256


# 交易所代码
class eMdsExchangeIdT(Enum):
    MDS_EXCH_UNDEFINE = 0  # 未定义的交易所代码
    MDS_EXCH_SSE = 1  # 交易所-上交所
    MDS_EXCH_SZSE = 2  # 交易所-深交所
    _MAX_MDS_EXCH = 3
    _MAX_MDS_EXCH_ALIGNED4 = 4  # 交易所代码最大值 (按4字节对齐的大小)
    _MAX_MDS_EXCH_ALIGNED8 = 8  # 交易所代码最大值 (按8字节对齐的大小)


# 消息来源
class eMdsMsgSourceT(Enum):
    MDS_MSGSRC_UNDEFINED = 0  # 消息来源-未定义
    MDS_MSGSRC_EZEI_TCP = 1  # 消息来源-EzEI(TCP)
    MDS_MSGSRC_EZEI_UDP = 2  # 消息来源-EzEI(UDP)
    MDS_MSGSRC_SSE_MDGW_BINARY = 10  # 消息来源-SSE-MDGW-BINARY
    MDS_MSGSRC_SSE_MDGW_STEP = 11  # 消息来源-SSE-MDGW-STEP
    MDS_MSGSRC_VDE_LEVEL1 = 20  # 消息来源-SSE-VDE-LEVEL1-FAST
    MDS_MSGSRC_VDE_LEVEL1_BINARY = 21  # 消息来源-SSE-VDE-LEVEL1-BINARY
    MDS_MSGSRC_VDE_LEVEL2 = 22  # 消息来源-SSE-VDE-LEVEL2
    MDS_MSGSRC_VDE_LEVEL2_REBUILD = 29  # 消息来源-SSE-VDE-LEVEL2-逐笔重建
    MDS_MSGSRC_SZSE_MDGW_BINARY = 31  # 消息来源-SZSE-MDGW-BINARY
    MDS_MSGSRC_SZSE_MDGW_STEP = 32  # 消息来源-SZSE-MDGW-STEP
    MDS_MSGSRC_SZSE_MDGW_MULTICAST = 33  # 消息来源-SZSE-MDGW-组播
    MDS_MSGSRC_SZSE_MDGW_REBUILD = 39  # 消息来源-SZSE-MDGW-Binary-逐笔重建
    MDS_MSGSRC_FILE_MKTDT = 90  # 消息来源-文件(mktdt, 实盘下不会出现)
    MDS_MSGSRC_MDS_TCP = 91  # 消息来源-MDS(TCP, 仅内部测试使用, 实盘下不会出现)
    MDS_MSGSRC_MDS_UDP = 92  # 消息来源-MDS(UDP, 仅内部测试使用, 实盘下不会出现)
    _MAX_MDS_MSGSRC = 93
    # 消息来源-SZSE-MDGW-Binary @deprecated 已过时, 请使用 MDS_MSGSRC_SZSE_MDGW_BINARY
    MDS_MSGSRC_MDGW_BINARY = MDS_MSGSRC_SZSE_MDGW_BINARY
    # 消息来源-SZSE-MDGW-STEP @deprecated 已过时, 请使用 MDS_MSGSRC_SZSE_MDGW_STEP
    MDS_MSGSRC_MDGW_STEP = MDS_MSGSRC_SZSE_MDGW_STEP


# 行情产品类型 (和交易端的产品类型不同, 行情数据中的产品类型只是用于区分是现货行情还是衍生品行情)
class eMdsMdProductTypeT(Enum):
    MDS_MD_PRODUCT_TYPE_UNDEFINE = 0  # 未定义的行情产品类型
    MDS_MD_PRODUCT_TYPE_STOCK = 1  # 股票 (包含基金和债券)
    MDS_MD_PRODUCT_TYPE_INDEX = 2  # 指数
    MDS_MD_PRODUCT_TYPE_OPTION = 3  # 期权
    _MAX_MDS_MD_PRODUCT_TYPE = 4
    _MAX_MDS_MD_PRODUCT_TYPE_ALIGNED4 = 4  # 行情产品类型最大值 (按4字节对齐的大小)
    _MAX_MDS_MD_PRODUCT_TYPE_ALIGNED8 = 8  # 行情产品类型最大值 (按8字节对齐的大小)
    # @deprecated 以下定义已过时, 为保持兼容而暂时保留
    MDS_SECURITY_TYPE_STOCK = MDS_MD_PRODUCT_TYPE_STOCK
    MDS_SECURITY_TYPE_INDEX = MDS_MD_PRODUCT_TYPE_INDEX
    MDS_SECURITY_TYPE_OPTION = MDS_MD_PRODUCT_TYPE_OPTION
    _MAX_MDS_SECURITY_TYPE = _MAX_MDS_MD_PRODUCT_TYPE


# 行情数据类别
class eMdsSubStreamTypeT(Enum):
    MDS_SUB_STREAM_TYPE_UNDEFINE = 0  # 未定义的行情数据类别
    MDS_SUB_STREAM_TYPE_MARKET_STATUS = 1  # 市场状态 (市场总览消息等状态消息)
    MDS_SUB_STREAM_TYPE_STOCK = 10  # 股票
    MDS_SUB_STREAM_TYPE_BOND = 20  # 债券
    MDS_SUB_STREAM_TYPE_BOND_NEGOTIATED = 21  # 债券 - 债券现券交易协商成交逐笔行情 (仅适用于深交所逐笔行情)
    MDS_SUB_STREAM_TYPE_BOND_CLICK = 22  # 债券 - 债券现券交易点击成交逐笔行情 (仅适用于深交所逐笔行情)
    MDS_SUB_STREAM_TYPE_BOND_INQUIRY = 23  # 债券 - 债券现券交易询价成交逐笔行情 (仅适用于深交所逐笔行情)
    MDS_SUB_STREAM_TYPE_BOND_IOI = 24  # 债券 - 债券现券交易意向申报逐笔行情 (Indication of Interest, 仅适用于深交所逐笔行情)
    MDS_SUB_STREAM_TYPE_BOND_BIDDING = 25  # 债券 - 债券现券交易竞买成交逐笔行情 (仅适用于深交所逐笔行情)
    MDS_SUB_STREAM_TYPE_FUND = 40  # 基金 (@note 上交所Level2行情尚无法区分基金数据, 将归类为股票)
    MDS_SUB_STREAM_TYPE_OPTION = 50  # 期权
    MDS_SUB_STREAM_TYPE_INDEX = 90  # 指数
    MDS_SUB_STREAM_TYPE_TRADE_STATS = 91  # 指数 - 成交量统计指标 (结构与指数行情相同, 仅适用于深交所)
    MDS_SUB_STREAM_TYPE_CN_INDEX = 92  # 指数 - 国证指数 (结构与指数快照相同, 仅适用于深交所)
    _MAX_MDS_SUB_STREAM_TYPE = 93


# 快照行情数据对应的消息类型 (@deprecated 已废弃, 请改为直接使用消息类型定义(eMdsMsgTypeT))
#
# @deprecated  已废弃
#              - 判断消息类型, 请直接使用快照行情相关的消息类型定义 @see eMdsMsgTypeT
#              - 判断行情类别, 请改为使用行情数据类别(subStreamType)字段 @see eMdsSubStreamTypeT
class eMdsMdStreamTypeT(Enum):
    # Level-1 行情快照数据类型
    # Level1 行情快照 @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH
    MDS_MD_STREAM_TYPE_L1_SNAPSHOT = 10
    # Level1/Level2 指数行情快照 @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_INDEX_SNAPSHOT_FULL_REFRESH
    MDS_MD_STREAM_TYPE_INDEX = 11
    # Level1/Level2 期权行情快照 @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_OPTION_SNAPSHOT_FULL_REFRESH
    MDS_MD_STREAM_TYPE_OPTION = 12
    # 上交所 Level1 行情快照-债券 @deprecated 已废弃
    MDS_MD_STREAM_TYPE_SSE_L1_BOND = MDS_MD_STREAM_TYPE_L1_SNAPSHOT
    # 上交所 Level1 行情快照-基金 @deprecated 已废弃
    MDS_MD_STREAM_TYPE_SSE_L1_FUND = MDS_MD_STREAM_TYPE_L1_SNAPSHOT
    # 深交所成交量统计指标 @deprecated 已废弃
    MDS_MD_STREAM_TYPE_SZSE_TRADE_STATS = MDS_MD_STREAM_TYPE_INDEX
    # 深交所国证指数行情快照 @deprecated 已废弃
    MDS_MD_STREAM_TYPE_SZSE_CN_INDEX = MDS_MD_STREAM_TYPE_INDEX
    # Level-2 行情快照数据类型
    # Level2 行情快照 @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT
    MDS_MD_STREAM_TYPE_L2_SNAPSHOT = 20
    # Level2 委托队列快照 (买一/卖一前五十笔) @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_L2_BEST_ORDERS_SNAPSHOT
    MDS_MD_STREAM_TYPE_L2_BEST_ORDERS_SNAPSHOT = 21
    # Level2 快照行情的增量更新消息 (仅适用于上交所) @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_L2_MARKET_DATA_INCREMENTAL
    MDS_MD_STREAM_TYPE_L2_SNAPSHOT_INCREMENTAL = 24
    # Level2 委托队列快照的增量更新消息 (仅适用于上交所) @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_L2_BEST_ORDERS_INCREMENTAL
    MDS_MD_STREAM_TYPE_L2_BEST_ORDERS_INCREMENTAL = 25
    # Level2 市场总览消息 (仅适用于上交所) @deprecated 已废弃, 请改为使用 @see MDS_MSGTYPE_L2_MARKET_OVERVIEW
    MDS_MD_STREAM_TYPE_L2_MARKET_OVERVIEW = 26
    # 最大的行情消息类型 @deprecated 已废弃, 请改为使用 @see _MDS_MSGTYPE_L2_MAX
    _MAX_MDS_MD_STREAM_TYPE = 27
    # @deprecated 以下定义已过时, 为保持兼容而暂时保留
    MDS_MD_STREAM_TYPE_BOND = MDS_MD_STREAM_TYPE_SSE_L1_BOND
    MDS_MD_STREAM_TYPE_FUND = MDS_MD_STREAM_TYPE_SSE_L1_FUND
    MDS_MD_STREAM_TYPE_OTHERS = MDS_MD_STREAM_TYPE_L2_MARKET_OVERVIEW


# 行情数据级别 (Level1 / Level2)
class eMdsMdLevelT(Enum):
    MDS_MD_LEVEL_0 = 0  # 未设置
    MDS_MD_LEVEL_1 = 1  # Level-1 行情
    MDS_MD_LEVEL_2 = 2  # Level-2 行情
    _MAX_MDS_MD_LEVEL = 3


# Level2增量更新消息的价位运算 (1=Add, 2=Update, 3=Delete)
class eMdsL2PriceLevelOperatorT(Enum):
    MDS_L2_PX_OPERATOR_ADD = 1  # L2价位运算 - Add
    MDS_L2_PX_OPERATOR_UPDATE = 2  # L2价位运算 - Update
    MDS_L2_PX_OPERATOR_DELETE = 3  # L2价位运算 - Delete
    _MAX_MDS_L2_PX_OPERATOR = 4


# Level2逐笔成交的成交类别
# - 仅适用于深交所 ('4'=撤销, 'F'=成交)
# - 对于上交所, 将固定取值为 'F'(成交)
class eMdsL2TradeExecTypeT(Enum):
    MDS_L2_TRADE_EXECTYPE_CANCELED = '4'  # L2执行类型 - 已撤销
    MDS_L2_TRADE_EXECTYPE_TRADE = 'F'  # L2执行类型 - 已成交


# Level2逐笔成交的内外盘标志
# - 仅适用于上交所 ('B'=外盘,主动买, 'S'=内盘,主动卖, 'N'=未知)
# - 对于深交所, 将固定取值为 'N'(未知)
class eMdsL2TradeBSFlagT(Enum):
    MDS_L2_TRADE_BSFLAG_BUY = 'B'  # L2内外盘标志 - 外盘,主动买
    MDS_L2_TRADE_BSFLAG_SELL = 'S'  # L2内外盘标志 - 内盘,主动卖
    MDS_L2_TRADE_BSFLAG_UNKNOWN = 'N'  # L2内外盘标志 - 未知


# Level2逐笔委托的买卖方向 ('1'=买 '2'=卖 'G'=借入 'F'=出借)
class eMdsL2OrderSideT(Enum):
    MDS_L2_ORDER_SIDE_BUY = '1'  # L2买卖方向 - 买
    MDS_L2_ORDER_SIDE_SELL = '2'  # L2买卖方向 - 卖
    MDS_L2_ORDER_SIDE_BORROW = 'G'  # L2买卖方向 - 借入 (仅适用于深交所)
    MDS_L2_ORDER_SIDE_LEND = 'F'  # L2买卖方向 - 出借 (仅适用于深交所)


# 深交所逐笔委托的订单类型
class eMdsL2OrderTypeT(Enum):
    MDS_L2_ORDER_TYPE_MKT = '1'  # 深交所订单类型 - 市价
    MDS_L2_ORDER_TYPE_LMT = '2'  # 深交所订单类型 - 限价
    MDS_L2_ORDER_TYPE_SAMEPARTY_BEST = 'U'  # 深交所订单类型 - 本方最优


# 上交所逐笔委托的订单类型
class eMdsL2SseOrderTypeT(Enum):
    MDS_L2_SSE_ORDER_TYPE_ADD = 'A'  # 上交所订单类型 - 增加 (即: 新订单)
    MDS_L2_SSE_ORDER_TYPE_DELETE = 'D'  # 上交所订单类型 - 删除 (即: 撤单)


# 客户端类型定义 (内部使用)
class eMdsClientTypeT(Enum):
    MDS_CLIENT_TYPE_UNDEFINED = 0  # 客户端类型-未定义
    MDS_CLIENT_TYPE_INVESTOR = 1  # 普通投资人
    MDS_CLIENT_TYPE_VIRTUAL = 2  # 虚拟账户 (仅开通行情, 不可交易)


# 客户端状态定义 (内部使用)
class eMdsClientStatusT(Enum):
    MDS_CLIENT_STATUS_UNACTIVATED = 0  # 未激活 (不加载)
    MDS_CLIENT_STATUS_ACTIVATED = 1  # 已激活 (正常加载)
    MDS_CLIENT_STATUS_PAUSE = 2  # 已暂停 (正常加载, 不可交易)
    MDS_CLIENT_STATUS_SUSPENDED = 3  # 已挂起 (不加载)
    MDS_CLIENT_STATUS_CANCELLED = 4  # 已注销 (不加载)


# 通信消息的消息类型定义
class eMdsMsgTypeT(Enum):
    # 会话类消息
    # 心跳消息 (1/0x01)
    MDS_MSGTYPE_HEARTBEAT = 1
    # 测试请求消息 (2/0x02)
    MDS_MSGTYPE_TEST_REQUEST = 2
    # 注销消息 (4/0x04)
    MDS_MSGTYPE_LOGOUT = 4
    # 证券行情订阅消息 (5/0x05)
    MDS_MSGTYPE_MARKET_DATA_REQUEST = 5
    # 压缩的数据包 (6/0x06, 内部使用)
    MDS_MSGTYPE_COMPRESSED_PACKETS = 6
    # 最大的会话消息类型
    _MDS_MSGTYPE_SESSION_MAX = 7
    # Level1 行情消息
    # Level1 市场行情快照 (10/0x0A)
    MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH = 10
    # Level1/Level2 指数行情快照 (11/0x0B)
    MDS_MSGTYPE_INDEX_SNAPSHOT_FULL_REFRESH = 11
    # Level1/Level2 期权行情快照 (12/0x0C)
    MDS_MSGTYPE_OPTION_SNAPSHOT_FULL_REFRESH = 12
    # 市场状态消息 (13/0x0D, 仅适用于上交所)
    MDS_MSGTYPE_TRADING_SESSION_STATUS = 13
    # 证券状态消息 (14/0x0E, 仅适用于深交所)
    MDS_MSGTYPE_SECURITY_STATUS = 14
    # 最大的Level-1行情消息类型
    _MDS_MSGTYPE_L1_MAX = 15
    # Level2 行情消息
    # Level2 市场行情快照 (20/0x14)
    MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT = 20
    # Level2 委托队列快照 (买一/卖一前五十笔) (21/0x15)
    MDS_MSGTYPE_L2_BEST_ORDERS_SNAPSHOT = 21
    # Level2 逐笔成交行情 (22/0x16)
    MDS_MSGTYPE_L2_TRADE = 22
    # Level2 深交所逐笔委托行情 (23/0x17, 仅适用于深交所)
    MDS_MSGTYPE_L2_ORDER = 23
    # Level2 上交所逐笔委托行情 (28/0x1C, 仅适用于上交所)
    MDS_MSGTYPE_L2_SSE_ORDER = 28
    # Level2 快照行情的增量更新消息 (24/0x18, 仅适用于上交所)
    MDS_MSGTYPE_L2_MARKET_DATA_INCREMENTAL = 24
    # Level2 委托队列快照的增量更新消息 (25/0x19, 仅适用于上交所)
    MDS_MSGTYPE_L2_BEST_ORDERS_INCREMENTAL = 25
    # Level2 市场总览消息 (26/0x1A, 仅适用于上交所)
    MDS_MSGTYPE_L2_MARKET_OVERVIEW = 26
    # Level2 虚拟集合竞价消息 (27/0x1B, 仅适用于上交所, @deprecated 已废弃)
    MDS_MSGTYPE_L2_VIRTUAL_AUCTION_PRICE = 27
    # 最大的Level-2行情消息类型
    _MDS_MSGTYPE_L2_MAX = 28
    # 指令类消息
    # 修改客户端登录密码 (60/0x3C)
    MDS_MSGTYPE_CMD_CHANGE_PASSWORD = 60
    # 最大的指令消息类型
    _MDS_MSGTYPE_CMD_MAX = 61
    # 查询类消息
    # 查询证券行情 (80/0x50)
    MDS_MSGTYPE_QRY_MARKET_DATA_SNAPSHOT = 80
    # 查询(深圳)证券状态 (81/0x51)
    MDS_MSGTYPE_QRY_SECURITY_STATUS = 81
    # 查询(上证)市场状态 (82/0x52)
    MDS_MSGTYPE_QRY_TRADING_SESSION_STATUS = 82
    # 批量查询行情快照列表 (86/0x56)
    MDS_MSGTYPE_QRY_SNAPSHOT_LIST = 86
    # 查询期权静态信息 (87/0x57)
    MDS_MSGTYPE_QRY_OPTION_STATIC_INFO = 87
    # 查询证券(股票/债券/基金)静态信息 (88/0x58)  (0x55的更新版本, @since 0.15.11)
    MDS_MSGTYPE_QRY_STOCK_STATIC_INFO = 88
    # 批量查询证券(股票/债券/基金)静态信息列表 (89/0x59)
    MDS_MSGTYPE_QRY_STOCK_STATIC_INFO_LIST = 89
    # 批量查询期权静态信息列表 (90/0x5A)
    MDS_MSGTYPE_QRY_OPTION_STATIC_INFO_LIST = 90
    # 最大的查询消息类型
    _MDS_MSGTYPE_QRY_MAX = 91


# 订阅模式 (SubMode) 定义
# -  0: (Set)          重新订阅, 设置为订阅列表中的股票 (之前的订阅参数将被清空)
# -  1: (Append)       追加订阅, 增加订阅列表中的股票
# -  2: (Delete)       删除订阅, 删除订阅列表中的股票
#
# 新增的批量订阅模式定义 (@since v0.15.9.1)
# - 10: (BatchBegin)   批量订阅-开始订阅, 开始一轮新的批量订阅 (之前的订阅参数将被清空,
#                      行情推送也将暂停直到批量订阅结束)
# - 11: (BatchAppend)  批量订阅-追加订阅, 增加订阅列表中的股票
# - 12: (BatchDelete)  批量订阅-删除订阅, 删除订阅列表中的股票
# - 13: (BatchEnd)     批量订阅-结束订阅, 结束本轮的批量订阅, 提交和启用本轮的订阅参数
#
# @note 当订阅模式为 Append/Delete/BatchDelete 时将忽略 isRequireInitialMktData 和
#       beginTime 这两个订阅参数
class eMdsSubscribeModeT(Enum):
    # 重新订阅, 设置为订阅列表中的股票 (之前的订阅参数将被清空)
    MDS_SUB_MODE_SET = 0
    # 追加订阅, 增加订阅列表中的股票
    MDS_SUB_MODE_APPEND = 1
    # 删除订阅, 删除订阅列表中的股票
    MDS_SUB_MODE_DELETE = 2
    _MAX_MDS_SUB_MODE_NONBATCH = 3
    # 批量订阅-开始订阅, 开始一轮新的批量订阅
    # (之前的订阅参数将被清空, 行情推送也将暂停直到批量订阅结束)
    MDS_SUB_MODE_BATCH_BEGIN = 10
    # 批量订阅-追加订阅, 增加订阅列表中的股票
    MDS_SUB_MODE_BATCH_APPEND = 11
    # 批量订阅-删除订阅, 删除订阅列表中的股票
    MDS_SUB_MODE_BATCH_DELETE = 12
    # 批量订阅-结束订阅, 结束本轮的批量订阅, 提交和启用本轮的订阅参数
    MDS_SUB_MODE_BATCH_END = 13
    _MAX_MDS_SUB_MODE = 14


# 市场-产品类型订阅标志 (SubFlag) 定义
# -  0: (Default) 根据订阅列表订阅产品行情
# -  1: (All) 订阅该市场和证券类型下的所有产品行情 (为兼容之前的版本, 也可以赋值为 -1)
# -  2: (Disable) 禁用该市场下的所有产品行情
class eMdsMktSubscribeFlagT(Enum):
    # 根据订阅列表订阅产品行情
    MDS_MKT_SUB_FLAG_DEFAULT = 0
    # 订阅该市场和证券类型下的所有产品行情
    MDS_MKT_SUB_FLAG_ALL = 1
    # 禁用该市场下的所有产品行情
    MDS_MKT_SUB_FLAG_DISABLE = 2
    _MAX_MDS_MKT_SUB_FLAG = 3


# 数据模式 (TickType) 定义 (仅对快照行情生效, 用于标识订阅最新的行情快照还是所有时点的行情快照)
#
# 取值说明:
# -  0: (LatestSimplified) 只订阅最新的行情快照数据, 并忽略和跳过已经过时的数据
#       - 该模式推送的数据量最小, 服务器端会做去重处理, 不会再推送重复的和已经过时的快照数据
#       - 优点: 该模式在时延和带宽方面都更加优秀, 该模式优先关注快照行情的时效性, 并避免推送
#         没有实质变化的重复快照
#       - 缺点: 当没有行情变化时 (例如没有交易或盘中休市等), 就不会推送任何快照行情了, 这一
#         点可能会带来困扰, 不好确定是发生丢包了还是没有行情导致的
#       - 注意: 过时和重复的快照都会被过滤掉
# -  1: (LatestTimely) 只订阅最新的行情快照数据, 并立即发送最新数据
#       - 只要有行情更新事件, 便立即推送该产品的最新行情, 但行情数据本身可能是重复的, 即只有
#         行情时间有变化, 行情数据本身没有变化
#       - 优点: 可以获取到时间点更完整的快照行情, 不会因为行情数据没有变化而跳过 (如果是因为
#         接收慢等原因导致快照已经过时了, 该快照还是会被忽略掉)
#       - 缺点: 会收到仅更新时间有变化, 但行情数据本身并没有更新的重复数据, 带宽和数据量上会
#         有一定的浪费
#       - 注意: 重复的快照不会被过滤掉, 但过时的快照还是会被过滤掉
# -  2: (AllIncrements) 订阅所有时点的行情快照数据 (包括Level2增量更新消息)
#       - 该模式会推送所有时点的行情数据, 包括Level2行情快照的增量更新消息
#       - 如果需要获取全量的行情明细, 或者需要直接使用Level2的增量更新消息, 可以使用该模式
#       - 如果没有特别需求的话, 不需要订阅增量更新消息, 增量消息处理起来比较麻烦
#          - 增量更新消息 (字段级别的增量更新) 只有上交所Level-2快照有, 深交所行情里面没有
#          - 在对下游系统进行推送时, 增量快照和完整快照在推送时间上是没有区别的, 增量更新并
#            不会比完整快照更快, 只是信息角度不一样
#
# 补充说明:
# - 当以 tickType=0 的模式订阅行情时, 服务器端会对重复的快照行情做去重处理, 不会再推送重复
#   的和已经过时的快照数据。
# - 如果需要获取到"所有时点"的快照, 可以使用 tickType=1 的模式订阅行情。此模式下只要行情时
#   间有变化, 即使数据重复也会对下游推送。但过时的快照还是会被忽略掉。
# - 只有通过 tickType=2 的模式才能接收到完整的所有时间点的行情数据。
# - 快照行情 "过时" 表示: 不是当前最新的快照即为"过时", 即存在时间点比该快照更新的快照 (同一
#   只股票)。
# - @note  上交所行情存在更新时间相同但数据不同的Level-2快照。(频率不高, 但会存在这样的数据)
class eMdsSubscribedTickTypeT(Enum):
    # 只订阅最新的行情快照数据, 并忽略和跳过已经过时的数据 (推送的数据量最小, 服务器端会做去重处理, 不会再推送重复的和已经过时的快照数据)
    MDS_TICK_TYPE_LATEST_SIMPLIFIED = 0
    # 只订阅最新的行情快照数据, 并立即发送最新数据 (可以获取到时间点更完整的快照行情, 只要行情时间有变化, 即使数据重复也会对下游推送)
    MDS_TICK_TYPE_LATEST_TIMELY = 1
    # 订阅所有时点的行情快照数据 (包括Level2增量更新消息)
    MDS_TICK_TYPE_ALL_INCREMENTS = 2
    _MAX_MDS_TICK_TYPE = 3


# 逐笔数据的过期时间定义 (仅对逐笔数据生效)
# @note    仅对压缩行情端口生效, 普通的非压缩行情端口不支持该选项
class eMdsSubscribedTickExpireTypeT(Enum):
    # 不过期
    MDS_TICK_EXPIRE_TYPE_NONE = 0
    # 立即过期 (1秒, 如果逐笔数据时间落后于最新快照时间1秒, 则视为过期并跳过该逐笔数据)
    MDS_TICK_EXPIRE_TYPE_IMMEDIATE = 1
    # 及时过期 (3秒, 如果逐笔数据时间落后于最新快照时间3秒, 则视为过期并跳过该逐笔数据)
    MDS_TICK_EXPIRE_TYPE_TIMELY = 2
    # 超时过期 (30秒, 如果逐笔数据时间落后于最新快照时间30秒, 则视为过期并跳过该逐笔数据)
    MDS_TICK_EXPIRE_TYPE_TIMEOUT = 3
    _MAX_MDS_TICK_EXPIRE_TYPE = 4


# 逐笔数据的数据重建标识定义 (标识是否订阅重建到的逐笔数据, 仅对逐笔数据生效)
class eMdsSubscribedTickRebuildFlagT(Enum):
    # 不订阅重建到的逐笔数据 (仅实时行情)
    MDS_TICK_REBUILD_FLAG_EXCLUDE_REBUILDED = 0
    # 订阅重建到的逐笔数据 (实时行情+重建数据)
    MDS_TICK_REBUILD_FLAG_INCLUDE_REBUILDED = 1
    # 只订阅重建到的逐笔数据 (仅重建数据)
    # @note    仅订阅重建数据需要通过压缩行情端口进行订阅, 普通的非压缩行情端口不支持该选项
    MDS_TICK_REBUILD_FLAG_ONLY_REBUILDED = 2
    _MAX_MDS_TICK_REBUILD_FLAG = 3


# 可订阅的数据种类 (DataType) 定义
# - 0:      默认数据种类 (所有)
# - 0x0001: L1快照/指数/期权
# - 0x0002: L2快照
# - 0x0004: L2委托队列
# - 0x0008: L2逐笔成交
# - 0x0010: L2深交所逐笔委托 (仅适用于深交所)
# - 0x0020: L2上交所逐笔委托 (仅适用于上交所)
# - 0x0040: L2市场总览 (仅适用于上交所)
# - 0x0100: 市场状态 (仅适用于上交所)
# - 0x0200: 证券实时状态 (仅适用于深交所)
# - 0x0400: 指数行情 (与0x0001的区别在于, 0x0400可以单独订阅指数行情)
# - 0x0800: 期权行情 (与0x0001的区别在于, 0x0800可以单独订阅期权行情)
# - 0xFFFF: 所有数据种类
class eMdsSubscribeDataTypeT(Enum):
    # 默认数据种类 (所有种类)
    MDS_SUB_DATA_TYPE_DEFAULT = 0
    # L1快照/指数/期权 (L1快照行情 + 指数行情 + 期权行情)
    MDS_SUB_DATA_TYPE_L1_SNAPSHOT = 0x0001
    # L2快照
    MDS_SUB_DATA_TYPE_L2_SNAPSHOT = 0x0002
    # L2委托队列
    MDS_SUB_DATA_TYPE_L2_BEST_ORDERS = 0x0004
    # 逐笔成交
    MDS_SUB_DATA_TYPE_L2_TRADE = 0x0008
    # 深交所逐笔委托 (*仅适用于深交所, 0x10/16)
    MDS_SUB_DATA_TYPE_L2_ORDER = 0x0010
    # 上交所逐笔委托 (*仅适用于上交所, 0x20/32)
    MDS_SUB_DATA_TYPE_L2_SSE_ORDER = 0x0020
    # L2市场总览 (*仅适用于上交所, 0x40/64)
    MDS_SUB_DATA_TYPE_L2_MARKET_OVERVIEW = 0x0040
    # 市场状态 (*仅适用于上交所, 0x100/256)
    MDS_SUB_DATA_TYPE_TRADING_SESSION_STATUS = 0x0100
    # 证券实时状态 (*仅适用于深交所, 0x200/512)
    MDS_SUB_DATA_TYPE_SECURITY_STATUS = 0x0200
    # 指数行情 (与L1_SNAPSHOT的区别在于, INDEX_SNAPSHOT可以单独订阅指数行情)
    MDS_SUB_DATA_TYPE_INDEX_SNAPSHOT = 0x0400
    # 期权行情 (与L1_SNAPSHOT的区别在于, OPTION_SNAPSHOT可以单独订阅期权行情)
    MDS_SUB_DATA_TYPE_OPTION_SNAPSHOT = 0x0800
    # 空数据种类 (可用于不指定任何数量种类的情况)
    MDS_SUB_DATA_TYPE_NONE = 0x8000
    # 所有数据种类
    MDS_SUB_DATA_TYPE_ALL = 0xFFFF
    _MAX_MDS_SUB_DATA_TYPE = 0x7FFFFFFF


# 可订阅的内部数据频道定义 (供内部使用, 尚未对外开放)
class eMdsTickChannelNoT(Enum):
    # 默认频道 (所有频道)
    MDS_CHANNEL_NO_DEFAULT = 0
    # 频道1
    MDS_CHANNEL_NO_ONE = 0x01
    # 频道2
    MDS_CHANNEL_NO_TWO = 0x02
    # 频道3
    MDS_CHANNEL_NO_THREE = 0x04
    # 频道4
    MDS_CHANNEL_NO_FOUR = 0x08
    # 所有频道
    MDS_CHANNEL_NO_ALL = 0x0F
    # 空数据频道 (可用于不订阅任何频道的情况)
    MDS_CHANNEL_NO_NONE = 0x80


class PrintableStructure(Structure):
    def __str__(self):
        result = "<" + self.__class__.__name__ + "("
        for name, _ in self._fields_:
            result = result + name + "=" + str(getattr(self, name)) + ", "
        return result[:-2] + ")>"

    def to_dict(self):
        new_d = {}
        for name, _ in self._fields_:
            val = getattr(self, name)
            if isinstance(val, bytes):
                val = val.decode('utf-8', "ignore")
            new_d[name] = val
        return new_d


class PrintableUnion(Union):
    def __str__(self):
        result = "<" + self.__class__.__name__ + "("
        for name, _ in self._fields_:
            result = result + name + "=" + str(getattr(self, name)) + ", "
        return result[:-2] + ")>"

    def to_dict(self):
        new_d = {}
        for name, _ in self._fields_:
            val = getattr(self, name)
            if isinstance(val, bytes):
                val = val.decode('utf-8', "ignore")
            new_d[name] = val
        return new_d


class STimespec32T(PrintableStructure):
    _fields_ = [
        ('tv_sec', c_int32),
        ('tv_nsec', c_int32),
    ]


class UserInfo(PrintableUnion):
    _fields_ = [
        ('u64', c_uint64),  # uint64 类型的用户私有信息
        ('i64', c_int64),  # int64 类型的用户私有信息
        ('u32', c_uint32 * 2),  # uint32[2] 类型的用户私有信息
        ('i32', c_int32 * 2),  # int32[2] 类型的用户私有信息
        ('c8', c_char * 8),  # char[8] 类型的用户私有信息
    ]


# 市场状态消息(MsgType=h)定义 (仅适用于上交所, 深交所行情中没有该数据)
class MdsTradingSessionStatusMsgT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码(沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/指数/期权) @see eMdsMdProductTypeT
        ('_isRepeated', c_int8),  # 是否是重复的行情 (供内部使用, 小于0 表示数据倒流)
        ('_origMdSource', c_uint8),  # 原始行情数据来源 @see eMdsMsgSourceT
        ('tradeDate', c_int32),  # 交易日期 (YYYYMMDD, 通过拆解SendingTime得到, 并非官方数据)
        ('updateTime', c_int32),  # 行情时间 (HHMMSSsss, 交易所时间, 通过拆解SendingTime得到, 并非官方数据)
        ('_exchSendingTime', c_int32),  # 交易所发送时间 (HHMMSSsss)
        ('_mdsRecvTime', c_int32),  # MDS接收到时间 (HHMMSSsss)
        ('TotNoRelatedSym', c_int32),  # 最大产品数目 (包括指数)
        # 全市场行情状态 (*C8)
        # 该字段为 8 位字符串,左起每位表示特定的含义,无定义则填空格。
        # 第 0 位: ‘S’表示全市场启动期间(开市前), ‘T’表示全市场处于交易期间 (含中间休市), ‘E’表示全市场处于闭市期间。
        # 第 1 位: ‘1’表示开盘集合竞价结束标志, 未结束取‘0’。
        # 第 2 位: ‘1’表示市场行情闭市标志, 未闭市取‘0’。
        ('TradingSessionID', c_char * MDS_MAX_TRADING_SESSION_ID_LEN),
        ('_filler3', c_uint8 * 3),  # 按64位对齐的填充域
        ('_dataVersion', c_uint16),  # 行情数据的更新版本号 (当_isRepeated!=0时, 该值仅作为参考值)
        ('_filler', c_uint16),  # 按64位对齐的填充域
        ('_origTickSeq', c_uint64),  # 对应的原始行情的序列号(供内部使用)
        # 消息原始接收时间 (从网络接收到数据的最初时间)
        ('_origNetTime', STimespec32T),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息加工处理完成时间
        ('_processedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


class _MdsSwitch(PrintableStructure):
    _fields_ = [
        # 业务开关的使能标志 (0 未启用, 1 启用)
        ('switchFlag', c_uint8),
        # 开关状态 (0 关闭, 1 开启)
        ('switchStatus', c_uint8),
    ]


# 证券实时状态定义 (仅适用于深交所, 上交所行情中没有该数据)
class MdsSecurityStatusMsgT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码(沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票(包含基金和债券)/期权) @see eMdsMdProductTypeT
        ('_isRepeated', c_int8),  # 是否是重复的行情 (供内部使用, 小于0 表示数据倒流)
        ('_origMdSource', c_uint8),  # 原始行情数据来源 @see eMdsMsgSourceT
        ('tradeDate', c_int32),  # 交易日期 (YYYYMMDD, 通过拆解数据生成时间OrigTime得到)
        ('updateTime', c_int32),  # 行情时间 (HHMMSSsss, 交易所时间, 通过拆解数据生成时间OrigTime得到)
        ('_exchSendingTime', c_int32),  # 交易所发送时间 (HHMMSSsss, 目前获取不到深交所的发送时间, 固定为 0)
        ('_mdsRecvTime', c_int32),  # MDS接收到时间 (HHMMSSsss)
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        # 证券代码 C6 / C8 (如: '000001' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 证券状态 (C8)
        # A=上市公司早间披露提示
        # B=上市公司午间披露提示
        ('FinancialStatus', c_char * MDS_MAX_FINANCIAL_STATUS_LEN),
        ('_filler2', c_uint8 * 2),  # 按64位对齐的填充域
        ('_dataVersion', c_uint16),  # 行情数据的更新版本号 (当_isRepeated!=0时, 该值仅作为参考值)
        ('_filler', c_uint16),  # 按64位对齐的填充域
        ('_origTickSeq', c_uint64),  # 对应的原始行情的序列号(供内部使用)
        ('NoSwitch', c_int32),  # 开关个数
        ('_filler4', c_int32),  # 按64位对齐的填充域
        # 证券业务开关列表
        # 业务开关列表为定长数组, 数组的下标位置对应于各个业务开关, 业务开关说明如下:
        # -  1: 融资买入, 适用于融资标的证券
        # -  2: 融券卖出, 适用于融券标的证券
        # -  3: 申购, 适用于 ETF/LOF 等开放式基金, 对于黄金 ETF 是指现金申购
        # -  4: 赎回, 适用于 ETF/LOF 等开放式基金, 对于黄金 ETF 是指现金赎回开关
        # -  5: 认购, 适用于网上发行认购代码
        # -  6: 转股, 适用于处于转股回售期的可转债
        # -  7: 回售, 适用于处于转股回售期的可转债
        # -  8: 行权, 适用于处于行权期的权证或期权
        # - 10: 买开仓, 适用于期权等衍生品
        # - 11: 卖开仓, 适用于期权等衍生品
        # - 12: 黄金ETF实物申购, 适用于黄金 ETF
        # - 13: 黄金ETF实物赎回, 适用于黄金 ETF
        # - 14: 预受要约, 适用于处于要约收购期的股票
        # - 15: 解除要约, 适用于处于要约收购期的股票
        # - 18: 转股撤单, 适用于处于转股回售期的可转债
        # - 19: 回售撤单, 适用于处于转股回售期的可转债
        # - 20: 质押, 适用于质押式回购可质押入库证券
        # - 21: 解押, 适用于质押式回购可质押入库证券
        # - 22: 表决权, 适用于优先股
        # - 23: 股票质押式回购, 适用于可开展股票质押式回购业务的证券
        # - 24: 实时分拆, 适用于分级基金
        # - 25: 实时合并, 适用于分级基金
        # - 26: 备兑开仓, 适用于期权等衍生品
        # - 27: 做市商报价, 适用于期权等支持做市商报价的证券
        # - 28: 港股通整手买
        # - 29: 港股通整手卖
        # - 30: 港股通零股买
        # - 31: 港股通零股卖
        # - 32: 期权普通转备兑仓
        # - 33: 期权备兑转普通仓
        ('switches', _MdsSwitch * MDS_MAX_SECURITY_SWITCH_CNT),
        # 消息原始接收时间 (从网络接收到数据的最初时间)
        ('_origNetTime', STimespec32T),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息加工处理完成时间
        ('_processedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# 价位信息定义
class MdsPriceLevelEntryT(PrintableStructure):
    _fields_ = [
        ('Price', c_int32),  # 委托价格
        ('NumberOfOrders', c_int32),  # 价位总委托笔数 (Level1不揭示该值, 固定为0)
        ('OrderQty', c_int64),  # 委托数量 (上交所债券的数量单位为手)
    ]


# Level1/Level2 快照行情(证券行情全幅消息)的消息头定义
class MdsMktDataSnapshotHeadT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码(沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/指数/期权) @see eMdsMdProductTypeT
        ('_isRepeated', c_int8),  # 是否是重复的行情 (内部使用, 小于0表示数据倒流)
        ('_origMdSource', c_uint8),  # 原始行情数据来源 @see eMdsMsgSourceT
        ('tradeDate', c_int32),  # 交易日期 (YYYYMMDD, 8位整型数值)
        ('updateTime', c_int32),  # 行情时间 (HHMMSSsss, 交易所时间)
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        ('bodyLength', c_int16),  # 实际数据长度
        ('bodyType', c_uint8),  # 快照数据对应的消息类型 @see eMdsMsgTypeT
        ('subStreamType', c_uint8),  # 行情数据类别 @see eMdsSubStreamTypeT
        ('_channelNo', c_uint16),  # 频道代码 (仅适用于深交所, 对于上交所快照该字段无意义, 取值范围[0..9999])
        ('_dataVersion', c_uint16),  # 行情数据的更新版本号
        ('_origTickSeq', c_uint32),  # 对应的原始行情的序列号 (供内部使用)
        ('_directSourceId', c_uint32),  # 内部数据来源标识 (仅内部使用)
        # 消息原始接收时间 (从网络接收到数据的最初时间)
        ('_origNetTime', STimespec32T),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息加工处理完成时间
        ('_processedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# Level1/Level2 指数快照行情定义
class MdsIndexSnapshotBodyT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '000001' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 产品实时阶段及标志 C8 (对于指数行情该字段为预留字段)
        # @see MdsStockSnapshotBodyT.TradingPhaseCode
        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('_filler', c_char * 6),  # 按64位对齐的填充域
        ('NumTrades', c_uint64),  # 成交笔数 (仅适用于深交所, 上交所指数行情中没有成交笔数信息)
        ('TotalVolumeTraded', c_uint64),  # 成交总量 (@note 上交所指数的成交量单位是手, 深交所指数的成交量单位是股)
        ('TotalValueTraded', c_int64),  # 成交总金额 (金额单位精确到元后四位, 即: 1元=10000)
        ('PrevCloseIdx', c_int64),  # 昨日收盘指数 (价格单位精确到元后四位, 即: 1元=10000)
        ('OpenIdx', c_int64),  # 今开盘指数 (价格单位精确到元后四位, 即: 1元=10000)
        ('HighIdx', c_int64),  # 最高指数
        ('LowIdx', c_int64),  # 最低指数
        ('LastIdx', c_int64),  # 最新指数
        ('CloseIdx', c_int64),  # 今收盘指数
        ('StockNum', c_int32),  # 统计量指标样本个数 (用于深交所成交量统计指标)
        ('_filler1', c_int32),  # 按64位对齐的填充域
    ]


# Level1 股票快照行情定义
# 股票(A、B股)、债券、基金、期权
#
# 关于集合竞价期间的虚拟集合竞价行情 (上交所L1、深交所L1):
# - 集合竞价期间的虚拟成交价通过买卖盘档位揭示, 其中买一和卖一都揭示虚拟成交价格和成交数量,
#   买二或卖二揭示虚拟成交价位上的买剩余量或卖剩余量
class MdsStockSnapshotBodyT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 产品实时阶段及标志 C8 / C4
        # 上交所股票 (C8):
        # -# 第 0 位:
        # - ‘S’表示启动 (开市前) 时段, ‘C’表示开盘集合竞价时段, ‘T’表示连续交易时段,
        # - ‘E’表示闭市时段, ‘P’表示产品停牌,
        # - ‘M’表示可恢复交易的熔断时段 (盘中集合竞价), ‘N’表示不可恢复交易的熔断时段 (暂停交易至闭市),
        # - ‘U’表示收盘集合竞价时段。
        # -# 第 1 位:
        # - ‘0’表示此产品不可正常交易,
        # - ‘1’表示此产品可正常交易,
        # - 无意义填空格。
        # - 在产品进入开盘集合竞价、连续交易、收盘集合竞价、熔断(盘中集合竞价)状态时值为‘1’,
        # 在产品进入停牌、熔断(暂停交易至闭市)状态时值为‘0’, 且闭市后保持该产品闭市前的是否可正常交易状态。
        # -# 第 2 位:
        # - ‘0’表示未上市, ‘1’表示已上市。
        # -# 第 3 位:
        # - ‘0’表示此产品在当前时段不接受订单申报,
        # - ‘1’表示此产品在当前时段可接受订单申报。
        # - 仅在交易时段有效，在非交易时段无效。无意义填空格。
        # 上交所期权 (C4):
        # -# 第 0 位:
        # - ‘S’表示启动(开市前)时段, ‘C’表示集合竞价时段, ‘T’表示连续交易时段,
        # - ‘B’表示休市时段, ‘E’表示闭市时段, ‘V’表示波动性中断, ‘P’表示临时停牌, ‘U’收盘集合竞价。
        # - ‘M’表示可恢复交易的熔断 (盘中集合竞价), ‘N’表示不可恢复交易的熔断 (暂停交易至闭市)
        # -# 第 1 位:
        # - ‘0’表示未连续停牌, ‘1’表示连续停牌。(预留, 暂填空格)
        # -# 第 2 位:
        # - ‘0’表示不限制开仓, ‘1’表示限制备兑开仓, ‘2’表示卖出开仓, ‘3’表示限制卖出开仓、备兑开仓,
        # - ‘4’表示限制买入开仓, ‘5’表示限制买入开仓、备兑开仓, ‘6’表示限制买入开仓、卖出开仓,
        # - ‘7’表示限制买入开仓、卖出开仓、备兑开仓
        # -# 第 3 位:
        # - ‘0’表示此产品在当前时段不接受进行新订单申报,
        # - ‘1’表示此产品在当前时段可接受进行新订单申报。
        # - 仅在交易时段有效，在非交易时段无效。
        # 深交所 (C8):
        # -# 第 0 位:
        # - S=启动(开市前) O=开盘集合竞价 T=连续竞价
        # - B=休市 C=收盘集合竞价 E=已闭市 H=临时停牌
        # - A=盘后交易 V=波动性中断
        # -# 第 1 位:
        # - 0=正常状态
        # - 1=全天停牌
        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('_filler', c_char * 6),  # 按64位对齐的填充域
        ('NumTrades', c_uint64),  # 成交笔数
        ('TotalVolumeTraded', c_uint64),  # 成交总量 (上交所债券的数量单位为手)
        ('TotalValueTraded', c_int64),  # 成交总金额 (金额单位精确到元后四位, 即: 1元=10000)
        ('PrevClosePx', c_int32),  # 昨日收盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('OpenPx', c_int32),  # 今开盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('HighPx', c_int32),  # 最高价
        ('LowPx', c_int32),  # 最低价
        ('TradePx', c_int32),  # 成交价 (最新价)
        ('ClosePx', c_int32),  # 今收盘价/期权收盘价 (适用于上交所行情和深交所债券现券交易产品)
        ('IOPV', c_int32),  # 基金份额参考净值/ETF申赎的单位参考净值 (适用于基金)
        ('NAV', c_int32),  # 基金 T-1 日净值 (适用于基金)
        ('TotalLongPosition', c_uint64),  # 合约总持仓量 (适用于期权)
        # 五档买盘价位信息
        ('BidLevels', MdsPriceLevelEntryT * 5),
        # 五档卖盘价位信息
        ('OfferLevels', MdsPriceLevelEntryT * 5),
    ]


class _MdsL1SnapshotUnion(PrintableUnion):
    _fields_ = [
        # 股票、债券、基金行情数据
        ('stock', MdsStockSnapshotBodyT),
        # 期权行情数据
        ('option', MdsStockSnapshotBodyT),
        # 指数行情数据
        ('index', MdsIndexSnapshotBodyT),
    ]


# 完整的 Level1 证券行情全幅消息定义
class MdsL1SnapshotT(PrintableStructure):
    _fields_ = [
        # 行情数据的消息头
        ('head', MdsMktDataSnapshotHeadT),
        ('union', _MdsL1SnapshotUnion),
    ]


class _MdsL2StockSnapshotBodyT_Fund(PrintableStructure):
    _fields_ = [
        ('IOPV', c_int32),  # 基金份额参考净值/ETF申赎的单位参考净值 (适用于基金)
        ('NAV', c_int32),  # 基金 T-1 日净值 (适用于基金, 上交所Level-2实时行情里面没有该字段)
        ('TotalLongPosition', c_uint64),  # 合约总持仓量 (适用于期权)
    ]


class _MdsL2StockSnapshotBodyT_Bond(PrintableStructure):
    _fields_ = [
        ('BondWeightedAvgPx', c_int32),  # 债券加权平均价 (适用于质押式回购及债券现券交易产品, 表示质押式回购成交量加权平均利率及债券现券交易成交量加权平均价)
        ('BondAuctionTradePx', c_int32),  # 深交所债券匹配成交的最近成交价 (仅适用于深交所债券现券交易产品. 价格单位精确到元后四位, 即: 1元=10000)
        ('BondAuctionVolumeTraded', c_uint64),  # 深交所债券匹配成交的成交总量 (仅适用于深交所债券现券交易产品)
    ]


class _MdsL2StockSnapshotBodyT_Union1(PrintableUnion):
    _fields_ = [
        ('fund', _MdsL2StockSnapshotBodyT_Fund),
        ('bond', _MdsL2StockSnapshotBodyT_Bond),
    ]


class _MdsL2StockSnapshotBodyT_PriceLevel(PrintableStructure):
    _fields_ = [
        ('BidPriceLevel', c_int32),  # 买方委托价位数 (实际的委托价位总数, 仅适用于上交所)
        ('OfferPriceLevel', c_int32),  # 卖方委托价位数 (实际的委托价位总数, 仅适用于上交所)
    ]


class _MdsL2StockSnapshotBodyT_Union2(PrintableUnion):
    _fields_ = [
        ('PriceLevel', _MdsL2StockSnapshotBodyT_PriceLevel),
        ('BondAuctionValueTraded', c_int64),  # 深交所债券匹配成交的成交总金额 (仅适用于深交所债券现券交易产品. 金额单位精确到元后四位, 即: 1元=10000)
    ]


# Level2 快照行情定义
# 股票(A、B股)、债券、基金
#
# 关于集合竞价期间的虚拟集合竞价行情 (上交所L2、深交所L2):
# - 集合竞价期间的虚拟成交价通过买卖盘档位揭示, 其中买一和卖一都揭示虚拟成交价格和成交数量,
#   买二或卖二揭示虚拟成交价位上的买剩余量或卖剩余量
class MdsL2StockSnapshotBodyT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 产品实时阶段及标志 C8 / C4
        # 上交所股票 (C8):
        # -# 第 0 位:
        # - ‘S’表示启动 (开市前) 时段, ‘C’表示开盘集合竞价时段, ‘T’表示连续交易时段,
        # - ‘E’表示闭市时段, ‘P’表示产品停牌,
        # - ‘M’表示可恢复交易的熔断时段 (盘中集合竞价), ‘N’表示不可恢复交易的熔断时段 (暂停交易至闭市),
        # - ‘U’表示收盘集合竞价时段。
        # -# 第 1 位:
        # - ‘0’表示此产品不可正常交易,
        # - ‘1’表示此产品可正常交易,
        # - 无意义填空格。
        # - 在产品进入开盘集合竞价、连续交易、收盘集合竞价、熔断(盘中集合竞价)状态时值为‘1’,
        # 在产品进入停牌、熔断(暂停交易至闭市)状态时值为‘0’, 且闭市后保持该产品闭市前的是否可正常交易状态。
        # -# 第 2 位:
        # - ‘0’表示未上市, ‘1’表示已上市。
        # -# 第 3 位:
        # - ‘0’表示此产品在当前时段不接受订单申报,
        # - ‘1’表示此产品在当前时段可接受订单申报。
        # - 仅在交易时段有效，在非交易时段无效。无意义填空格。
        # 上交所期权 (C4):
        # -# 第 0 位:
        # - ‘S’表示启动(开市前)时段, ‘C’表示集合竞价时段, ‘T’表示连续交易时段,
        # - ‘B’表示休市时段, ‘E’表示闭市时段, ‘V’表示波动性中断, ‘P’表示临时停牌, ‘U’收盘集合竞价。
        # - ‘M’表示可恢复交易的熔断 (盘中集合竞价), ‘N’表示不可恢复交易的熔断 (暂停交易至闭市)
        # -# 第 1 位:
        # - ‘0’表示未连续停牌, ‘1’表示连续停牌。(预留, 暂填空格)
        # -# 第 2 位:
        # - ‘0’表示不限制开仓, ‘1’表示限制备兑开仓, ‘2’表示卖出开仓, ‘3’表示限制卖出开仓、备兑开仓,
        # - ‘4’表示限制买入开仓, ‘5’表示限制买入开仓、备兑开仓, ‘6’表示限制买入开仓、卖出开仓,
        # - ‘7’表示限制买入开仓、卖出开仓、备兑开仓
        # -# 第 3 位:
        # - ‘0’表示此产品在当前时段不接受进行新订单申报,
        # - ‘1’表示此产品在当前时段可接受进行新订单申报。
        # - 仅在交易时段有效，在非交易时段无效。
        # 深交所 (C8):
        # -# 第 0 位:
        # - S=启动(开市前) O=开盘集合竞价 T=连续竞价
        # - B=休市 C=收盘集合竞价 E=已闭市 H=临时停牌
        # - A=盘后交易 V=波动性中断
        # -# 第 1 位:
        # - 0=正常状态
        # - 1=全天停牌
        ('TradingPhaseCode', c_char * MDS_MAX_TRADING_PHASE_CODE_LEN),
        ('_filler', c_char * 6),  # 按64位对齐的填充域
        ('NumTrades', c_uint64),  # 成交笔数
        ('TotalVolumeTraded', c_uint64),  # 成交总量 (上交所债券的数量单位为手)
        ('TotalValueTraded', c_int64),  # 成交总金额 (金额单位精确到元后四位, 即: 1元=10000)
        ('PrevClosePx', c_int32),  # 昨日收盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('OpenPx', c_int32),  # 今开盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('HighPx', c_int32),  # 最高价
        ('LowPx', c_int32),  # 最低价
        ('TradePx', c_int32),  # 成交价
        ('ClosePx', c_int32),  # 今收盘价/期权收盘价 (加权平均收盘价, 适用于上交所行情和深交所债券现券交易产品)
        ('union1', _MdsL2StockSnapshotBodyT_Union1),
        ('TotalBidQty', c_int64),  # 委托买入总量
        ('TotalOfferQty', c_int64),  # 委托卖出总量
        ('WeightedAvgBidPx', c_int32),  # 加权平均委买价格
        ('WeightedAvgOfferPx', c_int32),  # 加权平均委卖价格
        ('union2', _MdsL2StockSnapshotBodyT_Union2),
        # 十档买盘价位信息
        ('BidLevels', MdsPriceLevelEntryT * 10),
        # 十档卖盘价位信息
        ('OfferLevels', MdsPriceLevelEntryT * 10),
    ]


# Level2 快照行情的增量更新消息定义 (增量更新消息仅适用于上交所L2)
# 股票(A、B股)、债券、基金
#
# 关于增量更新消息补充说明如下:
# -# 增量更新只有上交所Level2快照有, 深交所行情里面没有
#    - 上交所的L2快照的更新频率为: 每3秒发送一次增量更新消息 (如果行情有变化的话),
#      每60秒发送一次全量快照 (无论行情有无变化)。
# -# 增量和全量快照的推送时点是一样的, 增量并不会比全量更快, 只是信息角度不一样
#    - 在对下游系统进行推送时, 增量快照和完整快照在推送时间上是没有区别的;
#    - MDS会先对交易所发下来的增量更新消息进行整合, 然后根据订阅条件向下游推送完整快照或增量
#      更新消息。
# -# 没有特别需求的话, 不需要订阅增量更新消息, 增量消息处理起来比较麻烦
#
# @note 上交所行情存在更新时间相同但数据不同的Level-2快照。(频率不高, 但会存在这样的数据)
class MdsL2StockSnapshotIncrementalT(PrintableStructure):
    _fields_ = [
        ('NumTrades', c_uint64),  # 成交笔数
        ('TotalVolumeTraded', c_uint64),  # 成交总量
        ('TotalValueTraded', c_int64),  # 成交总金额 (金额单位精确到元后四位, 即: 1元=10000)
        ('OpenPx', c_int32),  # 今开盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('HighPx', c_int32),  # 最高价
        ('LowPx', c_int32),  # 最低价
        ('TradePx', c_int32),  # 成交价
        ('ClosePx', c_int32),  # 今收盘价/期权收盘价 (仅适用于上交所, 深交所行情没有单独的收盘价)
        ('IOPV', c_int32),  # 基金份额参考净值/ETF申赎的单位参考净值 (适用于基金)
        ('TotalBidQty', c_int64),  # 委托买入总量 (上交所债券的数量单位为手)
        ('TotalOfferQty', c_int64),  # 委托卖出总量 (上交所债券的数量单位为手)
        ('WeightedAvgBidPx', c_int32),  # 加权平均委买价格
        ('WeightedAvgOfferPx', c_int32),  # 加权平均委卖价格
        ('BidPriceLevel', c_int32),  # 买方委托价位数 (实际的委托价位总数, 仅适用于上交所)
        ('OfferPriceLevel', c_int32),  # 卖方委托价位数 (实际的委托价位总数, 仅适用于上交所)
        # 最优申买价
        ('BestBidPrice', c_int32),
        # 增量更新消息中是否已经包含了最优申买价位
        ('HasContainedBestBidLevel', c_uint8),
        # 买盘价位数量 (不包括已删除且大于最优申买价的价位)
        ('NoBidLevel', c_uint8),
        # 买盘价位列表中是否有从队列尾部删除的价位
        ('_hasDeletedAtBidTail', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8),
        # 最优申卖价
        ('BestOfferPrice', c_int32),
        # 增量更新消息中是否已经包含了最优申买价位
        ('HasContainedBestOfferLevel', c_uint8),
        # 卖盘价位数量 (不包括已删除且小于最优申卖价的价位)
        ('NoOfferLevel', c_uint8),
        # 卖盘价位列表中是否有从队列尾部删除的价位
        ('_hasDeletedAtOfferTail', c_uint8),
        # 按64位对齐的填充域
        ('_filler2', c_uint8),
        # (发生变更的价位列表中) 各个价位的运算操作
        # - 1 = Add
        # - 2 = Update
        # - 3 = Delete
        # @see eMdsL2PriceLevelOperatorT
        ('PriceLevelOperator', c_uint8 * MDS_MAX_L2_PRICE_LEVEL_INCREMENTS),
        # 发生变更的价位列表 (该字段为变长数组, 实际元素数量为: NoBidLevel + NoOfferLevel)
        ('PriceLevels', MdsPriceLevelEntryT * MDS_MAX_L2_PRICE_LEVEL_INCREMENTS),
    ]


# Level2 委托队列信息 (买一／卖一前五十笔委托明细)
class MdsL2BestOrdersSnapshotBodyT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('_filler', c_uint8 * 5),  # 按64位对齐的填充域
        ('NoBidOrders', c_uint8),  # 买一价位的揭示委托笔数
        ('NoOfferOrders', c_uint8),  # 卖一价位的揭示委托笔数
        ('TotalVolumeTraded', c_uint64),  # 成交总量 (来自快照行情的冗余字段)
        ('BestBidPrice', c_int32),  # 最优申买价
        ('BestOfferPrice', c_int32),  # 最优申卖价
        # 买一价位的委托明细(前50笔)
        ('BidOrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_CNT),
        # 卖一价位的委托明细(前50笔)
        ('OfferOrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_CNT),
    ]


# Level2 委托队列的增量更新信息 (买一／卖一前五十笔委托明细, 增量更新消息仅适用于上交所L2)
class MdsL2BestOrdersSnapshotIncrementalT(PrintableStructure):
    _fields_ = [
        # 成交总量 (来自快照行情的冗余字段)
        ('TotalVolumeTraded', c_uint64),
        # 最优申买价
        ('BestBidPrice', c_int32),
        # 增量更新消息中是否已经包含了最优申买价位
        ('HasContainedBestBidLevel', c_uint8),
        # 当前最优申买价下被连续删除掉的订单笔数
        ('ContinualDeletedBidOrders', c_uint8),
        # 买盘需要更新的笔数 (不包括被连续删除掉的订单)
        ('NoBidOrders', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8),
        # 最优申卖价
        ('BestOfferPrice', c_int32),
        # 增量更新消息中是否已经包含了最优申买价位
        ('HasContainedBestOfferLevel', c_uint8),
        # 当前最优申卖价下被连续删除掉的订单笔数
        ('ContinualDeletedOfferOrders', c_uint8),
        # 卖盘需要更新的笔数 (不包括被连续删除掉的订单)
        ('NoOfferOrders', c_uint8),
        # 按64位对齐的填充域
        ('_filler2', c_uint8),
        # (发生变更的委托明细中) 待更新或删除的订单位置 (即需要删除和更新的上一次订单的位置)
        # - 订单位置从 0 开始
        # - 小于0, 表示删除该位置的订单
        # - 大于等于0, 表示更新该位置的订单
        # - CHAR_MAX, 表示新增
        ('OperatorEntryID', c_int8 * MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS),
        # 发生变更的委托明细 (该字段为变长数组, 实际元素数量为: NoBidOrders + NoOfferOrders)
        ('OrderQty', c_int32 * MDS_MAX_L2_DISCLOSE_ORDERS_INCREMENTS),
    ]


# Level2 市场总览消息定义
class MdsL2MarketOverviewT(PrintableStructure):
    _fields_ = [
        ('OrigDate', c_int32),  # 市场日期 (YYYYMMDD)
        ('OrigTime', c_int32),  # 市场时间 (HHMMSSss0, 实际精度为百分之一秒(HHMMSSss))
        ('_exchSendingTime', c_int32),  # 交易所发送时间 (HHMMSS000, 实际精度为秒(HHMMSS))
        ('_mdsRecvTime', c_int32),  # MDS接收到时间 (HHMMSSsss)
    ]


class _MdsMktDataSnapshotUnion(PrintableUnion):
    _fields_ = [
        # Level2 快照行情(股票、债券、基金)
        ('l2Stock', MdsL2StockSnapshotBodyT),
        # Level2 快照行情的增量更新消息
        ('l2StockIncremental', MdsL2StockSnapshotIncrementalT),
        # Level2 委托队列(买一／卖一前五十笔委托明细)
        ('l2BestOrders', MdsL2BestOrdersSnapshotBodyT),
        # Level2 委托队列(买一／卖一前五十笔委托明细)的增量更新消息
        ('l2BestOrdersIncremental', MdsL2BestOrdersSnapshotIncrementalT),
        # Level1 股票、债券、基金行情数据
        ('stock', MdsStockSnapshotBodyT),
        # Level1/Level2 期权行情数据
        ('option', MdsStockSnapshotBodyT),
        # Level1/Level2 指数行情数据
        ('index', MdsIndexSnapshotBodyT),
        # Level2 市场总览 (仅适用于上交所)
        ('l2MarketOverview', MdsL2MarketOverviewT),
    ]


# (对外发布的) 完整的 Level1/Level2 快照行情定义
class MdsMktDataSnapshotT(PrintableStructure):
    _fields_ = [
        # 行情数据的消息头
        ('head', MdsMktDataSnapshotHeadT),
        ('union', _MdsMktDataSnapshotUnion),
    ]


# Level2 逐笔成交行情定义
class MdsL2TradeT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码(沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票) @see eMdsMdProductTypeT
        ('_isRepeated', c_int8),  # 是否是重复的行情 (内部使用, 小于0表示回补的逐笔重建数据)
        ('_origMdSource', c_uint8),  # 原始行情数据来源 @see eMdsMsgSourceT
        ('tradeDate', c_int32),  # 交易日期 (YYYYMMDD, 非官方数据)
        ('TransactTime', c_int32),  # 成交时间 (HHMMSSsss)
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        ('ChannelNo', c_uint16),  # 频道代码 [0..9999]
        ('_reserve', c_uint16),  # 按64位对齐的保留字段
        # 深交所消息记录号/上交所成交序号 (从1开始, 按频道连续)
        # - 深交所为逐笔成交+逐笔委托统一编号
        # - 上交所新债券行情为逐笔成交+逐笔委托统一编号 (TickIndex)
        # - 上交所(非债券行情)为逐笔成交独立编号 (TradeIndex)
        ('ApplSeqNum', c_int32),
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 成交类别 (仅适用于深交所)
        # - 深交所: '4'=撤销, 'F'=成交
        # - 上交所: 将固定为 'F' (成交)
        # - @see eMdsL2TradeExecTypeT
        ('ExecType', c_char),
        # 内外盘标志 (仅适用于上交所)
        # - 上交所: 'B'=外盘(主动买), 'S'=内盘(主动卖), 'N'=未知
        # - 深交所: 将固定为 'N' (未知)
        # - @see eMdsL2TradeBSFlagT
        ('TradeBSFlag', c_char),
        # 行情数据类别 @see eMdsSubStreamTypeT
        ('subStreamType', c_uint8),
        # 业务序列号 (仅适用于上交所)
        # - 仅适用于上交所, 逐笔成交+逐笔委托统一编号, 从1开始, 按频道连续
        # - 对于深交所, 该字段将固定为 0
        # - 对于上交所新债券行情, 该字段的取值将与 ApplSeqNum 相同
        ('SseBizIndex', c_uint32),
        # 为保持协议兼容而定义的填充域
        ('_filler', c_uint64),
        # 成交价格 (价格单位精确到元后四位, 即: 1元=10000)
        ('TradePrice', c_int32),
        # 成交数量 (仅上交所债券的数量单位为手, 其它均为股或张)
        ('TradeQty', c_int32),
        # 成交金额 (金额单位精确到元后四位, 即: 1元=10000)
        ('TradeMoney', c_int64),
        # 买方订单号 (从 1 开始计数, 0 表示无对应委托)
        # - 对于深交所, 该字段对应于买方逐笔委托的 ApplSeqNum 字段
        # - 对于上交所, 该字段对应于买方逐笔委托的 SseOrderNo 字段
        ('BidApplSeqNum', c_int64),
        # 卖方订单号 (从 1 开始计数, 0 表示无对应委托)
        # - 对于深交所, 该字段对应于卖方逐笔委托的 ApplSeqNum 字段
        # - 对于上交所, 该字段对应于卖方逐笔委托的 SseOrderNo 字段
        ('OfferApplSeqNum', c_int64),
        # 消息原始接收时间 (从网络接收到数据的最初时间)
        ('_origNetTime', STimespec32T),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息加工处理完成时间
        ('_processedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# Level2 逐笔委托行情定义
class MdsL2OrderT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码(沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票) @see eMdsMdProductTypeT
        ('_isRepeated', c_int8),  # 是否是重复的行情 (内部使用, 小于0表示回补的逐笔重建数据)
        ('_origMdSource', c_uint8),  # 原始行情数据来源 @see eMdsMsgSourceT
        ('tradeDate', c_int32),  # 交易日期 YYYYMMDD (自然日)
        ('TransactTime', c_int32),  # 委托时间 HHMMSSsss
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        ('ChannelNo', c_uint16),  # 频道代码 [0..9999]
        ('_reserve', c_uint16),  # 按64位对齐的保留字段
        # 深交所消息记录号/上交所委托序号 (从1开始, 按频道连续)
        # - 深交所为逐笔成交+逐笔委托统一编号
        # - 上交所新债券行情为逐笔成交+逐笔委托统一编号 (TickIndex)
        # - 上交所(非债券行情)为逐笔委托独立编号 (OrderIndex)
        ('ApplSeqNum', c_int32),
        # 证券代码 C6 / C8 (如: '000001' 等)
        ('SecurityID', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 买卖方向
        # - 深交所: '1'=买, '2'=卖, 'G'=借入, 'F'=出借
        # - 上交所: '1'=买, '2'=卖
        ('Side', c_char),
        # 订单类型
        # - 深交所: '1'=市价, '2'=限价, 'U'=本方最优
        # - 上交所: 'A'=委托订单-增加(新订单), 'D'=委托订单-删除(撤单)
        ('OrderType', c_char),
        # 行情数据类别 @see eMdsSubStreamTypeT
        ('subStreamType', c_uint8),
        # 业务序列号 (仅适用于上交所)
        # - 仅适用于上交所, 逐笔成交+逐笔委托统一编号, 从1开始, 按频道连续
        # - 对于深交所, 该字段将固定为 0
        # - 对于上交所新债券行情, 该字段的取值将与 ApplSeqNum 相同
        ('SseBizIndex', c_uint32),
        # 原始订单号 (仅适用于上交所)
        # - 仅适用于上交所, 和逐笔成交中的买方/卖方订单号相对应
        # - 对于深交所, 该字段将固定为 0
        ('SseOrderNo', c_int64),
        # 委托价格 (价格单位精确到元后四位, 即: 1元=10000)
        ('Price', c_int32),
        # 委托数量
        # - @note 对于上交所, 该字段的含义为剩余委托量或撤单数量:
        # - 对于上交所, 当 OrderType='A' 时, 该字段表示的是剩余委托量 (竞价撮合成交后的剩余委托数量)
        # - 对于上交所, 当 OrderType='D' 时, 该字段表示的是撤单数量
        # - @note 对于上交所新债券行情, 该字段的含义为原始委托数量
        ('OrderQty', c_int32),
        # 消息原始接收时间 (从网络接收到数据的最初时间)
        ('_origNetTime', STimespec32T),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息加工处理完成时间
        ('_processedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# 证券信息(股票/基金/债券)的静态数据结构体定义
class MdsStockStaticInfoT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('securityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('exchId', c_uint8),  # 交易所代码 (沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/期权/指数) @see eMdsMdProductTypeT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('currType', c_uint8),  # 币种 @see eOesCurrTypeT
        ('qualificationClass', c_uint8),  # 投资者适当性管理分类 @see eOesQualificationClassT
        ('_filler1', c_uint8 * 5),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        ('securityStatus', c_uint32),  # 证券状态 @see eOesSecurityStatusT
        ('securityAttribute', c_uint32),  # 证券属性 @see eOesSecurityAttributeT
        ('suspFlag', c_uint8),  # 连续停牌标识 (0 未停牌, 1 已停牌)
        ('isDayTrading', c_uint8),  # 是否支持当日回转交易 (0 不支持, 1 支持)
        ('isRegistration', c_uint8),  # 是否注册制 (0 核准制, 1 注册制)
        ('isCrdCollateral', c_uint8),  # 是否为融资融券担保品 (0 不是担保品, 1 是担保品)
        # 是否为融资标的 (0 不是融资标的, 1 是融资标的)
        ('isCrdMarginTradeUnderlying', c_uint8),
        # 是否为融券标的 (0 不是融券标的, 1 是融券标的)
        ('isCrdShortSellUnderlying', c_uint8),
        ('isNoProfit', c_uint8),  # 是否尚未盈利 (0 已盈利, 1 未盈利 (仅适用于科创板和创业板产品))
        ('isWeightedVotingRights', c_uint8),  # 是否存在投票权差异 (0 无差异, 1 存在差异 (仅适用于科创板和创业板产品))
        ('isVie', c_uint8),  # 是否具有协议控制框架 (0 没有, 1 有 (仅适用于创业板产品))
        ('pricingMethod', c_uint8),  # 计价方式 (仅适用于债券 @see eOesPricingMethodT)
        ('_filler2', c_uint8 * 6),  # 按64位对齐的填充域
        ('upperLimitPrice', c_int32),  # 涨停价 (单位精确到元后四位, 即: 1元=10000)
        ('lowerLimitPrice', c_int32),  # 跌停价 (单位精确到元后四位, 即: 1元=10000)
        ('priceTick', c_int32),  # 价格档位 (价格单位精确到元后四位, 即: 1元=10000)
        ('prevClose', c_int32),  # 前收盘价 (价格单位精确到元后四位, 即: 1元=10000)
        ('lmtBuyMaxQty', c_int32),  # 单笔限价买委托数量上限
        ('lmtBuyMinQty', c_int32),  # 单笔限价买委托数量下限
        ('lmtBuyQtyUnit', c_int32),  # 单笔限价买入单位
        ('mktBuyQtyUnit', c_int32),  # 单笔市价买入单位
        ('mktBuyMaxQty', c_int32),  # 单笔市价买委托数量上限
        ('mktBuyMinQty', c_int32),  # 单笔市价买委托数量下限
        ('lmtSellMaxQty', c_int32),  # 单笔限价卖委托数量上限
        ('lmtSellMinQty', c_int32),  # 单笔限价卖委托数量下限
        ('lmtSellQtyUnit', c_int32),  # 单笔限价卖出单位
        ('mktSellQtyUnit', c_int32),  # 单笔市价卖出单位
        ('mktSellMaxQty', c_int32),  # 单笔市价卖委托数量上限
        ('mktSellMinQty', c_int32),  # 单笔市价卖委托数量下限
        ('bondInterest', c_int64),  # 债券的每张应计利息 (单位精确到元后八位)
        ('parValue', c_int64),  # 面值 (价格单位精确到元后四位, 即: 1元=10000)
        ('auctionLimitType', c_uint8),  # 连续交易时段的有效竞价范围限制类型 @see eOesAuctionLimitTypeT
        ('auctionReferPriceType', c_uint8),  # 连续交易时段的有效竞价范围基准价类型 @see eOesAuctionReferPriceTypeT
        ('_filler3', c_uint8 * 2),  # 按64位对齐的填充域
        ('auctionUpDownRange', c_int32),  # 连续交易时段的有效竞价范围涨跌幅度 (百分比或绝对价格, 取决于'有效竞价范围限制类型')
        ('listDate', c_int32),  # 上市日期
        ('maturityDate', c_int32),  # 到期日期 (仅适用于债券等有发行期限的产品)
        ('outstandingShare', c_int64),  # 总股本 (即: 总发行数量, 上交所无该字段, 未额外维护时取值为0)
        ('publicFloatShare', c_int64),  # 流通股数量
        # 基础证券代码 (标的产品代码)
        ('underlyingSecurityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 按64位对齐的填充域
        ('_filler4', c_uint8 * 7),
        # 证券名称 (UTF-8 编码)
        ('securityName', c_char * MDS_MAX_SECURITY_NAME_LEN),
        # 证券长名称 (UTF-8 编码)
        ('securityLongName', c_char * MDS_MAX_SECURITY_LONG_NAME_LEN),
        # 证券英文名称
        ('securityEnglishName', c_char * MDS_MAX_SECURITY_ENGLISH_NAME_LEN),
        # ISIN代码
        ('securityIsinCode', c_char * MDS_MAX_SECURITY_ISIN_CODE_LEN),
        # 预留的备用字段1
        ('_reserve1', c_char * 24),
        # 预留的备用字段2
        ('_reserve2', c_char * 64),
    ]


# 期权合约信息的静态数据结构体定义
class MdsOptionStaticInfoT(PrintableStructure):
    _fields_ = [
        # 期权合约代码 C8 (如: '10001230' 等)
        ('securityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        ('exchId', c_uint8),  # 交易所代码 (沪/深) @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/期权/指数) @see eMdsMdProductTypeT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('contractType', c_uint8),  # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('exerciseType', c_uint8),  # 行权方式 @see eOesOptExerciseTypeT
        ('deliveryType', c_uint8),  # 交割方式 @see eOesOptDeliveryTypeT
        ('_filler1', c_uint8 * 4),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的期权合约代码)
        ('contractUnit', c_int32),  # 合约单位 (经过除权除息调整后的单位)
        ('exercisePrice', c_int32),  # 期权行权价 (经过除权除息调整后的价格, 单位精确到元后四位, 即: 1元=10000)
        ('deliveryDate', c_int32),  # 交割日期 (格式为YYYYMMDD)
        ('deliveryMonth', c_int32),  # 交割月份 (格式为YYYYMM)
        ('listDate', c_int32),  # 上市日期 (格式为YYYYMMDD)
        ('lastTradeDay', c_int32),  # 最后交易日 (格式为YYYYMMDD)
        ('exerciseBeginDate', c_int32),  # 行权起始日期 (格式为YYYYMMDD)
        ('exerciseEndDate', c_int32),  # 行权结束日期 (格式为YYYYMMDD)
        ('prevClosePrice', c_int32),  # 合约前收盘价 (单位精确到元后四位, 即: 1元=10000)
        ('prevSettlPrice', c_int32),  # 合约前结算价 (单位精确到元后四位, 即: 1元=10000)
        ('underlyingClosePrice', c_int32),  # 标的证券前收盘价 (单位精确到元后四位, 即: 1元=10000)
        ('priceTick', c_int32),  # 最小报价单位 (单位精确到元后四位, 即: 1元=10000)
        ('upperLimitPrice', c_int32),  # 涨停价 (单位精确到元后四位, 即: 1元=10000)
        ('lowerLimitPrice', c_int32),  # 跌停价 (单位精确到元后四位, 即: 1元=10000)
        ('buyQtyUnit', c_int32),  # 买入单位
        ('lmtBuyMaxQty', c_int32),  # 限价买数量上限 (单笔申报的最大张数)
        ('lmtBuyMinQty', c_int32),  # 限价买数量下限 (单笔申报的最小张数)
        ('mktBuyMaxQty', c_int32),  # 市价买数量上限 (单笔申报的最大张数)
        ('mktBuyMinQty', c_int32),  # 市价买数量下限 (单笔申报的最小张数)
        ('sellQtyUnit', c_int32),  # 卖出单位
        ('lmtSellMaxQty', c_int32),  # 限价卖数量上限 (单笔申报的最大张数)
        ('lmtSellMinQty', c_int32),  # 限价卖数量下限 (单笔申报的最小张数)
        ('mktSellMaxQty', c_int32),  # 市价卖数量上限 (单笔申报的最大张数)
        ('mktSellMinQty', c_int32),  # 市价卖数量下限 (单笔申报的最小张数)
        ('sellMargin', c_int64),  # 单位保证金 (未上调的今卖开每张保证金, 单位精确到元后四位, 即: 1元=10000)
        # 期权合约交易所代码
        ('contractId', c_char * MDS_MAX_CONTRACT_EXCH_ID_LEN),
        # 期权合约名称 (UTF-8 编码)
        ('securityName', c_char * MDS_MAX_SECURITY_NAME_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * MDS_MAX_INSTR_CODE_LEN),
        # 按64位对齐的填充域
        ('_filler2', c_uint8 * 7),
        ('_reserve', c_char * 32),  # 预留的备用字段
    ]


# Level1 证券行情全幅消息的完整消息体定义
class MdsL1SnapshotBodyT(PrintableUnion):
    _fields_ = [
        # 股票、债券、基金行情数据
        ('stock', MdsStockSnapshotBodyT),
        # 期权行情数据
        ('option', MdsStockSnapshotBodyT),
        # 指数行情数据
        ('index', MdsIndexSnapshotBodyT),
    ]


# Level2 快照行情的完整消息体定义
class MdsL2SnapshotBodyT(PrintableUnion):
    _fields_ = [
        # Level2 快照行情(股票、债券、基金、期权)
        ('l2Stock', MdsL2StockSnapshotBodyT),
        # Level2 快照行情的增量更新消息
        ('l2StockIncremental', MdsL2StockSnapshotIncrementalT),
        # Level2 委托队列(买一／卖一前五十笔委托明细)
        ('l2BestOrders', MdsL2BestOrdersSnapshotBodyT),
        # Level2 委托队列(买一／卖一前五十笔委托明细)的增量更新消息
        ('l2BestOrdersIncremental', MdsL2BestOrdersSnapshotIncrementalT),
        # 期权行情数据
        ('option', MdsStockSnapshotBodyT),
        # 指数行情数据
        ('index', MdsIndexSnapshotBodyT),
        # Level2 市场总览 (仅适用于上交所)
        ('l2MarketOverview', MdsL2MarketOverviewT),
    ]


# 完整的行情数据消息体定义
class MdsWholeMktMsgBodyT(PrintableUnion):
    _fields_ = [
        # 快照行情 (Level1 快照 / Level2 快照 / 指数行情 / 期权行情)
        ('mktDataSnapshot', MdsMktDataSnapshotT),
        # Level2 逐笔成交行情
        ('trade', MdsL2TradeT),
        # Level2 逐笔委托行情
        ('order', MdsL2OrderT),
        # 市场状态消息 (仅适用于上交所)
        ('trdSessionStatus', MdsTradingSessionStatusMsgT),
        # 证券实时状态消息 (仅适用于深交所)
        ('securityStatus', MdsSecurityStatusMsgT),
    ]


DATASIZE_MDS_L2_STOCK_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2StockSnapshotBodyT))
DATASIZE_MDS_L2_BEST_ORDERS_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2BestOrdersSnapshotBodyT))
DATASIZE_MDS_STOCK_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsStockSnapshotBodyT))
DATASIZE_MDS_OPTION_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsStockSnapshotBodyT))
DATASIZE_MDS_INDEX_SNAPSHOT = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsIndexSnapshotBodyT))
DATASIZE_MDS_L2_MARKET_OVERVIEW = (sizeof(MdsMktDataSnapshotHeadT) + sizeof(MdsL2MarketOverviewT))


# 证券行情查询的请求报文
class MdsQryMktDataSnapshotReqT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/指数/期权) @see eMdsMdProductTypeT
        ('_filler', c_uint8 * 2),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
    ]


# (上证)市场状态查询的请求报文
class MdsQryTrdSessionStatusReqT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/指数/期权) @see eMdsMdProductTypeT
        ('_filler', c_uint8 * 6),  # 按64位对齐的填充域
    ]


# 查询请求的消息头定义
class MdsQryReqHeadT(PrintableStructure):
    _fields_ = [
        ('maxPageSize', c_int32),  # 最大分页大小
        ('lastPosition', c_int32),  # 查询起始位置
    ]


# 查询应答的消息头定义
class MdsQryRspHeadT(PrintableStructure):
    _fields_ = [
        ('itemCount', c_int32),  # 查询到的信息条目数
        ('lastPosition', c_int32),  # 查询到的最后一条信息的位置
        ('isEnd', c_int8),  # 是否是当前查询最后一个包
        ('_filler', c_uint8 * 7),  # 按64位对齐的填充域
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询定位的游标结构
class MdsQryCursorT(PrintableStructure):
    _fields_ = [
        # 查询位置
        ('seqNo', c_int32),
        # 是否是当前最后一个包
        ('isEnd', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_int8 * 3),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 行情查询请求中的证券代码信息
class MdsQrySecurityCodeEntryT(PrintableStructure):
    _fields_ = [
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/期权/指数) @see eMdsMdProductTypeT
        ('_filler', c_uint8 * 2),  # 按64位对齐的填充域
    ]


# 证券静态信息查询的过滤条件定义
class MdsQryStockStaticInfoFilterT(PrintableStructure):
    _fields_ = [
        # 证券代码 C6 / C8 (如: '600000' 等)
        ('securityId', c_char * MDS_MAX_POSTFIXED_INSTR_CODE_LEN),
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('_filler', c_uint8 * 5),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码) 如果同时指定 securityId, 则优先使用 securityId
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 证券静态信息查询的请求报文
class MdsQryStockStaticInfoReqT(PrintableStructure):
    _fields_ = [
        # 查询请求的消息头
        ('reqHead', MdsQryReqHeadT),
        # 查询请求的过滤条件
        ('qryFilter', MdsQryStockStaticInfoFilterT),
    ]


# 证券静态信息查询的应答报文
class MdsQryStockStaticInfoRspT(PrintableStructure):
    _fields_ = [
        # 查询应答的消息头
        ('rspHead', MdsQryRspHeadT),
        # 证券静态信息数组 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('qryItems', MdsStockStaticInfoT * 1),
    ]


# 期权合约静态信息查询的过滤条件定义
class MdsQryOptionStaticInfoFilterT(PrintableStructure):
    _fields_ = [
        # 期权合约代码 C8 (如: '10001230' 等)
        ('securityId', c_char * MDS_MAX_POSTFIXED_INSTR_CODE_LEN),
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('_filler', c_uint8 * 5),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的期权合约代码) 如果同时指定 securityId, 则优先使用 securityId
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 期权合约静态信息查询的请求报文
class MdsQryOptionStaticInfoReqT(PrintableStructure):
    _fields_ = [
        # 查询请求的消息头
        ('reqHead', MdsQryReqHeadT),
        # 查询请求的过滤条件
        ('qryFilter', MdsQryOptionStaticInfoFilterT),
    ]


# 期权合约静态信息查询的应答报文
class MdsQryOptionStaticInfoRspT(PrintableStructure):
    _fields_ = [
        # 查询应答的消息头
        ('rspHead', MdsQryRspHeadT),
        # 期权合约静态信息数组 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('qryItems', MdsOptionStaticInfoT * 1),
    ]


# 证券静态信息查询的过滤条件定义
class MdsQryStockStaticInfoListFilterT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('_filler', c_uint8 * 5),  # 按64位对齐的填充域
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 证券静态信息查询的请求报文
class MdsQryStockStaticInfoListReqT(PrintableStructure):
    _fields_ = [
        # 查询请求的消息头
        ('reqHead', MdsQryReqHeadT),
        # 查询请求的过滤条件
        ('qryFilter', MdsQryStockStaticInfoListFilterT),
        # 待查询的证券代码数量
        ('securityCodeCnt', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 待查询的证券代码列表 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('securityCodeList', MdsQrySecurityCodeEntryT * 1),
    ]


# 证券静态信息查询的应答报文
class MdsQryStockStaticInfoListRspT(PrintableStructure):
    _fields_ = [
        # 查询应答的消息头
        ('rspHead', MdsQryRspHeadT),
        # 证券静态信息数组 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('qryItems', MdsStockStaticInfoT * 1),
    ]


# 期权合约静态信息查询的应答报文
class MdsQryOptionStaticInfoListRspT(PrintableStructure):
    _fields_ = [
        # 查询应答的消息头
        ('rspHead', MdsQryRspHeadT),
        # 期权合约静态信息数组 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('qryItems', MdsOptionStaticInfoT * 1),
    ]


# 行情快照信息查询的过滤条件定义
class MdsQrySnapshotListFilterT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 行情产品类型 (股票/期权/指数) @see eMdsMdProductTypeT
        ('oesSecurityType', c_uint8),  # 证券类型 (股票/债券/基金/...) @see eOesSecurityTypeT
        ('subSecurityType', c_uint8),  # 证券子类型 @see eOesSubSecurityTypeT
        ('mdLevel', c_uint8),  # 行情数据级别 (Level1 / Level2) @see eMdsMdLevelT
        ('_filler', c_uint8 * 11),  # 按64位对齐的填充域
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 行情快照信息查询的请求报文
class MdsQrySnapshotListReqT(PrintableStructure):
    _fields_ = [
        # 查询请求的消息头
        ('reqHead', MdsQryReqHeadT),
        # 查询请求的过滤条件
        ('qryFilter', MdsQrySnapshotListFilterT),
        # 待查询的证券代码数量
        ('securityCodeCnt', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 待查询的证券代码列表 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('securityCodeList', MdsQrySecurityCodeEntryT * 1),
    ]


# 行情快照信息查询的应答报文
class MdsQrySnapshotListRspT(PrintableStructure):
    _fields_ = [
        # 查询应答的消息头
        ('rspHead', MdsQryRspHeadT),
        # 五档快照信息数组 (最大大小为 MDS_QRYRSP_MAX_STOCK_CNT)
        ('qryItems', MdsL1SnapshotT * 1),
    ]


# 应用程序升级源信息
class MdsApplUpgradeSourceT(PrintableStructure):
    _fields_ = [
        # IP地址
        ('ipAddress', c_char * MDS_MAX_IP_LEN),
        # 协议名称
        ('protocol', c_char * MDS_APPL_UPGRADE_PROTOCOL_MAX_LEN),
        # 用户名
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        # 登录密码
        ('password', c_char * MDS_MAX_PASSWORD_LEN),
        # 登录密码的加密方法
        ('encryptMethod', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 根目录地址
        ('homePath', c_char * SPK_MAX_PATH_LEN),
        # 文件名称
        ('fileName', c_char * SPK_MAX_PATH_LEN),
    ]


# 单个应用程序升级信息
class MdsApplUpgradeItemT(PrintableStructure):
    _fields_ = [
        # 应用程序名称
        ('applName', c_char * MDS_MAX_COMP_ID_LEN),
        # 应用程序的最低协议版本号
        ('minApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        # 应用程序的最高协议版本号
        ('maxApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        # 废弃的应用版本号列表
        ('discardApplVerId', c_char * MDS_VER_ID_MAX_LEN * MDS_APPL_DISCARD_VERSION_MAX_COUNT),
        # 废弃版本号的数目
        ('discardVerCount', c_int32),
        # 最新协议版本的日期
        ('newApplVerDate', c_int32),
        # 应用程序的最新协议版本号
        ('newApplVerId', c_char * MDS_VER_ID_MAX_LEN),
        # 最新协议版本的标签信息
        ('newApplVerTag', c_char * MDS_CLIENT_TAG_MAX_LEN),
        # 主用升级源配置信息
        ('primarySource', MdsApplUpgradeSourceT),
        # 备用升级源配置信息
        ('secondarySource', MdsApplUpgradeSourceT),
    ]


# MDS周边应用程序升级信息
class MdsApplUpgradeInfoT(PrintableStructure):
    _fields_ = [
        # 客户端升级配置信息
        ('clientUpgradeInfo', MdsApplUpgradeItemT),
        # C_API升级配置信息
        ('cApiUpgradeInfo', MdsApplUpgradeItemT),
        # JAVA_API升级配置信息
        ('javaApiUpgradeInfo', MdsApplUpgradeItemT),
    ]


# 查询周边应用升级配置信息应答
class MdsQryApplUpgradeInfoRspT(PrintableStructure):
    _fields_ = [
        ('applUpgradeInfo', MdsApplUpgradeInfoT),
    ]


# 行情订阅请求的订阅产品条目
class MdsMktDataRequestEntryT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eMdsExchangeIdT
        ('mdProductType', c_uint8),  # 证券类型 @see eMdsMdProductTypeT
        ('_filler', c_uint8 * 2),  # 按64位对齐的填充域
        ('instrId', c_int32),  # 证券代码 (转换为整数类型的证券代码)
    ]


# 行情订阅请求报文
#
# - 对于可同时订阅产品数量有如下限制:
#   - 每个订阅请求中最多能同时指定 4000 只产品, 可以通过追加订阅的方式订阅更多数量的产品
#   - 对于沪/深两市的现货产品没有总订阅数量的限制, 可以订阅任意数量的产品
#   - 对于沪/深两市的期权产品, 限制对每个市场最多允许同时订阅 2000 只期权产品
#
# @see MdsMktDataRequestEntryT
class MdsMktDataRequestReqT(PrintableStructure):
    _fields_ = [
        # 订阅模式
        # -  0: (Set)          重新订阅, 设置为订阅列表中的股票 (之前的订阅参数将被清空)
        # -  1: (Append)       追加订阅, 增加订阅列表中的股票
        # -  2: (Delete)       删除订阅, 删除订阅列表中的股票
        # 新增的批量订阅模式定义 (@since v0.15.9.1)
        # - 10: (BatchBegin)   批量订阅-开始订阅, 开始一轮新的批量订阅 (之前的订阅参数将被清空,
        # 行情推送也将暂停直到批量订阅结束)
        # - 11: (BatchAppend)  批量订阅-追加订阅, 增加订阅列表中的股票
        # - 12: (BatchDelete)  批量订阅-删除订阅, 删除订阅列表中的股票
        # - 13: (BatchEnd)     批量订阅-结束订阅, 结束本轮的批量订阅, 提交和启用本轮的订阅参数
        # @see eMdsSubscribeModeT
        ('subMode', c_uint8),
        # 数据模式, 订阅最新的行情快照还是所有时点的数据
        # -  0: (LatestSimplified) 只订阅最新的行情快照数据, 并忽略和跳过已经过时的数据
        # - 该模式推送的数据量最小, 没有重复数据, 也不会重复发送最新快照
        # - 该模式在时延和带宽方面都相对优秀, 如果没有特殊需求, 推荐使用该模式即可
        # -  1: (LatestTimely) 只订阅最新的行情快照数据, 并立即发送最新数据
        # - 只要有行情更新事件, 便立即推送该产品的最新行情, 但也会因此重复发送多次相同的最新行情
        # - 如果某些产品的交易很活跃, 而客户端处理又比较耗时的话, 那么该模式可能会更及时的获取到
        # 这些产品的最新行情
        # - 此外, 因为与 AllIncrements 模式下的数据一一对应, 可以方便与增量更新消息进行比对测试
        # - 通常情况下, 推荐使用 LatestSimplified 模式即可
        # -  2: (AllIncrements) 订阅所有时点的行情快照数据 (包括Level2增量更新消息)
        # - 该模式会推送所有时点的行情数据, 包括Level2行情快照的增量更新消息
        # - 如果需要获取全量的行情明细, 或者需要直接使用Level2的增量更新消息, 可以使用该模式
        # @see eMdsSubscribedTickTypeT
        ('tickType', c_uint8),
        # 上证股票(股票/债券/基金)产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情 (为兼容之前的版本, 也可以赋值为 -1)
        # -  2: (Disable) 禁用该市场下的所有股票/债券/基金行情
        # @see eMdsMktSubscribeFlagT
        ('sseStockFlag', c_int8),
        # 上证指数产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情
        # -  2: (Disable) 禁用该市场下的所有指数行情
        # @see eMdsMktSubscribeFlagT
        ('sseIndexFlag', c_int8),
        # 上证期权产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情
        # -  2: (Disable) 禁用该市场下的所有期权行情
        # @see eMdsMktSubscribeFlagT
        ('sseOptionFlag', c_int8),
        # 深圳股票(股票/债券/基金)产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情
        # -  2: (Disable) 禁用该市场下的所有股票/债券/基金行情
        # @see eMdsMktSubscribeFlagT
        ('szseStockFlag', c_int8),
        # 深圳指数产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情
        # -  2: (Disable) 禁用该市场下的所有指数行情
        # @see eMdsMktSubscribeFlagT
        ('szseIndexFlag', c_int8),
        # 深圳期权产品的订阅标志
        # -  0: (Default) 根据订阅列表订阅产品行情
        # -  1: (All) 订阅该市场和证券类型下的所有产品行情
        # -  2: (Disable) 禁用该市场下的所有期权行情
        # @see eMdsMktSubscribeFlagT
        ('szseOptionFlag', c_int8),
        # 在推送实时行情数据之前, 是否需要推送已订阅产品的初始的行情快照
        # -  0: 不需要推送初始的行情快照
        # -  1: 需要推送初始的行情快照, 即确保客户端可以至少收到一幅已订阅产品的快照行情 (如果有的话)
        # @note    从 0.15.9.1 开始, 允许在会话过程中任意时间指定 isRequireInitialMktData
        # 标志来订阅初始快照。不过频繁订阅初始行情快照, 会对当前客户端的行情获取速度产
        # 生不利影响。应谨慎使用, 避免频繁订阅
        # @note    当订阅模式为 Append/Delete/BatchDelete 时将忽略
        # isRequireInitialMktData、beginTime 这两个订阅参数
        ('isRequireInitialMktData', c_uint8),
        # 待订阅的内部频道号 (供内部使用, 尚未对外开放)
        ('_channelNos', c_uint8),
        # 逐笔数据的过期时间类型
        # -  0: 不过期
        # -  1: 立即过期 (1秒, 若落后于快照1秒则视为过期)
        # -  2: 及时过期 (3秒)
        # -  3: 超时过期 (30秒)
        # @see     eMdsSubscribedTickExpireTypeT
        # @note    仅对压缩行情端口生效, 普通的非压缩行情端口不支持该选项
        # @note    因为存在不可控的网络因素, 所以做不到百分百的精确过滤, 如果对数据的
        # 时效性有精确要求, 就需要在前端对数据再进行一次过滤
        ('tickExpireType', c_uint8),
        # 逐笔数据的数据重建标识 (标识是否订阅重建到的逐笔数据)
        # -  0: 不订阅重建到的逐笔数据 (仅实时行情)
        # -  1: 订阅重建到的逐笔数据 (实时行情+重建数据)
        # -  2: 只订阅重建到的逐笔数据 (仅重建数据 @note 需要通过压缩行情端口进行订阅, 非压缩行情端口不支持该选项)
        # @see     eMdsSubscribedTickRebuildFlagT
        ('tickRebuildFlag', c_uint8),
        # 订阅的数据种类
        # - 0:      默认数据种类 (所有)
        # - 0x0001: L1快照/指数/期权
        # - 0x0002: L2快照
        # - 0x0004: L2委托队列
        # - 0x0008: L2逐笔成交
        # - 0x0010: L2深交所逐笔委托 (仅适用于深交所)
        # - 0x0020: L2上交所逐笔委托 (仅适用于上交所)
        # - 0x0040: L2市场总览 (仅适用于上交所)
        # - 0x0100: 市场状态 (仅适用于上交所)
        # - 0x0200: 证券实时状态 (仅适用于深交所)
        # - 0x0400: 指数行情 (与0x0001的区别在于, 0x0400可以单独订阅指数行情)
        # - 0x0800: 期权行情 (与0x0001的区别在于, 0x0800可以单独订阅期权行情)
        # - 0xFFFF: 所有数据
        # @see eMdsSubscribeDataTypeT
        ('dataTypes', c_int32),
        # 请求订阅的行情数据的起始时间 (格式为: HHMMSS 或 HHMMSSsss)
        # - -1: 从头开始获取
        # -  0: 从最新位置开始获取实时行情
        # - >0: 从指定的起始时间开始获取 (HHMMSS / HHMMSSsss)
        # - 对于应答数据, 若为 0 则表示当前没有比起始时间更加新的行情数据
        # @note    从 0.15.9.1 开始, 允许在会话过程中任意时间指定 beginTime 订阅参数。不过
        # 频繁指定起始时间, 会对当前客户端的行情获取速度产生不利影响。应谨慎使用, 避免
        # 频繁订阅
        # @note    当订阅模式为 Append/Delete/BatchDelete 时将忽略
        # isRequireInitialMktData、beginTime 这两个订阅参数
        ('beginTime', c_int32),
        # 本次订阅的产品数量 (订阅列表中的产品数量)
        # - 该字段表示后续报文为subSecurityCnt个订阅产品条目结构体, 通过这样的方式可以实现同
        # 时订阅多只产品的行情快照
        # - 每个订阅请求中最多能同时指定 4000 只产品, 可以通过追加订阅的方式订阅更多数量的产品
        # - 订阅产品总数量的限制如下:
        # - 对于沪/深两市的现货产品没有订阅数量限制, 可以订阅任意数量的产品
        # - 对于沪/深两市的期权产品, 限制对每个市场最多允许同时订阅 2000 只期权产品
        # @see MdsMktDataRequestEntryT
        # @see MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE
        ('subSecurityCnt', c_int32),
        # 后续报文为 subSecurityCnt 个订阅产品条目结构体
        # @see MdsMktDataRequestEntryT
        # @see MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE
    ]


# 完整的行情订阅请求报文缓存
class MdsMktDataRequestReqBufT(PrintableStructure):
    _fields_ = [
        # 行情订阅请求
        ('mktDataRequestReq', MdsMktDataRequestReqT),
        # 订阅产品列表
        ('entries', MdsMktDataRequestEntryT * MDS_MAX_SECURITY_CNT_PER_SUBSCRIBE),
    ]


# 行情订阅请求的应答报文
class MdsMktDataRequestRspT(PrintableStructure):
    _fields_ = [
        # 订阅模式
        # -  0: (Set)          重新订阅, 设置为订阅列表中的股票 (之前的订阅参数将被清空)
        # -  1: (Append)       追加订阅, 增加订阅列表中的股票
        # -  2: (Delete)       删除订阅, 删除订阅列表中的股票
        # 新增的批量订阅模式定义 (@since v0.15.9.1)
        # - 10: (BatchBegin)   批量订阅-开始订阅, 开始一轮新的批量订阅 (之前的订阅参数将被清空,
        # 行情推送也将暂停直到批量订阅结束)
        # - 11: (BatchAppend)  批量订阅-追加订阅, 增加订阅列表中的股票
        # - 12: (BatchDelete)  批量订阅-删除订阅, 删除订阅列表中的股票
        # - 13: (BatchEnd)     批量订阅-结束订阅, 结束本轮的批量订阅, 提交和启用本轮的订阅参数
        # @see     eMdsSubscribeModeT
        ('subMode', c_uint8),
        # 数据模式, 订阅最新的行情快照还是所有时点的数据
        # -  0: (LatestSimplified) 只订阅最新的行情快照数据, 并忽略和跳过已经过时的数据
        # - 该模式推送的数据量最小, 没有重复数据, 也不会重复发送最新快照
        # - 该模式在时延和带宽方面都相对优秀, 如果没有特殊需求, 推荐使用该模式即可
        # -  1: (LatestTimely) 只订阅最新的行情快照数据, 并立即发送最新数据
        # - 只要有行情更新事件, 便立即推送该产品的最新行情, 但也会因此重复发送多次相同的最新行情
        # - 如果某些产品的交易很活跃, 而客户端处理又比较耗时的话, 那么该模式可能会更及时的获取到
        # 这些产品的最新行情
        # - 此外, 因为与 AllIncrements 模式下的数据一一对应, 可以方便与增量更新消息进行比对测试
        # - 通常情况下, 推荐使用 LatestSimplified 模式即可
        # -  2: (AllIncrements) 订阅所有时点的行情快照数据 (包括Level2增量更新消息)
        # - 该模式会推送所有时点的行情数据, 包括Level2行情快照的增量更新消息
        # - 如果需要获取全量的行情明细, 或者需要直接使用Level2的增量更新消息, 可以使用该模式
        # @see eMdsSubscribedTickTypeT
        ('tickType', c_uint8),
        # 在推送实时行情数据之前, 是否需要推送已订阅产品的初始的行情快照
        # -  0: 不需要推送初始的行情快照
        # -  1: 需要推送初始的行情快照, 即确保客户端可以至少收到一幅已订阅产品的快照行情 (如果有的话)
        # @note    从 0.15.9.1 开始, 允许在会话过程中任意时间指定 isRequireInitialMktData
        # 标志来订阅初始快照。不过频繁订阅初始行情快照, 会对当前客户端的行情获取速度产
        # 生不利影响。应谨慎使用, 避免频繁订阅
        # @note    当订阅模式为 Append/Delete/BatchDelete 时将忽略
        # isRequireInitialMktData、beginTime 这两个订阅参数
        ('isRequireInitialMktData', c_uint8),
        # 订阅的内部频道号 (供内部使用, 尚未对外开放)
        ('_channelNos', c_uint8),
        # 逐笔数据的过期时间类型
        # -  0: 不过期
        # -  1: 立即过期 (1秒, 若落后于快照1秒则视为过期)
        # -  2: 及时过期 (3秒)
        # -  3: 超时过期 (30秒)
        # @see     eMdsSubscribedTickExpireTypeT
        # @note    仅对压缩行情端口生效, 普通的非压缩行情端口不支持该选项
        # @note    因为存在不可控的网络因素, 所以做不到百分百的精确过滤, 如果对数据的
        # 时效性有精确要求, 就需要在前端对数据再进行一次过滤
        ('tickExpireType', c_uint8),
        # 逐笔数据的数据重建标识 (标识是否订阅重建到的逐笔数据)
        # -  0: 不订阅重建到的逐笔数据 (仅实时行情)
        # -  1: 订阅重建到的逐笔数据 (实时行情+重建数据)
        # -  2: 只订阅重建到的逐笔数据 (仅重建数据 @note 需要通过压缩行情端口进行订阅, 非压缩行情端口不支持该选项)
        # @see     eMdsSubscribedTickRebuildFlagT
        ('tickRebuildFlag', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 2),
        # 订阅的数据种类
        # - 0:      默认数据种类 (所有)
        # - 0x0001: L1快照/指数/期权
        # - 0x0002: L2快照
        # - 0x0004: L2委托队列
        # - 0x0008: L2逐笔成交
        # - 0x0010: L2深交所逐笔委托 (仅适用于深交所)
        # - 0x0020: L2上交所逐笔委托 (仅适用于上交所)
        # - 0x0040: L2市场总览 (仅适用于上交所)
        # - 0x0100: 市场状态 (仅适用于上交所)
        # - 0x0200: 证券实时状态 (仅适用于深交所)
        # - 0x0400: 指数行情 (与0x0001的区别在于, 0x0400可以单独订阅指数行情)
        # - 0x0800: 期权行情 (与0x0001的区别在于, 0x0800可以单独订阅期权行情)
        # - 0xFFFF: 所有数据
        # @see eMdsSubscribeDataTypeT
        ('dataTypes', c_int32),
        # 请求订阅的行情数据的起始时间 (格式为: HHMMSS 或 HHMMSSsss)
        # - -1: 从头开始获取
        # -  0: 从最新位置开始获取实时行情
        # - >0: 从指定的起始时间开始获取 (HHMMSS / HHMMSSsss)
        # - 对于应答数据, 若为 0 则表示当前没有比起始时间更加新的行情数据
        # @note    从 0.15.9.1 开始, 允许在会话过程中任意时间指定 beginTime 订阅参数。不过
        # 频繁指定起始时间, 会对当前客户端的行情获取速度产生不利影响。所以应谨慎使用,
        # 避免频繁订阅
        # @note    当订阅模式为 Append/Delete/BatchDelete 时将忽略
        # isRequireInitialMktData、beginTime 这两个订阅参数
        ('beginTime', c_int32),
        # 上证股票(股票/债券/基金)产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('sseStockSubscribed', c_int32),
        # 上证指数产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('sseIndexSubscribed', c_int32),
        # 上证期权产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('sseOptionSubscribed', c_int32),
        # 深圳股票(股票/债券/基金)产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('szseStockSubscribed', c_int32),
        # 深圳指数产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('szseIndexSubscribed', c_int32),
        # 深圳期权产品的订阅结果 (实际已订阅的产品数量)
        # - -1: 订阅了所有产品;
        # -  0: 未订阅或已禁用;
        # - >0: 已订阅的产品数量 (当前已生效的合计值)
        ('szseOptionSubscribed', c_int32),
    ]


# 测试请求报文
class MdsTestRequestReqT(PrintableStructure):
    _fields_ = [
        # 测试请求标识符
        ('testReqId', c_char * MDS_MAX_TEST_REQ_ID_LEN),
        # 发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('sendTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler', c_char * 2),
    ]


# 测试请求的应答报文
class MdsTestRequestRspT(PrintableStructure):
    _fields_ = [
        # 测试请求标识符
        ('testReqId', c_char * MDS_MAX_TEST_REQ_ID_LEN),
        # 测试请求的原始发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('origSendTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler1', c_char * 2),
        # 测试请求应答的发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('respTime', c_char * MDS_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler2', c_char * 2),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# 修改登录密码请求报文
class MdsChangePasswordReqT(PrintableStructure):
    _fields_ = [
        # 加密方法
        ('encryptMethod', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 登录用户名
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 之前的登录密码
        ('oldPassword', c_char * MDS_MAX_PASSWORD_LEN),
        # 新的登录密码
        ('newPassword', c_char * MDS_MAX_PASSWORD_LEN),
    ]


# 修改登录密码应答报文
class MdsChangePasswordRspT(PrintableStructure):
    _fields_ = [
        # 加密方法
        ('encryptMethod', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 登录用户名
        ('username', c_char * MDS_MAX_USERNAME_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', UserInfo),
        # 按64位对齐的填充域
        ('_filler2', c_int32),
        # 发生日期 (格式为 YYYYMMDD, 形如 20160830)
        ('transDate', c_int32),
        # 发生时间 (格式为 HHMMSSsss, 形如 141205000)
        ('transTime', c_int32),
        # 拒绝原因
        ('rejReason', c_int32),
    ]


MdsQrySecurityStatusReqT = MdsQryMktDataSnapshotReqT
MdsQryOptionStaticInfoListFilterT = MdsQryStockStaticInfoListFilterT
MdsQryOptionStaticInfoListReqT = MdsQryStockStaticInfoListReqT


# 汇总的请求消息的消息体定义
class MdsMktReqMsgBodyT(PrintableUnion):
    _fields_ = [
        # 完整的行情订阅请求报文缓存
        ('wholeMktDataReqBuf', MdsMktDataRequestReqBufT),
        # 行情订阅请求报文
        ('mktDataRequestReq', MdsMktDataRequestReqT),
        # 测试请求报文
        ('testRequestReq', MdsTestRequestReqT),
        # 证券行情查询请求
        ('qryMktDataSnapshotReq', MdsQryMktDataSnapshotReqT),
        # (深圳)证券实时状态查询请求
        ('qrySecurityStatusReq', MdsQrySecurityStatusReqT),
        # (上证)市场状态查询请求
        ('qryTrdSessionStatusReq', MdsQryTrdSessionStatusReqT),
        # 证券静态信息查询请求 (@deprecated 已废弃)
        ('qryStockStaticInfoReq', MdsQryStockStaticInfoReqT),
        # 期权静态信息批量查询请求 (@deprecated 已废弃)
        ('qryOptionStaticInfoReq', MdsQryOptionStaticInfoReqT),
        # 证券静态信息列表批量查询请求
        ('qryStockStaticInfoListReq', MdsQryStockStaticInfoListReqT),
        # 期权静态信息批量查询请求
        ('qryOptionStaticInfoListReq', MdsQryOptionStaticInfoListReqT),
        # 行情快照列表批量查询请求
        ('qrySnapshotListReq', MdsQrySnapshotListReqT),
        # 修改登录密码请求
        ('changePasswordReq', MdsChangePasswordReqT),
    ]


# 汇总的应答消息的消息体定义
class MdsMktRspMsgBodyT(PrintableUnion):
    _fields_ = [
        # 会话消息
        # 行情订阅请求的应答报文
        ('mktDataRequestRsp', MdsMktDataRequestRspT),
        # 测试请求的应答报文
        ('testRequestRsp', MdsTestRequestRspT),
        # 行情消息
        # 证券行情全幅消息
        ('mktDataSnapshot', MdsMktDataSnapshotT),
        # Level2 逐笔成交行情
        ('trade', MdsL2TradeT),
        # Level2 逐笔委托行情
        ('order', MdsL2OrderT),
        # 市场状态消息
        ('trdSessionStatus', MdsTradingSessionStatusMsgT),
        # 证券实时状态消息
        ('securityStatus', MdsSecurityStatusMsgT),
        # 查询消息
        # 证券静态信息查询的应答数据 (@deprecated 已废弃)
        ('qryStockStaticInfoRsp', MdsQryStockStaticInfoRspT),
        # 期权静态信息查询的应答数据 (@deprecated 已废弃)
        ('qryOptionStaticInfoRsp', MdsQryOptionStaticInfoRspT),
        # 证券静态信息列表批量查询的应答数据
        ('qryStockStaticInfoListRsp', MdsQryStockStaticInfoListRspT),
        # 期权静态信息查询的应答数据
        ('qryOptionStaticInfoListRsp', MdsQryOptionStaticInfoListRspT),
        # 行情快照列表批量查询的应答数据
        ('qrySnapshotListRsp', MdsQrySnapshotListRspT),
        # 周边应用升级信息查询的应答数据
        ('qryApplUpgradeInfoRsp', MdsQryApplUpgradeInfoRspT),
        # 指令消息
        # 修改登录密码的应答数据
        ('changePasswordRsp', MdsChangePasswordRspT),
    ]

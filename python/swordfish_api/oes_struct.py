# -*- coding: utf-8 -*-
from enum import Enum
from ctypes import Structure, Union
from ctypes import sizeof, POINTER
from ctypes import c_char, c_char_p, c_void_p
from ctypes import c_int8, c_int16, c_int32, c_int64
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64


OES_CLIENT_NAME_MAX_LEN = 32  # 客户端名称最大长度
OES_CLIENT_DESC_MAX_LEN = 32  # 客户端说明最大长度
OES_CLIENT_TAG_MAX_LEN = 32  # 客户端标签最大长度
OES_PWD_MAX_LEN = 40  # 密码最大长度
OES_VER_ID_MAX_LEN = 32  # 协议版本号的最大长度
OES_MAX_COMP_ID_LEN = 32  # 发送方/接收方代码字符串的最大长度
OES_MAX_CLIENT_ENVID_COUNT = 128  # 系统支持的最大客户端环境号数量
OES_MAX_BATCH_ORDERS_COUNT = 500  # 批量委托的每批次最大委托数量 @deprecated 已过时
OES_MAX_BATCH_ORDERS_SINGLE_COMMIT = 300  # 批量委托接口建议的每批次最大委托数量 (@note 超过该数量将自动拆分为多次提交, 可能会因为超出流量限制而导致部分委托被服务器端拒绝)
OES_MAX_BATCH_ORDERS_UPPER_LIMIT = 10000  # 批量委托接口允许同时下单的最大委托数量上限
OES_CUST_ID_MAX_LEN = 16  # 客户代码最大长度
OES_CUST_ID_REAL_LEN = 12  # 客户代码真实长度
OES_CUST_NAME_MAX_LEN = 64  # 客户名称最大长度
OES_CASH_ACCT_ID_MAX_LEN = 16  # 资金账户代码最大长度
OES_CASH_ACCT_ID_REAL_LEN = 12  # 资金账户代码的实际长度
OES_INV_ACCT_ID_MAX_LEN = 16  # 股东账户代码最大长度
OES_INV_ACCT_ID_REAL_LEN = 10  # 股东账户代码实际长度
OES_BRANCH_ID_MAX_LEN = 8  # 营业部代码最大长度
OES_BRANCH_ID_REAL_LEN = 6  # 营业部代码实际长度
OES_BANK_NO_MAX_LEN = 8  # 银行代码最大长度
OES_BANK_NO_REAL_LEN = 4  # 银行代码实际使用长度
OES_PBU_MAX_LEN = 8  # PBU域长度
OES_PBU_REAL_LEN = 6  # PBU实际长度
OES_SECURITY_ID_MAX_LEN = 16  # 证券代码的最大长度
OES_STOCK_ID_REAL_LEN = 6  # 实际的股票产品代码长度
OES_SECURITY_NAME_MAX_LEN = 24  # 证券名称长度
OES_SECURITY_NAME_REAL_LEN = 20  # 证券名称实际长度
OES_SECURITY_LONG_NAME_MAX_LEN = 80  # 证券长名称长度
OES_SECURITY_ENGLISH_NAME_MAX_LEN = 48  # 证券英文名称长度
OES_SECURITY_ISIN_CODE_MAX_LEN = 16  # 证券ISIN代码长度
OES_EXCH_ORDER_ID_MAX_LEN = 17  # 交易所订单编号的最大长度
OES_EXCH_ORDER_ID_SSE_LEN = 8  # 交易所订单编号的实际长度 (上证)
OES_EXCH_ORDER_ID_SZSE_LEN = 16  # 交易所订单编号的实际长度 (深证)
OES_MAX_IP_LEN = 16  # 点分十进制的IPv4, 字符串的最大长度
OES_MAX_MAC_LEN = 20  # MAC地址字符串的最大长度
OES_MAX_MAC_ALGIN_LEN = 24  # MAC地址字符串的最大长度(按64位对齐的长度)
OES_MAX_DRIVER_ID_LEN = 21  # 设备序列号字符串的最大长度
OES_MAX_DRIVER_ID_ALGIN_LEN = 24  # 设备序列号字符串的最大长度(按64位对齐的长度)
OES_MAX_TEST_REQ_ID_LEN = 32  # 测试请求标识符的最大长度
OES_MAX_SENDING_TIME_LEN = 22  # 发送时间字段(YYYYMMDD-HH:mm:SS.sss (*C21))的最大长度
OES_REAL_SENDING_TIME_LEN = 21  # 发送时间字段(YYYYMMDD-HH:mm:SS.sss (*C21))的实际有效数据长度
OES_MAX_ERROR_INFO_LEN = 64  # 错误描述信息长度
OES_NOTIFY_CONTENT_MAX_LEN = 296  # 消息通知内容的最大长度
OES_MAX_ALLOT_SERIALNO_LEN = 64  # 主柜调拨流水号信息长度
OES_CASH_UNIT = 10000  # 资金的转换单位
OES_FUND_TRSF_UNIT = 100  # 出入金的金额单位
OES_FEE_RATE_UNIT = 10000000  # 费用 (佣金/固定费用) 的费率单位
OES_ETF_CASH_RATIO_UNIT = 100000  # ETF使用的资金百分比单位
OES_BOND_INTEREST_UNIT = 100000000  # 债券每张应计利息的转换单位
OES_STK_POSITION_LIMIT_UNIT = 1000000  # 个股持仓比例阀值百分比单位 @deprecated 已废弃, 为了兼容旧版本而保留
OES_BASIS_POINT_RATIO_UNIT = 10000  # 基础比例单位 (万分比)
OES_PERCENTAGE_RATIO_UNIT = 100  # 百分比比例单位 (百分比)
OES_PERMILLAGE_RATIO_UNIT = 1000  # 千分比比例单位 (千分比)
OES_AUCTION_UP_DOWN_RATE_UNIT = 100  # 产品有效竞价范围涨跌幅度转换单位
OES_MAX_BS_PRICE = 10000 * OES_CASH_UNIT  # 最大买卖价格, 委托价格不能等于或超过此价格
OES_BROKER_NAME_MAX_LEN = 128  # 券商名称最大长度
OES_BROKER_MARGIN_ACCT_MAX_LEN = 32  # 券商保证金账户最大长度
OES_BROKER_PHONE_MAX_LEN = 32  # 券商联系电话最大长度
OES_BROKER_WEBSITE_MAX_LEN = 256  # 券商网址最大长度
OES_APPL_DISCARD_VERSION_MAX_COUNT = 5  # 周边应用废弃版本数目的最大个数
OES_APPL_UPGRADE_PROTOCOL_MAX_LEN = 32  # 周边应用升级协议名称的最大长度
OES_OPTION_ID_REAL_LEN = 8  # 实际的期权产品代码长度
OES_SECURITY_STATUS_FLAG_MAX_LEN = 8  # 期权合约状态信息长度
OES_CONTRACT_EXCH_ID_MAX_LEN = 24  # 期权合约交易代码长度
OES_CONTRACT_EXCH_ID_REAL_LEN = 19  # 期权合约交易代码实际长度
OES_MARGIN_RATIO_UNIT = 10000  # 期权保证金计算比例百分比单位
OES_LINE_RATIO_UNIT = 10000  # 期权监控线计算比例百分比单位
OES_OPTION_MARGIN_MAX_RATIO = 99999999  # 期权业务保证金比例最大值
OES_CREDIT_COMPACT_ID_MAX_LEN = 32  # 融资融券合同编号最大长度
OES_CREDIT_DEBT_ID_MAX_LEN = 32  # 融资融券合约编号最大长度
OES_CREDIT_DEBT_ID_REAL_LEN = 23  # 融资融券合约编号实际长度
OES_CREDIT_MARGIN_RATIO_UNIT = 10000  # 融资融券保证金比例/可充抵保证金折算率单位 (万分比)
OES_CREDIT_INTEREST_RATIO_UNIT = 10000  # 融资融券利率费率比例单位 (万分比)
OES_CREDIT_MAINTENANCE_RATIO_UNIT = 1000  # 融资融券维持担保比例/集中度比例单位 (千分比)
OES_CREDIT_INTEREST_CALC_DAYS = 360  # 融资融券业务计息天数
OES_CREDIT_MAINTENANCE_MAX_RATIO = 99999999  # 融资融券业务维持担保比例最大值
OES_LIMIT_BUY = 1 << 1  # 禁止买入
OES_LIMIT_SELL = 1 << 2  # 禁止卖出
OES_LIMIT_RECALL_DESIGNATION = 1 << 3  # 禁止撤销指定
OES_LIMIT_DESIGNATION = 1 << 4  # 禁止转托管
OES_LIMIT_REPO = 1 << 5  # 禁止回购融资
OES_LIMIT_REVERSE_REPO = 1 << 6  # 禁止质押式逆回购
OES_LIMIT_SUBSCRIPTION = 1 << 7  # 禁止新股认购 (新股/可转债/可交换债认购)
OES_LIMIT_CONVERTIBLE_BOND = 1 << 8  # 禁止交易可转债
OES_LIMIT_MARKET_ORDER = 1 << 9  # 禁止市价委托 (自动根据市价权限映射)
OES_LIMIT_BUY_OPEN = 1 << 10  # 禁止买入开仓
OES_LIMIT_SELL_CLOSE = 1 << 11  # 禁止卖出平仓
OES_LIMIT_SELL_OPEN = 1 << 12  # 禁止卖出开仓
OES_LIMIT_BUY_CLOSE = 1 << 13  # 禁止买入平仓
OES_LIMIT_COVERED_OPEN = 1 << 14  # 禁止备兑开仓
OES_LIMIT_COVERED_CLOSE = 1 << 15  # 禁止备兑平仓
OES_LIMIT_UNDERLYING_FREEZE = 1 << 16  # 禁止标的锁定
OES_LIMIT_UNDERLYING_UNFREEZE = 1 << 17  # 禁止标的解锁
OES_LIMIT_OPTION_EXERCISE = 1 << 18  # 禁止期权行权
OES_LIMIT_DEPOSIT = 1 << 21  # 禁止入金
OES_LIMIT_WITHDRAW = 1 << 22  # 禁止出金
OES_LIMIT_SSE_BOND_PLATFORM = 1 << 23  # 禁止交易上交所新债券平台 (指定交易当日不支持债券交易)
OES_LIMIT_COLLATERAL_TRANSFER_IN = 1 << 31  # 禁止担保品划入
OES_LIMIT_COLLATERAL_TRANSFER_OUT = 1 << 32  # 禁止担保品划出
OES_LIMIT_MARGIN_BUY = 1 << 33  # 禁止融资买入
OES_LIMIT_REPAY_MARGIN_BY_SELL = 1 << 34  # 禁止卖券还款
OES_LIMIT_REPAY_MARGIN_DIRECT = 1 << 35  # 禁止直接还款
OES_LIMIT_SHORT_SELL = 1 << 36  # 禁止融券卖出
OES_LIMIT_REPAY_STOCK_BY_BUY = 1 << 37  # 禁止买券还券
OES_LIMIT_REPAY_STOCK_DIRECT = 1 << 38  # 禁止直接还券

OES_MAX_ORD_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中委托信息的最大数量
OES_MAX_TRD_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中成交信息的最大数量
OES_MAX_CASH_ASSET_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中客户资金信息的最大数量
OES_MAX_HOLDING_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中持仓信息的最大数量
OES_MAX_CUST_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中客户信息的最大数量
OES_MAX_INV_ACCT_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中证券账户信息的最大数量
OES_MAX_COMMS_RATE_ITEM_CNT_PER_PACK = 50  # 每条查询应答报文中客户佣金信息的最大数量
OES_MAX_FUND_TRSF_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中出入金流水记录的最大数量
OES_MAX_LOG_WINNING_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中新股认购、中签信息的最大数量
OES_MAX_ISSUE_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中证券发行信息的最大数量
OES_MAX_STOCK_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中现货产品信息的最大数量
OES_MAX_ETF_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中ETF申赎产品信息的最大数量
OES_MAX_ETF_COMPONENT_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中ETF成份证券的最大数量
OES_MAX_MKT_STATE_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中市场状态的最大数量
OES_MAX_NOTIFY_INFO_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中通知消息的最大数量
OES_MAX_CUST_PER_CLIENT = 1  # 客户端对应的最大客户数量

OES_MAX_CRD_DEBT_CONTRACT_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中融资融券合约信息的最大数量
OES_MAX_CRD_DEBT_JOURNAL_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中融资融券合约流水信息的最大数量
OES_MAX_CRD_CREDIT_ASSET_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中信用资产信息的最大数量
OES_MAX_CRD_SECURITY_DEBT_STATS_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中客户单证券融资融券负债统计信息的最大数量
OES_MAX_CRD_CASH_REPAY_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中直接还款信息的最大数量
OES_MAX_CRD_CASH_POSITION_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中资金头寸信息 (可融资头寸信息) 的最大数量
OES_MAX_CRD_SECURITY_POSITION_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中证券头寸信息 (可融券头寸信息) 的最大数量
OES_MAX_CRD_EXCESS_STOCK_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中余券信息的最大数量
OES_MAX_CRD_INTEREST_RATE_ITEM_CNT_PER_PACK = 100  # 每条查询应答报文中融资融券息费利率的最大数量
OES_MAX_CRD_UNDERLYING_INFO_ITEM_CNT_PER_PACK = 500  # 每条查询应答报文中融资融券可充抵保证金证券及融资融券标的信息的最大数量

OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中期权持仓信息的最大数量
OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中期权产品的最大数量
OES_MAX_OPT_UNDERLYING_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中期权标的信息的最大数量
OES_MAX_OPT_PURCHASE_LIMIT_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中期权限购额度信息的最大数量
OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK = 30  # 每条查询应答报文中期权行权指派信息的最大数量
# 每条查询应答报文中期权产品的最大数量 @deprecated 已过时, 请使用 OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK
OES_MAX_OPTION_ITEM_CNT_PER_PACK = OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK
# 每条查询应答报文中期权行权指派信息的最大数量 @deprecated 已过时, 请使用 OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK
OES_MAX_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK = OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK

OES_APPL_VER_ID = "0.17.4.3"  # 当前采用的协议版本号
OES_APPL_VER_VALUE = 1001704031
OES_MIN_APPL_VER_ID = "0.15.5"  # 兼容的最低协议版本号
OES_APPL_NAME = "OES"  # 应用名称

# 最大路径长度
SPK_MAX_PATH_LEN = 256


# 交易所代码定义
class eOesExchangeIdT(Enum):
    OES_EXCH_UNDEFINE = 0  # 未定义的交易所代码
    OES_EXCH_SSE = 1  # 上海证券交易所
    OES_EXCH_SZSE = 2  # 深圳证券交易所
    _MAX_OES_EXCH = 3
    # 上海证券交易所 @deprecated 已过时, 请使用 OES_EXCH_SSE
    OES_EXCHANGE_TYPE_SSE = OES_EXCH_SSE
    # 深圳证券交易所 @deprecated 已过时, 请使用 OES_EXCH_SZSE
    OES_EXCHANGE_TYPE_SZSE = OES_EXCH_SZSE
    _OES_EXCH_ID_MAX_ALIGNED4 = 4  # 交易所代码最大值 (按4字节对齐的大小)
    _OES_EXCH_ID_MAX_ALIGNED8 = 8  # 交易所代码最大值 (按8字节对齐的大小)


# 市场类型定义
class eOesMarketIdT(Enum):
    OES_MKT_UNDEFINE = 0  # 未定义的市场类型
    OES_MKT_SH_ASHARE = 1  # 上海A股
    OES_MKT_SZ_ASHARE = 2  # 深圳A股
    OES_MKT_SH_OPTION = 3  # 上海期权
    OES_MKT_SZ_OPTION = 4  # 深圳期权
    _OES_MKT_ID_MAX = 5  # 市场类型最大值
    _OES_MKT_ID_MAX_ALIGNED8 = 8  # 市场类型最大值 (按8字节对齐的大小)
    # 扩展的外部市场定义 (仅用于查询)
    OES_MKT_EXT_HK = 11  # 港股, 仅用于跨沪深港ETF的成分股查询
    _OES_MKT_EXT_MAX = 12  # 扩展市场类型的最大值
    # 未定义的市场类型 @deprecated 已过时, 请使用 OES_MKT_UNDEFINE
    OES_MKT_ID_UNDEFINE = OES_MKT_UNDEFINE
    # 上海A股 @deprecated 已过时, 请使用 OES_MKT_SH_ASHARE
    OES_MKT_ID_SH_A = OES_MKT_SH_ASHARE
    # 深圳A股 @deprecated 已过时, 请使用 OES_MKT_SZ_ASHARE
    OES_MKT_ID_SZ_A = OES_MKT_SZ_ASHARE
    # 上海期权 @deprecated 已过时, 请使用 OES_MKT_SH_OPTION
    OES_MKT_ID_SH_OPT = OES_MKT_SH_OPTION


# 交易平台类型定义
class eOesPlatformIdT(Enum):
    OES_PLATFORM_UNDEFINE = 0  # 未定义的交易平台类型
    OES_PLATFORM_CASH_AUCTION = 1  # 现货集中竞价交易平台
    OES_PLATFORM_FINANCIAL_SERVICES = 2  # 综合金融服务平台
    OES_PLATFORM_NON_TRADE = 3  # 非交易处理平台
    OES_PLATFORM_DERIVATIVE_AUCTION = 4  # 衍生品集中竞价交易平台
    OES_PLATFORM_INTERNATIONAL_MARKET = 5  # 国际市场互联平台 (暂未对接)
    OES_PLATFORM_BOND_TRADING = 6  # 新债券交易平台
    _OES_PLATFORM_ID_MAX = 7  # 平台号的最大值
    _OES_PLATFORM_ID_MAX_ALIGNED8 = 8  # 平台号的最大值 (按8字节对齐的大小)


# 市场状态定义
class eOesMarketStateT(Enum):
    OES_MKT_STATE_UNDEFINE = 0  # 未定义的市场状态
    OES_MKT_STATE_PRE_OPEN = 1  # 未开放 (PreOpen)
    OES_MKT_STATE_OPEN_UP_COMING = 2  # 即将开放 (OpenUpComing)
    OES_MKT_STATE_OPEN = 3  # 开放 (Open)
    OES_MKT_STATE_HALT = 4  # 暂停开放 (Halt)
    OES_MKT_STATE_CLOSE = 5  # 关闭 (Close)
    _OES_MKT_STATE_MAX = 6  # 市场状态最大值


# OES 竞价时段定义
class eOesTrdSessTypeT(Enum):
    OES_TRD_SESS_TYPE_O = 0  # 开盘集合竞价时段
    OES_TRD_SESS_TYPE_T = 1  # 连续竞价时段
    OES_TRD_SESS_TYPE_C = 2  # 收盘集合竞价
    _OES_TRD_SESS_TYPE_MAX = 3  # 时段类型最大值 (时段类型数量)


# 产品类型 (high-level category)
class eOesProductTypeT(Enum):
    OES_PRODUCT_TYPE_UNDEFINE = 0  # 未定义的产品类型
    OES_PRODUCT_TYPE_EQUITY = 1  # 普通股票/存托凭证/债券/基金/科创板
    OES_PRODUCT_TYPE_BOND_STD = 2  # 逆回购标准券
    OES_PRODUCT_TYPE_IPO = 3  # 新股认购
    OES_PRODUCT_TYPE_ALLOTMENT = 4  # 配股认购
    OES_PRODUCT_TYPE_OPTION = 5  # 期权
    _OES_PRODUCT_TYPE_MAX = 6  # 产品类型最大值


# 证券类别
class eOesSecurityTypeT(Enum):
    OES_SECURITY_TYPE_UNDEFINE = 0  # 未定义的证券类型
    OES_SECURITY_TYPE_STOCK = 1  # 股票
    OES_SECURITY_TYPE_BOND = 2  # 债券
    OES_SECURITY_TYPE_ETF = 3  # ETF
    OES_SECURITY_TYPE_FUND = 4  # 基金
    OES_SECURITY_TYPE_OPTION = 5  # 期权
    OES_SECURITY_TYPE_MGR = 9  # 管理类
    _OES_SECURITY_TYPE_MAX = 10  # 证券类型最大值
    _OES_SECURITY_TYPE_NOT_SUPPORT = 100  # 不支持的证券类别
    _OES_SECURITY_TYPE_VIRTUAL = 101  # 虚拟证券的证券类别


# 证券子类别
class eOesSubSecurityTypeT(Enum):
    OES_SUB_SECURITY_TYPE_UNDEFINE = 0  # 未定义的证券子类型
    _OES_SUB_SECURITY_TYPE_STOCK_MIN = 10  # 股票类证券子类型最小值
    OES_SUB_SECURITY_TYPE_STOCK_ASH = 11  # A股股票, A Share
    OES_SUB_SECURITY_TYPE_STOCK_SME = 12  # 中小板股票, Small & Medium Enterprise (SME) Board
    OES_SUB_SECURITY_TYPE_STOCK_GEM = 13  # 创业板股票, Growth Enterprise Market (GEM)
    OES_SUB_SECURITY_TYPE_STOCK_KSH = 14  # 科创板股票
    OES_SUB_SECURITY_TYPE_STOCK_KCDR = 15  # 科创板存托凭证
    OES_SUB_SECURITY_TYPE_STOCK_CDR = 16  # 存托凭证, Chinese Depository Receipt (CDR)
    OES_SUB_SECURITY_TYPE_STOCK_HLTCDR = 17  # 沪伦通CDR本地交易业务产品
    OES_SUB_SECURITY_TYPE_STOCK_GEMCDR = 18  # 创业板存托凭证
    _OES_SUB_SECURITY_TYPE_STOCK_MAX = 19  # 股票类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_BOND_MIN = 20  # 债券类证券子类型最小值
    OES_SUB_SECURITY_TYPE_BOND_GBF = 21  # 国债 (国债/地方债/政策性金融债/上交所政府支持债)
    OES_SUB_SECURITY_TYPE_BOND_CBF = 22  # 企业债 (深交所企业债/上交所存量企业债)
    OES_SUB_SECURITY_TYPE_BOND_CPF = 23  # 公司债 (公司债/上交所企业债/上交所存量政府支持债)
    OES_SUB_SECURITY_TYPE_BOND_CCF = 24  # 可转换债券
    OES_SUB_SECURITY_TYPE_BOND_FBF = 25  # 金融机构发行债券 (仅适用于深交所, 上交所已废弃)
    OES_SUB_SECURITY_TYPE_BOND_PRP = 26  # 通用质押式回购
    OES_SUB_SECURITY_TYPE_BOND_STD = 27  # 债券标准券
    OES_SUB_SECURITY_TYPE_BOND_EXG = 28  # 可交换债券
    _OES_SUB_SECURITY_TYPE_BOND_MAX = 29  # 债券类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_ETF_MIN = 30  # ETF类证券子类型最小值
    OES_SUB_SECURITY_TYPE_ETF_SINGLE_MKT = 31  # 单市场股票ETF
    OES_SUB_SECURITY_TYPE_ETF_CROSS_MKT = 32  # 跨市场股票ETF
    OES_SUB_SECURITY_TYPE_ETF_BOND = 33  # 实物债券ETF
    OES_SUB_SECURITY_TYPE_ETF_CURRENCY = 34  # 货币ETF
    OES_SUB_SECURITY_TYPE_ETF_CROSS_BORDER = 35  # 跨境ETF
    OES_SUB_SECURITY_TYPE_ETF_GOLD = 36  # 黄金ETF
    OES_SUB_SECURITY_TYPE_ETF_COMMODITY_FUTURES = 37  # 商品期货ETF
    _OES_SUB_SECURITY_TYPE_ETF_MAX = 38  # ETF类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_FUND_MIN = 40  # 基金类证券子类型最小值
    OES_SUB_SECURITY_TYPE_FUND_LOF = 41  # LOF基金
    OES_SUB_SECURITY_TYPE_FUND_CEF = 42  # 封闭式基金, Close-end Fund
    OES_SUB_SECURITY_TYPE_FUND_OEF = 43  # 开放式基金, Open-end Fund
    OES_SUB_SECURITY_TYPE_FUND_GRADED = 44  # 分级子基金
    OES_SUB_SECURITY_TYPE_FUND_REITS = 45  # 基础设施基金
    _OES_SUB_SECURITY_TYPE_FUND_MAX = 46  # 基金类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_OPTION_MIN = 50  # 期权类证券子类型最小值
    OES_SUB_SECURITY_TYPE_OPTION_ETF = 51  # ETF期权
    OES_SUB_SECURITY_TYPE_OPTION_STOCK = 52  # 个股期权
    _OES_SUB_SECURITY_TYPE_OPTION_MAX = 53  # 期权类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_MGR_MIN = 90  # 管理类证券子类型最小值
    OES_SUB_SECURITY_TYPE_MGR_SSE_DESIGNATION = 91  # 指定登记
    OES_SUB_SECURITY_TYPE_MGR_SSE_RECALL_DESIGNATION = 92  # 指定撤消
    OES_SUB_SECURITY_TYPE_MGR_SZSE_DESIGNATION = 93  # 托管注册
    OES_SUB_SECURITY_TYPE_MGR_SZSE_CANCEL_DESIGNATION = 94  # 托管撤消
    OES_SUB_SECURITY_TYPE_MGR_OPT_EXERCISE_TRANSFER = 95  # 期权转处置
    OES_SUB_SECURITY_TYPE_MGR_CRD_COLLATERAL_TRANSFER = 96  # 信用担保证券划转
    _OES_SUB_SECURITY_TYPE_MGR_MAX = 97  # 管理类证券子类型最大值
    _OES_SUB_SECURITY_TYPE_MAX = _OES_SUB_SECURITY_TYPE_MGR_MAX


# 证券级别
class eOesSecurityLevelT(Enum):
    OES_SECURITY_LEVEL_UNDEFINE = 0
    OES_SECURITY_LEVEL_N = 1  # 正常证券
    OES_SECURITY_LEVEL_XST = 2  # *ST股
    OES_SECURITY_LEVEL_ST = 3  # ST股
    OES_SECURITY_LEVEL_P = 4  # 退市整理证券
    OES_SECURITY_LEVEL_T = 5  # 退市转让证券
    OES_SECURITY_LEVEL_U = 6  # 优先股
    OES_SECURITY_LEVEL_B = 7  # B级基金
    _OES_SECURITY_LEVEL_MAX = 8


# 证券风险等级
class eOesSecurityRiskLevelT(Enum):
    OES_RISK_LEVEL_VERY_LOW = 0  # 最低风险
    OES_RISK_LEVEL_LOW = 1  # 低风险
    OES_RISK_LEVEL_MEDIUM_LOW = 2  # 中低风险
    OES_RISK_LEVEL_MEDIUM = 3  # 中风险
    OES_RISK_LEVEL_MEDIUM_HIGH = 4  # 中高风险
    OES_RISK_LEVEL_HIGH = 5  # 高风险
    OES_RISK_LEVEL_VERY_HIGH = 6  # 极高风险
    _OES_RISK_LEVEL_MAX = 7


# 证券禁止交易标识
class eOesSecuritySuspFlagT(Enum):
    OES_SUSPFLAG_NONE = 0x0  # 无禁止交易标识
    OES_SUSPFLAG_EXCHANGE = 0x1  # 因证券连续停牌而禁止交易
    OES_SUSPFLAG_BROKER = 0x2  # 因券商设置而禁止交易
    OES_SUSPFLAG_MARKET_CLOSE = 0x4  # 因闭市而禁止交易
    _OES_SUSPFLAG_OTHER = 5


# 证券状态的枚举值定义
class eOesSecurityStatusT(Enum):
    OES_SECURITY_STATUS_NONE = 0  # 无特殊状态
    OES_SECURITY_STATUS_FIRST_LISTING = 1 << 0  # 上市首日
    OES_SECURITY_STATUS_RESUME_FIRST_LISTING = 1 << 1  # 恢复上市首日
    OES_SECURITY_STATUS_NEW_LISTING = 1 << 2  # 上市初期
    OES_SECURITY_STATUS_EXCLUDE_RIGHT = 1 << 3  # 除权
    OES_SECURITY_STATUS_EXCLUDE_DIVIDEN = 1 << 4  # 除息
    OES_SECURITY_STATUS_SUSPEND = 1 << 5  # 证券连续停牌
    OES_SECURITY_STATUS_SPECIAL_TREATMENT = 1 << 6  # ST股
    OES_SECURITY_STATUS_X_SPECIAL_TREATMENT = 1 << 7  # *ST股
    OES_SECURITY_STATUS_DELIST_PERIOD = 1 << 8  # 退市整理期
    OES_SECURITY_STATUS_DELIST_TRANSFER = 1 << 9  # 退市转让期


# 证券属性的枚举值定义
class eOesSecurityAttributeT(Enum):
    OES_SECURITY_ATTR_NONE = 0  # 无特殊属性
    OES_SECURITY_ATTR_INNOVATION = 1 << 0  # 创新企业
    OES_SECURITY_ATTR_KSH = 1 << 1  # 科创板标记
    # 科创板ETF/科创板LOF @deprecated 已过时, 请使用 OES_SECURITY_ATTR_KSH
    OES_SECURITY_ATTR_KSH_FUND = OES_SECURITY_ATTR_KSH


# 有效竞价范围限制类型
class eOesAuctionLimitTypeT(Enum):
    OES_AUCTION_LIMIT_TYPE_NONE = 0  # 无竞价范围限制
    OES_AUCTION_LIMIT_TYPE_RATE = 1  # 按幅度限制 (百分比)
    OES_AUCTION_LIMIT_TYPE_ABSOLUTE = 2  # 按价格限制 (绝对值)


# 有效竞价范围基准价类型
class eOesAuctionReferPriceTypeT(Enum):
    OES_AUCTION_REFER_PRICE_TYPE_LAST = 1  # 最近价
    OES_AUCTION_REFER_PRICE_TYPE_BEST = 2  # 对手方最优价


# OES中签、配号记录类型
class eOesLotTypeT(Enum):
    OES_LOT_TYPE_UNDEFINE = 0  # 未定义的中签、配号记录类型
    OES_LOT_TYPE_FAILED = 1  # 配号失败记录
    OES_LOT_TYPE_ASSIGNMENT = 2  # 配号成功记录
    OES_LOT_TYPE_LOTTERY = 3  # 中签记录
    _OES_LOT_TYPE_MAX = 4  # 中签、配号记录类型最大值


# OES配号失败原因
class eOesLotRejReasonT(Enum):
    OES_LOT_REJ_REASON_DUPLICATE = 1  # 配号失败-重复申购
    OES_LOT_REJ_REASON_INVALID_DUPLICATE = 2  # 配号失败-违规重复
    OES_LOT_REJ_REASON_OFFLINE_FIRST = 3  # 配号失败-网下在先
    OES_LOT_REJ_REASON_BAD_RECORD = 4  # 配号失败-不良记录
    OES_LOT_REJ_REASON_UNKNOW = 5  # 配号失败-未知原因


# 产品发行方式
class eOesSecurityIssueTypeT(Enum):
    OES_ISSUE_TYPE_UNDEFINE = 0  # 未定义的发行方式
    OES_ISSUE_TYPE_MKT_QUOTA = 1  # 按市值限额申购 (检查认购限额, 不预冻结资金)
    OES_ISSUE_TYPE_CASH = 2  # 增发资金申购 (不检查认购限额, 预冻结资金)
    OES_ISSUE_TYPE_CREDIT = 3  # 信用申购 (不检查认购限额, 不预冻结资金)


# 计价方式
class eOesPricingMethodT(Enum):
    OES_PRICING_METHOD_UNDEFINE = 0  # 未定义的计价方式
    OES_PRICING_METHOD_CLEAN = 1  # 净价
    OES_PRICING_METHOD_DIRTY = 2  # 全价


# 订单执行状态定义
class eOesOrdStatusT(Enum):
    OES_ORD_STATUS_PENDING = 0  # 待处理 (仅内部使用)
    OES_ORD_STATUS_NEW = 1  # 新订单 (风控通过)
    OES_ORD_STATUS_DECLARED = 2  # 已确认
    OES_ORD_STATUS_PARTIALLY_FILLED = 3  # 部分成交
    _OES_ORD_STATUS_FINAL_MIN = 4  # 订单终结状态判断标志
    OES_ORD_STATUS_CANCEL_DONE = 5  # 撤单指令已执行 (适用于撤单请求, 并做为撤单请求的终结状态)
    OES_ORD_STATUS_PARTIALLY_CANCELED = 6  # 部分撤单 (部分成交, 剩余撤单)
    OES_ORD_STATUS_CANCELED = 7  # 已撤单
    OES_ORD_STATUS_FILLED = 8  # 已成交 (全部成交)
    _OES_ORD_STATUS_VALID_MAX = 9
    _OES_ORD_STATUS_INVALID_MIN = 10  # 废单判断标志 (委托状态大于该值的全部为废单)
    OES_ORD_STATUS_INVALID_OES = 11  # OES内部废单
    OES_ORD_STATUS_INVALID_EXCHANGE = 12  # 交易所后台废单
    OES_ORD_STATUS_INVALID_TGW_REJECT = 13  # 交易所前台废单 (因订单不合法而被交易网关拒绝)
    OES_ORD_STATUS_INVALID_TGW_COMM = 14  # 交易所通信故障 (仅适用于上交所)
    OES_ORD_STATUS_INVALID_TGW_TRY_AGAIN = 18  # 因平台尚未开放(非交易时段)而被交易网关拒绝 (@note 前端需要关注该状态, 可以根据需要尝试重新发送委托请求)
    _OES_ORD_STATUS_INVALID_MAX = 19
    # 以下订单状态定义已废弃, 只是为了兼容之前的版本而暂时保留
    OES_ORD_STATUS_NORMAL = OES_ORD_STATUS_NEW
    OES_ORD_STATUS_DECLARING = OES_ORD_STATUS_NEW
    _OES_ORD_STATUS_INVALID_OES = OES_ORD_STATUS_INVALID_OES
    # 上证后台判断该订单为废单 @deprecated 已废弃
    OES_ORD_STATUS_INVALID_SH_F = OES_ORD_STATUS_INVALID_EXCHANGE
    # 上证前台判断该订单为废单 @deprecated 已废弃
    OES_ORD_STATUS_INVALID_SH_E = OES_ORD_STATUS_INVALID_TGW_REJECT
    # 通信故障(仅适用于上交所) @deprecated 已废弃
    OES_ORD_STATUS_INVALID_SH_COMM = OES_ORD_STATUS_INVALID_TGW_COMM
    # 深证前台废单 @deprecated 已废弃 (深交所不会返回该错误, 之前版本的取值为: 15)
    OES_ORD_STATUS_INVALID_SZ_F = OES_ORD_STATUS_INVALID_TGW_REJECT
    # 深证后台废单 @deprecated 已废弃 (@note 取值发生变化, 之前版本的取值为: 16)
    OES_ORD_STATUS_INVALID_SZ_E = OES_ORD_STATUS_INVALID_EXCHANGE
    # 深证业务拒绝 @deprecated 已废弃 (@note 取值发生变化, 之前版本的取值为: 17)
    OES_ORD_STATUS_INVALID_SZ_REJECT = OES_ORD_STATUS_INVALID_TGW_REJECT
    # 深证平台未开放(需尝试重报) @deprecated 已废弃
    OES_ORD_STATUS_INVALID_SZ_TRY_AGAIN = OES_ORD_STATUS_INVALID_TGW_TRY_AGAIN


# 委托类型
#
# 部分缩写解释如下:
#  - LMT (Limit)           : 限价
#  - MTL (Market To Limit) : 剩余转限价(市价)
#  - FAK (Fill and Kill)   : 剩余转撤销(市价)
#  - FOK (Fill or Kill)    : 全部成交或全部撤销(市价/限价)
#
# 上海A股支持类型:
#      1. OES_ORD_TYPE_LMT
#      2. OES_ORD_TYPE_MTL_BEST_5
#      3. OES_ORD_TYPE_FAK_BEST_5
#      4. OES_ORD_TYPE_MTL_BEST (仅适用于科创板)
#      5. OES_ORD_TYPE_MTL_SAMEPARTY_BEST (仅适用于科创板)
#
# 上海期权支持市价类型:
#      1. OES_ORD_TYPE_LMT
#      2. OES_ORD_TYPE_LMT_FOK
#      3. OES_ORD_TYPE_MTL
#      4. OES_ORD_TYPE_FAK
#      5. OES_ORD_TYPE_FOK
#
# 深圳A股支持市价类型:
#      1. OES_ORD_TYPE_LMT
#      2. OES_ORD_TYPE_MTL_BEST
#      3. OES_ORD_TYPE_MTL_SAMEPARTY_BEST
#      4. OES_ORD_TYPE_FAK_BEST_5
#      5. OES_ORD_TYPE_FAK
#      6. OES_ORD_TYPE_FOK
#
# 深圳期权支持市价类型:
#      1. OES_ORD_TYPE_LMT
#      2. OES_ORD_TYPE_LMT_FOK
#      3. OES_ORD_TYPE_MTL_BEST
#      4. OES_ORD_TYPE_MTL_SAMEPARTY_BEST
#      5. OES_ORD_TYPE_FAK_BEST_5
#      6. OES_ORD_TYPE_FAK
#      7. OES_ORD_TYPE_FOK
class eOesOrdTypeT(Enum):
    OES_ORD_TYPE_LMT = 0  # 限价委托
    OES_ORD_TYPE_LMT_FOK = 1  # 限价全部成交或全部撤销委托
    _OES_ORD_TYPE_LMT_MAX = 2
    OES_ORD_TYPE_MTL_BEST_5 = 10  # 最优五档即时成交剩余转限价委托
    OES_ORD_TYPE_MTL_BEST = 11  # 对手方最优价格委托
    OES_ORD_TYPE_MTL_SAMEPARTY_BEST = 12  # 本方最优价格委托
    OES_ORD_TYPE_MTL = 13  # 市价剩余转限价委托
    _OES_ORD_TYPE_MTL_MAX = 14
    OES_ORD_TYPE_FAK_BEST_5 = 20  # 最优五档即时成交剩余撤销委托
    OES_ORD_TYPE_FAK = 21  # 即时成交剩余撤销委托
    _OES_ORD_TYPE_FAK_MAX = 22
    OES_ORD_TYPE_FOK = 30  # 市价全部成交或全部撤销委托
    _OES_ORD_TYPE_FOK_MAX = 31
    _OES_ORD_TYPE_MAX = 32
    _OES_ORD_TYPE_MAX_ALIGNED = 32  # 委托类型最大值 (按8字节对齐的大小)


# 上证委托类型
#
# 部分缩写解释如下:
#  - LMT (Limit)           : 限价
#  - MTL (Market To Limit) : 剩余转限价(市价)
#  - FAK (Fill and Kill)   : 剩余转撤销(市价)
#  - FOK (Fill or Kill)    : 全部成交或全部撤销(市价/限价)
class eOesOrdTypeShT(Enum):
    # 限价, 0
    OES_ORD_TYPE_SH_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    # 最优五档即时成交剩余转限价委托, 10
    OES_ORD_TYPE_SH_MTL_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST_5.value
    # 对手方最优价格委托(仅适用于科创板), 11
    OES_ORD_TYPE_SH_MTL_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST.value
    # 本方最优价格委托(仅适用于科创板), 12
    OES_ORD_TYPE_SH_MTL_SAMEPARTY_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_SAMEPARTY_BEST.value
    # 最优五档即时成交剩余撤销委托, 20
    OES_ORD_TYPE_SH_FAK_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_FAK_BEST_5.value


# 上证期权业务委托类型
#
# 部分缩写解释如下:
#  - LMT (Limit)           : 限价
#  - MTL (Market To Limit) : 剩余转限价(市价)
#  - FAK (Fill and Kill)   : 剩余转撤销(市价)
#  - FOK (Fill or Kill)    : 全部成交或全部撤销(市价/限价)
class eOesOrdTypeShOptT(Enum):
    # 限价, 0
    OES_ORD_TYPE_SHOPT_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    # 限价全部成交或全部撤销委托, 1
    OES_ORD_TYPE_SHOPT_LMT_FOK = eOesOrdTypeT.OES_ORD_TYPE_LMT_FOK.value
    # 市价剩余转限价委托, 13
    OES_ORD_TYPE_SHOPT_MTL = eOesOrdTypeT.OES_ORD_TYPE_MTL.value
    # 即时成交剩余撤销委托, 21
    OES_ORD_TYPE_SHOPT_FAK = eOesOrdTypeT.OES_ORD_TYPE_FAK.value
    # 市价全部成交或全部撤销委托, 30
    OES_ORD_TYPE_SHOPT_FOK = eOesOrdTypeT.OES_ORD_TYPE_FOK.value
    # 以下委托类型已废弃, 只是为了兼容之前的版本而暂时保留
    OES_ORD_TYPE_SH_LMT_FOK = OES_ORD_TYPE_SHOPT_LMT_FOK
    OES_ORD_TYPE_SH_FOK = OES_ORD_TYPE_SHOPT_FOK


# 深证委托类型
#
# 部分缩写解释如下:
#  - LMT (Limit)           : 限价
#  - MTL (Market To Limit) : 剩余转限价(市价)
#  - FAK (Fill and Kill)   : 剩余转撤销(市价)
#  - FOK (Fill or Kill)    : 全部成交或全部撤销(市价/限价)
class eOesOrdTypeSzT(Enum):
    # 限价, 0
    OES_ORD_TYPE_SZ_LMT = eOesOrdTypeT.OES_ORD_TYPE_LMT.value
    # 限价全部成交或全部撤销委托(仅适用于期权), 1
    OES_ORD_TYPE_SZ_LMT_FOK = eOesOrdTypeT.OES_ORD_TYPE_LMT_FOK.value
    # 对手方最优价格委托, 11
    OES_ORD_TYPE_SZ_MTL_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_BEST.value
    # 本方最优价格委托, 12
    OES_ORD_TYPE_SZ_MTL_SAMEPARTY_BEST = eOesOrdTypeT.OES_ORD_TYPE_MTL_SAMEPARTY_BEST.value
    # 最优五档即时成交剩余撤销委托, 20
    OES_ORD_TYPE_SZ_FAK_BEST_5 = eOesOrdTypeT.OES_ORD_TYPE_FAK_BEST_5.value
    # 即时成交剩余撤销委托, 21
    OES_ORD_TYPE_SZ_FAK = eOesOrdTypeT.OES_ORD_TYPE_FAK.value
    # 市价全部成交或全部撤销委托, 30
    OES_ORD_TYPE_SZ_FOK = eOesOrdTypeT.OES_ORD_TYPE_FOK.value


# 买卖类型
class eOesBuySellTypeT(Enum):
    OES_BS_TYPE_UNDEFINE = 0  # 未定义的买卖类型
    OES_BS_TYPE_BUY = 1  # 普通买入/信用担保品买入
    OES_BS_TYPE_SELL = 2  # 普通卖出/信用担保品卖出
    OES_BS_TYPE_CREATION = 3  # 申购
    OES_BS_TYPE_REDEMPTION = 4  # 赎回
    OES_BS_TYPE_REVERSE_REPO = 6  # 质押式逆回购
    OES_BS_TYPE_SUBSCRIPTION = 7  # 新股/可转债/可交换债认购
    OES_BS_TYPE_ALLOTMENT = 8  # 配股/配债认购
    _OES_BS_TYPE_MAX_SPOT = 9  # 现货交易的买卖类型最大值
    # -------------------------
    _OES_BS_TYPE_MIN_OPTION = 10  # 期权交易的买卖类型最小值
    OES_BS_TYPE_BUY_OPEN = 11  # 期权买入开仓
    OES_BS_TYPE_SELL_CLOSE = 12  # 期权卖出平仓
    OES_BS_TYPE_SELL_OPEN = 13  # 期权卖出开仓
    OES_BS_TYPE_BUY_CLOSE = 14  # 期权买入平仓
    OES_BS_TYPE_COVERED_OPEN = 15  # 期权备兑开仓
    OES_BS_TYPE_COVERED_CLOSE = 16  # 期权备兑平仓
    OES_BS_TYPE_OPTION_EXERCISE = 17  # 期权行权
    OES_BS_TYPE_UNDERLYING_FREEZE = 18  # 期权标的锁定
    OES_BS_TYPE_UNDERLYING_UNFREEZE = 19  # 期权标的解锁
    _OES_BS_TYPE_MAX_OPTION = 20  # 期权交易的买卖类型最大值
    # -------------------------
    OES_BS_TYPE_CANCEL = 30  # 撤单
    # -------------------------
    _OES_BS_TYPE_MIN_CREDIT = 30  # 信用交易特有的买卖类型最小值
    # 信用担保品买入
    OES_BS_TYPE_COLLATERAL_BUY = OES_BS_TYPE_BUY
    # 信用担保品卖出
    OES_BS_TYPE_COLLATERAL_SELL = OES_BS_TYPE_SELL
    OES_BS_TYPE_COLLATERAL_TRANSFER_IN = 31  # 信用担保品转入
    OES_BS_TYPE_COLLATERAL_TRANSFER_OUT = 32  # 信用担保品转出
    OES_BS_TYPE_MARGIN_BUY = 33  # 信用融资买入
    OES_BS_TYPE_REPAY_MARGIN_BY_SELL = 34  # 信用卖券还款
    OES_BS_TYPE_SHORT_SELL = 35  # 信用融券卖出
    OES_BS_TYPE_REPAY_STOCK_BY_BUY = 36  # 信用买券还券
    OES_BS_TYPE_REPAY_STOCK_DIRECT = 37  # 信用直接还券
    _OES_BS_TYPE_MAX_CREDIT = 38  # 信用交易特有的买卖类型最大值
    _OES_BS_TYPE_MAX_TRADING = 39  # 对外开放的交易类业务的买卖类型最大值
    _OES_BS_TYPE_MAX_TRADING_ALIGNED8 = 40  # 对外开放的交易类业务的买卖类型最大值 (按8字节对齐的大小)
    # -------------------------
    # 仅用于兼容之前版本的质押式逆回购, 不可用于‘信用融券卖出’交易
    OES_BS_TYPE_CREDIT_SELL = OES_BS_TYPE_REVERSE_REPO
    OES_BS_TYPE_B = OES_BS_TYPE_BUY
    OES_BS_TYPE_S = OES_BS_TYPE_SELL
    OES_BS_TYPE_KB = OES_BS_TYPE_CREATION
    OES_BS_TYPE_KS = OES_BS_TYPE_REDEMPTION
    OES_BS_TYPE_CS = OES_BS_TYPE_REVERSE_REPO
    OES_BS_TYPE_BO = OES_BS_TYPE_BUY_OPEN
    OES_BS_TYPE_BC = OES_BS_TYPE_BUY_CLOSE
    OES_BS_TYPE_SO = OES_BS_TYPE_SELL_OPEN
    OES_BS_TYPE_SC = OES_BS_TYPE_SELL_CLOSE
    OES_BS_TYPE_CO = OES_BS_TYPE_COVERED_OPEN
    OES_BS_TYPE_CC = OES_BS_TYPE_COVERED_CLOSE
    OES_BS_TYPE_TE = OES_BS_TYPE_OPTION_EXERCISE
    OES_BS_TYPE_UF = OES_BS_TYPE_UNDERLYING_FREEZE
    OES_BS_TYPE_UU = OES_BS_TYPE_UNDERLYING_UNFREEZE


# 订单的买卖方向 (内部使用)
class eOesOrdDirT(Enum):
    OES_ORD_DIR_BUY = 0  # 买
    OES_ORD_DIR_SELL = 1  # 卖
    _OES_ORD_DIR_MAX = 2  # 买卖方向最大值


# 委托强制标志
class eOesOrdMandatoryFlagT(Enum):
    OES_ORD_MANDATORY_FLAG_NONE = 0  # 无强制标志
    OES_ORD_MANDATORY_FLAG_DELEGATE = 1  # 代客下单标志
    _OES_ORD_MANDATORY_FLAG_MEMBER_MIN = 10  # 会员管理委托的最小值
    OES_ORD_MANDATORY_FLAG_LIQUDATION = 11  # 强制平仓标志
    OES_ORD_MANDATORY_FLAG_MANAGEMENT = 12  # 管理指令标志
    _OES_ORD_MANDATORY_FLAG_MAX = 13  # 委托强制标志的最大值


# 成交回报记录的成交类型
#
# 上证接口规范 (IS103_ETFInterface_CV14_20130123) 中规定如下:
# - 二级市场记录表示一笔申购/赎回交易连续记录的开始,对一笔申购/赎回交易而言,有且只有一条;
# - 一级市场记录不再表示对应申购/赎回交易连续记录的结束,对一笔申购/赎回交易而言,有且只有一条。
#
# 上证期权接口规格说明书 (IS113_DTPInterface_CV1.1_20161017) 中描述如下:
# - 执行报告中的会员内部编号(clOrdId)以QP1开头，表示为交易所保证金强制平仓
# - 执行报告中的会员内部编号(clOrdId)以CV1开头，表示为交易所备兑强制平仓
class eOesTrdCnfmTypeT(Enum):
    OES_TRDCNFM_TYPE_NORMAL = 0  # 普通成交记录
    OES_TRDCNFM_TYPE_ETF_FIRST = 1  # ETF 二级市场记录
    OES_TRDCNFM_TYPE_ETF_CMPOENT = 2  # ETF 成份股记录
    OES_TRDCNFM_TYPE_ETF_CASH = 3  # ETF 资金记录
    OES_TRDCNFM_TYPE_ETF_LAST = 4  # ETF 一级市场记录
    _OES_TRDCNFM_TYPE_ETF_MAX = 5
    OES_TRDCNFM_TYPE_OPT_QP1 = 11  # OPT 交易所保证金强制平仓
    OES_TRDCNFM_TYPE_OPT_CV1 = 12  # OPT 交易所备兑强制平仓
    _OES_TRDCNFM_TYPE_OPT_MAX = 13
    _OES_TRDCNFM_TYPE_MAX = _OES_TRDCNFM_TYPE_OPT_MAX
    # 以下成交类型定义即将被废弃
    OES_ETF_TRDCNFM_TYPE_NONE = OES_TRDCNFM_TYPE_NORMAL
    OES_ETF_TRDCNFM_TYPE_ETF_FIRST = OES_TRDCNFM_TYPE_ETF_FIRST
    OES_ETF_TRDCNFM_TYPE_CMPOENT = OES_TRDCNFM_TYPE_ETF_CMPOENT
    OES_ETF_TRDCNFM_TYPE_CASH = OES_TRDCNFM_TYPE_ETF_CASH
    OES_ETF_TRDCNFM_TYPE_ETF_LAST = OES_TRDCNFM_TYPE_ETF_LAST
    _OES_ETF_TRDCNFM_TYPE_MAX = _OES_TRDCNFM_TYPE_ETF_MAX


# ETF成份证券现金替代标志
class eOesEtfSubFlagT(Enum):
    OES_ETF_SUBFLAG_FORBID_SUB = 0  # 禁止现金替代 (必须有证券)
    OES_ETF_SUBFLAG_ALLOW_SUB = 1  # 可以进行现金替代(先用证券, 如证券不足可用现金替代)
    OES_ETF_SUBFLAG_MUST_SUB = 2  # 必须用现金替代
    OES_ETF_SUBFLAG_SZ_REFUND_SUB = 3  # 该证券为深市证券, 退补现金替代
    OES_ETF_SUBFLAG_SZ_MUST_SUB = 4  # 该证券为深市证券, 必须现金替代
    OES_ETF_SUBFLAG_OTHER_REFUND_SUB = 5  # 非沪深市场成份证券退补现金替代
    OES_ETF_SUBFLAG_OTHER_MUST_SUB = 6  # 非沪深市场成份证券必须现金替代
    OES_ETF_SUBFLAG_HK_REFUND_SUB = 7  # 港市退补现金替代 (仅适用于跨沪深港ETF产品)
    OES_ETF_SUBFLAG_HK_MUST_SUB = 8  # 港市必须现金替代 (仅适用于跨沪深港ETF产品)


# OES执行类型
class eOesExecTypeT(Enum):
    OES_EXECTYPE_UNDEFINE = 0  # 未定义的执行类型
    OES_EXECTYPE_INSERT = 1  # 已接收 (OES已接收)
    OES_EXECTYPE_CONFIRMED = 2  # 已确认 (交易所已确认/出入金主柜台已确认)
    OES_EXECTYPE_CANCELLED = 3  # 已撤单 (原始委托的撤单完成回报)
    OES_EXECTYPE_AUTO_CANCELLED = 4  # 自动撤单 (市价委托发生自动撤单后的委托回报)
    OES_EXECTYPE_REJECT = 5  # 拒绝 (OES拒绝/交易所废单/出入金主柜台拒绝)
    OES_EXECTYPE_TRADE = 6  # 成交 (成交回报)
    OES_EXECTYPE_REPAY = 7  # 归还 (融资融券业务的合约归还回报)
    _OES_EXECTYPE_MAX = 8  # 执行类型最大值


# 货币类型
class eOesCurrTypeT(Enum):
    OES_CURR_TYPE_RMB = 0  # 人民币
    OES_CURR_TYPE_HKD = 1  # 港币
    OES_CURR_TYPE_USD = 2  # 美元
    _OES_CURR_TYPE_MAX = 3  # 货币种类最大值


# 费用类型标识符
class eOesFeeTypeT(Enum):
    _OES_FEE_TYPE_UNDEFINE = 0  # 未定义的费用类型
    OES_FEE_TYPE_EXCHANGE_STAMP = 0x1  # 交易所固定费用-印花税
    OES_FEE_TYPE_EXCHANGE_TRANSFER = 0x2  # 交易所固定费用-过户费
    OES_FEE_TYPE_EXCHANGE_SETTLEMENT = 0x3  # 交易所固定费用-结算费
    OES_FEE_TYPE_EXCHANGE_TRADE_RULE = 0x4  # 交易所固定费用-交易规费
    OES_FEE_TYPE_EXCHANGE_EXCHANGE = 0x5  # 交易所固定费用-经手费
    OES_FEE_TYPE_EXCHANGE_ADMINFER = 0x6  # 交易所固定费用-证管费
    OES_FEE_TYPE_EXCHANGE_OTHER = 0x7  # 交易所固定费用-其他费
    _OES_FEE_TYPE_EXCHANGE_MAX = 8  # 交易所固定费用最大值
    OES_FEE_TYPE_BROKER_BACK_END = 0x11  # 券商佣金-后台费用
    OES_FEE_TYPE_BROKER_CREDIT_INTEREST = 0x21  # 券商息费-融资融券息费


# 费用 (佣金/固定费用) 计算模式
class eOesCalcFeeModeT(Enum):
    OES_CALC_FEE_MODE_AMOUNT = 0  # 按金额
    OES_CALC_FEE_MODE_QTY = 1  # 按份额
    OES_CALC_FEE_MODE_ORD = 2  # 按笔数


# 出入金方向定义
class eOesFundTrsfDirectT(Enum):
    OES_FUND_TRSF_DIRECT_IN = 0  # 转入OES (入金)
    OES_FUND_TRSF_DIRECT_OUT = 1  # 转出OES (出金)


# 出入金转账类型定义
class eOesFundTrsfTypeT(Enum):
    OES_FUND_TRSF_TYPE_OES_BANK = 0  # OES和银行之间转账
    OES_FUND_TRSF_TYPE_OES_COUNTER = 1  # OES和主柜之间划拨资金
    OES_FUND_TRSF_TYPE_COUNTER_BANK = 2  # 主柜和银行之间转账
    OES_FUND_TRSF_TYPE_OES_TO_OES = 3  # 沪深OES之间的内部资金划拨
    _OES_FUND_TRSF_TYPE_MAX = 4  # 出入金转账类型最大值


# 出入金委托状态
class eOesFundTrsfStatusT(Enum):
    OES_FUND_TRSF_STS_UNDECLARED = 0  # 尚未上报
    OES_FUND_TRSF_STS_DECLARED = 1  # 已上报
    OES_FUND_TRSF_STS_WAIT_DONE = 2  # 主柜处理完成, 等待事务结束
    OES_FUND_TRSF_STS_DONE = 3  # 出入金处理完成
    _OES_FUND_TRSF_STS_ROLLBACK_MIN = 5  # 废单判断标志
    OES_FUND_TRSF_STS_UNDECLARED_ROLLBACK = 6  # 待回滚(未上报前)
    OES_FUND_TRSF_STS_DECLARED_ROLLBACK = 7  # 待回滚(已上报后)
    _OES_FUND_TRSF_STS_INVALID_MIN = 10  # 废单判断标志
    OES_FUND_TRSF_STS_INVALID_OES = 11  # OES内部判断为废单
    OES_FUND_TRSF_STS_INVALID_COUNTER = 12  # 主柜判断为废单
    OES_FUND_TRSF_STS_SUSPENDED = 13  # 挂起状态 (主柜的出入金执行状态未知, 待人工干预处理)


# 出入金指令来源分类
class eOesFundTrsfSourceTypeT(Enum):
    OES_FUND_TRSF_SOURCE_UNDEFINE = 0  # 未定义
    OES_FUND_TRSF_SOURCE_CUST = 1  # 客户发起
    OES_FUND_TRSF_SOURCE_TIMER = 2  # 系统内部定时任务发起
    OES_FUND_TRSF_SOURCE_COLO_PEER = 3  # 两地交易的对端结点发起
    _OES_FUND_TRSF_SOURCE_MAX = 4


# 业务类型定义
class eOesBusinessTypeT(Enum):
    OES_BUSINESS_TYPE_UNDEFINE = 0x0  # 未定义的业务范围
    OES_BUSINESS_TYPE_STOCK = 0x01  # 现货业务
    OES_BUSINESS_TYPE_OPTION = 0x02  # 期权业务
    OES_BUSINESS_TYPE_CREDIT = 0x04  # 信用业务
    _OES_BUSINESS_TYPE_MAX = 5  # 业务范围最大值 (单一业务)
    _OES_BUSINESS_TYPE_MAX_ALIGNED8 = 0x08  # 业务范围最大值 (单一业务, 按8字节对齐的大小)
    OES_BUSINESS_TYPE_ALL = 0xFF  # 所有业务


# 交易业务范围
# @deprecated 已废弃, 改为使用 eOesBusinessTypeT
class eOesBusinessScopeT(Enum):
    # 未定义的业务范围 @deprecated 已废弃
    OES_BIZ_SCOPE_UNDEFINE = eOesBusinessTypeT.OES_BUSINESS_TYPE_UNDEFINE.value
    # 现货业务 @deprecated 已废弃
    OES_BIZ_SCOPE_STOCK = eOesBusinessTypeT.OES_BUSINESS_TYPE_STOCK.value
    # 期权业务 @deprecated 已废弃
    OES_BIZ_SCOPE_OPTION = eOesBusinessTypeT.OES_BUSINESS_TYPE_OPTION.value
    # 所有业务 @deprecated 已废弃
    OES_BIZ_SCOPE_ALL = eOesBusinessTypeT.OES_BUSINESS_TYPE_ALL.value


# 账户类别定义
# 资金账户类别与证券账户类别定义相同
class eOesAcctTypeT(Enum):
    OES_ACCT_TYPE_NORMAL = 0  # 普通账户
    OES_ACCT_TYPE_CREDIT = 1  # 信用账户
    OES_ACCT_TYPE_OPTION = 2  # 衍生品账户
    _OES_ACCT_TYPE_MAX = 3  # 账户类别最大值
    _OES_ACCT_TYPE_MAX_ALIGNED4 = 4  # 账户类别最大值 (按4字节对齐的大小)
    _OES_ACCT_TYPE_MAX_ALIGNED8 = 8  # 账户类别最大值 (按8字节对齐的大小)


# 资金类型定义
# @deprecated 已废弃, 改为使用 eOesAcctTypeT
class eOesCashTypeT(Enum):
    # 普通账户资金/现货资金
    OES_CASH_TYPE_SPOT = eOesAcctTypeT.OES_ACCT_TYPE_NORMAL.value
    # 信用账户资金/信用资金
    OES_CASH_TYPE_CREDIT = eOesAcctTypeT.OES_ACCT_TYPE_CREDIT.value
    # 衍生品账户资金/期权保证金
    OES_CASH_TYPE_OPTION = eOesAcctTypeT.OES_ACCT_TYPE_OPTION.value
    # 资金类型最大值
    _OES_CASH_TYPE_MAX = eOesAcctTypeT._OES_ACCT_TYPE_MAX.value
    # 资金类型最大值 (按4字节对齐的大小)
    _OES_CASH_TYPE_MAX_ALIGNED4 = eOesAcctTypeT._OES_ACCT_TYPE_MAX_ALIGNED4.value
    # 资金类型最大值 (按8字节对齐的大小)
    _OES_CASH_TYPE_MAX_ALIGNED8 = eOesAcctTypeT._OES_ACCT_TYPE_MAX_ALIGNED8.value
    # 兼容性定义, 即将废弃
    OES_CASH_TYPE_CRE = eOesAcctTypeT.OES_ACCT_TYPE_CREDIT.value
    OES_CASH_TYPE_OPT = eOesAcctTypeT.OES_ACCT_TYPE_OPTION.value


# 客户状态/证券帐户/资金账户状态
class eOesAcctStatusT(Enum):
    OES_ACCT_STATUS_NORMAL = 0  # 正常
    OES_ACCT_STATUS_DISABLED = 1  # 非正常
    OES_ACCT_STATUS_LOCKED = 2  # 已锁定


# 交易权限的枚举值定义
class eOesTradingPermissionT(Enum):
    OES_PERMIS_MARKET_ORDER = 1 << 1  # 市价委托
    OES_PERMIS_STRUCTURED_FUND = 1 << 2  # 分级基金适当性
    OES_PERMIS_BOND_QUALIFIED_INVESTOR = 1 << 3  # 债券合格投资者
    OES_PERMIS_DELISTING = 1 << 5  # 退市整理股票
    OES_PERMIS_RISK_WARNING = 1 << 6  # 风险警示股票
    OES_PERMIS_SINGLE_MARKET_ETF = 1 << 7  # 单市场ETF申赎
    OES_PERMIS_CROSS_BORDER_ETF = 1 << 8  # 跨境ETF申赎
    OES_PERMIS_CROSS_MARKET_ETF = 1 << 9  # 跨市场ETF申赎
    OES_PERMIS_CURRENCY_ETF = 1 << 10  # 货币ETF申赎
    OES_PERMIS_GEMCDR = 1 << 11  # 创业板存托凭证
    OES_PERMIS_GEM_REGISTRATION = 1 << 12  # 注册制创业板交易
    OES_PERMIS_GEM_UNREGISTRATION = 1 << 13  # 核准制创业板交易
    OES_PERMIS_SH_HK_STOCK_CONNECT = 1 << 14  # 沪港通
    OES_PERMIS_SZ_HK_STOCK_CONNECT = 1 << 15  # 深港通
    OES_PERMIS_HLTCDR = 1 << 16  # 沪伦通存托凭证
    OES_PERMIS_CDR = 1 << 17  # 存托凭证
    OES_PERMIS_INNOVATION = 1 << 18  # 创新企业股票
    OES_PERMIS_KSH = 1 << 19  # 科创板交易
    OES_PERMIS_BOND_ETF = 1 << 20  # 债券ETF申赎
    OES_PERMIS_GOLD_ETF = 1 << 21  # 黄金ETF申赎
    OES_PERMIS_COMMODITY_FUTURES_ETF = 1 << 22  # 商品期货ETF申赎
    OES_PERMIS_GEM_INNOVATION = 1 << 23  # 创业板创新企业股票
    OES_PERMIS_CONVERTIBLE_BOND = 1 << 24  # 可转换公司债券
    OES_PERMIS_REITS = 1 << 25  # 基础设施基金
    _OES_PERMIS_ALL = 0xFFFFFFFFFFFFFFFF  # 全部权限
    # 以下定义已废弃, 只是为了兼容之前的版本而暂时保留
    OES_PERMIS_GEM = OES_PERMIS_GEM_UNREGISTRATION


# 投资者适当性管理分类
class eOesQualificationClassT(Enum):
    OES_QUALIFICATION_PUBLIC_INVESTOR = 0  # 公众投资者
    OES_QUALIFICATION_QUALIFIED_INVESTOR = 1  # 合格投资者(个人投资者)
    OES_QUALIFICATION_QUALIFIED_INSTITUTIONAL = 2  # 合格投资者(机构投资者)


# 投资者分类
#
# A类专业投资者: 满足《证券期货投资者适当性管理办法》第八条 (一)、 (二)、 (三) 点,
#      比如证券公司、期货公司、基金管理公司、商业银行、保险公司、发行的理财产品等
# B类专业投资者: 满足《证券期货投资者适当性管理办法》第八条 (四)、 (五) 点,
#      可以是法人或者其他组织、自然人, 满足一定的净资产和金融资产的要求, 具有相关的投资经验
# C类专业投资者: 满足《证券期货投资者适当性管理办法》第十一条 (一)、 (二) 点,
#      由普通投资者主动申请转化而来, 满足一定的净资产和金融资产的要求, 具有相关的投资经验
class eOesInvestorClassT(Enum):
    OES_INVESTOR_CLASS_NORMAL = 0  # 普通投资者
    OES_INVESTOR_CLASS_PROFESSIONAL_A = 1  # A类专业投资者
    OES_INVESTOR_CLASS_PROFESSIONAL_B = 2  # B类专业投资者
    OES_INVESTOR_CLASS_PROFESSIONAL_C = 3  # C类专业投资者
    _OES_INVESTOR_CLASS_MAX = 4  # 投资者分类的最大值


# 客户类型定义
class eOesCustTypeT(Enum):
    OES_CUST_TYPE_PERSONAL = 0  # 个人
    OES_CUST_TYPE_INSTITUTION = 1  # 机构
    OES_CUST_TYPE_PROPRIETARY = 2  # 自营
    OES_CUST_TYPE_PRODUCT = 3  # 产品
    OES_CUST_TYPE_MKT_MAKER = 4  # 做市商
    OES_CUST_TYPE_OTHERS = 5  # 其他
    _OES_CUST_TYPE_MAX = 6  # 客户类型的最大值


# 所有者类型 (内部使用)
class eOesOwnerTypeT(Enum):
    OES_OWNER_TYPE_UNDEFINE = 0  # 未定义
    OES_OWNER_TYPE_PERSONAL = 1  # 个人投资者
    OES_OWNER_TYPE_EXCHANGE = 101  # 交易所
    OES_OWNER_TYPE_MEMBER = 102  # 会员
    OES_OWNER_TYPE_INSTITUTION = 103  # 机构投资者
    OES_OWNER_TYPE_PROPRIETARY = 104  # 自营
    OES_OWNER_TYPE_MKT_MAKER = 105  # 做市商
    OES_OWNER_TYPE_SETTLEMENT = 106  # 结算机构
    _OES_OWNER_TYPE_MAX = 107  # 所有者类型的最大值


# 客户端类型定义 (内部使用)
class eOesClientTypeT(Enum):
    OES_CLIENT_TYPE_UNDEFINED = 0  # 客户端类型-未定义
    OES_CLIENT_TYPE_INVESTOR = 1  # 普通投资人
    OES_CLIENT_TYPE_VIRTUAL = 2  # 虚拟账户 (仅开通行情, 不可交易)


# 客户端状态定义 (内部使用)
class eOesClientStatusT(Enum):
    OES_CLIENT_STATUS_UNACTIVATED = 0  # 未激活 (不加载)
    OES_CLIENT_STATUS_ACTIVATED = 1  # 已激活 (正常加载)
    OES_CLIENT_STATUS_PAUSE = 2  # 已暂停 (正常加载, 不可交易)
    OES_CLIENT_STATUS_SUSPENDED = 3  # 已挂起 (不加载)
    OES_CLIENT_STATUS_CANCELLED = 4  # 已注销 (不加载)


# 通知消息来源分类
class eOesNotifySourceT(Enum):
    OES_NOTIFY_SOURCE_UNDEFINE = 0  # 未定义
    OES_NOTIFY_SOURCE_OES = 1  # OES 交易系统发起
    OES_NOTIFY_SOURCE_MON = 2  # MON 监控管理端发起
    OES_NOTIFY_SOURCE_BROKER = 3  # BROKER 期权经营机构发起
    OES_NOTIFY_SOURCE_EXCHANGE = 4  # EXCHANGE 交易所发起
    OES_NOTIFY_SOURCE_CSDC = 5  # CSDC 中国结算发起
    _OES_NOTIFY_SOURCE_MAX = 6  # 通知消息来源分类最大值


# 通知消息类型
class eOesNotifyTypeT(Enum):
    OES_NOTIFY_TYPE_UNDEFINE = 0  # 未定义
    # 从MON管理端下发的通知消息
    OES_NOTIFY_TYPE_CONTRACT_EXPIRE = 1  # 合约即将到期
    OES_NOTIFY_TYPE_CONTRACT_ADJUSTED = 2  # 合约近期有调整
    OES_NOTIFY_TYPE_UNDERLYING_DR_PROXIMITY = 3  # 合约标的即将除权除息
    OES_NOTIFY_TYPE_EXERCISE_DATE_PROXIMITY = 4  # 合约临近行权日
    OES_NOTIFY_TYPE_EXERCISED_POSSIBILITY = 5  # 合约可能被行权
    OES_NOTIFY_TYPE_EXERCISE_ASSIGNED = 6  # 合约被指派行权
    OES_NOTIFY_TYPE_COVERED_NOT_ENOUGH = 7  # 备兑证券标的不足
    OES_NOTIFY_TYPE_DELIVERY_NOT_ENOUGH = 8  # 交收证券不足
    OES_NOTIFY_TYPE_MARGIN_CALL = 9  # 追加保证金
    OES_NOTIFY_TYPE_FORCED_CLOSE = 10  # 强制平仓
    # -------------------------
    # 由OES主动触发的通知消息
    OES_NOTIFY_TYPE_CRD_COLLATERAL_INFO_UPDATE = 61  # 融资融券担保品信息更新
    OES_NOTIFY_TYPE_CRD_UNDERLYING_INFO_UPDATE = 62  # 融资融券标的信息更新
    OES_NOTIFY_TYPE_CRD_CASH_POSITION_UPDATE = 63  # 融资融券资金头寸信息更新
    OES_NOTIFY_TYPE_CRD_SECURITY_POSITION_UPDATE = 64  # 融资融券证券头寸信息更新
    OES_NOTIFY_TYPE_CRD_MAINTENANCE_RATIO_UPDATE = 65  # 融资融券维持担保比例更新
    OES_NOTIFY_TYPE_CRD_LINE_OF_CERDIT_UPDATE = 66  # 融资融券授信额度更新
    # -------------------------
    OES_NOTIFY_TYPE_OTHERS = 100  # 其它
    _OES_NOTIFY_TYPE_MAX = 101  # 通知消息类型最大值


# 通知消息等级
class eOesNotifyLevelT(Enum):
    OES_NOTIFY_LEVEL_UNDEFINE = 0  # 未定义
    OES_NOTIFY_LEVEL_LOW = 1  # 较低
    OES_NOTIFY_LEVEL_GENERAL = 2  # 一般
    OES_NOTIFY_LEVEL_IMPORTANT = 3  # 重要
    OES_NOTIFY_LEVEL_URGENT = 4  # 紧急
    _OES_NOTIFY_LEVEL_MAX = 5  # 通知消息等级最大值


# 消息通知范围
class eOesNotifyScopeT(Enum):
    OES_NOTIFY_SCOPE_UNDEFINE = 0  # 未定义
    OES_NOTIFY_SCOPE_CUST = 1  # 通知指定客户
    OES_NOTIFY_SCOPE_ALL = 2  # 通知所有投资者
    _OES_NOTIFY_SCOPE_MAX = 3  # 通知消息范围最大值


# 期权合约类型 (认购/认沽)
class eOesOptContractTypeT(Enum):
    OES_OPT_CONTRACT_TYPE_UNDEFINE = 0  # 未定义
    OES_OPT_CONTRACT_TYPE_CALL = 1  # 认购
    OES_OPT_CONTRACT_TYPE_PUT = 2  # 认沽
    _OES_OPT_CONTRACT_TYPE_MAX = 3  # 合约类型最大值


# 限制开仓标志
class eOesOptLimitOpenFlagT(Enum):
    OES_OPT_LIMIT_OPEN_FLAG_NORMAL = 0  # 可以开仓
    OES_OPT_LIMIT_OPEN_FLAG_LIMITED = 1  # 限制卖出开仓(不包括备兑开仓)和买入开仓


# 期权行权方式 (欧式/美式)
class eOesOptExerciseTypeT(Enum):
    OES_OPT_EXERCISE_TYPE_E = 0  # 欧式
    OES_OPT_EXERCISE_TYPE_A = 1  # 美式
    OES_OPT_EXERCISE_TYPE_B = 2  # 百慕大式
    _OES_OPT_EXERCISE_TYPE_MAX = 3  # 行权方式最大值


# 期权交割方式 (证券结算/现金结算, 适用于深交所)
class eOesOptDeliveryTypeT(Enum):
    OES_OPT_DELIVERY_TYPE_UNDEFINE = 0  # 未定义
    OES_OPT_DELIVERY_TYPE_SECURITY = 1  # 证券结算
    OES_OPT_DELIVERY_TYPE_CASH = 2  # 现金结算
    _OES_OPT_DELIVERY_TYPE_MAX = 3  # 交割方式最大值


# 期权持仓类型
class eOesOptPositionTypeT(Enum):
    OES_OPT_POSITION_TYPE_UNDEFINE = 0  # 未定义
    OES_OPT_POSITION_TYPE_LONG = 1  # 权利方
    OES_OPT_POSITION_TYPE_SHORT = 2  # 义务方
    OES_OPT_POSITION_TYPE_COVERED = 3  # 备兑方
    _OES_OPT_POSITION_TYPE_MAX = 4  # 期权持仓类型最大值


# 投资者期权等级
class eOesOptInvLevelT(Enum):
    OES_OPT_INV_LEVEL_UNDEFINE = 0  # 未定义 (机构投资者)
    OES_OPT_INV_LEVEL_1 = 1  # 个人投资者-一级交易权限
    OES_OPT_INV_LEVEL_2 = 2  # 个人投资者-二级交易权限
    OES_OPT_INV_LEVEL_3 = 3  # 个人投资者-三级交易权限
    _OES_OPT_INV_LEVEL_MAX = 4  # 期权投资人级别最大值


# 仓位影响 (平仓标识)
class eOesPositionEffectT(Enum):
    OES_POSITION_EFFECT_UNDEFINE = 0  # 未定义
    OES_POSITION_EFFECT_OPEN = 1  # 开仓
    OES_POSITION_EFFECT_CLOSE = 2  # 平仓
    _OES_POSITION_EFFECT_MAX = 3  # 仓位影响最大值


# 融资融券负债类型
class eOesCrdDebtTypeT(Enum):
    OES_CRD_DEBT_TYPE_UNDEFINE = 0  # 未定义的负债类型
    OES_CRD_DEBT_TYPE_MARGIN_BUY = 1  # 融资负债
    OES_CRD_DEBT_TYPE_SHORT_SELL = 2  # 融券负债
    OES_CRD_DEBT_TYPE_OTHER_DEBT = 3  # 其它负债
    _OES_CRD_DEBT_TYPE_MAX = 4


# 头寸性质
class eOesCrdCashGroupPropertyT(Enum):
    OES_CRD_CASH_GROUP_PROP_UNDEFINE = 0  # 未定义的头寸性质
    OES_CRD_CASH_GROUP_PROP_PUBLIC = 1  # 公共头寸
    OES_CRD_CASH_GROUP_PROP_SPECIAL = 2  # 专项头寸
    _OES_CRD_CASH_GROUP_PROP_MAX = 3


# 融资融券负债状态
class eOesCrdDebtStatusT(Enum):
    OES_CRD_DEBT_STATUS_UNDEFINE = 0  # 未定义的负债状态
    OES_CRD_DEBT_STATUS_NOT_TRADE = 1  # 合约尚未成交
    OES_CRD_DEBT_STATUS_NOT_REPAID = 2  # 未归还
    OES_CRD_DEBT_STATUS_PARTIALLY_REPAID = 3  # 部分归还
    OES_CRD_DEBT_STATUS_EXPIRED = 4  # 到期未了结
    OES_CRD_DEBT_STATUS_REPAID = 5  # 客户自行了结
    OES_CRD_DEBT_STATUS_MANNUAL_REPAID = 6  # 手工了结
    OES_CRD_DEBT_STATUS_NOT_DEBT = 7  # 未形成负债
    _OES_CRD_DEBT_STATUS_MAX = 8


# 融资融券负债展期状态
class eOesCrdDebtPostponeStatusT(Enum):
    OES_CRD_DEBT_POSTPONE_STATUS_UNDEFINE = 0  # 未定义的展期状态
    OES_CRD_DEBT_POSTPONE_STATUS_APPLICABLE = 1  # 可申请
    OES_CRD_DEBT_POSTPONE_STATUS_APPLIED = 2  # 已申请
    OES_CRD_DEBT_POSTPONE_STATUS_APPROVED = 3  # 审批通过
    OES_CRD_DEBT_POSTPONE_STATUS_UNAPPROVED = 4  # 审批不通过
    OES_CRD_DEBT_POSTPONE_STATUS_UNAPPLICABLE = 5  # 不可申请
    _OES_CRD_DEBT_POSTPONE_STATUS_MAX = 6


# 融资融券合同约定的负债归还模式
class eOesCrdDebtRepayModeT(Enum):
    OES_CRD_DEBT_REPAY_MODE_UNDEFINE = 0  # 未定义的负债归还模式
    OES_CRD_DEBT_REPAY_MODE_MATCHING_PRINCIPAL = 1  # 按比例归还 (利随本清)
    OES_CRD_DEBT_REPAY_MODE_INTEREST_FIRST = 2  # 优先归还息费 (先息后本)
    OES_CRD_DEBT_REPAY_MODE_PRINCIPAL_FIRST = 3  # 优先归还本金 (先本后息)
    _OES_CRD_DEBT_REPAY_MODE_MAX_COMPACT = 4  # 融资融券合同约定的负债归还模式的最大值
    _OES_CRD_DEBT_REPAY_MODE_INTEREST_ONLY = 10  # 仅归还息费 (仅适用于API接口 @see OES_CRD_ASSIGNABLE_REPAY_MODE_INTEREST_ONLY)
    _OES_CRD_DEBT_REPAY_MODE_MAX = 11


# 可以由API接口指定的融资融券负债归还模式
class eOesCrdAssignableRepayModeT(Enum):
    OES_CRD_ASSIGNABLE_REPAY_MODE_DEFAULT = 0  # 默认的负债归还模式 (使用融资融券合同约定的负债归还模式)
    OES_CRD_ASSIGNABLE_REPAY_MODE_INTEREST_ONLY = 10  # 仅归还息费
    _OES_CRD_ASSIGNABLE_REPAY_MODE_MAX = 11


# 融资融券负债流水类型
class eOesCrdDebtJournalTypeT(Enum):
    OES_CRD_DEBT_JOURNAL_TYPE_OPEN_POSITION = 0  # 合约开仓
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_BY_SELL = 1  # 卖券还款
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_DIRECT = 2  # 直接还款
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_BUY = 3  # 买券还券
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_DIRECT = 4  # 直接还券
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_CASH = 5  # 现金了结融券负债
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_STOCK_BY_OUTSIDE = 6  # 场外了结融券负债
    OES_CRD_DEBT_JOURNAL_TYPE_REPAY_MARGIN_BY_OUTSIDE = 7  # 场外了结融资负债
    OES_CRD_DEBT_JOURNAL_TYPE_CONTRACT_POST_PONE = 8  # 合约展期(审批)
    OES_CRD_DEBT_JOURNAL_TYPE_OTHER = 9  # 其它类型
    _OES_CRD_DEBT_JOURNAL_TYPE_MAX = 10


# 信用客户警戒状态
class eOesCrdCustGuardStatusT(Enum):
    OES_CRD_CUST_GUARD_STATUS_NORMAL = 0  # 正常
    OES_CRD_CUST_GUARD_STATUS_ALERT = 1  # 警惕
    OES_CRD_CUST_GUARD_STATUS_BLOCKLIST = 2  # 黑名单
    _OES_CRD_CUST_GUARD_STATUS_MAX = 3


# 通信消息的消息类型定义
class eOesMsgTypeT(Enum):
    # 交易类消息
    OESMSG_ORD_NEW_ORDER = 0x01  # 0x01/01  委托申报消息
    OESMSG_ORD_CANCEL_REQUEST = 0x02  # 0x02/02  撤单请求消息
    OESMSG_ORD_BATCH_ORDERS = 0x03  # 0x03/03  批量委托消息
    OESMSG_ORD_CREDIT_REPAY = 0x04  # 0x04/04  融资融券负债归还请求消息
    OESMSG_ORD_CREDIT_CASH_REPAY = 0x05  # 0x05/05  融资融券直接还款请求消息
    _OESMSG_ORD_MAX = 6  # 最大的委托消息类型
    # 非交易类消息
    _OESMSG_NONTRD_MIN = 0xC0  # 0xC0/192 最小的非交易消息类型
    OESMSG_NONTRD_FUND_TRSF_REQ = 0xC1  # 0xC1/193 出入金委托
    OESMSG_NONTRD_CHANGE_PASSWORD = 0xC2  # 0xC2/194 修改客户端登录密码
    OESMSG_NONTRD_OPT_CONFIRM_SETTLEMENT = 0xC3  # 0xC3/195 期权账户结算单确认
    _OESMSG_NONTRD_MAX = 196  # 最大的非交易消息类型
    # 执行报告类消息
    _OESMSG_RPT_MIN = 0x0A  # 0x0A/10  最小的执行报告消息类型
    OESMSG_RPT_SERVICE_STATE = 0x0E  # 0x0E/15  OES服务状态信息 (暂不支持订阅推送)
    OESMSG_RPT_MARKET_STATE = 0x10  # 0x10/16  市场状态信息
    OESMSG_RPT_REPORT_SYNCHRONIZATION = 0x11  # 0x11/17  回报同步的应答消息
    OESMSG_RPT_BUSINESS_REJECT = 0x12  # 0x12/18  OES业务拒绝 (因未通过风控检查等原因而被OES拒绝)
    OESMSG_RPT_ORDER_INSERT = 0x13  # 0x13/19  OES委托已生成 (已通过风控检查)
    OESMSG_RPT_ORDER_REPORT = 0x14  # 0x14/20  交易所委托回报 (包括交易所委托拒绝、委托确认和撤单完成通知)
    OESMSG_RPT_TRADE_REPORT = 0x15  # 0x15/21  交易所成交回报
    OESMSG_RPT_FUND_TRSF_REJECT = 0x16  # 0x16/22  出入金委托拒绝
    OESMSG_RPT_FUND_TRSF_REPORT = 0x17  # 0x17/23  出入金委托执行报告
    OESMSG_RPT_CASH_ASSET_VARIATION = 0x18  # 0x18/24  资金变动信息
    OESMSG_RPT_STOCK_HOLDING_VARIATION = 0x19  # 0x19/25  持仓变动信息 (股票)
    OESMSG_RPT_OPTION_HOLDING_VARIATION = 0x1A  # 0x1A/26  持仓变动信息 (期权)
    OESMSG_RPT_OPTION_UNDERLYING_HOLDING_VARIATION = 0x1B  # 0x1B/27  期权标的持仓变动信息
    OESMSG_RPT_OPTION_SETTLEMENT_CONFIRMED = 0x1C  # 0x1C/28  期权账户结算单确认消息
    OESMSG_RPT_NOTIFY_INFO = 0x1E  # 0x1E/30  OES通知消息
    OESMSG_RPT_CREDIT_CASH_REPAY_REPORT = 0x20  # 0x20/32  融资融券直接还款委托执行报告
    OESMSG_RPT_CREDIT_DEBT_CONTRACT_VARIATION = 0x21  # 0x21/33  融资融券合约变动信息
    OESMSG_RPT_CREDIT_DEBT_JOURNAL = 0x22  # 0x22/34  融资融券合约流水信息
    _OESMSG_RPT_MAX = 35  # 最大的回报消息类型
    # 查询类消息
    _OESMSG_QRYMSG_MIN = 0x2F  # 0x2F/47  最小的查询消息类型
    OESMSG_QRYMSG_OPT_HLD = 0x35  # 0x35/53  查询期权持仓信息
    OESMSG_QRYMSG_CUST = 0x36  # 0x36/54  查询客户信息
    OESMSG_QRYMSG_COMMISSION_RATE = 0x38  # 0x38/56  查询客户佣金信息
    OESMSG_QRYMSG_FUND_TRSF = 0x39  # 0x39/57  查询出入金信息
    OESMSG_QRYMSG_ETF = 0x3B  # 0x3B/59  查询ETF申赎产品信息
    OESMSG_QRYMSG_OPTION = 0x3D  # 0x3D/61  查询期权产品信息
    OESMSG_QRYMSG_LOT_WINNING = 0x3F  # 0x3F/63  查询新股配号、中签信息
    OESMSG_QRYMSG_TRADING_DAY = 0x40  # 0x40/64  查询当前交易日
    OESMSG_QRYMSG_MARKET_STATE = 0x41  # 0x41/65  查询市场状态
    OESMSG_QRYMSG_COUNTER_CASH = 0x42  # 0x42/66  查询客户主柜资金信息
    OESMSG_QRYMSG_OPT_UNDERLYING_HLD = 0x43  # 0x43/67  查询期权标的持仓信息
    OESMSG_QRYMSG_NOTIFY_INFO = 0x44  # 0x44/68  查询通知消息
    OESMSG_QRYMSG_OPT_POSITION_LIMIT = 0x45  # 0x45/69  查询期权限仓额度信息
    OESMSG_QRYMSG_OPT_PURCHASE_LIMIT = 0x46  # 0x46/70  查询期权限购额度信息
    OESMSG_QRYMSG_BROKER_PARAMS = 0x48  # 0x48/72  查询券商参数信息
    OESMSG_QRYMSG_COLOCATION_PEER_CASH = 0x49  # 0x49/73  查询两地交易时对端结点的资金资产信息
    OESMSG_QRYMSG_INV_ACCT = 0x51  # 0x51/81  查询证券账户信息 (0x37的更新版本, @since 0.15.9)
    OESMSG_QRYMSG_ORD = 0x54  # 0x54/84  查询委托信息 (0x31的更新版本, @since 0.16)
    OESMSG_QRYMSG_TRD = 0x55  # 0x55/85  查询成交信息 (0x32的更新版本, @since 0.16)
    OESMSG_QRYMSG_OPT_EXERCISE_ASSIGN = 0x56  # 0x56/86  查询期权行权指派信息 (0x47的更新版本, @since 0.16.0.3)
    OESMSG_QRYMSG_ISSUE = 0x57  # 0x57/87  查询证券发行信息 (0x3E的更新版本, @since 0.15.11)
    OESMSG_QRYMSG_STOCK = 0x58  # 0x58/88  查询现货产品信息 (0x52的更新版本, @since 0.15.11)
    OESMSG_QRYMSG_ETF_COMPONENT = 0x59  # 0x59/89  查询ETF成份证券信息 (0x3C的更新版本, @since 0.15.11)
    OESMSG_QRYMSG_CLIENT_OVERVIEW = 0x5A  # 0x5A/90  查询客户端总览信息 (0x30的更新版本, @since 0.15.11.11)
    OESMSG_QRYMSG_CASH_ASSET = 0x5B  # 0x5B/91  查询客户资金信息 (0x53的更新版本, @since 0.17)
    OESMSG_QRYMSG_STK_HLD = 0x5C  # 0x5C/92  查询股票持仓信息 (0x34的更新版本, @since 0.17)
    OESMSG_QRYMSG_CRD_DEBT_CONTRACT = 0x80  # 0x80/128 查询融资融券合约信息
    OESMSG_QRYMSG_CRD_CUST_SECU_DEBT_STATS = 0x81  # 0x81/129 查询客户单证券融资融券负债统计信息
    OESMSG_QRYMSG_CRD_CREDIT_ASSET = 0x82  # 0x82/130 查询信用资产信息
    OESMSG_QRYMSG_CRD_CASH_REPAY_INFO = 0x83  # 0x83/131 查询融资融券业务直接还款信息
    OESMSG_QRYMSG_CRD_CASH_POSITION = 0x84  # 0x84/132 查询融资融券业务资金头寸信息 (可融资头寸信息)
    OESMSG_QRYMSG_CRD_SECURITY_POSITION = 0x85  # 0x85/133 查询融资融券业务证券头寸信息 (可融券头寸信息)
    OESMSG_QRYMSG_CRD_EXCESS_STOCK = 0x86  # 0x86/134 查询融资融券业务余券信息
    OESMSG_QRYMSG_CRD_DEBT_JOURNAL = 0x87  # 0x87/135 查询融资融券合约流水信息 (仅当日流水)
    OESMSG_QRYMSG_CRD_INTEREST_RATE = 0x88  # 0x88/136 查询融资融券息费利率
    OESMSG_QRYMSG_CRD_UNDERLYING_INFO = 0x89  # 0x89/137 查询融资融券可充抵保证金证券及融资融券标的信息
    OESMSG_QRYMSG_CRD_DRAWABLE_BALANCE = 0x90  # 0x90/138 查询融资融券业务可取资金
    OESMSG_QRYMSG_CRD_COLLATERAL_TRANSFER_OUT_MAX_QTY = 0x91  # 0x91/139 查询融资融券担保品可转出的最大数量
    _OESMSG_QRYMSG_MAX = 146  # 最大的查询消息类型
    # 公共的会话类消息
    OESMSG_SESS_HEARTBEAT = 0xFA  # 0xFA/250 心跳消息
    OESMSG_SESS_TEST_REQUEST = 0xFB  # 0xFB/251 测试请求消息
    OESMSG_SESS_LOGIN_EXTEND = 0xFC  # 0xFC/252 登录扩展消息
    OESMSG_SESS_LOGOUT = 0xFE  # 0xFE/254 登出消息
    # 以下消息类型定义已废弃, 只是为了兼容之前的版本而暂时保留
    OESMSG_RPT_ORDER_REJECT = OESMSG_RPT_BUSINESS_REJECT


# 可订阅的回报消息类型定义
# - 0:      默认回报 (等价于: 0x01,0x02,0x04,0x08,0x10,0x20,0x40)
# - 0x0001: OES业务拒绝 (未通过风控检查等)
# - 0x0002: OES委托已生成 (已通过风控检查)
# - 0x0004: 交易所委托回报 (包括交易所委托拒绝、委托确认和撤单完成通知)
# - 0x0008: 交易所成交回报
# - 0x0010: 出入金委托执行报告 (包括出入金委托拒绝、出入金委托回报)
# - 0x0020: 资金变动信息
# - 0x0040: 持仓变动信息
# - 0x0080: 市场状态信息
# - 0x0100: 通知消息回报
# - 0x0200: 结算单确认消息
# - 0x0400: 融资融券直接还款委托执行报告
# - 0x0800: 融资融券合约变动信息
# - 0x1000: 融资融券合约流水信息
# - 0xFFFF: 所有回报
class eOesSubscribeReportTypeT(Enum):
    # 默认回报
    OES_SUB_RPT_TYPE_DEFAULT = 0
    # OES业务拒绝 (未通过风控检查等)
    OES_SUB_RPT_TYPE_BUSINESS_REJECT = 0x01
    # OES委托已生成 (已通过风控检查)
    OES_SUB_RPT_TYPE_ORDER_INSERT = 0x02
    # 交易所委托回报 (包括交易所委托拒绝、委托确认和撤单完成通知)
    OES_SUB_RPT_TYPE_ORDER_REPORT = 0x04
    # 交易所成交回报
    OES_SUB_RPT_TYPE_TRADE_REPORT = 0x08
    # 出入金委托执行报告 (包括出入金委托拒绝、出入金委托回报)
    OES_SUB_RPT_TYPE_FUND_TRSF_REPORT = 0x10
    # 资金变动信息
    OES_SUB_RPT_TYPE_CASH_ASSET_VARIATION = 0x20
    # 持仓变动信息
    OES_SUB_RPT_TYPE_HOLDING_VARIATION = 0x40
    # 市场状态信息
    OES_SUB_RPT_TYPE_MARKET_STATE = 0x80
    # 通知消息
    OES_SUB_RPT_TYPE_NOTIFY_INFO = 0x100
    # 结算单确认消息
    OES_SUB_RPT_TYPE_SETTLEMETN_CONFIRMED = 0x200
    # 融资融券直接还款委托执行报告
    OES_SUB_RPT_TYPE_CREDIT_CASH_REPAY_REPORT = 0x400
    # 融资融券合约变动信息
    OES_SUB_RPT_TYPE_CREDIT_DEBT_CONTRACT_VARIATION = 0x800
    # 融资融券合约流水信息
    OES_SUB_RPT_TYPE_CREDIT_DEBT_JOURNAL = 0x1000
    # 所有回报
    OES_SUB_RPT_TYPE_ALL = 0xFFFF
    _MAX_OES_SUB_RPT_TYPE = 0x7FFFFFFF


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


# 客户信用资产基础信息的结构体定义
class OesCrdCreditAssetBaseInfoT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 资金帐户类别(冗余自资金账户) @see eOesAcctTypeT
        ('cashType', c_uint8),
        # 资金帐户状态(冗余自资金账户) @see eOesAcctStatusT
        ('cashAcctStatus', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8 * 5),
        # 总资产 (包含其它担保资产价值; 单位精确到元后四位, 即1元=10000)
        # - 公式: 总资产 = 现金余额(包含冻结资金在内的资金余额) + 担保证券市值(不包含买入在途,包含卖出在途和转出在途) + 其它担保资产价值
        ('totalAssetValue', c_int64),
        # 总负债 (不包括在途负债; 单位精确到元后四位, 即1元=10000)
        # - 公式: 总负债 = 融资已买入金额 + 融券已卖出证券市值 + 利息及费用(不包含未成交部分的利息及费用) + 其它负债金额
        ('totalDebtValue', c_int64),
        # 维持担保比例 (千分比)
        ('maintenaceRatio', c_int32),
        # 按64位对齐的填充域
        ('_filler2', c_int32),
        # 保证金可用余额 (单位精确到元后四位, 即1元=10000)
        ('marginAvailableBal', c_int64),
        # 现金余额 (包含融券卖出所得资金和冻结资金在内的总现金资产; 单位精确到元后四位, 即1元=10000)
        ('cashBalance', c_int64),
        # 可用余额 (现金还款/买融资标的可用余额; 单位精确到元后四位, 即1元=10000)
        ('availableBal', c_int64),
        # 可取余额 (单位精确到元后四位, 即1元=10000)
        ('drawableBal', c_int64),
        # 买担保品可用余额 (单位精确到元后四位, 即1元=10000)
        ('buyCollateralAvailableBal', c_int64),
        # 买券还券可用余额 (单位精确到元后四位, 即1元=10000)
        ('repayStockAvailableBal', c_int64),
        # 融券卖出所得总额 (单位精确到元后四位, 即1元=10000)
        ('shortSellGainedAmt', c_int64),
        # 融券卖出所得可用金额 (单位精确到元后四位, 即1元=10000)
        ('shortSellGainedAvailableAmt', c_int64),
        # 日中累计已用于归还负债的资金总额 (卖券还款或现金归还金额; 单位精确到元后四位, 即1元=10000)
        ('totalRepaidAmt', c_int64),
        # 日中为归还负债而在途冻结的资金总额 (卖券还款或现金归还冻结金额; 单位精确到元后四位, 即1元=10000)
        ('repayFrzAmt', c_int64),
        # 融资买入授信额度 (单位精确到元后四位, 即1元=10000)
        ('marginBuyMaxQuota', c_int64),
        # 融券卖出授信额度 (单位精确到元后四位, 即1元=10000)
        ('shortSellMaxQuota', c_int64),
        # 融资融券总授信额度 (单位精确到元后四位, 即1元=10000)
        ('creditTotalMaxQuota', c_int64),
        # 融资买入已用授信额度 (单位精确到元后四位, 即1元=10000)
        # - 公式: 融资买入已用授信额度 = 融资负债金额 + 融资负债交易费用 + 在途融资金额 + 在途融资交易费用 + 其他负债金额
        ('marginBuyUsedQuota', c_int64),
        # 融资买入可用授信额度 (单位精确到元后四位, 即1元=10000)
        ('marginBuyAvailableQuota', c_int64),
        # 融券卖出已用授信额度 (单位精确到元后四位, 即1元=10000)
        # - 公式: 融券卖出已用授信额度 = 融券卖出金额 + 在途融券卖出金额
        ('shortSellUsedQuota', c_int64),
        # 融券卖出可用授信额度 (单位精确到元后四位, 即1元=10000)
        ('shortSellAvailableQuota', c_int64),
        # 专项资金头寸金额 (含已用; 单位精确到元后四位, 即1元=10000)
        ('specialCashPositionAmt', c_int64),
        # 专项资金头寸可用余额 (单位精确到元后四位, 即1元=10000)
        ('specialCashPositionAvailableBal', c_int64),
        # 公共资金头寸金额 (含已用; 单位精确到元后四位, 即1元=10000)
        ('publicCashPositionAmt', c_int64),
        # 公共资金头寸可用余额 (单位精确到元后四位, 即1元=10000)
        ('publicCashPositionAvailableBal', c_int64),
        # 证券持仓总市值 (日初持仓市值+累计买入持仓-累计卖出持仓; 单位精确到元后四位, 即1元=10000)
        # - 包括自有持仓和融资买入持仓
        # - 包含在途卖出冻结的持仓市值
        # - 包含转出冻结的证券持仓市值
        # - 包含直接还券冻结的持仓市值
        # - 不包含在途买入持仓市值
        # - 不包含在途担保品转入持仓市值
        ('collateralHoldingMarketCap', c_int64),
        # 在途卖出证券持仓市值 (单位精确到元后四位, 即1元=10000)
        ('collateralUncomeSellMarketCap', c_int64),
        # 转出冻结的证券持仓市值 (单位精确到元后四位, 即1元=10000)
        ('collateralTrsfOutMarketCap', c_int64),
        # 直接还券冻结的证券持仓市值 (单位精确到元后四位, 即1元=10000)
        ('collateralRepayDirectMarketCap', c_int64),
        # 融资负债金额 (单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtAmt', c_int64),
        # 融资负债交易费用 (单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtFee', c_int64),
        # 融资负债利息 (单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtInterest', c_int64),
        # 在途融资金额 (单位精确到元后四位, 即1元=10000)
        ('marginBuyUncomeAmt', c_int64),
        # 在途融资交易费用 (单位精确到元后四位, 即1元=10000)
        ('marginBuyUncomeFee', c_int64),
        # 在途融资利息 (单位精确到元后四位, 即1元=10000)
        ('marginBuyUncomeInterest', c_int64),
        # 融资买入证券市值 (单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtMarketCap', c_int64),
        # 融资买入负债占用的保证金金额 (单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtUsedMargin', c_int64),
        # 融券卖出金额 (单位精确到元后四位, 即1元=10000)
        ('shortSellDebtAmt', c_int64),
        # 融券负债交易费用 (单位精确到元后四位, 即1元=10000)
        ('shortSellDebtFee', c_int64),
        # 融券负债利息 (单位精确到元后四位, 即1元=10000)
        ('shortSellDebtInterest', c_int64),
        # 在途融券卖出金额 (单位精确到元后四位, 即1元=10000)
        ('shortSellUncomeAmt', c_int64),
        # 在途融券交易费用 (单位精确到元后四位, 即1元=10000)
        ('shortSellUncomeFee', c_int64),
        # 在途融券利息 (单位精确到元后四位, 即1元=10000)
        ('shortSellUncomeInterest', c_int64),
        # 融券卖出证券市值 (单位精确到元后四位, 即1元=10000)
        ('shortSellDebtMarketCap', c_int64),
        # 融券卖出负债占用的保证金金额 (单位精确到元后四位, 即1元=10000)
        ('shortSellDebtUsedMargin', c_int64),
        # 其他负债金额 (单位精确到元后四位, 即1元=10000)
        ('otherDebtAmt', c_int64),
        # 其他负债利息 (单位精确到元后四位, 即1元=10000)
        ('otherDebtInterest', c_int64),
        # 融资融券其他费用 (单位精确到元后四位, 即1元=10000)
        ('otherCreditFee', c_int64),
        # 融资融券专项头寸总费用 (包含融资专项头寸成本费、融券专项头寸成本费和转融通成本费; 单位精确到元后四位, 即1元=10000)
        ('creditTotalSpecialFee', c_int64),
        # 融资专项头寸成本费 (已包含在 '融资融券专项头寸总费用' 中; 单位精确到元后四位, 即1元=10000)
        ('marginBuySpecialFee', c_int64),
        # 融券专项头寸成本费 (已包含在 '融资融券专项头寸总费用' 中; 单位精确到元后四位, 即1元=10000)
        ('shortSellSpecialFee', c_int64),
        # 其它担保资产价值 (已包含在 '总资产' 中; 单位精确到元后四位, 即1元=10000)
        ('otherBackedAssetValue', c_int64),
        # 保留字段
        ('_reserve', c_char * 32),
    ]


# 融资融券可充抵保证金证券及融资融券标的基础信息的结构体定义
class OesCrdUnderlyingBaseInfoT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 是否为融资融券可充抵保证金证券 (0:不可充抵保证金, 1:可充抵保证金)
        ('isCrdCollateral', c_uint8),
        # 是否为融资标的 (0:不是融资标的, 1:是融资标的)
        ('isCrdMarginTradeUnderlying', c_uint8),
        # 是否为融券标的 (0:不是融券标的, 1:是融券标的)
        ('isCrdShortSellUnderlying', c_uint8),
        # 融资融券可充抵保证金证券的交易状态 (0:不可交易, 1:可交易)
        ('isCrdCollateralTradable', c_uint8),
        # 是否已为个人设置融资融券担保品参数
        ('isIndividualCollateral', c_uint8),
        # 是否已为个人设置融资融券标的参数
        ('isIndividualUnderlying', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8 * 6),
        # 可充抵保证金折算率 (单位:万分比)
        ('collateralRatio', c_int32),
        # 融资买入保证金比例 (单位:万分比)
        ('marginBuyRatio', c_int32),
        # 融券卖出保证金比例 (单位:万分比)
        ('shortSellRatio', c_int32),
        # 按64位对齐的填充域
        ('_filler2', c_int32 * 3),
    ]


# 融资融券资金头寸的基础信息结构体定义
class OesCrdCashPositionBaseInfoT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 头寸性质 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_CASH_POSITION_BASE_filler', c_uint8 * 2),
        # 资金头寸金额 (含已用)
        ('positionAmt', c_int64),
        # 日间已归还金额
        ('repaidPositionAmt', c_int64),
        # 累计已用金额 (含日初已用)
        ('usedPositionAmt', c_int64),
        # 当前尚未成交的在途冻结金额
        ('frzPositionAmt', c_int64),
        # 期初余额 (单位精确到元后四位, 即1元=10000)
        ('originalBalance', c_int64),
        # 期初可用余额 (单位精确到元后四位, 即1元=10000)
        ('originalAvailable', c_int64),
        # 期初已用金额 (期初待归还负债金额; 单位精确到元后四位, 即1元=10000)
        ('originalUsed', c_int64),
        # 预留的备用字段
        ('_CRD_CASH_POSITION_BASE_reserve', c_char * 32),
    ]


# 融资融券证券头寸的基础信息结构体定义
class OesCrdSecurityPositionBaseInfoT(PrintableStructure):
    _fields_ = [
        # 证券账户
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 头寸性质 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 按64位对齐的填充域
        ('_SECURITY_POSITION_BASE_filler', c_uint8 * 2),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 证券头寸数量 (含已用)
        ('positionQty', c_int64),
        # 日间已归还数量 (当日归还不可用)
        ('repaidPositionQty', c_int64),
        # 累计已用数量 (含日初已用)
        ('usedPositionQty', c_int64),
        # 当前尚未成交的在途冻结数量
        ('frzPositionQty', c_int64),
        # 期初数量
        ('originalBalanceQty', c_int64),
        # 期初可用数量
        ('originalAvailableQty', c_int64),
        # 期初已用数量 (期初待归还负债数量)
        ('originalUsedQty', c_int64),
        # 预留的备用字段
        ('_SECURITY_POSITION_BASE_reserve', c_char * 32),
    ]


# 融资融券合约的基础信息结构体定义
class OesCrdDebtContractBaseInfoT(PrintableStructure):
    _fields_ = [
        # 合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 证券的产品类型 @see eOesProductTypeT
        ('securityProductType', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 负债状态 @see eOesCrdDebtStatusT
        ('debtStatus', c_uint8),
        # 期初负债状态 @see eOesCrdDebtStatusT
        ('originalDebtStatus', c_uint8),
        # 负债归还模式 @see eOesCrdDebtRepayModeT
        ('debtRepayMode', c_uint8),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托价格 (单位精确到元后四位, 即1元=10000)
        ('ordPrice', c_int32),
        # 委托数量
        ('ordQty', c_int32),
        # 成交数量
        ('trdQty', c_int32),
        # 委托金额 (单位精确到元后四位, 即1元=10000)
        ('ordAmt', c_int64),
        # 成交金额 (单位精确到元后四位, 即1元=10000)
        ('trdAmt', c_int64),
        # 成交费用 (仅用于展示, 负债部分参见合约手续费(currentDebtFee)字段. 单位精确到元后四位, 即1元=10000)
        ('trdFee', c_int64),
        # 实时合约金额 (单位精确到元后四位, 即1元=10000)
        ('currentDebtAmt', c_int64),
        # 实时合约手续费 (单位精确到元后四位, 即1元=10000)
        ('currentDebtFee', c_int64),
        # 实时合约利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('currentDebtInterest', c_int64),
        # 实时合约数量
        ('currentDebtQty', c_int32),
        # 在途冻结数量
        ('uncomeDebtQty', c_int32),
        # 在途冻结金额 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtAmt', c_int64),
        # 在途冻结手续费 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtFee', c_int64),
        # 在途冻结利息 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtInterest', c_int64),
        # 累计已归还金额 (单位精确到元后四位, 即1元=10000)
        # - 对于融资，是归还的融资负债金额
        # - 对于融券，是归还的融券数量*归还时的成交价格 (即实际归还金额)
        ('totalRepaidAmt', c_int64),
        # 累计已归还手续费 (仅包含当日归还. 单位精确到元后四位, 即1元=10000)
        ('totalRepaidFee', c_int64),
        # 累计已归还利息 (单位精确到元后四位, 即1元=10000)
        ('totalRepaidInterest', c_int64),
        # 累计已归还数量
        # - 对于融券，是归还的融券负债数量
        # - 对于融资，是归还的融资金额/归还时该证券最新价格
        ('totalRepaidQty', c_int32),
        # 按64位对齐的填充域
        ('_CRD_DEBT_CONTRACT_BASE_filler2', c_int32),
        # 期初待归还金额 (单位精确到元后四位, 即1元=10000)
        ('originalDebtAmt', c_int64),
        # 期初待归还手续费 (单位精确到元后四位, 即1元=10000)
        ('originalDebtFee', c_int64),
        # 期初待归还利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('originalDebtInterest', c_int64),
        # 期初待归还数量
        ('originalDebtQty', c_int32),
        # 期初已归还数量
        # - 对于融券，是归还的融券负债数量
        # - 对于融资，是归还的融资金额/归还时该证券最新价格
        ('originalRepaidQty', c_int32),
        # 期初已归还金额 (单位精确到元后四位, 即1元=10000)
        # - 对于融资，是归还的融资负债金额
        # - 对于融券，是归还的融券数量*归还时成交价格
        ('originalRepaidAmt', c_int64),
        # 期初已归还利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('originalRepaidInterest', c_int64),
        # 罚息 (仅供展示, 已在利息中体现. 单位精确到元后四位, 即1元=10000)
        ('punishInterest', c_int64),
        # 保证金比例 (单位:万分比)
        ('marginRatio', c_int32),
        # 融资利率/融券费率 (单位精确到万分之一, 即费率8.36% = 836)
        ('interestRate', c_int32),
        # 负债截止日期 (格式为 YYYYMMDD, 形如 20160830)
        ('repayEndDate', c_int32),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 展期次数
        ('postponeTimes', c_int32),
        # 展期状态 @see eOesCrdDebtPostponeStatusT
        ('postponeStatus', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_DEBT_CONTRACT_BASE_filler3', c_uint8 * 3),
        # 预留的备用字段
        ('_CREDIT_DEBT_BASE_reserve', c_char * 32),
    ]


# 融资融券合约回报信息结构体定义
class OesCrdDebtContractReportT(PrintableStructure):
    _fields_ = [
        # 合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 证券的产品类型 @see eOesProductTypeT
        ('securityProductType', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 负债状态 @see eOesCrdDebtStatusT
        ('debtStatus', c_uint8),
        # 期初负债状态 @see eOesCrdDebtStatusT
        ('originalDebtStatus', c_uint8),
        # 负债归还模式 @see eOesCrdDebtRepayModeT
        ('debtRepayMode', c_uint8),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托价格 (单位精确到元后四位, 即1元=10000)
        ('ordPrice', c_int32),
        # 委托数量
        ('ordQty', c_int32),
        # 成交数量
        ('trdQty', c_int32),
        # 委托金额 (单位精确到元后四位, 即1元=10000)
        ('ordAmt', c_int64),
        # 成交金额 (单位精确到元后四位, 即1元=10000)
        ('trdAmt', c_int64),
        # 成交费用 (仅用于展示, 负债部分参见合约手续费(currentDebtFee)字段. 单位精确到元后四位, 即1元=10000)
        ('trdFee', c_int64),
        # 实时合约金额 (单位精确到元后四位, 即1元=10000)
        ('currentDebtAmt', c_int64),
        # 实时合约手续费 (单位精确到元后四位, 即1元=10000)
        ('currentDebtFee', c_int64),
        # 实时合约利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('currentDebtInterest', c_int64),
        # 实时合约数量
        ('currentDebtQty', c_int32),
        # 在途冻结数量
        ('uncomeDebtQty', c_int32),
        # 在途冻结金额 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtAmt', c_int64),
        # 在途冻结手续费 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtFee', c_int64),
        # 在途冻结利息 (单位精确到元后四位, 即1元=10000)
        ('uncomeDebtInterest', c_int64),
        # 累计已归还金额 (单位精确到元后四位, 即1元=10000)
        # - 对于融资，是归还的融资负债金额
        # - 对于融券，是归还的融券数量*归还时的成交价格 (即实际归还金额)
        ('totalRepaidAmt', c_int64),
        # 累计已归还手续费 (仅包含当日归还. 单位精确到元后四位, 即1元=10000)
        ('totalRepaidFee', c_int64),
        # 累计已归还利息 (单位精确到元后四位, 即1元=10000)
        ('totalRepaidInterest', c_int64),
        # 累计已归还数量
        # - 对于融券，是归还的融券负债数量
        # - 对于融资，是归还的融资金额/归还时该证券最新价格
        ('totalRepaidQty', c_int32),
        # 按64位对齐的填充域
        ('_CRD_DEBT_CONTRACT_BASE_filler2', c_int32),
        # 期初待归还金额 (单位精确到元后四位, 即1元=10000)
        ('originalDebtAmt', c_int64),
        # 期初待归还手续费 (单位精确到元后四位, 即1元=10000)
        ('originalDebtFee', c_int64),
        # 期初待归还利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('originalDebtInterest', c_int64),
        # 期初待归还数量
        ('originalDebtQty', c_int32),
        # 期初已归还数量
        # - 对于融券，是归还的融券负债数量
        # - 对于融资，是归还的融资金额/归还时该证券最新价格
        ('originalRepaidQty', c_int32),
        # 期初已归还金额 (单位精确到元后四位, 即1元=10000)
        # - 对于融资，是归还的融资负债金额
        # - 对于融券，是归还的融券数量*归还时成交价格
        ('originalRepaidAmt', c_int64),
        # 期初已归还利息 (含罚息. 单位精确到元后四位, 即1元=10000)
        ('originalRepaidInterest', c_int64),
        # 罚息 (仅供展示, 已在利息中体现. 单位精确到元后四位, 即1元=10000)
        ('punishInterest', c_int64),
        # 保证金比例 (单位:万分比)
        ('marginRatio', c_int32),
        # 融资利率/融券费率 (单位精确到万分之一, 即费率8.36% = 836)
        ('interestRate', c_int32),
        # 负债截止日期 (格式为 YYYYMMDD, 形如 20160830)
        ('repayEndDate', c_int32),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 展期次数
        ('postponeTimes', c_int32),
        # 展期状态 @see eOesCrdDebtPostponeStatusT
        ('postponeStatus', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_DEBT_CONTRACT_BASE_filler3', c_uint8 * 3),
        # 预留的备用字段
        ('_CREDIT_DEBT_BASE_reserve', c_char * 32),
        # 同一证券所有融券合约的合计可归还负债数量
        # - 公式: 同一证券合计可归还负债数量 = 日初融券负债数量 - 当日已归还融券数量 - 在途归还融券数量
        ('securityRepayableDebtQty', c_int64),
        # 该融券合约的当前可归还负债数量
        # - 公式: 合约当前可归还负债数量 = 实时合约数量 - 归还指定合约的在途归还数量
        # - @note 实际允许归还的负债数量, 为该融券合约可归还负债数量与对应证券可归还负债数量的较小者
        ('contractRepayableDebtQty', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 保留字段
        ('_reserve', c_char * 32),
    ]


# 融资融券合约负债流水的基础信息结构体定义
class OesCrdDebtJournalBaseInfoT(PrintableStructure):
    _fields_ = [
        # 合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 流水类型 @see eOesCrdDebtJournalTypeT
        ('journalType', c_uint8),
        # 强制标志 @see eOesOrdMandatoryFlagT
        ('mandatoryFlag', c_uint8),
        # 同一融资融券合约的负债流水的顺序号
        ('seqNo', c_int32),
        # 发生金额 (不含息费; 单位精确到元后四位, 即1元=10000)
        ('occurAmt', c_int64),
        # 发生费用 (单位精确到元后四位, 即1元=10000)
        ('occurFee', c_int64),
        # 发生利息 (单位精确到元后四位, 即1元=10000)
        ('occurInterest', c_int64),
        # 发生证券数量
        ('occurQty', c_int32),
        # 后余证券数量
        ('postQty', c_int32),
        # 后余金额 (不含息费; 单位精确到元后四位, 即1元=10000)
        ('postAmt', c_int64),
        # 后余费用 (单位精确到元后四位, 即1元=10000)
        ('postFee', c_int64),
        # 后余利息 (单位精确到元后四位, 即1元=10000)
        ('postInterest', c_int64),
        # 融券合约流水的理论发生金额 (单位精确到元后四位, 即1元=10000)
        # - 开仓流水中等同于发生金额, 即成交金额
        # - 归还流水中为对应于合约开仓价格的理论上的发生金额
        ('shortSellTheoryOccurAmt', c_int64),
        # 归还息费时使用融券卖出所得抵扣的金额 (单位精确到元后四位, 即1元=10000)
        ('useShortSellGainedAmt', c_int64),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 预留的备用字段
        ('_CRD_DEBT_JOURNAL_BASE_reserve', c_char * 32),
    ]


# 融资融券合约流水变动信息回报结构体定义
class OesCrdDebtJournalReportT(PrintableStructure):
    _fields_ = [
        # 合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 流水类型 @see eOesCrdDebtJournalTypeT
        ('journalType', c_uint8),
        # 强制标志 @see eOesOrdMandatoryFlagT
        ('mandatoryFlag', c_uint8),
        # 同一融资融券合约的负债流水的顺序号
        ('seqNo', c_int32),
        # 发生金额 (不含息费; 单位精确到元后四位, 即1元=10000)
        ('occurAmt', c_int64),
        # 发生费用 (单位精确到元后四位, 即1元=10000)
        ('occurFee', c_int64),
        # 发生利息 (单位精确到元后四位, 即1元=10000)
        ('occurInterest', c_int64),
        # 发生证券数量
        ('occurQty', c_int32),
        # 后余证券数量
        ('postQty', c_int32),
        # 后余金额 (不含息费; 单位精确到元后四位, 即1元=10000)
        ('postAmt', c_int64),
        # 后余费用 (单位精确到元后四位, 即1元=10000)
        ('postFee', c_int64),
        # 后余利息 (单位精确到元后四位, 即1元=10000)
        ('postInterest', c_int64),
        # 融券合约流水的理论发生金额 (单位精确到元后四位, 即1元=10000)
        # - 开仓流水中等同于发生金额, 即成交金额
        # - 归还流水中为对应于合约开仓价格的理论上的发生金额
        ('shortSellTheoryOccurAmt', c_int64),
        # 归还息费时使用融券卖出所得抵扣的金额 (单位精确到元后四位, 即1元=10000)
        ('useShortSellGainedAmt', c_int64),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 预留的备用字段
        ('_CRD_DEBT_JOURNAL_BASE_reserve', c_char * 32),
    ]


# 客户单证券融资融券负债统计基础信息的结构体定义
class OesCrdSecurityDebtStatsBaseInfoT(PrintableStructure):
    _fields_ = [
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 是否为融资融券可充抵保证金证券 (0:不可充抵保证金, 1:可充抵保证金)
        ('isCrdCollateral', c_uint8),
        # 是否为融资标的 (0:不是融资标的, 1:是融资标的)
        ('isCrdMarginTradeUnderlying', c_uint8),
        # 是否为融券标的 (0:不是融券标的, 1:是融券标的)
        ('isCrdShortSellUnderlying', c_uint8),
        # 融资融券可充抵保证金证券的交易状态 (0:不可交易, 1:可交易)
        ('isCrdCollateralTradable', c_uint8),
        # 可充抵保证金折算率 (单位:万分比)
        ('collateralRatio', c_int32),
        # 融资买入保证金比例 (单位:万分比)
        ('marginBuyRatio', c_int32),
        # 融券卖出保证金比例 (单位:万分比)
        ('shortSellRatio', c_int32),
        # 市值计算使用的证券价格 (等价于最新价或公允价, 取决于是否开启公允价格; 价格单位精确到元后四位, 即1元=10000)
        ('marketCapPrice', c_int32),
        # 可卖持仓数量
        ('sellAvlHld', c_int64),
        # 可划出持仓数量 (可充抵保证金证券(担保品)可划出数量)
        ('trsfOutAvlHld', c_int64),
        # 直接还券可用持仓数量
        ('repayStockDirectAvlHld', c_int64),
        # 同一证券所有融券合约的合计待归还负债数量
        # - 公式: 同一证券合计待归还负债数量 = 日初融券负债数量 - 当日已归还融券数量 - 在途归还融券数量
        ('shortSellRepayableDebtQty', c_int64),
        # 专项证券头寸数量 (含已用)
        ('specialSecurityPositionQty', c_int64),
        # 专项证券头寸已用数量 (含尚未成交的在途冻结数量)
        ('specialSecurityPositionUsedQty', c_int64),
        # 专项证券头寸可用数量
        # - 当可用头寸低于有效数量下限(卖委托数量下限)时该字段将返回0
        # - @note 实际剩余的未使用头寸数量可通过如下公式计算:
        # 实际剩余的可用头寸数量 = 专项证券头寸数量 - 专项证券头寸已用数量
        ('specialSecurityPositionAvailableQty', c_int64),
        # 公共证券头寸数量 (含已用)
        ('publicSecurityPositionQty', c_int64),
        # 公共证券头寸可用数量
        ('publicSecurityPositionAvailableQty', c_int64),
        # 担保证券持仓统计信息
        # 总持仓数量 (日初持仓数量+累计买入数量-累计卖出数量)
        # - 包括自有持仓和融资买入持仓
        # - 包含在途卖出冻结的持仓数量
        # - 包含转出冻结的持仓数量
        # - 包含直接还券冻结的持仓数量
        # - 不包含在途买入数量
        # - 不包含在途担保品转入持仓数量
        ('collateralHoldingQty', c_int64),
        # 在途买入数量 (不包括融资买入在途数量)
        ('collateralUncomeBuyQty', c_int64),
        # 在途转入持仓数量 (包含已确认和未确认数量, 不包含已撤单数量)
        ('collateralUncomeTrsfInQty', c_int64),
        # 在途卖出冻结的持仓数量
        ('collateralUncomeSellQty', c_int64),
        # 转出冻结的持仓数量 (包含已确认和未确认数量, 不包含已撤单数量)
        ('collateralTrsfOutQty', c_int64),
        # 直接还券冻结的持仓数量 (包含已确认和未确认数量, 不包含已撤单/废单数量)
        ('collateralRepayDirectQty', c_int64),
        # 融资买入负债统计信息
        # 融资负债金额 (不包括已还; 单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtAmt', c_int64),
        # 融资交易费用 (不包括已还; 单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtFee', c_int64),
        # 融资负债利息 (包括罚息, 不包括已还; 单位精确到元后四位, 即1元=10000)
        ('marginBuyDebtInterest', c_int64),
        # 融资负债数量 (不包括已还)
        ('marginBuyDebtQty', c_int64),
        # 在途融资买入金额, 单位精确到元后四位, 即1元 = 10000
        ('marginBuyUncomeAmt', c_int64),
        # 在途融资交易费用, 单位精确到元后四位, 即1元 = 10000
        ('marginBuyUncomeFee', c_int64),
        # 在途融资利息, 单位精确到元后四位, 即1元 = 10000
        ('marginBuyUncomeInterest', c_int64),
        # 在途融资数量
        ('marginBuyUncomeQty', c_int64),
        # 日初融资负债金额 (日初融资余额, 不包括日初已还)
        ('marginBuyOriginDebtAmt', c_int64),
        # 日初融资负债数量 (不包括日初已还)
        ('marginBuyOriginDebtQty', c_int64),
        # 当日已归还融资金额 (日中发生的归还金额, 不包括日初已还)
        ('marginBuyRepaidAmt', c_int64),
        # 当日已归还融资数量 (对应于合约开仓价格的理论上的已归还融资数量)
        ('marginBuyRepaidQty', c_int64),
        # 融券卖出负债统计信息
        # 融券负债金额 (不包括已还; 单位精确到元后四位, 即1元=10000)
        ('shortSellDebtAmt', c_int64),
        # 融券交易费用 (不包括已还; 单位精确到元后四位, 即1元=10000)
        ('shortSellDebtFee', c_int64),
        # 融券负债利息 (包括罚息, 不包括已还; 单位精确到元后四位, 即1元=10000)
        ('shortSellDebtInterest', c_int64),
        # 融券负债数量 (不包括已还)
        ('shortSellDebtQty', c_int64),
        # 在途融券卖出金额, 单位精确到元后四位, 即1元 = 10000
        ('shortSellUncomeAmt', c_int64),
        # 在途融券交易费用, 单位精确到元后四位, 即1元 = 10000
        ('shortSellUncomeFee', c_int64),
        # 在途融券利息, 单位精确到元后四位, 即1元 = 10000
        ('shortSellUncomeInterest', c_int64),
        # 在途融券数量
        ('shortSellUncomeQty', c_int64),
        # 日初融券负债数量 (日初融券余量, 不包括日初已还)
        ('shortSellOriginDebtQty', c_int64),
        # 当日已归还融券数量 (日中发生的归还数量, 不包括日初已还)
        ('shortSellRepaidQty', c_int64),
        # 在途归还融券数量
        ('shortSellUncomeRepaidQty', c_int64),
        # 当日已归还融券金额 (按开仓价格计算的理论上已归还融券金额; 单位精确到元后四位, 即1元=10000)
        ('shortSellRepaidAmt', c_int64),
        # 当日实际归还融券金额 (按成交价计算的当日实际归还融券金额; 单位精确到元后四位, 即1元=10000)
        ('shortSellRealRepaidAmt', c_int64),
        # '其它负债' 统计信息
        # '其它负债'的负债金额 (不包括已还; 单位精确到元后四位, 即1元=10000)
        ('otherDebtAmt', c_int64),
        # '其它负债'利息 (包括罚息, 不包括已还; 单位精确到元后四位, 即1元=10000)
        ('otherDebtInterest', c_int64),
        # 保留字段
        ('_reserve', c_char * 32),
    ]


# 余券基础信息的结构体定义
class OesCrdExcessStockBaseInfoT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码  @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 日初余券数量
        ('originExcessStockQty', c_int64),
        # 余券数量 (日初余券数量 + 日中余券数量)
        ('excessStockTotalQty', c_int64),
        # 余券已划转数量 (包含已确认和未确认数量, 不包含已撤单数量)
        ('excessStockUncomeTrsfQty', c_int64),
        # 余券可划转数量
        ('excessStockTrsfAbleQty', c_int64),
        # 保留字段
        ('_reserve', c_char * 32),
    ]


# 期权产品基础信息的结构体定义
class OesOptionBaseInfoT(PrintableStructure):
    _fields_ = [
        # 期权合约代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('contractType', c_uint8),
        # 行权方式 @see eOesOptExerciseTypeT
        ('exerciseType', c_uint8),
        # 交割方式 @see eOesOptDeliveryTypeT
        ('deliveryType', c_uint8),
        # 是否支持当日回转交易 (0: 不支持; 其他: 支持)
        ('isDayTrading', c_uint8),
        # 限制开仓标识 @see eOesOptLimitOpenFlagT
        ('limitOpenFlag', c_uint8),
        # 禁止交易标识 (0:正常交易, 非0:禁止交易) @see eOesSecuritySuspFlagT
        ('suspFlag', c_uint8),
        # 临时停牌标识 (0 未停牌, 1 已停牌)
        ('temporarySuspFlag', c_uint8),
        # 按64位对齐的填充域
        ('_OPTION_BASE_filler1', c_uint8 * 5),
        # 合约单位 (经过除权除息调整后的单位)
        ('contractUnit', c_int32),
        # 期权行权价 (经过除权除息调整后的价格, 单位精确到元后四位, 即1元 = 10000)
        ('exercisePrice', c_int32),
        # 交割日期 (格式为YYYYMMDD)
        ('deliveryDate', c_int32),
        # 交割月份 (格式为YYYYMM)
        ('deliveryMonth', c_int32),
        # 上市日期 (格式为YYYYMMDD)
        ('listDate', c_int32),
        # 最后交易日 (格式为YYYYMMDD)
        ('lastTradeDay', c_int32),
        # 行权起始日期 (格式为YYYYMMDD)
        ('exerciseBeginDate', c_int32),
        # 行权结束日期 (格式为YYYYMMDD)
        ('exerciseEndDate', c_int32),
        # 合约持仓量 (当前合约未平仓数)
        ('contractPosition', c_int64),
        # 合约前收盘价 (单位精确到元后四位, 即1元 = 10000)
        ('prevClosePrice', c_int32),
        # 合约前结算价 (单位精确到元后四位, 即1元 = 10000)
        ('prevSettlPrice', c_int32),
        # 标的证券前收盘价 (单位精确到元后四位, 即1元 = 10000)
        ('underlyingClosePrice', c_int32),
        # 最小报价单位 (单位精确到元后四位, 即1元 = 10000)
        ('priceTick', c_int32),
        # 涨停价 (单位精确到元后四位, 即1元 = 10000)
        ('upperLimitPrice', c_int32),
        # 跌停价 (单位精确到元后四位, 即1元 = 10000)
        ('lowerLimitPrice', c_int32),
        # 买入单位
        ('buyQtyUnit', c_int32),
        # 限价买数量上限 (单笔申报的最大张数)
        ('lmtBuyMaxQty', c_int32),
        # 限价买数量下限 (单笔申报的最小张数)
        ('lmtBuyMinQty', c_int32),
        # 市价买数量上限 (单笔申报的最大张数)
        ('mktBuyMaxQty', c_int32),
        # 市价买数量下限 (单笔申报的最小张数)
        ('mktBuyMinQty', c_int32),
        # 卖出单位
        ('sellQtyUnit', c_int32),
        # 限价卖数量上限 (单笔申报的最大张数)
        ('lmtSellMaxQty', c_int32),
        # 限价卖数量下限 (单笔申报的最小张数)
        ('lmtSellMinQty', c_int32),
        # 市价卖数量上限 (单笔申报的最大张数)
        ('mktSellMaxQty', c_int32),
        # 市价卖数量下限 (单笔申报的最小张数)
        ('mktSellMinQty', c_int32),
        # 单位保证金 (上调后的今卖开每张保证金, 单位精确到元后四位, 即1元 = 10000)
        ('sellMargin', c_int64),
        # 原始的单位保证金 (未上调的今卖开每张保证金, 单位精确到元后四位, 即1元 = 10000)
        ('originalSellMargin', c_int64),
        # 交易所保证金比例计算参数一 (单位:万分比)
        ('marginRatioParam1', c_int32),
        # 交易所保证金比例计算参数二 (单位:万分比)
        ('marginRatioParam2', c_int32),
        # 券商保证金上浮比例 (单位:万分比)
        ('increasedMarginRatio', c_int32),
        # 临近到期天数
        ('expireDays', c_int32),
        # 期权合约交易所代码
        ('contractId', c_char * OES_CONTRACT_EXCH_ID_MAX_LEN),
        # 期权合约名称 (UTF-8 编码)
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 期权合约状态信息
        # 该字段为 8 位字符串，左起每位表示特定的含义，无定义则填空格。
        # 第 1 位: ‘0’表示可开仓，‘1’表示限制卖出开仓（不包括备兑开仓）和买入开仓。
        # 第 2 位: 预留，暂填 ‘0’
        # 第 3 位: ‘0’表示未临近到期日，‘1’表示距离到期日不足 5 个交易日。
        # 第 4 位: ‘0’表示近期未做调整，‘1’表示最近 5 个交易日内合约发生过调整。
        # 第 5 位: ‘A’表示当日新挂牌的合约，‘E’表示存续的合约。
        ('securityStatusFlag', c_char * OES_SECURITY_STATUS_FLAG_MAX_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_OPTION_BASE_filler3', c_uint8 * 6),
        # 预留的备用字段
        ('_OPTION_BASE_reserve', c_char * 32),
    ]


# 期权持仓基础信息的结构体定义
class OesOptHoldingBaseInfoT(PrintableStructure):
    _fields_ = [
        # 账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 期权合约代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓类型 @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('contractType', c_uint8),
        # 套保标志 (0 非套保, 1 套保)
        ('hedgeFlag', c_uint8),
        # 按64位对齐的填充域
        ('_HOLD_BASE_filler', c_uint8),
        # 日初总持仓张数
        ('originalQty', c_int64),
        # 日初可用持仓
        ('originalAvlQty', c_int64),
        # 按摊薄持仓成本价计的日初总持仓成本 (日初摊薄持仓成本价 * 日初总持仓)
        ('originalCostAmt', c_int64),
        # 权利仓的日初持有成本 (日初持仓均价 * 日初总持仓, 不含费用)
        ('originalCarryingAmt', c_int64),
        # 日中累计开仓张数
        ('totalOpenQty', c_int64),
        # 开仓委托未成交张数
        ('uncomeQty', c_int64),
        # 日中累计平仓张数
        ('totalCloseQty', c_int64),
        # 平仓在途冻结张数
        ('closeFrzQty', c_int64),
        # 手动冻结张数
        ('manualFrzQty', c_int64),
        # 日中累计获得权利金
        ('totalInPremium', c_int64),
        # 日中累计付出权利金
        ('totalOutPremium', c_int64),
        # 日中累计开仓费用
        ('totalOpenFee', c_int64),
        # 日中累计平仓费用
        ('totalCloseFee', c_int64),
        # 权利仓行权冻结张数
        ('exerciseFrzQty', c_int64),
        # 义务仓占用保证金
        ('positionMargin', c_int64),
        # 预留的备用字段
        ('_OPT_HOLDING_BASE_reserve', c_char * 32),
    ]


# 期权持仓回报结构体定义
class OesOptHoldingReportT(PrintableStructure):
    _fields_ = [
        # 账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 期权合约代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓类型 @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('contractType', c_uint8),
        # 套保标志 (0 非套保, 1 套保)
        ('hedgeFlag', c_uint8),
        # 按64位对齐的填充域
        ('_HOLD_BASE_filler', c_uint8),
        # 日初总持仓张数
        ('originalQty', c_int64),
        # 日初可用持仓
        ('originalAvlQty', c_int64),
        # 按摊薄持仓成本价计的日初总持仓成本 (日初摊薄持仓成本价 * 日初总持仓)
        ('originalCostAmt', c_int64),
        # 权利仓的日初持有成本 (日初持仓均价 * 日初总持仓, 不含费用)
        ('originalCarryingAmt', c_int64),
        # 日中累计开仓张数
        ('totalOpenQty', c_int64),
        # 开仓委托未成交张数
        ('uncomeQty', c_int64),
        # 日中累计平仓张数
        ('totalCloseQty', c_int64),
        # 平仓在途冻结张数
        ('closeFrzQty', c_int64),
        # 手动冻结张数
        ('manualFrzQty', c_int64),
        # 日中累计获得权利金
        ('totalInPremium', c_int64),
        # 日中累计付出权利金
        ('totalOutPremium', c_int64),
        # 日中累计开仓费用
        ('totalOpenFee', c_int64),
        # 日中累计平仓费用
        ('totalCloseFee', c_int64),
        # 权利仓行权冻结张数
        ('exerciseFrzQty', c_int64),
        # 义务仓占用保证金
        ('positionMargin', c_int64),
        # 预留的备用字段
        ('_OPT_HOLDING_BASE_reserve', c_char * 32),
        # 可平仓张数 (单位: 张)
        ('closeAvlQty', c_int64),
        # 可行权张数 (单位: 张)
        ('exerciseAvlQty', c_int64),
        # 总持仓张数 (单位: 张)
        ('sumQty', c_int64),
        # 摊薄持仓成本价
        ('costPrice', c_int64),
        # 权利仓的持仓均价
        ('carryingAvgPrice', c_int64),
        # 可用的备兑持仓数量 (已锁定的标的持仓数量, 单位: 股)
        ('coveredAvlUnderlyingQty', c_int64),
        # 限仓额度信息
        # 可用的权利仓限额
        ('availableLongPositionLimit', c_int32),
        # 可用的总持仓限额
        ('availableTotalPositionLimit', c_int32),
        # 可用的单日买入开仓限额
        ('availableDailyBuyOpenLimit', c_int32),
        # 按64位对齐的填充域
        ('_OPT_HOLDING_EXT_filler2', c_int32),
        # 预留的备用字段
        ('_OPT_HOLDING_EXT_reserve', c_char * 32),
    ]


# 期权标的持仓基础信息的结构体定义
class OesOptUnderlyingHoldingBaseInfoT(PrintableStructure):
    _fields_ = [
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 期权市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 标的证券子类型 @see eOesSubSecurityTypeT
        ('underlyingSubSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_OPT_UNDERLYING_HOLD_BASE_filler', c_uint8 * 4),
        # 日初标的证券的总持仓数量 (单位: 股)
        ('originalHld', c_int64),
        # 日初标的证券的可用持仓数量 (单位: 股)
        ('originalAvlHld', c_int64),
        # 日初备兑仓主柜实际占用的标的证券数量 (单位: 股)
        ('originalCoveredQty', c_int64),
        # 日初备兑仓应占用的标的证券数量 (单位: 股)
        ('initialCoveredQty', c_int64),
        # 当前备兑仓实际占用的标的证券数量 (单位: 股)
        ('coveredQty', c_int64),
        # 当前备兑仓占用标的证券的缺口数量 (单位: 股)
        ('coveredGapQty', c_int64),
        # 当前可用于备兑开仓的标的持仓数量 (单位: 股)
        ('coveredAvlQty', c_int64),
        # 当前可锁定的标的持仓数量 (单位: 股)
        ('lockAvlQty', c_int64),
        # 标的证券总持仓, 包括当前可用持仓、不可交易持仓和在途冻结持仓在內的汇总值 (单位: 股)
        ('sumHld', c_int64),
        # 当日最大可减持额度
        # - 小于0, 不进行减持额度控制
        # - 大于或等于0, 最大可减持额度
        ('maxReduceQuota', c_int64),
    ]


# 期权标的持仓回报信息的结构体定义
class OesOptUnderlyingHoldingReportT(PrintableStructure):
    _fields_ = [
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 期权市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 标的证券子类型 @see eOesSubSecurityTypeT
        ('underlyingSubSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_OPT_UNDERLYING_HOLD_BASE_filler', c_uint8 * 4),
        # 日初标的证券的总持仓数量 (单位: 股)
        ('originalHld', c_int64),
        # 日初标的证券的可用持仓数量 (单位: 股)
        ('originalAvlHld', c_int64),
        # 日初备兑仓主柜实际占用的标的证券数量 (单位: 股)
        ('originalCoveredQty', c_int64),
        # 日初备兑仓应占用的标的证券数量 (单位: 股)
        ('initialCoveredQty', c_int64),
        # 当前备兑仓实际占用的标的证券数量 (单位: 股)
        ('coveredQty', c_int64),
        # 当前备兑仓占用标的证券的缺口数量 (单位: 股)
        ('coveredGapQty', c_int64),
        # 当前可用于备兑开仓的标的持仓数量 (单位: 股)
        ('coveredAvlQty', c_int64),
        # 当前可锁定的标的持仓数量 (单位: 股)
        ('lockAvlQty', c_int64),
        # 标的证券总持仓, 包括当前可用持仓、不可交易持仓和在途冻结持仓在內的汇总值 (单位: 股)
        ('sumHld', c_int64),
        # 当日最大可减持额度
        # - 小于0, 不进行减持额度控制
        # - 大于或等于0, 最大可减持额度
        ('maxReduceQuota', c_int64),
    ]


# 期权客户限仓额度基础信息的结构体定义
class OesOptionPositionLimitBaseInfoT(PrintableStructure):
    _fields_ = [
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 (衍生品市场) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 标的证券子类型 @see eOesSubSecurityTypeT
        ('underlyingSubSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_POSITION_LIMIT_BASE_filler1', c_uint8 * 4),
        # 限仓额度信息
        # 权利仓限额
        ('longPositionLimit', c_int32),
        # 总持仓限额
        ('totalPositionLimit', c_int32),
        # 单日买入开仓限额
        ('dailyBuyOpenLimit', c_int32),
        # 按64位对齐的填充域
        ('_POSITION_LIMIT_BASE_filler2', c_int32),
        # 合约品种维度的统计信息 (限仓相关)
        # 日初权利仓持仓数量 (单位: 张)
        ('originalLongQty', c_int32),
        # 累计买入开仓数量 (单位: 张)
        ('totalBuyOpenQty', c_int32),
        # 当前尚未成交的买入开仓数量
        ('uncomeBuyOpenQty', c_int32),
        # 累计卖出平仓数量 (单位: 张)
        ('totalSellCloseQty', c_int32),
        # 日初义务仓持仓数量 (单位: 张)
        ('originalShortQty', c_int32),
        # 累计卖出开仓数量 (单位: 张)
        ('totalSellOpenQty', c_int32),
        # 当前尚未成交的卖出开仓数量
        ('uncomeSellOpenQty', c_int32),
        # 累计买入平仓数量 (单位: 张)
        ('totalBuyCloseQty', c_int32),
        # 日初备兑义务仓持仓数量 (单位: 张)
        ('originalCoveredQty', c_int32),
        # 累计备兑开仓数量 (单位: 张)
        ('totalCoveredOpenQty', c_int32),
        # 当前尚未成交的备兑开仓数量 (单位: 张)
        ('uncomeCoveredOpenQty', c_int32),
        # 累计备兑平仓数量 (单位: 张)
        ('totalCoveredCloseQty', c_int32),
    ]


# 期权行权指派基础信息的结构体定义
class OesOptionExerciseAssignBaseT(PrintableStructure):
    _fields_ = [
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 期权合约代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓方向 (权利: 行权方, 义务/备兑: 被行权方) @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('contractType', c_uint8),
        # 交割方式 @see eOesOptDeliveryTypeT
        ('deliveryType', c_uint8),
        # 按64位对齐的填充域
        ('_OPTION_EXERCISE_ASSIGN_filler1', c_uint8),
        # 行权价格 (单位精确到元后四位, 即1元 = 10000)
        ('exercisePrice', c_int32),
        # 行权张数
        ('exerciseQty', c_int32),
        # 标的证券收付数量 (正数表示应收, 负数表示应付)
        ('deliveryQty', c_int64),
        # 行权开始日期 (格式为YYYYMMDD)
        ('exerciseBeginDate', c_int32),
        # 行权结束日期 (格式为YYYYMMDD)
        ('exerciseEndDate', c_int32),
        # 清算日期 (格式为YYYYMMDD)
        ('clearingDate', c_int32),
        # 交收日期 (格式为YYYYMMDD)
        ('deliveryDate', c_int32),
        # 清算金额
        ('clearingAmt', c_int64),
        # 清算费用 (费用合计, 佣金+过户费+结算费+其它费用)
        ('clearingFee', c_int64),
        # 实际收付金额 (正数表示应收, 负数表示应付)
        ('settlementAmt', c_int64),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_OPTION_EXERCISE_ASSIGN_filler3', c_uint8 * 6),
        # 期权合约名称 (UTF-8 编码)
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 预留的备用字段
        ('_OPTION_EXERCISE_ASSIGN_reserve', c_char * 16),
    ]


# 期权结算单确认信息的结构体定义
class OesOptSettlementConfirmBaseInfoT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', UserInfo),
        # 登录客户端编号
        ('clientId', c_int16),
        # 登录客户端环境号
        ('clEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler2', c_int8),
        # 发生日期 (格式为 YYYYMMDD, 形如 20160830)
        ('transDate', c_int32),
        # 发生时间 (格式为 HHMMSSsss, 形如 141205000)
        ('transTime', c_int32),
        # 拒绝原因
        ('rejReason', c_int32),
        # 预留的备用字段
        ('_OPT_SETTLEMENT_CONFIRM_BASE_reserve', c_char * 24),
    ]


# 期权结算单确认回报信息的结构体定义
class OesOptSettlementConfirmReportT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', UserInfo),
        # 登录客户端编号
        ('clientId', c_int16),
        # 登录客户端环境号
        ('clEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler2', c_int8),
        # 发生日期 (格式为 YYYYMMDD, 形如 20160830)
        ('transDate', c_int32),
        # 发生时间 (格式为 HHMMSSsss, 形如 141205000)
        ('transTime', c_int32),
        # 拒绝原因
        ('rejReason', c_int32),
        # 预留的备用字段
        ('_OPT_SETTLEMENT_CONFIRM_BASE_reserve', c_char * 24),
    ]


# 委托请求的结构体定义
class OesOrdReqT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水, 用于识别重复的委托申报)
        ('clSeqNo', c_int32),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 订单类型 @see eOesOrdTypeShT eOesOrdTypeSzT
        ('ordType', c_uint8),
        # 买卖类型 @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_ORD_BASE_INFO_filler', c_uint8),
        # 证券账户 (可以为空, 为空则自动填充)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码 (撤单时被撤委托的证券代码可不填)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 委托数量
        ('ordQty', c_int32),
        # 委托价格, 单位精确到元后四位, 即1元 = 10000
        ('ordPrice', c_int32),
        # 原始订单(待撤销的订单)的客户订单编号 (仅撤单时需要填充)
        ('origClOrdId', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
    ]


# 撤单请求的结构体定义
class OesOrdCancelReqT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水, 用于识别重复的委托申报, 必填)
        ('clSeqNo', c_int32),
        # 市场代码 (必填) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_ORD_CANCEL_BASE_INFO_filler1', c_uint8 * 3),
        # 证券账户 (选填, 若不为空则校验待撤订单是否匹配)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码 (选填, 若不为空则校验待撤订单是否匹配)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 原始订单(待撤销的订单)的客户委托流水号 (若使用 origClOrdId, 则不必填充该字段)
        ('origClSeqNo', c_int32),
        # 原始订单(待撤销的订单)的客户端环境号 (小于等于0, 则使用当前会话的 clEnvId)
        ('origClEnvId', c_int8),
        # 按64位对齐的填充域
        ('_ORD_CANCEL_BASE_INFO_filler2', c_uint8 * 3),
        # 原始订单(待撤销的订单)的客户订单编号 (若使用 origClSeqNo, 则不必填充该字段)
        ('origClOrdId', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
    ]


# 委托拒绝(OES业务拒绝)的结构体定义
class OesOrdRejectT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水, 用于识别重复的委托申报)
        ('clSeqNo', c_int32),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 订单类型 @see eOesOrdTypeShT eOesOrdTypeSzT
        ('ordType', c_uint8),
        # 买卖类型 @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_ORD_BASE_INFO_filler', c_uint8),
        # 证券账户 (可以为空, 为空则自动填充)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码 (撤单时被撤委托的证券代码可不填)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 委托数量
        ('ordQty', c_int32),
        # 委托价格, 单位精确到元后四位, 即1元 = 10000
        ('ordPrice', c_int32),
        # 原始订单(待撤销的订单)的客户订单编号 (仅撤单时需要填充)
        ('origClOrdId', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
        # 原始订单(待撤销的订单)的客户委托流水号 (仅适用于撤单请求)
        ('origClSeqNo', c_int32),
        # 原始订单(待撤销的订单)的客户端环境号 (仅适用于撤单请求)
        ('origClEnvId', c_int8),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 客户端编号
        ('clientId', c_int16),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 订单拒绝原因
        ('ordRejReason', c_int32),
        # 业务类型 @see eOesBusinessTypeT
        ('businessType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
    ]


# 委托确认的结构体定义
class OesOrdCnfmT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水, 用于识别重复的委托申报)
        ('clSeqNo', c_int32),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 订单类型 @see eOesOrdTypeShT eOesOrdTypeSzT
        ('ordType', c_uint8),
        # 买卖类型 @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_ORD_BASE_INFO_filler', c_uint8),
        # 证券账户 (可以为空, 为空则自动填充)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码 (撤单时被撤委托的证券代码可不填)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 委托数量
        ('ordQty', c_int32),
        # 委托价格, 单位精确到元后四位, 即1元 = 10000
        ('ordPrice', c_int32),
        # 原始订单(待撤销的订单)的客户订单编号 (仅撤单时需要填充)
        ('origClOrdId', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
        # 客户订单编号 (在OES内具有唯一性的内部委托编号)
        ('clOrdId', c_int64),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 原始订单(待撤销的订单)的客户端环境号 (仅适用于撤单委托)
        ('origClEnvId', c_int8),
        # 原始订单(待撤销的订单)的客户委托流水号 (仅适用于撤单委托)
        ('origClSeqNo', c_int32),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 委托确认时间 (格式为 HHMMSSsss, 形如 141206000)
        ('ordCnfmTime', c_int32),
        # 订单当前状态 @see eOesOrdStatusT
        ('ordStatus', c_uint8),
        # 委托确认状态 (交易所返回的回报状态, 仅供参考)  @see eOesOrdStatusT
        ('ordCnfmSts', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 平台号 (OES内部使用) @see eOesPlatformIdT
        ('_platformId', c_uint8),
        # 交易网关组序号 (OES内部使用)
        ('_tgwGrpNo', c_uint8),
        # 交易网关平台分区号 (OES内部使用)
        ('_tgwPartitionNo', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 交易所订单编号 (深交所的订单编号是16位的非数字字符串)
        ('exchOrdId', c_char * OES_EXCH_ORDER_ID_MAX_LEN),
        # 已报盘标志 (OES内部使用)
        ('_declareFlag', c_uint8),
        # 重复回报标志 (OES内部使用)
        ('_repeatFlag', c_uint8),
        # 所有者类型 @see eOesOwnerTypeT
        ('ownerType', c_uint8),
        # 委托当前冻结的交易金额
        ('frzAmt', c_int64),
        # 委托当前冻结的利息
        ('frzInterest', c_int64),
        # 委托当前冻结的交易费用
        ('frzFee', c_int64),
        # 委托累计已发生的交易金额
        ('cumAmt', c_int64),
        # 委托累计已发生的利息
        ('cumInterest', c_int64),
        # 委托累计已发生的交易费用
        ('cumFee', c_int64),
        # 累计执行数量 (累计成交数量)
        ('cumQty', c_int32),
        # 已撤单数量
        ('canceledQty', c_int32),
        # 订单/撤单拒绝原因
        ('ordRejReason', c_int32),
        # 交易所错误码
        ('exchErrCode', c_int32),
        # PBU代码 (席位号)
        ('pbuId', c_int32),
        # 营业部代码
        ('branchId', c_int32),
        # 回报记录号 (OES内部使用)
        ('_rowNum', c_int32),
        # OIW委托编号 (OES内部使用)
        ('_recNum', c_uint32),
        # 委托请求的初始接收时间
        ('_ordReqOrigRecvTime', STimespec32T),
        # 委托请求的入队时间
        ('_ordReqCollectedTime', STimespec32T),
        # 委托请求的实际处理开始时间
        ('_ordReqActualDealTime', STimespec32T),
        # 委托请求的处理完成时间
        ('_ordReqProcessedTime', STimespec32T),
        # 委托确认的开始采集时间
        ('_ordCnfmOrigRecvTime', STimespec32T),
        # 委托确认的采集完成时间
        ('_ordCnfmCollectedTime', STimespec32T),
        # 委托确认的实际处理开始时间
        ('_ordCnfmActualDealTime', STimespec32T),
        # 委托确认的处理完成时间
        ('_ordCnfmProcessedTime', STimespec32T),
        # 初始报盘时间
        ('_ordDeclareTime', STimespec32T),
        # 报盘完成时间
        ('_ordDeclareDoneTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
        # 委托当前冻结的保证金
        ('frzMargin', c_int64),
        # 委托累计已使用的保证金
        ('cumMargin', c_int64),
        # 业务类型 @see eOesBusinessTypeT
        ('businessType', c_uint8),
        # 强制标志 @see eOesOrdMandatoryFlagT
        ('mandatoryFlag', c_uint8),
        # 归还模式 (仅适用于卖券还款委托) @see eOesCrdDebtRepayModeT
        ('repayMode', c_uint8),
        # 按64位对齐的填充域
        ('_ORD_CNFM_EXT_filler', c_uint8 * 5),
        # 预留的备用字段
        ('_ORD_CNFM_EXT_reserve', c_char * 16),
    ]


# 融资融券负债归还请求 (除直接还款以外的直接还券、买券还券、卖券还款等负债归还请求)
class OesCrdRepayReqT(PrintableStructure):
    _fields_ = [
        # 委托请求信息
        ('ordReq', OesOrdReqT),
        # 归还模式 (仅适用于归还融资负债) @see eOesCrdAssignableRepayModeT
        ('repayMode', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 指定归还的合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
    ]


# 融资融券直接还款请求定义
class OesCrdCashRepayReqT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 归还模式 @see eOesCrdAssignableRepayModeT
        ('repayMode', c_uint8),
        # 归还指令类型 @see eOesCrdDebtJournalTypeT
        ('repayJournalType', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_CASH_REPAY_REQ_BASE_filler', c_uint8 * 2),
        # 归还金额 (单位精确到元后四位, 即1元=10000)
        ('repayAmt', c_int64),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 指定归还的合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
    ]


# 融资融券直接还款请求执行状态回报的结构体定义
class OesCrdCashRepayReportT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 归还模式 @see eOesCrdAssignableRepayModeT
        ('repayMode', c_uint8),
        # 归还指令类型 @see eOesCrdDebtJournalTypeT
        ('repayJournalType', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_CASH_REPAY_REQ_BASE_filler', c_uint8 * 2),
        # 归还金额 (单位精确到元后四位, 即1元=10000)
        ('repayAmt', c_int64),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 指定归还的合约编号
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托请求的客户端原始发送时间 (OES内部使用, 由API在发送时自动填充)
        ('_ordReqOrigSendTime', STimespec32T),
        # 证券账户 (仅适用于管理端现金了结/场外了结融券负债委托回报)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码 (仅适用于管理端现金了结/场外了结融券负债委托回报)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8 * 7),
        # 委托价格 (公允价格, 仅适用于管理端现金了结/场外了结融券负债委托回报; 单位精确到元后四位, 即1元=10000)
        ('ordPrice', c_int32),
        # 归还数量 (仅适用于管理端现金了结/场外了结融券负债委托回报)
        ('ordQty', c_int32),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 客户订单编号 (在OES内具有唯一性的内部委托编号, 只有有效的委托才会生成, 被拒绝的委托该字段为0)
        ('clOrdId', c_int64),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 委托强制标志
        ('mandatoryFlag', c_uint8),
        # 订单当前状态 @see eOesOrdStatusT
        ('ordStatus', c_uint8),
        # 所有者类型 (被拒绝的委托该字段为0) @see eOesOwnerTypeT
        ('ownerType', c_uint8),
        # 按64位对齐的填充域
        ('_filler2', c_uint8 * 2),
        # 订单拒绝原因
        ('ordRejReason', c_int32),
        # 实际归还数量 (仅适用于管理端现金了结/场外了结融券负债委托回报)
        ('repaidQty', c_int32),
        # 实际归还金额 (单位精确到元后四位, 即1元=10000)
        ('repaidAmt', c_int64),
        # 实际归还费用 (单位精确到元后四位, 即1元=10000)
        ('repaidFee', c_int64),
        # 实际归还利息 (单位精确到元后四位, 即1元=10000)
        ('repaidInterest', c_int64),
        # 营业部编号 (被拒绝的委托该字段为0)
        ('branchId', c_int32),
        # 按64位对齐的填充域
        ('_filler3', c_int32),
    ]


# 成交基础信息的结构体定义
class OesTrdBaseInfoT(PrintableStructure):
    _fields_ = [
        # 交易所成交编号 (以下的6个字段是成交信息的联合索引字段)
        ('exchTrdNum', c_int64),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 买卖类型 (取值范围: 买/卖, 申购/赎回(仅深圳)) @see eOesBuySellTypeT
        ('trdSide', c_uint8),
        # 平台号 (OES内部使用) @see eOesPlatformIdT
        ('_platformId', c_uint8),
        # 成交类型 (OES内部使用) @see eOesTrdCnfmTypeT
        ('_trdCnfmType', c_uint8),
        # ETF成交回报顺序号 (OES内部使用), 为区分ETF成交记录而设置 (以订单为单位)
        ('_etfTrdCnfmSeq', c_uint32),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成交日期 (格式为 YYYYMMDD, 形如 20160830)
        ('trdDate', c_int32),
        # 成交时间 (格式为 HHMMSSsss, 形如 141205000)
        ('trdTime', c_int32),
        # 成交数量
        ('trdQty', c_int32),
        # 成交价格 (单位精确到元后四位, 即: 1元=10000)
        ('trdPrice', c_int32),
        # 成交金额 (单位精确到元后四位, 即: 1元=10000)
        ('trdAmt', c_int64),
        # 客户订单编号
        ('clOrdId', c_int64),
        # 累计执行数量
        ('cumQty', c_int32),
        # 回报记录号 (OES内部使用)
        ('_rowNum', c_int32),
        # 交易网关组序号 (OES内部使用)
        ('_tgwGrpNo', c_uint8),
        # ETF赎回得到的替代资金是否当日可用 (OES内部使用)
        ('_isTrsfInCashAvailable', c_uint8),
        # 交易网关平台分区号 (OES内部使用)
        ('_tgwPartitionNo', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 原始委托数量
        ('origOrdQty', c_int32),
        # PBU代码 (席位号)
        ('pbuId', c_int32),
        # 营业部代码
        ('branchId', c_int32),
    ]


# 成交回报结构体定义
class OesTrdCnfmT(PrintableStructure):
    _fields_ = [
        # 交易所成交编号 (以下的6个字段是成交信息的联合索引字段)
        ('exchTrdNum', c_int64),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 买卖类型 (取值范围: 买/卖, 申购/赎回(仅深圳)) @see eOesBuySellTypeT
        ('trdSide', c_uint8),
        # 平台号 (OES内部使用) @see eOesPlatformIdT
        ('_platformId', c_uint8),
        # 成交类型 (OES内部使用) @see eOesTrdCnfmTypeT
        ('_trdCnfmType', c_uint8),
        # ETF成交回报顺序号 (OES内部使用), 为区分ETF成交记录而设置 (以订单为单位)
        ('_etfTrdCnfmSeq', c_uint32),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成交日期 (格式为 YYYYMMDD, 形如 20160830)
        ('trdDate', c_int32),
        # 成交时间 (格式为 HHMMSSsss, 形如 141205000)
        ('trdTime', c_int32),
        # 成交数量
        ('trdQty', c_int32),
        # 成交价格 (单位精确到元后四位, 即: 1元=10000)
        ('trdPrice', c_int32),
        # 成交金额 (单位精确到元后四位, 即: 1元=10000)
        ('trdAmt', c_int64),
        # 客户订单编号
        ('clOrdId', c_int64),
        # 累计执行数量
        ('cumQty', c_int32),
        # 回报记录号 (OES内部使用)
        ('_rowNum', c_int32),
        # 交易网关组序号 (OES内部使用)
        ('_tgwGrpNo', c_uint8),
        # ETF赎回得到的替代资金是否当日可用 (OES内部使用)
        ('_isTrsfInCashAvailable', c_uint8),
        # 交易网关平台分区号 (OES内部使用)
        ('_tgwPartitionNo', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 原始委托数量
        ('origOrdQty', c_int32),
        # PBU代码 (席位号)
        ('pbuId', c_int32),
        # 营业部代码
        ('branchId', c_int32),
        # 客户委托流水号
        ('clSeqNo', c_int32),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 证券子类别 (为保持兼容而位置凌乱, 后续会做调整) @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 订单当前状态 @see eOesOrdStatusT
        ('ordStatus', c_uint8),
        # 订单类型 @see eOesOrdTypeShT eOesOrdTypeSzT
        ('ordType', c_uint8),
        # 买卖类型 @see eOesBuySellTypeT
        ('ordBuySellType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 原始委托价格, 单位精确到元后四位, 即1元 = 10000
        ('origOrdPrice', c_int32),
        # 累计成交金额
        ('cumAmt', c_int64),
        # 累计成交利息
        ('cumInterest', c_int64),
        # 累计交易费用
        ('cumFee', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 成交确认的开始采集时间
        ('_trdCnfmOrigRecvTime', STimespec32T),
        # 成交确认的采集完成时间
        ('_trdCnfmCollectedTime', STimespec32T),
        # 成交确认的实际处理开始时间 (POC测试时会被复用于存储委托请求的原始发送时间)
        ('_trdCnfmActualDealTime', STimespec32T),
        # 成交确认的处理完成时间
        ('_trdCnfmProcessedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
        # 债券利息
        ('trdInterest', c_int64),
        # 交易费用
        ('trdFee', c_int64),
        # 占用/释放的保证金
        ('trdMargin', c_int64),
        # 累计占用/释放的保证金
        ('cumMargin', c_int64),
        # 业务类型 @see eOesBusinessTypeT
        ('businessType', c_uint8),
        # 强制标志 @see eOesOrdMandatoryFlagT
        ('mandatoryFlag', c_uint8),
        # 所有者类型 @see eOesOwnerTypeT
        ('ownerType', c_uint8),
        # 按64位对齐的填充域
        ('_TRD_CNFM_EXT_filler', c_uint8 * 5),
        # 预留的备用字段
        ('_TRD_CNFM_EXT_reserve', c_char * 16),
    ]


# 新股配号、中签记录信息定义
class OesLotWinningBaseInfoT(PrintableStructure):
    _fields_ = [
        # 证券账户
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 配号代码/中签代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 记录类型 @see eOesLotTypeT
        ('lotType', c_uint8),
        # 失败原因, 当且仅当 lotType 为 OES_LOT_TYPE_FAILED 时此字段有效
        # @see eOesLotRejReasonT
        ('rejReason', c_uint8),
        # 按64位对齐的填充域
        ('_LOT_WINNING_BASE_INFO_filler', c_int8),
        # 配号日期/中签日期 (格式为 YYYYMMDD, 形如 20160830)
        ('lotDate', c_int32),
        # 证券名称 (UTF-8 编码)
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 起始配号号码 (当为中签记录时此字段固定为0)
        ('assignNum', c_int64),
        # 配号成功数量/中签股数
        ('lotQty', c_int32),
        # 最终发行价, 单位精确到元后四位, 即1元 = 10000。当为配号记录时此字段值固定为0
        ('lotPrice', c_int32),
        # 中签金额, 单位精确到元后四位, 即1元 = 10000。当为配号记录时此字段值固定为0
        ('lotAmt', c_int64),
    ]


# 出入金委托的基础信息结构体定义
class OesFundTrsfBaseInfoT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 划转方向 @see eOesFundTrsfDirectT
        ('direct', c_uint8),
        # 出入金转账类型 @see eOesFundTrsfTypeT
        ('fundTrsfType', c_uint8),
        # 按64位对齐的填充域
        ('_FUND_TRSF_BASE_filler', c_uint8 * 2),
        # 资金账户代码 (可以为空, 为空则自动填充)
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 交易密码 (沪深OES之间内部资金划拨时无需填写该字段, 其它场景该字段必填)
        ('trdPasswd', c_char * OES_PWD_MAX_LEN),
        # 转账密码
        # - 转账方向为转入(银行转证券)时, 此密码为银行密码
        # - 转账方向为转出(证券转银行)时, 此密码为主柜资金密码
        # - OES和主柜之间划拨资金时, 此密码为主柜资金密码
        # - 沪深OES之间内部资金划拨时, 无需填写该字段
        ('trsfPasswd', c_char * OES_PWD_MAX_LEN),
        # 发生金额 (单位精确到元后四位, 即1元=10000)
        # @note 注意事项:
        # - 无论入金还是出金, 发生金额的取值都应为正数
        # - 精度将被自动向下舍入到分, 例如: 金额 1.9999 将被自动转换为 1.9900
        ('occurAmt', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
    ]


# 出入金请求定义
class OesFundTrsfReqT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 划转方向 @see eOesFundTrsfDirectT
        ('direct', c_uint8),
        # 出入金转账类型 @see eOesFundTrsfTypeT
        ('fundTrsfType', c_uint8),
        # 按64位对齐的填充域
        ('_FUND_TRSF_BASE_filler', c_uint8 * 2),
        # 资金账户代码 (可以为空, 为空则自动填充)
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 交易密码 (沪深OES之间内部资金划拨时无需填写该字段, 其它场景该字段必填)
        ('trdPasswd', c_char * OES_PWD_MAX_LEN),
        # 转账密码
        # - 转账方向为转入(银行转证券)时, 此密码为银行密码
        # - 转账方向为转出(证券转银行)时, 此密码为主柜资金密码
        # - OES和主柜之间划拨资金时, 此密码为主柜资金密码
        # - 沪深OES之间内部资金划拨时, 无需填写该字段
        ('trsfPasswd', c_char * OES_PWD_MAX_LEN),
        # 发生金额 (单位精确到元后四位, 即1元=10000)
        # @note 注意事项:
        # - 无论入金还是出金, 发生金额的取值都应为正数
        # - 精度将被自动向下舍入到分, 例如: 金额 1.9999 将被自动转换为 1.9900
        ('occurAmt', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
    ]


# 出入金拒绝的回报结构定义 (因风控检查未通过而被OES拒绝)
class OesFundTrsfRejectT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 划转方向 @see eOesFundTrsfDirectT
        ('direct', c_uint8),
        # 出入金转账类型 @see eOesFundTrsfTypeT
        ('fundTrsfType', c_uint8),
        # 按64位对齐的填充域
        ('_FUND_TRSF_BASE_filler', c_uint8 * 2),
        # 资金账户代码 (可以为空, 为空则自动填充)
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 交易密码 (沪深OES之间内部资金划拨时无需填写该字段, 其它场景该字段必填)
        ('trdPasswd', c_char * OES_PWD_MAX_LEN),
        # 转账密码
        # - 转账方向为转入(银行转证券)时, 此密码为银行密码
        # - 转账方向为转出(证券转银行)时, 此密码为主柜资金密码
        # - OES和主柜之间划拨资金时, 此密码为主柜资金密码
        # - 沪深OES之间内部资金划拨时, 无需填写该字段
        ('trsfPasswd', c_char * OES_PWD_MAX_LEN),
        # 发生金额 (单位精确到元后四位, 即1元=10000)
        # @note 注意事项:
        # - 无论入金还是出金, 发生金额的取值都应为正数
        # - 精度将被自动向下舍入到分, 例如: 金额 1.9999 将被自动转换为 1.9900
        ('occurAmt', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('ordDate', c_int32),
        # 委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('ordTime', c_int32),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 64位对齐的填充域
        ('_filler', c_int8),
        # 错误码
        ('rejReason', c_int32),
        # 错误信息
        ('errorInfo', c_char * OES_MAX_ERROR_INFO_LEN),
    ]


# 出入金委托执行状态回报的结构体定义
class OesFundTrsfReportT(PrintableStructure):
    _fields_ = [
        # 客户委托流水号 (由客户端维护的递增流水)
        ('clSeqNo', c_int32),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 划转方向 @see eOesFundTrsfDirectT
        ('direct', c_uint8),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 发生金额 (单位精确到元后四位, 即1元=10000)
        # @note 注意事项:
        # - 无论入金还是出金, 发生金额的取值都应为正数
        # - 精度将被自动向下舍入到分, 例如: 金额 1.9999 将被自动转换为 1.9900
        ('occurAmt', c_int64),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # OES出入金委托编号 (在OES内具有唯一性的内部出入金委托编号)
        ('fundTrsfId', c_int32),
        # 柜台出入金委托编号
        ('counterEntrustNo', c_int32),
        # 出入金委托日期 (格式为 YYYYMMDD, 形如 20160830)
        ('operDate', c_int32),
        # 出入金委托时间 (格式为 HHMMSSsss, 形如 141205000)
        ('operTime', c_int32),
        # 上报柜台时间 (格式为 HHMMSSsss, 形如 141205000)
        ('dclrTime', c_int32),
        # 柜台执行结果采集时间 (格式为 HHMMSSsss, 形如 141205000)
        ('doneTime', c_int32),
        # 出入金转账类型 @see eOesFundTrsfTypeT
        ('fundTrsfType', c_uint8),
        # /** 出入金委托执行状态 @see eOesFundTrsfStatusT
        ('trsfStatus', c_uint8),
        # 是否有转账到主柜
        ('_hasCounterTransfered', c_uint8),
        # 指令来源 @see eOesFundTrsfSourceTypeT
        ('fundTrsfSourceType', c_uint8),
        # 错误原因
        ('rejReason', c_int32),
        # 主柜错误码
        ('counterErrCode', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_uint32),
        # 资金调拨流水号
        ('allotSerialNo', c_char * OES_MAX_ALLOT_SERIALNO_LEN),
        # 错误信息
        ('errorInfo', c_char * OES_MAX_ERROR_INFO_LEN),
    ]


# 客户基础信息的结构体定义
class OesCustBaseInfoT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 客户类型 @see eOesCustTypeT
        ('custType', c_uint8),
        # 客户状态 (0:正常, 非0:不正常)
        ('status', c_uint8),
        # OES风险等级 @see eOesSecurityRiskLevelT
        ('riskLevel', c_uint8),
        # 客户原始风险等级
        ('originRiskLevel', c_uint8),
        # 机构标志 (0:个人投资者, 1:机构投资者)
        ('institutionFlag', c_uint8),
        # 投资者分类 @see eOesInvestorClassT
        ('investorClass', c_uint8),
        # 期权账户结算单确认标志 (0:未确认, 1:已确认)
        ('optSettlementCnfmFlag', c_uint8),
        # 按64位对齐的填充域
        ('_CUST_BASE_filler1', c_uint8),
        # 营业部代码
        ('branchId', c_int32),
        # 按64位对齐的填充域
        ('_CUST_BASE_filler2', c_uint32),
    ]


# 证券账户基础信息的结构体定义
class OesInvAcctBaseInfoT(PrintableStructure):
    _fields_ = [
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 账户类型 @see eOesAcctTypeT
        ('acctType', c_uint8),
        # 账户状态, 同步于主柜或者通过MON手动设置 @see eOesAcctStatusT
        ('status', c_uint8),
        # 股东账户的所有者类型 @see eOesOwnerTypeT
        ('ownerType', c_uint8),
        # 投资者期权等级 @see eOesOptInvLevelT
        ('optInvLevel', c_uint8),
        # 是否禁止交易 (仅供API查询使用)
        ('isTradeDisabled', c_uint8),
        # 按64位对齐的填充域
        ('_INV_ACCT_BASE_filler', c_uint8 * 2),
        # 证券账户权限限制 @see OES_LIMIT_xxx
        ('limits', c_uint64),
        # 股东权限/客户权限 @see eOesTradingPermissionT
        ('permissions', c_uint64),
        # 席位号
        ('pbuId', c_int32),
        # 个股持仓比例阀值 @deprecated 已废弃, 为了兼容旧版本而保留
        ('stkPositionLimitRatio', c_int32),
        # 主板权益 (新股认购限额)
        ('subscriptionQuota', c_int32),
        # 科创板权益 (新股认购限额)
        ('kcSubscriptionQuota', c_int32),
        # 预留的备用字段
        ('_INV_ACCT_BASE_reserve', c_char * 32),
    ]


# 竞价交易的限价参数(涨停价/跌停价)定义
class OesPriceLimitT(PrintableStructure):
    _fields_ = [
        # 涨停价 (单位精确到元后四位, 即1元 = 10000)
        ('upperLimitPrice', c_int32),
        # 跌停价 (单位精确到元后四位, 即1元 = 10000)
        ('lowerLimitPrice', c_int32),
    ]


OesCustItemT = OesCustBaseInfoT
OesLotWinningItemT = OesLotWinningBaseInfoT
OesOrdItemT = OesOrdCnfmT
OesTrdItemT = OesTrdCnfmT
OesFundTransferSerialItemT = OesFundTrsfReportT


class _OesStockBaseInfoT_CreditExt(PrintableStructure):
    _fields_ = [
        # 可充抵保证金折算率 (单位:万分比)
        ('collateralRatio', c_int32),
        # 融资买入保证金比例 (单位:万分比)
        ('marginBuyRatio', c_int32),
        # 融券卖出保证金比例 (单位:万分比)
        ('shortSellRatio', c_int32),
        # 公允价格, 大于0代表启用 (价格单位精确到元后四位, 即: 1元=10000)
        ('fairPrice', c_int32),
    ]


# 现货产品基础信息的结构体定义
class OesStockBaseInfoT(PrintableStructure):
    _fields_ = [
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 证券级别 @see eOesSecurityLevelT
        ('securityLevel', c_uint8),
        # 证券风险等级 @see eOesSecurityRiskLevelT
        ('securityRiskLevel', c_uint8),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 投资者适当性管理分类 @see eOesQualificationClassT
        ('qualificationClass', c_uint8),
        # 证券状态 @see eOesSecurityStatusT
        ('securityStatus', c_uint32),
        # 证券属性 @see eOesSecurityAttributeT
        ('securityAttribute', c_uint32),
        # 禁止交易标识 (0:正常交易, 非0:禁止交易) @see eOesSecuritySuspFlagT
        ('suspFlag', c_uint8),
        # 临时停牌标识 (0:未停牌, 1:已停牌)
        ('temporarySuspFlag', c_uint8),
        # 是否支持当日回转交易 (0:不支持, 1:支持)
        ('isDayTrading', c_uint8),
        # 是否注册制 (0:核准制, 1:注册制)
        ('isRegistration', c_uint8),
        # 是否为融资融券可充抵保证金证券 (0:不可充抵保证金, 1:可充抵保证金)
        ('isCrdCollateral', c_uint8),
        # 是否为融资标的 (0:不是融资标的, 1:是融资标的)
        ('isCrdMarginTradeUnderlying', c_uint8),
        # 是否为融券标的 (0:不是融券标的, 1:是融券标的)
        ('isCrdShortSellUnderlying', c_uint8),
        # 是否尚未盈利 (0:已盈利, 1:未盈利 (仅适用于科创板和创业板产品))
        ('isNoProfit', c_uint8),
        # 是否存在投票权差异 (0:无差异, 1:存在差异 (仅适用于科创板和创业板产品))
        ('isWeightedVotingRights', c_uint8),
        # 是否具有协议控制框架 (0:没有, 1:有 (仅适用于创业板产品))
        ('isVie', c_uint8),
        # 是否为高流通性证券 (目前仅适用于融资融券业务, 融券卖出所得可买高流通性证券)
        ('isHighLiquidity', c_uint8),
        # 融资融券可充抵保证金证券的交易状态 (0:不可交易, 1:可交易)
        ('isCrdCollateralTradable', c_uint8),
        # 计价方式 (仅适用于债券 @see eOesPricingMethodT)
        ('pricingMethod', c_uint8),
        # 按64位对齐的填充域
        ('_STOCK_BASE_filler', c_uint8 * 3),
        # 限价参数表 (涨/跌停价格, 数组下标为当前时段标志 @see eOesTrdSessTypeT)
        ('priceLimit', OesPriceLimitT * 3),
        # 最小报价单位 (单位精确到元后四位, 即1元 = 10000)
        ('priceTick', c_int32),
        # 前收盘价, 单位精确到元后四位, 即1元 = 10000
        ('prevClose', c_int32),
        # 单笔限价买委托数量上限
        ('lmtBuyMaxQty', c_int32),
        # 单笔限价买委托数量下限
        ('lmtBuyMinQty', c_int32),
        # 单笔限价买入单位
        ('lmtBuyQtyUnit', c_int32),
        # 单笔市价买委托数量上限
        ('mktBuyMaxQty', c_int32),
        # 单笔市价买委托数量下限
        ('mktBuyMinQty', c_int32),
        # 单笔市价买入单位
        ('mktBuyQtyUnit', c_int32),
        # 单笔限价卖委托数量上限
        ('lmtSellMaxQty', c_int32),
        # 单笔限价卖委托数量下限
        ('lmtSellMinQty', c_int32),
        # 单笔限价卖出单位
        ('lmtSellQtyUnit', c_int32),
        # 单笔市价卖委托数量上限
        ('mktSellMaxQty', c_int32),
        # 单笔市价卖委托数量下限
        ('mktSellMinQty', c_int32),
        # 单笔市价卖出单位
        ('mktSellQtyUnit', c_int32),
        # 债券的每张应计利息, 单位精确到元后八位, 即应计利息1元 = 100000000
        ('bondInterest', c_int64),
        # 面值, 单位精确到元后四位, 即1元 = 10000
        ('parValue', c_int64),
        # 逆回购期限
        ('repoExpirationDays', c_int32),
        # 占款天数
        ('cashHoldDays', c_int32),
        # 连续交易时段的有效竞价范围限制类型 @see eOesAuctionLimitTypeT
        ('auctionLimitType', c_uint8),
        # 连续交易时段的有效竞价范围基准价类型 @see eOesAuctionReferPriceTypeT
        ('auctionReferPriceType', c_uint8),
        # 按64位对齐的填充域
        ('_STOCK_BASE_filler1', c_uint8 * 2),
        # 连续交易时段的有效竞价范围涨跌幅度 (百分比或绝对价格, 取决于'有效竞价范围限制类型')
        ('auctionUpDownRange', c_int32),
        # 上市日期
        ('listDate', c_int32),
        # 到期日期 (仅适用于债券等有发行期限的产品)
        ('maturityDate', c_int32),
        # 总股本 (即: 总发行数量, 上证无该字段, 未额外维护时取值为0)
        ('outstandingShare', c_int64),
        # 流通股数量
        ('publicFloatShare', c_int64),
        # 基础证券代码 (标的产品代码)
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # ETF基金申赎代码
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 证券名称 (UTF-8 编码)
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 预留的备用字段
        ('_STOCK_BASE_reserve1', c_char * 80),
        # 融资融券业务专用字段
        ('creditExt', _OesStockBaseInfoT_CreditExt),
        # 预留的备用字段
        ('_STOCK_BASE_reserve2', c_char * 48),
    ]


# 证券发行基础信息的结构体定义
class OesIssueBaseInfoT(PrintableStructure):
    _fields_ = [
        # 证券发行代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 发行方式 @see eOesSecurityIssueTypeT
        ('issueType', c_uint8),
        # 是否允许撤单
        ('isCancelAble', c_uint8),
        # 是否允许重复认购
        ('isReApplyAble', c_uint8),
        # 禁止交易标识 (0:正常交易, 非0:禁止交易) @see eOesSecuritySuspFlagT
        ('suspFlag', c_uint8),
        # 证券属性 @see eOesSecurityAttributeT
        ('securityAttribute', c_uint32),
        # 是否注册制 (0 核准制, 1 注册制)
        ('isRegistration', c_uint8),
        # 是否尚未盈利 (0 已盈利, 1 未盈利 (仅适用于创业板产品))
        ('isNoProfit', c_uint8),
        # 是否存在投票权差异 (0 无差异, 1 存在差异 (仅适用于创业板产品))
        ('isWeightedVotingRights', c_uint8),
        # 是否具有协议控制框架 (0 没有, 1 有 (仅适用于创业板产品))
        ('isVie', c_uint8),
        # 按64位对齐的填充域
        ('_ISSUE_BASE_filler', c_uint8 * 8),
        # 发行起始日
        ('startDate', c_int32),
        # 发行结束日
        ('endDate', c_int32),
        # 发行价格
        ('issuePrice', c_int32),
        # 申购价格上限 (单位精确到元后四位, 即1元 = 10000)
        ('upperLimitPrice', c_int32),
        # 申购价格下限 (单位精确到元后四位, 即1元 = 10000)
        ('lowerLimitPrice', c_int32),
        # 委托最大份数
        ('ordMaxQty', c_int32),
        # 委托最小份数
        ('ordMinQty', c_int32),
        # 委托份数单位
        ('qtyUnit', c_int32),
        # 总发行量
        ('issueQty', c_int64),
        # 配股股权登记日(仅上海市场有效)
        ('alotRecordDay', c_int32),
        # 配股股权除权日(仅上海市场有效)
        ('alotExRightsDay', c_int32),
        # 基础证券代码 (正股代码)
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 证券名称 (UTF-8 编码)
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 预留的备用字段
        ('_ISSUE_BASE_reserve1', c_char * 56),
        # 预留的备用字段
        ('_ISSUE_BASE_reserve2', c_char * 64),
    ]


# ETF申赎产品基础信息的结构体定义
class OesEtfBaseInfoT(PrintableStructure):
    _fields_ = [
        # ETF基金申赎代码
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # ETF基金买卖代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # ETF基金市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 是否需要发布IOPV  1: 是; 0: 否
        ('isPublishIOPV', c_uint8),
        # 交易所/基金公司的允许申购标志  1: 是; 0: 否
        ('isCreationAble', c_uint8),
        # 交易所/基金公司的允许赎回标志  1: 是; 0: 否
        ('isRedemptionAble', c_uint8),
        # 券商管理端的禁止交易标志  1: 是; 0: 否
        ('isDisabled', c_uint8),
        # 按64位对齐的填充域
        ('_ETF_BASE_filler', c_uint8),
        # 成份证券数目
        ('componentCnt', c_int32),
        # 每个篮子 (最小申购、赎回单位) 对应的ETF份数, 即申购赎回单位
        ('creRdmUnit', c_int32),
        # 最大现金替代比例, 单位精确到十万分之一, 即替代比例50% = 50000
        ('maxCashRatio', c_int32),
        # 前一日基金的单位净值, 单位精确到元后四位, 即1元 = 10000
        ('nav', c_int32),
        # 前一日最小申赎单位净值, 单位精确到元后四位, 即1元 = 10000
        ('navPerCU', c_int64),
        # 红利金额, 单位精确到元后四位, 即1元 = 10000
        ('dividendPerCU', c_int64),
        # 当前交易日, 格式YYYYMMDD
        ('tradingDay', c_int32),
        # 前一交易日, 格式YYYYMMDD
        ('preTradingDay', c_int32),
        # 每个篮子的预估现金差额, 单位精确到元后四位, 即1元 = 10000
        ('estiCashCmpoent', c_int64),
        # 前一日现金差额, 单位精确到元后四位, 即1元 = 10000
        ('cashCmpoent', c_int64),
        # 单个账户当日累计申购总额限制
        ('creationLimit', c_int64),
        # 单个账户当日累计赎回总额限制
        ('redemLimit', c_int64),
        # 单个账户当日净申购总额限制
        ('netCreationLimit', c_int64),
        # 单个账户当日净赎回总额限制
        ('netRedemLimit', c_int64),
    ]


# ETF成份证券基础信息的结构体定义
class OesEtfComponentBaseInfoT(PrintableStructure):
    _fields_ = [
        # ETF基金申赎代码
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成份证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成份证券市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # ETF基金市场代码 @see eOesMarketIdT
        ('fundMktId', c_uint8),
        # 现金替代标识 @see eOesEtfSubFlagT
        ('subFlag', c_uint8),
        # 成份证券的证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 成份证券的证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 是否是作为申赎对价的成份证券
        # @note 注意事项:
        # - 非申赎对价的成份证券信息仅供参考, 申赎时不能对该类成份证券进行股份计算
        # 或现金替代处理。
        # - 例如: 深交所跨市场ETF中的沪市成份证券信息就属于非申赎对价的成份证券信息,
        # 对深交所跨市场ETF进行申赎时应使用 159900 虚拟成份券进行沪市成份证券份额
        # 的现金替代处理
        ('isTrdComponent', c_uint8),
        # 按64位对齐的填充域
        ('_ETF_COMPONENT_BASE_filler', c_uint8 * 2),
        # 前收盘价格, 单位精确到元后四位, 即1元 = 10000
        ('prevClose', c_int32),
        # 成份证券数量
        ('qty', c_int32),
        # 申购溢价比例, 单位精确到十万分之一, 即溢价比例10% = 10000
        ('premiumRatio', c_int32),
        # 赎回折价比例, 单位精确到十万分之一, 即折价比例10% = 10000
        ('discountRatio', c_int32),
        # 申购替代金额, 单位精确到元后四位, 即1元 = 10000
        ('creationSubCash', c_int64),
        # 赎回替代金额, 单位精确到元后四位, 即1元 = 10000
        ('redemptionSubCash', c_int64),
    ]


# 客户资金基础信息结构体定义
class OesCashAssetBaseInfoT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 资金帐户类别(冗余自资金账户) @see eOesAcctTypeT
        ('cashType', c_uint8),
        # 资金帐户状态(冗余自资金账户) @see eOesAcctStatusT
        ('cashAcctStatus', c_uint8),
        # 是否禁止出入金 (仅供API查询使用)
        ('isFundTrsfDisabled', c_uint8),
        # 按64位对齐的填充域
        ('_CASH_ASSET_BASE_filler', c_uint8 * 4),
        # 期初余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningBal', c_int64),
        # 期初可用余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningAvailableBal', c_int64),
        # 期初可取余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningDrawableBal', c_int64),
        # 不可用资金余额(既不可交易又不可提取), 单位精确到元后四位, 即1元 = 10000
        ('disableBal', c_int64),
        # 当前冲正金额(红冲蓝补的资金净额), 取值可以为负数(表示资金调出), 单位精确到元后四位, 即1元 = 10000
        ('reversalAmt', c_int64),
        # 手动冻结资金, 单位精确到元后四位, 即1元 = 10000
        ('manualFrzAmt', c_int64),
        # 日中累计存入资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalDepositAmt', c_int64),
        # 日中累计提取资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalWithdrawAmt', c_int64),
        # 当前提取冻结资金金额, 单位精确到元后四位, 即1元 = 10000
        ('withdrawFrzAmt', c_int64),
        # 日中累计 卖/赎回 获得的可用资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalSellAmt', c_int64),
        # 日中累计 买/申购/逆回购 使用资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalBuyAmt', c_int64),
        # 当前交易冻结金额, 单位精确到元后四位, 即1元 = 10000
        ('buyFrzAmt', c_int64),
        # 日中累计交易费用金额, 单位精确到元后四位, 即1元 = 10000
        ('totalFeeAmt', c_int64),
        # 当前冻结交易费用金额, 单位精确到元后四位, 即1元 = 10000
        ('feeFrzAmt', c_int64),
        # 维持保证金金额, 单位精确到元后四位, 即1元 = 10000
        # 对于普通资金账户, 此字段为ETF申赎时的预估现金差额
        # 对于信用资金账户, 此字段固定为0
        # 对于衍生品资金账户, 此字段为当前维持的开仓保证金
        ('marginAmt', c_int64),
        # 在途冻结保证金金额, 单位精确到元后四位, 即1元 = 10000
        # 对于普通资金账户, 此字段为ETF申赎在途时冻结的预估现金差额
        # 对于信用资金账户, 此字段固定为0
        # 对于衍生品资金账户, 此字段为尚未成交的开仓保证金
        ('marginFrzAmt', c_int64),
    ]


class _OesCashAssetReportT_OptionExt(PrintableStructure):
    _fields_ = [
        # 日初实际占用保证金, 单位精确到元后四位, 即1元 = 10000
        ('initialMargin', c_int64),
        # 行权累计待交收冻结资金, 单位精确到元后四位, 即1元 = 10000
        ('totalExerciseFrzAmt', c_int64),
        # 待追加保证金, 单位精确到元后四位, 即1元 = 10000
        ('pendingSupplMargin', c_int64),
        # 上海市场可用限购/套保额度
        ('sseAvailablePurchaseLimit', c_int64),
        # 深圳市场可用限购/套保额度
        ('szseAvailablePurchaseLimit', c_int64),
        # 未对冲实时价格保证金, 单位精确到元后四位, 即1元 = 10000
        ('totalMarketMargin', c_int64),
        # 已对冲实时价格保证金, 单位精确到元后四位, 即1元 = 10000
        ('totalNetMargin', c_int64),
    ]


class _OesCashAssetReportT_Union(PrintableUnion):
    _fields_ = [
        # 融资融券业务专用字段 (即: 客户信用资产信息; @note 非两融业务不要使用这些字段)
        ('creditExt', OesCrdCreditAssetBaseInfoT),
        # 期权业务专用字段 (@note 非期权业务不要使用这些字段)
        ('optionExt', _OesCashAssetReportT_OptionExt),
        # 预留的备用字段 (@note 不要直接使用该字段)
        ('_CASH_ASSET_EXT_reserve', c_char * 512),
    ]


# 客户资金回报结构体定义
#
# @note 可用余额等信息参考如下字段:
# - 总现金资产请参考 '当前余额 (currentTotalBal)' 字段
# - 可用余额请参考 '当前可用余额 (currentAvailableBal)' 字段
# - 可取余额请参考 '当前可取余额 (currentDrawableBal)' 字段
# - 信用系统现金还款/买融资标的可用余额请参考 '当前可用余额 (currentAvailableBal)' 字段
# - 信用系统买担保品可用余额请参考 '买担保品可用余额 (creditExt.buyCollateralAvailableBal)' 字段
# - 信用系统买券还券可用余额请参考 '买券还券可用余额 (creditExt.repayStockAvailableBal)' 字段
class OesCashAssetReportT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 资金帐户类别(冗余自资金账户) @see eOesAcctTypeT
        ('cashType', c_uint8),
        # 资金帐户状态(冗余自资金账户) @see eOesAcctStatusT
        ('cashAcctStatus', c_uint8),
        # 是否禁止出入金 (仅供API查询使用)
        ('isFundTrsfDisabled', c_uint8),
        # 按64位对齐的填充域
        ('_CASH_ASSET_BASE_filler', c_uint8 * 4),
        # 期初余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningBal', c_int64),
        # 期初可用余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningAvailableBal', c_int64),
        # 期初可取余额, 单位精确到元后四位, 即1元 = 10000
        ('beginningDrawableBal', c_int64),
        # 不可用资金余额(既不可交易又不可提取), 单位精确到元后四位, 即1元 = 10000
        ('disableBal', c_int64),
        # 当前冲正金额(红冲蓝补的资金净额), 取值可以为负数(表示资金调出), 单位精确到元后四位, 即1元 = 10000
        ('reversalAmt', c_int64),
        # 手动冻结资金, 单位精确到元后四位, 即1元 = 10000
        ('manualFrzAmt', c_int64),
        # 日中累计存入资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalDepositAmt', c_int64),
        # 日中累计提取资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalWithdrawAmt', c_int64),
        # 当前提取冻结资金金额, 单位精确到元后四位, 即1元 = 10000
        ('withdrawFrzAmt', c_int64),
        # 日中累计 卖/赎回 获得的可用资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalSellAmt', c_int64),
        # 日中累计 买/申购/逆回购 使用资金金额, 单位精确到元后四位, 即1元 = 10000
        ('totalBuyAmt', c_int64),
        # 当前交易冻结金额, 单位精确到元后四位, 即1元 = 10000
        ('buyFrzAmt', c_int64),
        # 日中累计交易费用金额, 单位精确到元后四位, 即1元 = 10000
        ('totalFeeAmt', c_int64),
        # 当前冻结交易费用金额, 单位精确到元后四位, 即1元 = 10000
        ('feeFrzAmt', c_int64),
        # 维持保证金金额, 单位精确到元后四位, 即1元 = 10000
        # 对于普通资金账户, 此字段为ETF申赎时的预估现金差额
        # 对于信用资金账户, 此字段固定为0
        # 对于衍生品资金账户, 此字段为当前维持的开仓保证金
        ('marginAmt', c_int64),
        # 在途冻结保证金金额, 单位精确到元后四位, 即1元 = 10000
        # 对于普通资金账户, 此字段为ETF申赎在途时冻结的预估现金差额
        # 对于信用资金账户, 此字段固定为0
        # 对于衍生品资金账户, 此字段为尚未成交的开仓保证金
        ('marginFrzAmt', c_int64),
        # 当前余额 (总现金资产), 包括当前可用余额和在途冻结资金在內的汇总值, 单位精确到元后四位, 即1元 = 10000
        # - @note 可用余额请参考 '当前可用余额 (currentAvailableBal)' 字段
        ('currentTotalBal', c_int64),
        # 当前可用余额, 单位精确到元后四位, 即1元 = 10000
        # - 对于信用资金账户, 该字段表示现金还款/买融资标的可用余额
        ('currentAvailableBal', c_int64),
        # 当前可取余额, 单位精确到元后四位, 即1元 = 10000
        ('currentDrawableBal', c_int64),
        # 日中沪深结点内部划拨的累计净发生资金 (正数代表累计净划入, 负数代表累计净划出), 单位精确到元后四位, 即1元 = 10000
        ('totalInternalAllotAmt', c_int64),
        # 日中沪深结点内部划拨的在途资金 (正数代表在途划入, 负数代表在途划出), 单位精确到元后四位, 即1元 = 10000
        ('internalAllotUncomeAmt', c_int64),
        # 预留的备用字段
        ('_CASH_ASSET_RPT_reserve', c_char * 16),
        # 仅适用于融资融券业务和期权业务的扩展字段
        # @note 现货业务的资金回报中不会携带以下扩展字段, 不要读写和操作这些扩展字段
        ('union', _OesCashAssetReportT_Union),
    ]


# 股票持仓基础信息的结构体定义
class OesStkHoldingBaseInfoT(PrintableStructure):
    _fields_ = [
        # 账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 信用持仓标识 (0:不是信用持仓, 1:是信用持仓)
        ('isCreditHolding', c_uint8),
        # 按64位对齐的填充域
        ('_HOLD_BASE_filler', c_uint8 * 3),
        # 日初持仓
        ('originalHld', c_int64),
        # 日初总持仓成本 (日初持仓成本价=日初总持仓成本/日初持仓)
        ('originalCostAmt', c_int64),
        # 日中累计买入持仓
        ('totalBuyHld', c_int64),
        # 日中累计卖出持仓
        ('totalSellHld', c_int64),
        # 当前卖出冻结持仓
        ('sellFrzHld', c_int64),
        # 手动冻结持仓
        ('manualFrzHld', c_int64),
        # 日中累计买入金额
        ('totalBuyAmt', c_int64),
        # 日中累计卖出金额
        ('totalSellAmt', c_int64),
        # 日中累计买入费用
        ('totalBuyFee', c_int64),
        # 日中累计卖出费用
        ('totalSellFee', c_int64),
        # 日中累计转入持仓
        # - 对于现货持仓:
        # - 表示赎回ETF获得的成份证券持仓数量, 或申购ETF获得的ETF基金持仓数量
        # - 对于信用持仓:
        # - 表示担保品划入的在途持仓数量
        ('totalTrsfInHld', c_int64),
        # 日中累计转出持仓
        # - 对于现货持仓:
        # - 表示申购ETF已使用的成份证券持仓数量, 或赎回ETF已使用的ETF基金持仓数量
        # - 对于信用持仓:
        # - 固定为0
        ('totalTrsfOutHld', c_int64),
        # 当前转出冻结持仓
        # - 对于现货持仓:
        # - 包括申购ETF在途冻结的成份证券持仓数量, 或赎回ETF在途冻结的ETF基金持仓数量
        # - 包括融资融券业务提交担保品在途冻结的持仓数量
        # - 对于信用持仓:
        # - 表示融资融券业务返还担保品在途冻结的持仓数量
        ('trsfOutFrzHld', c_int64),
        # 日初锁定持仓 (日初备兑占用的持仓数量, OES内部处理时需注意对初始值进行处理)
        ('originalLockHld', c_int64),
        # 日中累计锁定持仓
        ('totalLockHld', c_int64),
        # 日中累计解锁持仓
        ('totalUnlockHld', c_int64),
        # 日初可用持仓
        ('originalAvlHld', c_int64),
        # 当日最大可减持额度
        # - 小于0, 不进行减持额度控制
        # - 大于或等于0, 最大可减持额度
        ('maxReduceQuota', c_int64),
    ]


class _OesStkHoldingReportT_Union(PrintableUnion):
    _fields_ = [
        # 融资融券业务专用字段 (即: 客户单证券融资融券负债统计信息; @note 非两融业务不要使用这些字段)
        ('creditExt', OesCrdSecurityDebtStatsBaseInfoT),
        # 预留的备用字段
        ('_STK_HOLDING_EXT_reserve', c_char * 432),
    ]


# 股票持仓回报结构体定义
#
# @note 可卖持仓等信息参考如下字段:
# - 总持仓请参考 '总持仓数量 (sumHld)' 字段
# - 可卖持仓请参考 '当前可卖持仓数量 (sellAvlHld)' 字段
# - ETF申赎可使用的成份证券数量（申购）和ETF基金数量（赎回）请参考 '当前可转换和信用系统可划出持仓数量 (trsfOutAvlHld)' 字段
# - 现货系统可锁定（期权业务）持仓数量和现货系统可划出（两融业务）持仓数量请参考 '当前可锁定和现货系统可划出持仓数量 (lockAvlHld)' 字段
# - 信用系统直接还券可用持仓请参考 '直接还券可用持仓数量 (creditExt.repayStockDirectAvlHld)' 字段
# - 信用系统可划出持仓请参考 '当前可转换和信用系统可划出持仓数量 (trsfOutAvlHld)' 字段
class OesStkHoldingReportT(PrintableStructure):
    _fields_ = [
        # 账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 信用持仓标识 (0:不是信用持仓, 1:是信用持仓)
        ('isCreditHolding', c_uint8),
        # 按64位对齐的填充域
        ('_HOLD_BASE_filler', c_uint8 * 3),
        # 日初持仓
        ('originalHld', c_int64),
        # 日初总持仓成本 (日初持仓成本价=日初总持仓成本/日初持仓)
        ('originalCostAmt', c_int64),
        # 日中累计买入持仓
        ('totalBuyHld', c_int64),
        # 日中累计卖出持仓
        ('totalSellHld', c_int64),
        # 当前卖出冻结持仓
        ('sellFrzHld', c_int64),
        # 手动冻结持仓
        ('manualFrzHld', c_int64),
        # 日中累计买入金额
        ('totalBuyAmt', c_int64),
        # 日中累计卖出金额
        ('totalSellAmt', c_int64),
        # 日中累计买入费用
        ('totalBuyFee', c_int64),
        # 日中累计卖出费用
        ('totalSellFee', c_int64),
        # 日中累计转入持仓
        # - 对于现货持仓:
        # - 表示赎回ETF获得的成份证券持仓数量, 或申购ETF获得的ETF基金持仓数量
        # - 对于信用持仓:
        # - 表示担保品划入的在途持仓数量
        ('totalTrsfInHld', c_int64),
        # 日中累计转出持仓
        # - 对于现货持仓:
        # - 表示申购ETF已使用的成份证券持仓数量, 或赎回ETF已使用的ETF基金持仓数量
        # - 对于信用持仓:
        # - 固定为0
        ('totalTrsfOutHld', c_int64),
        # 当前转出冻结持仓
        # - 对于现货持仓:
        # - 包括申购ETF在途冻结的成份证券持仓数量, 或赎回ETF在途冻结的ETF基金持仓数量
        # - 包括融资融券业务提交担保品在途冻结的持仓数量
        # - 对于信用持仓:
        # - 表示融资融券业务返还担保品在途冻结的持仓数量
        ('trsfOutFrzHld', c_int64),
        # 日初锁定持仓 (日初备兑占用的持仓数量, OES内部处理时需注意对初始值进行处理)
        ('originalLockHld', c_int64),
        # 日中累计锁定持仓
        ('totalLockHld', c_int64),
        # 日中累计解锁持仓
        ('totalUnlockHld', c_int64),
        # 日初可用持仓
        ('originalAvlHld', c_int64),
        # 当日最大可减持额度
        # - 小于0, 不进行减持额度控制
        # - 大于或等于0, 最大可减持额度
        ('maxReduceQuota', c_int64),
        # 当前可卖持仓数量
        ('sellAvlHld', c_int64),
        # 当前可转换和信用系统可划出持仓数量
        # - 对于ETF申赎业务:
        # - 对于成份证券持仓, 表示申购时可以使用的成份证券数量 (现货系统)
        # - 对于ETF基金持仓, 表示赎回时可以使用的ETF基金数量 (现货系统)
        # - 对于融资融券业务:
        # - 表示信用系统可划出的担保品持仓数量 (信用系统)
        ('trsfOutAvlHld', c_int64),
        # 当前可锁定和现货系统可划出持仓数量
        # - 对于期权业务:
        # - 表示现货系统可锁定的标的证券持仓数量 (现货系统)
        # - 对于融资融券业务:
        # - 表示现货系统可划出的担保品持仓数量 (现货系统)
        # - 对于信用系统, 该字段固定为0
        ('lockAvlHld', c_int64),
        # 按64位对齐的填充域 (为兼容旧版本而保留)
        ('_STK_HOLDING_RPT_filler', c_int64),
        # 总持仓数量 (日初持仓数量+累计买入数量-累计卖出数量)
        # - 对于现货系统:
        # - 包含在途卖出冻结的持仓数量
        # - 包含在途ETF申购冻结的成份证券持仓数量
        # - 不包含在途买入数量
        # - 对于信用系统:
        # - 包含在途卖出冻结的持仓数量
        # - 包含担保品转出冻结的持仓数量
        # - 包含直接还券冻结的持仓数量
        # - 不包含在途买入数量
        # - 不包含在途担保品转入持仓数量
        # - @note 可卖持仓等相关字段:
        # - 可卖持仓请参考 '当前可卖持仓数量 (sellAvlHld)' 字段
        # - 信用系统直接还券可用持仓请参考 '直接还券可用持仓数量 (repayStockDirectAvlHld)' 字段
        # - 信用系统可划出持仓请参考 '当前可转换和信用系统可划出持仓数量 (trsfOutAvlHld)' 字段
        ('sumHld', c_int64),
        # 持仓成本价
        ('costPrice', c_int64),
        # 预留的备用字段
        ('_STK_HOLDING_RPT_reserve', c_char * 32),
        # 仅适用于融资融券业务的扩展字段
        # @note 现货业务的持仓回报中不会携带以下扩展字段, 不要读写和操作这些扩展字段
        ('union', _OesStkHoldingReportT_Union),
    ]


# 市场状态信息的结构体定义
class OesMarketStateInfoT(PrintableStructure):
    _fields_ = [
        ('exchId', c_uint8),  # 交易所代码 @see eOesExchangeIdT
        ('platformId', c_uint8),  # 交易平台类型 @see eOesPlatformIdT
        ('mktId', c_uint8),  # 市场代码 @see eOesMarketIdT
        ('mktState', c_uint8),  # 市场状态 @see eOesMarketStateT
        ('_filler', c_uint8 * 4),  # 按64位对齐的填充域
    ]


# 通知消息的结构体定义
class OesNotifyBaseInfoT(PrintableStructure):
    _fields_ = [
        # 通知消息序号
        ('notifySeqNo', c_int32),
        # 通知消息来源 @see eOesNotifySourceT
        ('notifySource', c_uint8),
        # 通知消息类型 @see eOesNotifyTypeT
        ('notifyType', c_uint8),
        # 通知消息等级 @see eOesNotifyLevelT
        ('notifyLevel', c_uint8),
        # 通知范围 @see eOesNotifyScopeT
        ('notifyScope', c_uint8),
        # 通知发出时间 (格式为 HHMMSSsss, 形如 141205000)
        ('tranTime', c_int32),
        # 业务类型 @see eOesBusinessTypeT
        ('businessType', c_uint8),
        # 按64位对齐的填充域
        ('_NOTIFY_INFO_filler1', c_uint8 * 3),
        # 客户代码 (仅当消息通知范围为指定客户时有效)
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码 (仅当通知消息与特定证券相关时有效)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 (仅用于修饰证券代码) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_NOTIFY_INFO_filler2', c_uint8 * 3),
        # 通知内容长度 (不包含'\0'结束符的有效字符长度)
        ('contentLen', c_int32),
        # 通知内容
        ('content', c_char * OES_NOTIFY_CONTENT_MAX_LEN),
    ]


# 通知消息回报结构体定义
class OesNotifyInfoReportT(PrintableStructure):
    _fields_ = [
        # 通知消息序号
        ('notifySeqNo', c_int32),
        # 通知消息来源 @see eOesNotifySourceT
        ('notifySource', c_uint8),
        # 通知消息类型 @see eOesNotifyTypeT
        ('notifyType', c_uint8),
        # 通知消息等级 @see eOesNotifyLevelT
        ('notifyLevel', c_uint8),
        # 通知范围 @see eOesNotifyScopeT
        ('notifyScope', c_uint8),
        # 通知发出时间 (格式为 HHMMSSsss, 形如 141205000)
        ('tranTime', c_int32),
        # 业务类型 @see eOesBusinessTypeT
        ('businessType', c_uint8),
        # 按64位对齐的填充域
        ('_NOTIFY_INFO_filler1', c_uint8 * 3),
        # 客户代码 (仅当消息通知范围为指定客户时有效)
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码 (仅当通知消息与特定证券相关时有效)
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 (仅用于修饰证券代码) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_NOTIFY_INFO_filler2', c_uint8 * 3),
        # 通知内容长度 (不包含'\0'结束符的有效字符长度)
        ('contentLen', c_int32),
        # 通知内容
        ('content', c_char * OES_NOTIFY_CONTENT_MAX_LEN),
    ]


# 查询请求的消息头定义
class OesQryReqHeadT(PrintableStructure):
    _fields_ = [
        # 查询窗口大小
        ('maxPageSize', c_int32),
        # 查询起始位置
        ('lastPosition', c_int32),
    ]


# 查询应答的消息头定义
class OesQryRspHeadT(PrintableStructure):
    _fields_ = [
        # 查询到的信息条目数
        ('itemCount', c_int32),
        # 查询到的最后一条信息的位置
        ('lastPosition', c_int32),
        # 是否是当前查询最后一个包
        ('isEnd', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询定位的游标结构
class OesQryCursorT(PrintableStructure):
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


# 查询当前交易日信息应答
class OesQryTradingDayRspT(PrintableStructure):
    _fields_ = [
        # 交易日
        ('tradingDay', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
    ]


# 客户端总览信息 - 股东账户信息总览
class OesInvAcctOverviewT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        ('isValid', c_uint8),  # 股东账户是否有效标识
        ('mktId', c_uint8),  # 市场 @see eOesMarketIdT
        ('acctType', c_uint8),  # 账户类型 @see eOesAcctTypeT
        ('status', c_uint8),  # 账户状态 @see eOesAcctStatusT
        ('ownerType', c_uint8),  # 股东账户的所有者类型 @see eOesOwnerTypeT
        ('optInvLevel', c_uint8),  # 期权投资者级别 @see eOesOptInvLevelT
        ('isTradeDisabled', c_uint8),  # 是否禁止交易 (仅供API查询使用)
        ('_filler1', c_uint8),  # 按64位对齐的填充域
        ('limits', c_uint64),  # 证券账户权限限制 @see OES_LIMIT_xxx
        ('permissions', c_uint64),  # 股东权限/客户权限 @see eOesTradingPermissionT
        ('pbuId', c_int32),  # 席位号
        ('subscriptionQuota', c_int32),  # 主板权益 (新股/配股认购限额)
        ('kcSubscriptionQuota', c_int32),  # 科创板权益 (新股/配股认购限额)
        ('_filler2', c_int32),  # 按64位对齐的填充域
        ('trdOrdCnt', c_int32),  # 当日累计有效交易类委托笔数统计
        ('nonTrdOrdCnt', c_int32),  # 当日累计有效非交易类委托笔数统计
        ('cancelOrdCnt', c_int32),  # 当日累计有效撤单笔数统计
        ('oesRejectOrdCnt', c_int32),  # 当日累计被OES拒绝的委托笔数统计
        ('exchRejectOrdCnt', c_int32),  # 当日累计被交易所拒绝的委托笔数统计
        ('trdCnt', c_int32),  # 当日累计成交笔数统计
        ('_reserve', c_char * 64),  # 备用字段
    ]


# 客户端总览信息 - 资金账户信息总览
class OesCashAcctOverviewT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 银行代码
        ('bankId', c_char * OES_BANK_NO_MAX_LEN),
        ('isValid', c_uint8),  # 资金账户是否有效标识
        ('cashType', c_uint8),  # 资金账户类别 @see eOesAcctTypeT
        ('cashAcctStatus', c_uint8),  # 资金账户状态 @see eOesAcctStatusT
        ('currType', c_uint8),  # 币种类型 @see eOesCurrTypeT
        ('isFundTrsfDisabled', c_uint8),  # 出入金是否禁止标识
        ('_filler', c_uint8 * 3),  # 按64位对齐的填充域
        ('_reserve', c_char * 64),  # 备用字段
    ]


# 客户端总览信息 - 客户信息总览
class OesCustOverviewT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 客户类型 @see eOesCustTypeT
        ('custType', c_uint8),
        # 客户状态 (0:正常, 非0:不正常)
        ('status', c_uint8),
        # OES风险等级 @see eOesSecurityRiskLevelT
        ('riskLevel', c_uint8),
        # 客户原始风险等级
        ('originRiskLevel', c_uint8),
        # 机构标志 (0:个人投资者, 1:机构投资者)
        ('institutionFlag', c_uint8),
        # 投资者分类 @see eOesInvestorClassT
        ('investorClass', c_uint8),
        # 期权账户结算单确认标志 (0:未确认, 1:已确认)
        ('optSettlementCnfmFlag', c_uint8),
        # 按64位对齐的填充域
        ('_CUST_BASE_filler1', c_uint8),
        # 营业部代码
        ('branchId', c_int32),
        # 按64位对齐的填充域
        ('_CUST_BASE_filler2', c_uint32),
        # 资金账户信息
        ('cashAcct', OesCashAcctOverviewT),
        # 上海股东账户信息
        ('sseInvAcct', OesInvAcctOverviewT),
        # 深圳股东账户信息
        ('szseInvAcct', OesInvAcctOverviewT),
        # 客户姓名
        ('custName', c_char * OES_CUST_NAME_MAX_LEN),
        # 备用字段
        ('_reserve', c_char * 128),
    ]


# 客户端总览信息内容
class OesClientOverviewT(PrintableStructure):
    _fields_ = [
        # 客户端名称
        ('clientName', c_char * OES_CLIENT_NAME_MAX_LEN),
        # 客户端说明
        ('clientMemo', c_char * OES_CLIENT_DESC_MAX_LEN),
        ('clientId', c_int16),  # 客户端编号
        ('clientType', c_uint8),  # 客户端类型  @see eOesClientTypeT
        ('clientStatus', c_uint8),  # 客户端状态  @see eOesClientStatusT
        ('isApiForbidden', c_uint8),  # API禁用标识
        ('isBlockTrader', c_uint8),  # 是否大宗交易标识 @deprecated 已废弃
        ('businessScope', c_uint8),  # 服务端支持的业务范围 @see eOesBusinessTypeT
        ('currentBusinessType', c_uint8),  # 当前会话对应的业务类型 @see eOesBusinessTypeT
        ('logonTime', c_int64),  # 客户端登录(委托接收服务)时间
        ('sseStkPbuId', c_int32),  # 上海现货/信用账户对应的PBU代码
        ('sseOptPbuId', c_int32),  # 上海衍生品账户对应的PBU代码
        ('sseQualificationClass', c_uint8),  # 上海股东账户的投资者适当性管理分类 @see eOesQualificationClassT
        ('_filler2', c_uint8 * 7),  # 按64位对齐的填充域
        ('szseStkPbuId', c_int32),  # 深圳现货/信用账户对应的PBU代码
        ('szseOptPbuId', c_int32),  # 深圳衍生品账户对应的PBU代码
        ('szseQualificationClass', c_uint8),  # 深圳股东账户的投资者适当性管理分类 @see eOesQualificationClassT
        ('_filler3', c_uint8 * 7),  # 按64位对齐的填充域
        ('currOrdConnected', c_int32),  # 当前已连接的委托通道数量
        ('currRptConnected', c_int32),  # 当前已连接的回报通道数量
        ('currQryConnected', c_int32),  # 当前已连接的查询通道数量
        ('maxOrdConnect', c_int32),  # 委托通道允许的最大同时连接数量
        ('maxRptConnect', c_int32),  # 回报通道允许的最大同时连接数量
        ('maxQryConnect', c_int32),  # 查询通道允许的最大同时连接数量
        ('ordTrafficLimit', c_int32),  # 委托通道的流量控制
        ('qryTrafficLimit', c_int32),  # 查询通道的流量控制
        ('maxOrdCount', c_int32),  # 最大委托笔数限制
        ('initialCashAssetRatio', c_uint8),  # 客户在本结点的初始资金资产占比(百分比)
        ('isSupportInternalAllot', c_uint8),  # 是否支持两地交易内部资金划拨
        ('isCheckStkConcentrate', c_uint8),  # 是否启用现货集中度控制
        ('_reserve', c_char * 125),  # 备用字段
        ('associatedCustCnt', c_int32),  # 客户端关联的客户数量
        # 客户端关联的客户列表
        ('custItems', OesCustOverviewT * OES_MAX_CUST_PER_CLIENT),
    ]


# 查询客户信息过滤条件
class OesQryCustFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询客户信息请求
class OesQryCustReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCustFilterT),
    ]


# 查询客户信息应答
class OesQryCustRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 客户信息数组
        ('qryItems', OesCustItemT * OES_MAX_CUST_ITEM_CNT_PER_PACK),
    ]


# 查询证券账户信息过滤条件
class OesQryInvAcctFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 证券账户内容
class OesInvAcctItemT(PrintableStructure):
    _fields_ = [
        # 股东账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 账户类型 @see eOesAcctTypeT
        ('acctType', c_uint8),
        # 账户状态, 同步于主柜或者通过MON手动设置 @see eOesAcctStatusT
        ('status', c_uint8),
        # 股东账户的所有者类型 @see eOesOwnerTypeT
        ('ownerType', c_uint8),
        # 投资者期权等级 @see eOesOptInvLevelT
        ('optInvLevel', c_uint8),
        # 是否禁止交易 (仅供API查询使用)
        ('isTradeDisabled', c_uint8),
        # 按64位对齐的填充域
        ('_INV_ACCT_BASE_filler', c_uint8 * 2),
        # 证券账户权限限制 @see OES_LIMIT_xxx
        ('limits', c_uint64),
        # 股东权限/客户权限 @see eOesTradingPermissionT
        ('permissions', c_uint64),
        # 席位号
        ('pbuId', c_int32),
        # 个股持仓比例阀值 @deprecated 已废弃, 为了兼容旧版本而保留
        ('stkPositionLimitRatio', c_int32),
        # 主板权益 (新股认购限额)
        ('subscriptionQuota', c_int32),
        # 科创板权益 (新股认购限额)
        ('kcSubscriptionQuota', c_int32),
        # 预留的备用字段
        ('_INV_ACCT_BASE_reserve', c_char * 32),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
    ]


# 查询证券账户信息请求
class OesQryInvAcctReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryInvAcctFilterT),
    ]


# 查询证券账户信息应答
class OesQryInvAcctRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 证券账户信息数组
        ('qryItems', OesInvAcctItemT * OES_MAX_INV_ACCT_ITEM_CNT_PER_PACK),
    ]


# 查询证券信息(现货产品信息)过滤条件
class OesQryStockFilterT(PrintableStructure):
    _fields_ = [
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别  @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类别  @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 融资融券担保品标识 (0:未指定, 1:是担保品, 2:不是担保品)
        ('crdCollateralFlag', c_int8),
        # 融资标的标识 (0:未指定, 1:是融资标的, 2:不是融资标的)
        ('crdMarginTradeUnderlyingFlag', c_int8),
        # 融券标的标识 (0:未指定, 1:是融券标的, 2:不是融券标的)
        ('crdShortSellUnderlyingFlag', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 2),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询证券信息(现货产品信息)请求
class OesQryStockReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryStockFilterT),
    ]


OesStockItemT = OesStockBaseInfoT
OesIssueItemT = OesIssueBaseInfoT
OesEtfItemT = OesEtfBaseInfoT
OesCashAssetItemT = OesCashAssetReportT
OesStkHoldingItemT = OesStkHoldingReportT
OesMarketStateItemT = OesMarketStateInfoT
OesNotifyInfoItemT = OesNotifyBaseInfoT


# 查询证券信息(现货产品信息)应答
class OesQryStockRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 现货产品信息数组
        ('qryItems', OesStockItemT * OES_MAX_STOCK_ITEM_CNT_PER_PACK),
    ]


# 查询证券发行信息过滤条件
class OesQryIssueFilterT(PrintableStructure):
    _fields_ = [
        # 证券发行代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 产品类型, 默认将仅查询新股发行信息, 即产品类型默认为 OES_PRODUCT_TYPE_IPO;
        # 如需查询配股发行信息, 需指定产品类型为 OES_PRODUCT_TYPE_ALLOTMENT
        # @see eOesProductTypeT
        ('productType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询证券发行信息请求
class OesQryIssueReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryIssueFilterT),
    ]


# 查询证券发行信息应答
class OesQryIssueRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 证券发行信息数组
        ('qryItems', OesIssueItemT * OES_MAX_ISSUE_ITEM_CNT_PER_PACK),
    ]


# 查询ETF申赎产品信息过滤条件
class OesQryEtfFilterT(PrintableStructure):
    _fields_ = [
        # ETF基金申赎代码, 可选项
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # ETF基金市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询ETF申赎产品信息请求
class OesQryEtfReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryEtfFilterT),
    ]


# 查询ETF申赎产品信息应答
class OesQryEtfRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # ETF申赎产品信息数组
        ('qryItems', OesEtfItemT * OES_MAX_ETF_ITEM_CNT_PER_PACK),
    ]


# 查询ETF成份证券信息过滤条件
class OesQryEtfComponentFilterT(PrintableStructure):
    _fields_ = [
        # ETF基金申赎代码
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # ETF基金市场代码 (可选项, 如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE)
        # @see eOesMarketIdT
        ('fundMktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# ETF基金成份证券信息内容
class OesEtfComponentItemT(PrintableStructure):
    _fields_ = [
        # ETF基金申赎代码
        ('fundId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成份证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 成份证券市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # ETF基金市场代码 @see eOesMarketIdT
        ('fundMktId', c_uint8),
        # 现金替代标识 @see eOesEtfSubFlagT
        ('subFlag', c_uint8),
        # 成份证券的证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 成份证券的证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 是否是作为申赎对价的成份证券
        # @note 注意事项:
        # - 非申赎对价的成份证券信息仅供参考, 申赎时不能对该类成份证券进行股份计算
        # 或现金替代处理。
        # - 例如: 深交所跨市场ETF中的沪市成份证券信息就属于非申赎对价的成份证券信息,
        # 对深交所跨市场ETF进行申赎时应使用 159900 虚拟成份券进行沪市成份证券份额
        # 的现金替代处理
        ('isTrdComponent', c_uint8),
        # 按64位对齐的填充域
        ('_ETF_COMPONENT_BASE_filler', c_uint8 * 2),
        # 前收盘价格, 单位精确到元后四位, 即1元 = 10000
        ('prevClose', c_int32),
        # 成份证券数量
        ('qty', c_int32),
        # 申购溢价比例, 单位精确到十万分之一, 即溢价比例10% = 10000
        ('premiumRatio', c_int32),
        # 赎回折价比例, 单位精确到十万分之一, 即折价比例10% = 10000
        ('discountRatio', c_int32),
        # 申购替代金额, 单位精确到元后四位, 即1元 = 10000
        ('creationSubCash', c_int64),
        # 赎回替代金额, 单位精确到元后四位, 即1元 = 10000
        ('redemptionSubCash', c_int64),
        # 成份证券名称
        ('securityName', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 预留的备用字段
        ('_reserve', c_char * 96),
    ]


# 查询ETF基金成份证券信息请求
class OesQryEtfComponentReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryEtfComponentFilterT),
    ]


# 查询ETF基金成份证券信息应答
class OesQryEtfComponentRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # ETF基金成份证券信息数组
        ('qryItems', OesEtfComponentItemT * OES_MAX_ETF_COMPONENT_ITEM_CNT_PER_PACK),
    ]


# 查询客户资金信息过滤条件
class OesQryCashAssetFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询客户资金信息请求
class OesQryCashAssetReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCashAssetFilterT),
    ]


# 查询客户资金信息应答
class OesQryCashAssetRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 客户资金信息数组
        ('qryItems', OesCashAssetItemT * OES_MAX_CASH_ASSET_ITEM_CNT_PER_PACK),
    ]


# 查询两地交易时对端结点资金资产信息请求
class OesQryColocationPeerCashReqT(PrintableStructure):
    _fields_ = [
        # 资金账号, 选填项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


# 查询两地交易时对端结点资金资产信息应答
class OesQryColocationPeerCashRspT(PrintableStructure):
    _fields_ = [
        # 两地交易时对端结点的资金信息
        ('colocationPeerCashItem', OesCashAssetItemT),
    ]


# 主柜资金信息内容
class OesCounterCashItemT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 客户姓名
        ('custName', c_char * OES_CUST_NAME_MAX_LEN),
        # 银行代码
        ('bankId', c_char * OES_BANK_NO_MAX_LEN),
        ('cashType', c_uint8),  # 资金账户类别 @see eOesAcctTypeT
        ('cashAcctStatus', c_uint8),  # 资金账户状态 @see eOesAcctStatusT
        ('currType', c_uint8),  # 币种类型 @see eOesCurrTypeT
        ('isFundTrsfDisabled', c_uint8),  # 是否禁止出入金
        ('_filler', c_uint8 * 4),  # 按64位对齐的填充域
        ('counterAvailableBal', c_int64),  # 主柜可用资金余额，单位精确到元后四位，即1元 = 10000
        ('counterDrawableBal', c_int64),  # 主柜可取资金余额，单位精确到元后四位，即1元 = 10000
        ('counterCashUpdateTime', c_int64),  # 主柜资金更新时间 (seconds since the Epoch)
        ('_reserve', c_char * 32),  # 保留字段
    ]


# 查询主柜资金信息请求
class OesQryCounterCashReqT(PrintableStructure):
    _fields_ = [
        # 资金账号, 选填项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


# 查询主柜资金信息应答
class OesQryCounterCashRspT(PrintableStructure):
    _fields_ = [
        # 主柜资金信息
        ('counterCashItem', OesCounterCashItemT),
    ]


# 查询股票持仓信息/信用持仓信息过滤条件
class OesQryStkHoldingFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码  @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别  @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 5),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询股票持仓信息/信用持仓信息请求
class OesQryStkHoldingReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryStkHoldingFilterT),
    ]


# 查询股票持仓信息/信用持仓信息应答
class OesQryStkHoldingRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 持仓信息数组
        ('qryItems', OesStkHoldingItemT * OES_MAX_HOLDING_ITEM_CNT_PER_PACK),
    ]


# 查询新股配号、中签信息过滤条件
class OesQryLotWinningFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 中签、配号记录类型, 可选项。如无需此过滤条件请使用 OES_LOT_TYPE_UNDEFINE
        # @see eOesLotTypeT
        ('lotType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 查询起始日期 (格式为 YYYYMMDD)
        ('startDate', c_int32),
        # 查询结束日期 (格式为 YYYYMMDD)
        ('endDate', c_int32),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询新股认购、中签信息请求
class OesQryLotWinningReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryLotWinningFilterT),
    ]


# 查询新股配号、中签信息应答
class OesQryLotWinningRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 新股认购、中签信息数组
        ('qryItems', OesLotWinningItemT * OES_MAX_LOG_WINNING_ITEM_CNT_PER_PACK),
    ]


# 查询委托信息过滤条件
class OesQryOrdFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 是否仅查询未关闭委托 (包括未全部成交或撤销的委托)
        ('isUnclosedOnly', c_uint8),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 证券类别  @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 买卖类型  @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
        # 客户委托编号, 可选项
        ('clOrdId', c_int64),
        # 客户委托流水号, 可选项
        ('clSeqNo', c_int64),
        # 查询委托的起始时间 (格式为 HHMMSSsss, 比如 141205000 表示 14:12:05.000)
        ('startTime', c_int32),
        # 查询委托的结束时间 (格式为 HHMMSSsss, 比如 141205000 表示 14:12:05.000)
        ('endTime', c_int32),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询委托信息请求
class OesQryOrdReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOrdFilterT),
    ]


# 查询委托信息应答
class OesQryOrdRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 委托信息数组
        ('qryItems', OesOrdItemT * OES_MAX_ORD_ITEM_CNT_PER_PACK),
    ]


# 查询成交信息过滤条件
class OesQryTrdFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 证券类别  @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 买卖类型  @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint32),
        # 内部委托编号, 可选项
        ('clOrdId', c_int64),
        # 客户委托流水号, 可选项
        ('clSeqNo', c_int64),
        # 成交开始时间 (格式为 HHMMSSsss, 形如 141205000)
        ('startTime', c_int32),
        # 成交结束时间
        ('endTime', c_int32),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询成交信息请求
class OesQryTrdReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryTrdFilterT),
    ]


# 查询成交信息应答
class OesQryTrdRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 成交信息数组
        ('qryItems', OesTrdItemT * OES_MAX_TRD_ITEM_CNT_PER_PACK),
    ]


# 查询出入金流水信息过滤条件
class OesQryFundTransferSerialFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 出入金流水号, 可选项
        ('clSeqNo', c_int32),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询出入金流水信息请求
class OesQryFundTransferSerialReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryFundTransferSerialFilterT),
    ]


# 查询出入金流水信息应答
class OesQryFundTransferSerialRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 出入金流水信息数组
        ('qryItems', OesFundTransferSerialItemT * OES_MAX_FUND_TRSF_ITEM_CNT_PER_PACK),
    ]


# 查询客户佣金信息过滤条件
class OesQryCommissionRateFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别, 可选项。如无需此过滤条件请使用 OES_SECURITY_TYPE_UNDEFINE
        # @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 买卖类型, 可选项。如无需此过滤条件请使用 OES_BS_TYPE_UNDEFINE
        # @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 5),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 客户佣金信息内容定义
class OesCommissionRateItemT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类别 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 买卖类型 @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 费用标识 @see eOesFeeTypeT
        ('feeType', c_uint8),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 计算模式 @see eOesCalcFeeModeT
        ('calcFeeMode', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8),
        # 费率, 单位精确到千万分之一, 即费率0.02% = 2000
        ('feeRate', c_int64),
        # 最低费用, 大于0时有效 (单位：万分之一元)
        ('minFee', c_int32),
        # 最高费用, 大于0时有效 (单位：万分之一元)
        ('maxFee', c_int32),
    ]


# 查询客户佣金信息请求
class OesQryCommissionRateReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCommissionRateFilterT),
    ]


# 查询客户佣金信息应答
class OesQryCommissionRateRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 客户佣金信息数组
        ('qryItems', OesCommissionRateItemT * OES_MAX_COMMS_RATE_ITEM_CNT_PER_PACK),
    ]


# 查询市场状态信息过滤条件
class OesQryMarketStateFilterT(PrintableStructure):
    _fields_ = [
        # 交易所代码 (可选项, 为 0 则匹配所有交易所)
        # @see eOesExchangeIdT
        ('exchId', c_uint8),
        # 交易平台代码 (可选项, 为 0 则匹配所有交易平台)
        # @see eOesPlatformIdT
        ('platformId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询市场状态信息请求
class OesQryMarketStateReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryMarketStateFilterT),
    ]


# 查询市场状态信息应答
class OesQryMarketStateRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 市场状态信息数组
        ('qryItems', OesMarketStateItemT * OES_MAX_MKT_STATE_ITEM_CNT_PER_PACK),
    ]


# 查询通知消息过滤条件
class OesQryNotifyInfoFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 通知消息等级 @see eOesNotifyLevelT
        ('notifyLevel', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询通知消息请求
class OesQryNotifyInfoReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryNotifyInfoFilterT),
    ]


# 查询通知消息应答
class OesQryNotifyInfoRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 通知消息数组
        ('qryItems', OesNotifyInfoItemT * OES_MAX_NOTIFY_INFO_ITEM_CNT_PER_PACK),
    ]


class _OesBrokerParamsInfoT_CreditExt(PrintableStructure):
    _fields_ = [
        ('singleMarginBuyCeiling', c_int64),  # 单笔融资买入委托金额上限
        ('singleShortSellCeiling', c_int64),  # 单笔融券卖出委托金额上限
        ('safetyLineRatio', c_int32),  # 维持担保比安全线 (千分比)
        ('withdrawLineRatio', c_int32),  # 维持担保比提取线 (千分比)
        ('warningLineRatio', c_int32),  # 维持担保比警戒线 (千分比)
        ('liqudationLineRatio', c_int32),  # 维持担保比平仓线 (千分比)
        # 是否支持使用 '仅归还息费' 模式归还融资融券负债的息费
        ('isRepayInterestOnlyAble', c_uint8),
        ('_filler', c_uint8 * 7),  # 按64位对齐的填充域
    ]


class _OesBrokerParamsInfoT_OptionExt(PrintableStructure):
    _fields_ = [
        ('withdrawLineRatio', c_int32),  # 出金提取线 (万分比)
        ('marginCallLineRatio', c_int32),  # 保证金盘中追保线 (万分比)
        ('liqudationLineRatio', c_int32),  # 保证金盘中平仓线 (万分比)
        ('marginDisposalLineRatio', c_int32),  # 保证金即时处置线 (万分比)
    ]


class _OesBrokerParamsInfoT_Union(PrintableUnion):
    _fields_ = [
        ('creditExt', _OesBrokerParamsInfoT_CreditExt),
        ('optionExt', _OesBrokerParamsInfoT_OptionExt),
        ('_extInfo', c_char * 192),  # 占位用的扩展信息
    ]


# 券商参数信息内容
class OesBrokerParamsInfoT(PrintableStructure):
    _fields_ = [
        # 券商名称
        ('brokerName', c_char * OES_BROKER_NAME_MAX_LEN),
        # 券商联系电话
        ('brokerPhone', c_char * OES_BROKER_PHONE_MAX_LEN),
        # 券商网址
        ('brokerWebsite', c_char * OES_BROKER_WEBSITE_MAX_LEN),
        # 当前API协议版本号
        ('apiVersion', c_char * OES_VER_ID_MAX_LEN),
        # 为兼容协议而添加的填充域
        ('_filler1', c_char * 8),
        # API兼容的最低协议版本号
        ('apiMinVersion', c_char * OES_VER_ID_MAX_LEN),
        # 为兼容协议而添加的填充域
        ('_filler2', c_char * 8),
        # 客户端最新的版本号
        ('clientVersion', c_char * OES_VER_ID_MAX_LEN),
        # 为兼容协议而添加的填充域
        ('_filler3', c_char * 8),
        # 允许客户端修改密码的开始时间 (HHMMSSsss)
        ('changePwdLimitTime', c_int32),
        # 客户端密码允许的最小长度
        ('minClientPasswordLen', c_int32),
        # 客户端密码强度级别
        # 密码强度范围[0~4]，密码含有字符种类(大写字母、小写字母、数字、有效符号)的个数
        ('clientPasswordStrength', c_int32),
        # 服务端支持的业务范围 @see eOesBusinessTypeT
        ('businessScope', c_uint32),
        # 当前会话对应的业务类型 @see eOesBusinessTypeT
        ('currentBusinessType', c_uint8),
        # 服务端是否支持两地交易内部资金划拨
        ('isSupportInternalAllot', c_uint8),
        # 按64位对齐的填充域
        ('_filler4', c_uint8 * 6),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 上证风险警示板证券单日买入数量限制
        ('sseRiskWarningSecurityBuyQtyLimit', c_int64),
        # 深证风险警示板证券单日买入数量限制
        ('szseRiskWarningSecurityBuyQtyLimit', c_int64),
        # 预留的备用字段
        ('_reserve', c_char * 24),
        # 业务范围扩展信息
        ('union', _OesBrokerParamsInfoT_Union),
    ]


# 查询券商参数信息应答
class OesQryBrokerParamsInfoRspT(PrintableStructure):
    _fields_ = [
        ('brokerParams', OesBrokerParamsInfoT),
    ]


# 应用程序升级源信息
class OesApplUpgradeSourceT(PrintableStructure):
    _fields_ = [
        # IP地址
        ('ipAddress', c_char * OES_MAX_IP_LEN),
        # 协议名称
        ('protocol', c_char * OES_APPL_UPGRADE_PROTOCOL_MAX_LEN),
        # 用户名
        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        # 登录密码
        ('password', c_char * OES_PWD_MAX_LEN),
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
class OesApplUpgradeItemT(PrintableStructure):
    _fields_ = [
        # 应用程序名称
        ('applName', c_char * OES_MAX_COMP_ID_LEN),
        # 应用程序的最低协议版本号
        ('minApplVerId', c_char * OES_VER_ID_MAX_LEN),
        # 应用程序的最高协议版本号
        ('maxApplVerId', c_char * OES_VER_ID_MAX_LEN),
        # 废弃的应用版本号列表
        ('discardApplVerId', c_char * OES_VER_ID_MAX_LEN*OES_APPL_DISCARD_VERSION_MAX_COUNT),
        # 废弃版本号的数目
        ('discardVerCount', c_int32),
        # 最新协议版本的日期
        ('newApplVerDate', c_int32),
        # 应用程序的最新协议版本号
        ('newApplVerId', c_char * OES_VER_ID_MAX_LEN),
        # 最新协议版本的标签信息
        ('newApplVerTag', c_char * OES_CLIENT_TAG_MAX_LEN),
        # 主用升级源配置信息
        ('primarySource', OesApplUpgradeSourceT),
        # 备用升级源配置信息
        ('secondarySource', OesApplUpgradeSourceT),
    ]


# OES周边应用程序升级信息
class OesApplUpgradeInfoT(PrintableStructure):
    _fields_ = [
        # 客户端升级配置信息
        ('clientUpgradeInfo', OesApplUpgradeItemT),
        # C_API升级配置信息
        ('cApiUpgradeInfo', OesApplUpgradeItemT),
        # JAVA_API升级配置信息
        ('javaApiUpgradeInfo', OesApplUpgradeItemT),
    ]


# 查询周边应用升级配置信息应答
class OesQryApplUpgradeInfoRspT(PrintableStructure):
    _fields_ = [
        ('applUpgradeInfo', OesApplUpgradeInfoT),
    ]


# 查询信用资产信息过滤条件
class OesQryCrdCreditAssetFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询信用资产信息请求
class OesQryCrdCreditAssetReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdCreditAssetFilterT),
    ]


OesCrdCreditAssetItemT = OesCrdCreditAssetBaseInfoT
OesCrdUnderlyingInfoItemT = OesCrdUnderlyingBaseInfoT
OesCrdDebtContractItemT = OesCrdDebtContractReportT
OesCrdDebtJournalItemT = OesCrdDebtJournalBaseInfoT
OesCrdCashRepayItemT = OesCrdCashRepayReportT
OesCrdSecurityDebtStatsItemT = OesCrdSecurityDebtStatsBaseInfoT
OesCrdExcessStockItemT = OesCrdExcessStockBaseInfoT
OesCrdInterestRateItemT = OesCommissionRateItemT


# 查询信用资产信息应答
class OesQryCrdCreditAssetRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 信用资产信息数组
        ('qryItems', OesCrdCreditAssetItemT * OES_MAX_CRD_CREDIT_ASSET_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券可充抵保证金证券及融资融券标的信息过滤条件
class OesQryCrdUnderlyingInfoFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 是否为融资标的 (0:未指定, 1:是融资标的, 2:不是融资标的)
        ('crdMarginTradeUnderlyingFlag', c_uint8),
        # 是否为融券标的 (0:未指定, 1:是融券标的, 2:不是融券标的)
        ('crdShortSellUnderlyingFlag', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 5),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券可充抵保证金证券及融资融券标的信息请求
class OesQryCrdUnderlyingInfoReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdUnderlyingInfoFilterT),
    ]


# 查询融资融券可充抵保证金证券及融资融券标的信息应答
class OesQryCrdUnderlyingInfoRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券可充抵保证金证券及融资融券标的信息数组
        ('qryItems', OesCrdUnderlyingInfoItemT * OES_MAX_CRD_UNDERLYING_INFO_ITEM_CNT_PER_PACK),
    ]


# 查询资金头寸信息 (可融资头寸信息) 过滤条件
class OesQryCrdCashPositionFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 头寸性质, 可选项 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询到的资金头寸信息 (可融资头寸信息) 内容
class OesCrdCashPositionItemT(PrintableStructure):
    _fields_ = [
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 头寸性质 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 币种 @see eOesCurrTypeT
        ('currType', c_uint8),
        # 按64位对齐的填充域
        ('_CRD_CASH_POSITION_BASE_filler', c_uint8 * 2),
        # 资金头寸金额 (含已用)
        ('positionAmt', c_int64),
        # 日间已归还金额
        ('repaidPositionAmt', c_int64),
        # 累计已用金额 (含日初已用)
        ('usedPositionAmt', c_int64),
        # 当前尚未成交的在途冻结金额
        ('frzPositionAmt', c_int64),
        # 期初余额 (单位精确到元后四位, 即1元=10000)
        ('originalBalance', c_int64),
        # 期初可用余额 (单位精确到元后四位, 即1元=10000)
        ('originalAvailable', c_int64),
        # 期初已用金额 (期初待归还负债金额; 单位精确到元后四位, 即1元=10000)
        ('originalUsed', c_int64),
        # 预留的备用字段
        ('_CRD_CASH_POSITION_BASE_reserve', c_char * 32),
        # 资金头寸剩余可融资金额
        ('availableBalance', c_int64),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 保留字段
        ('_reserve', c_char * 16),
    ]


# 查询融资融券业务资金头寸信息 (可融资头寸信息) 请求
class OesQryCrdCashPositionReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdCashPositionFilterT),
    ]


# 查询融资融券业务资金头寸信息 (可融资头寸信息) 应答
class OesQryCrdCashPositionRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券业务资金头寸信息数组
        ('qryItems', OesCrdCashPositionItemT * OES_MAX_CRD_CASH_POSITION_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券业务证券头寸信息 (可融券头寸信息) 过滤条件
class OesQryCrdSecurityPositionFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 头寸性质, 可选项 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询到的证券头寸信息 (可融券头寸信息) 内容
class OesCrdSecurityPositionItemT(PrintableStructure):
    _fields_ = [
        # 证券账户
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 头寸性质 @see eOesCrdCashGroupPropertyT
        ('cashGroupProperty', c_uint8),
        # 按64位对齐的填充域
        ('_SECURITY_POSITION_BASE_filler', c_uint8 * 2),
        # 头寸编号
        ('cashGroupNo', c_int32),
        # 证券头寸数量 (含已用)
        ('positionQty', c_int64),
        # 日间已归还数量 (当日归还不可用)
        ('repaidPositionQty', c_int64),
        # 累计已用数量 (含日初已用)
        ('usedPositionQty', c_int64),
        # 当前尚未成交的在途冻结数量
        ('frzPositionQty', c_int64),
        # 期初数量
        ('originalBalanceQty', c_int64),
        # 期初可用数量
        ('originalAvailableQty', c_int64),
        # 期初已用数量 (期初待归还负债数量)
        ('originalUsedQty', c_int64),
        # 预留的备用字段
        ('_SECURITY_POSITION_BASE_reserve', c_char * 32),
        # 当前可用头寸数量
        ('availablePositionQty', c_int64),
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 保留字段
        ('_reserve', c_char * 32),
    ]


# 查询融资融券业务证券头寸信息 (可融券头寸信息) 请求
class OesQryCrdSecurityPositionReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdSecurityPositionFilterT),
    ]


# 查询融资融券业务证券头寸信息 (可融券头寸信息) 应答
class OesQryCrdSecurityPositionRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券业务证券头寸信息 (可融券头寸信息) 数组
        ('qryItems', OesCrdSecurityPositionItemT * OES_MAX_CRD_SECURITY_POSITION_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券合约信息过滤条件
class OesQryCrdDebtContractFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 合约编号, 可选项
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 是否仅查询未了结的融资融券合约
        ('isUnclosedOnly', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 历史合约标识 (0:未指定, 1:是历史合约, 2:不是历史合约)
        ('historyContractFlag', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 4),
        # 查询融资融券合约的起始日期 (格式为 YYYYMMDD, 形如 20160830)
        ('startDate', c_int32),
        # 查询融资融券合约的结束日期 (格式为 YYYYMMDD, 形如 20160830))
        ('endDate', c_int32),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券合约信息请求
class OesQryCrdDebtContractReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdDebtContractFilterT),
    ]


# 查询融资融券合约信息应答
class OesQryCrdDebtContractRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券合约信息数组
        ('qryItems', OesCrdDebtContractItemT * OES_MAX_CRD_DEBT_CONTRACT_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券合约流水信息过滤条件
class OesQryCrdDebtJournalFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 合约编号, 可选项
        ('debtId', c_char * OES_CREDIT_DEBT_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 负债类型 @see eOesCrdDebtTypeT
        ('debtType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 查询融资融券合约流水的起始日期 (目前仅支持查询当日流水, 格式为 YYYYMMDD, 形如 20160830)
        ('startDate', c_int32),
        # 查询融资融券合约流水的结束日期 (格式为 YYYYMMDD, 形如 20160830))
        ('endDate', c_int32),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券合约流水信息请求
class OesQryCrdDebtJournalReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdDebtJournalFilterT),
    ]


# 查询融资融券合约流水信息应答
class OesQryCrdDebtJournalRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券合约流水信息数组
        ('qryItems', OesCrdDebtJournalItemT * OES_MAX_CRD_DEBT_JOURNAL_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券业务直接还款信息过滤条件
class OesQryCrdCashRepayFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 直接还款指令流水号, 可选项
        ('clSeqNo', c_int32),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券业务直接还款信息请求
class OesQryCrdCashRepayReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdCashRepayFilterT),
    ]


# 查询融资融券业务直接还款信息应答
class OesQryCrdCashRepayRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券业务直接还款信息数组
        ('qryItems', OesCrdCashRepayItemT * OES_MAX_CRD_CASH_REPAY_ITEM_CNT_PER_PACK),
    ]


# 查询客户单证券融资融券负债统计信息过滤条件
class OesQryCrdSecurityDebtStatsFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码  @see eOesMarketIdT
        ('mktId', c_uint8),
        # 是否有融资融券负债标识 (0:未指定, 1:有融资负债(含其他负债), 2:有融券负债, 3:有融资或融券负债)
        ('hasCreditDebtFlag', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询客户单证券融资融券负债统计信息请求
class OesQryCrdSecurityDebtStatsReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdSecurityDebtStatsFilterT),
    ]


# 查询客户单证券融资融券负债统计信息应答
class OesQryCrdSecurityDebtStatsRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 客户单证券融资融券负债统计信息数组
        ('qryItems', OesCrdSecurityDebtStatsItemT * OES_MAX_CRD_SECURITY_DEBT_STATS_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券业务余券信息过滤条件
class OesQryCrdExcessStockFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券业务余券信息请求
class OesQryCrdExcessStockReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdExcessStockFilterT),
    ]


# 查询融资融券业务余券信息应答
class OesQryCrdExcessStockRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 融资融券业务余券信息数组
        ('qryItems', OesCrdExcessStockItemT * OES_MAX_CRD_EXCESS_STOCK_ITEM_CNT_PER_PACK),
    ]


# 查询融资融券息费利率过滤条件
class OesQryCrdInterestRateFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 买卖类型, 可选项。如无需此过滤条件请使用 OES_BS_TYPE_UNDEFINE
        # @see eOesBuySellTypeT
        ('bsType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询融资融券息费利率请求
class OesQryCrdInterestRateReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryCrdInterestRateFilterT),
    ]


# 查询融资融券息费利率应答
class OesQryCrdInterestRateRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 客户佣金信息数组
        ('qryItems', OesCrdInterestRateItemT * OES_MAX_CRD_INTEREST_RATE_ITEM_CNT_PER_PACK),
    ]


# 融资融券业务最大可取资金信息内容
class OesCrdDrawableBalanceItemT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 可取资金
        ('drawableBal', c_int64),
    ]


# 查询融资融券业务最大可取资金信息请求
class OesQryCrdDrawableBalanceReqT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 资金账户代码, 可选项
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
    ]


# 查询融资融券业务最大可取资金信息应答
class OesQryCrdDrawableBalanceRspT(PrintableStructure):
    _fields_ = [
        # 融资融券业务最大可取资金信息
        ('drawableBalanceItem', OesCrdDrawableBalanceItemT),
    ]


# 融资融券担保品可转出的最大数量信息内容
class OesCrdCollateralTransferOutMaxQtyItemT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐填充域
        ('_filler', c_uint8 * 7),
        # 融资融券担保品可转出的最大数量
        ('collateralTransferOutMaxQty', c_int64),
    ]


# 查询融资融券担保品可转出的最大数量信息请求
class OesQryCrdCollateralTransferOutMaxQtyReqT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券代码, 必填项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充数据
        ('_filler', c_uint8 * 7),
    ]


# 查询融资融券担保品可转出的最大数量信息应答
class OesQryCrdCollateralTransferOutMaxQtyRspT(PrintableStructure):
    _fields_ = [
        # 融资融券担保品可转出的最大数量信息
        ('collateralTransferOutMaxQtyItem', OesCrdCollateralTransferOutMaxQtyItemT),
    ]


# 查询期权产品信息过滤条件
class OesQryOptionFilterT(PrintableStructure):
    _fields_ = [
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码, 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询期权产品信息请求
class OesQryOptionReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptionFilterT),
    ]


OesOptionItemT = OesOptionBaseInfoT
OesOptUnderlyingHoldingItemT = OesOptUnderlyingHoldingBaseInfoT
OesOptExerciseAssignItemT = OesOptionExerciseAssignBaseT


# 查询期权产品信息应答
class OesQryOptionRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 期权产品信息数组
        ('qryItems', OesOptionItemT * OES_MAX_OPT_OPTION_ITEM_CNT_PER_PACK),
    ]


# 查询期权持仓信息过滤条件
class OesQryOptHoldingFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 证券代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓类型 @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询到的期权持仓信息内容
class OesOptHoldingItemT(PrintableStructure):
    _fields_ = [
        # 账户代码
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 期权合约代码
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓类型 @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 产品类型 @see eOesProductTypeT
        ('productType', c_uint8),
        # 证券类型 @see eOesSecurityTypeT
        ('securityType', c_uint8),
        # 证券子类型 @see eOesSubSecurityTypeT
        ('subSecurityType', c_uint8),
        # 合约类型 (认购/认沽) @see eOesOptContractTypeT
        ('contractType', c_uint8),
        # 套保标志 (0 非套保, 1 套保)
        ('hedgeFlag', c_uint8),
        # 按64位对齐的填充域
        ('_HOLD_BASE_filler', c_uint8),
        # 日初总持仓张数
        ('originalQty', c_int64),
        # 日初可用持仓
        ('originalAvlQty', c_int64),
        # 按摊薄持仓成本价计的日初总持仓成本 (日初摊薄持仓成本价 * 日初总持仓)
        ('originalCostAmt', c_int64),
        # 权利仓的日初持有成本 (日初持仓均价 * 日初总持仓, 不含费用)
        ('originalCarryingAmt', c_int64),
        # 日中累计开仓张数
        ('totalOpenQty', c_int64),
        # 开仓委托未成交张数
        ('uncomeQty', c_int64),
        # 日中累计平仓张数
        ('totalCloseQty', c_int64),
        # 平仓在途冻结张数
        ('closeFrzQty', c_int64),
        # 手动冻结张数
        ('manualFrzQty', c_int64),
        # 日中累计获得权利金
        ('totalInPremium', c_int64),
        # 日中累计付出权利金
        ('totalOutPremium', c_int64),
        # 日中累计开仓费用
        ('totalOpenFee', c_int64),
        # 日中累计平仓费用
        ('totalCloseFee', c_int64),
        # 权利仓行权冻结张数
        ('exerciseFrzQty', c_int64),
        # 义务仓占用保证金
        ('positionMargin', c_int64),
        # 预留的备用字段
        ('_OPT_HOLDING_BASE_reserve', c_char * 32),
        # 可平仓张数 (单位: 张)
        ('closeAvlQty', c_int64),
        # 可行权张数 (单位: 张)
        ('exerciseAvlQty', c_int64),
        # 总持仓张数 (单位: 张)
        ('sumQty', c_int64),
        # 摊薄持仓成本价
        ('costPrice', c_int64),
        # 权利仓的持仓均价
        ('carryingAvgPrice', c_int64),
        # 可用的备兑持仓数量 (已锁定的标的持仓数量, 单位: 股)
        ('coveredAvlUnderlyingQty', c_int64),
        # 限仓额度信息
        # 可用的权利仓限额
        ('availableLongPositionLimit', c_int32),
        # 可用的总持仓限额
        ('availableTotalPositionLimit', c_int32),
        # 可用的单日买入开仓限额
        ('availableDailyBuyOpenLimit', c_int32),
        # 按64位对齐的填充域
        ('_OPT_HOLDING_EXT_filler2', c_int32),
        # 预留的备用字段
        ('_OPT_HOLDING_EXT_reserve', c_char * 32),
        # 交易所合约代码
        ('contractId', c_char * OES_CONTRACT_EXCH_ID_MAX_LEN),
        # 期权合约简称
        ('contractSymbol', c_char * OES_SECURITY_NAME_MAX_LEN),
        # 昨结算价
        ('prevSettlPrice', c_int64),
    ]


# 查询期权持仓信息请求
class OesQryOptHoldingReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptHoldingFilterT),
    ]


# 查询期权持仓信息应答
class OesQryOptHoldingRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 持仓信息数组
        ('qryItems', OesOptHoldingItemT * OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK),
    ]


# 查询期权标的持仓信息过滤条件
class OesQryOptUnderlyingHoldingFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码, 可选项
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码  @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别  @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询期权标的持仓信息请求
class OesQryOptUnderlyingHoldingReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptUnderlyingHoldingFilterT),
    ]


# 查询期权标的持仓信息应答
class OesQryOptUnderlyingHoldingRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 期权标的持仓信息数组
        ('qryItems', OesOptUnderlyingHoldingItemT * OES_MAX_OPT_HOLDING_ITEM_CNT_PER_PACK),
    ]


# 查询期权限仓额度信息过滤条件
class OesQryOptPositionLimitFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码, 可选项
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码  @see eOesMarketIdT
        ('mktId', c_uint8),
        # 证券类别  @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询到的期权限仓额度信息内容
class OesOptPositionLimitItemT(PrintableStructure):
    _fields_ = [
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 标的证券代码
        ('underlyingSecurityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 (衍生品市场) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 标的市场代码 @see eOesMarketIdT
        ('underlyingMktId', c_uint8),
        # 标的证券类型 @see eOesSecurityTypeT
        ('underlyingSecurityType', c_uint8),
        # 标的证券子类型 @see eOesSubSecurityTypeT
        ('underlyingSubSecurityType', c_uint8),
        # 按64位对齐的填充域
        ('_filler1', c_uint8 * 4),
        # 权利仓限额
        ('longPositionLimit', c_int32),
        # 总持仓限额
        ('totalPositionLimit', c_int32),
        # 单日买入开仓限额
        ('dailyBuyOpenLimit', c_int32),
        # 按64位对齐的填充域
        ('_filler2', c_int32),
        # 日初权利仓持仓数量 (单位: 张)
        ('originalLongQty', c_int32),
        # 日初义务仓持仓数量 (单位: 张)
        ('originalShortQty', c_int32),
        # 日初备兑义务仓持仓数量 (单位: 张)
        ('originalCoveredQty', c_int32),
        # 未占用的权利仓限额
        ('availableLongPositionLimit', c_int32),
        # 未占用的总持仓限额
        ('availableTotalPositionLimit', c_int32),
        # 未占用的单日买入开仓限额
        ('availableDailyBuyOpenLimit', c_int32),
        # 预留的备用字段
        ('_reserve', c_char * 8),
    ]


# 查询期权限仓额度信息请求
class OesQryOptPositionLimitReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptPositionLimitFilterT),
    ]


# 查询期权限仓额度信息应答
class OesQryOptPositionLimitRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 期权标的持仓信息数组
        ('qryItems', OesOptPositionLimitItemT * OES_MAX_OPT_UNDERLYING_ITEM_CNT_PER_PACK),
    ]


# 查询期权限购额度信息过滤条件
class OesQryOptPurchaseLimitFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码 (不带'888'编码的原始股东账户代码), 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码 (衍生品市场), 可选项。如无需此过滤条件请使用 OES_MKT_ID_UNDEFINE
        # @see eOesMarketIdT
        ('mktId', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 7),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 期权限购额度信息内容
class OesOptPurchaseLimitItemT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 资金账户代码
        ('cashAcctId', c_char * OES_CASH_ACCT_ID_MAX_LEN),
        # 股东账户代码 (不带'888'编码的原始股东账户代码)
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 市场代码 (衍生品市场) @see eOesMarketIdT
        ('mktId', c_uint8),
        # 客户类别 @see eOesCustTypeT
        ('custType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 限购额度/套保额度
        ('purchaseLimit', c_int64),
        # 日初占用的期权限购额度
        ('originalUsedPurchaseAmt', c_int64),
        # 日中累计开仓占用的期权限购额度
        ('totalOpenPurchaseAmt', c_int64),
        # 当前挂单冻结的期权限购额度
        ('frzPurchaseAmt', c_int64),
        # 日中累计平仓释放的期权限购额度
        ('totalClosePurchaseAmt', c_int64),
        # 可用限购额度/套保额度
        ('availablePurchaseLimit', c_int64),
    ]


# 查询期权限购额度信息请求
class OesQryOptPurchaseLimitReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptPurchaseLimitFilterT),
    ]


# 查询期权限购额度信息应答
class OesQryOptPurchaseLimitRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 通知消息数组
        ('qryItems', OesOptPurchaseLimitItemT * OES_MAX_OPT_PURCHASE_LIMIT_ITEM_CNT_PER_PACK),
    ]


# 查询期权行权指派信息过滤条件
class OesQryOptExerciseAssignFilterT(PrintableStructure):
    _fields_ = [
        # 客户代码, 可选项
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 证券账户代码, 可选项
        ('invAcctId', c_char * OES_INV_ACCT_ID_MAX_LEN),
        # 期权合约代码, 可选项
        ('securityId', c_char * OES_SECURITY_ID_MAX_LEN),
        # 市场代码 @see eOesMarketIdT
        ('mktId', c_uint8),
        # 持仓类型 @see eOesOptPositionTypeT
        ('positionType', c_uint8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 6),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', c_int64),
    ]


# 查询期权行权指派信息请求
class OesQryOptExerciseAssignReqT(PrintableStructure):
    _fields_ = [
        # 查询请求消息头
        ('reqHead', OesQryReqHeadT),
        # 查询过滤条件
        ('qryFilter', OesQryOptExerciseAssignFilterT),
    ]


# 查询期权行权指派信息应答
class OesQryOptExerciseAssignRspT(PrintableStructure):
    _fields_ = [
        # 查询应答消息头
        ('rspHead', OesQryRspHeadT),
        # 期权行权指派信息数组
        ('qryItems', OesOptExerciseAssignItemT * OES_MAX_OPT_EXERCISE_ASSIGN_ITEM_CNT_PER_PACK),
    ]


# 回报同步请求消息
class OesReportSynchronizationReqT(PrintableStructure):
    _fields_ = [
        # 客户端最后接收到的回报数据的回报编号
        # - 等于0, 从头开始推送回报数据
        # - 大于0, 从指定的回报编号开始推送回报数据
        # - 小于0, 从最新的数据开始推送回报数据
        ('lastRptSeqNum', c_int64),
        # 待订阅的客户端环境号
        # - 大于0, 区分环境号, 仅订阅环境号对应的回报数据
        # - 小于等于0, 不区分环境号, 订阅该客户下的所有回报数据
        ('subscribeEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
        # 待订阅的回报消息种类
        # - 0:      默认回报 (等价于: 0x01,0x02,0x04,0x08,0x10,0x20,0x40)
        # - 0x0001: OES业务拒绝 (未通过风控检查等)
        # - 0x0002: OES委托已生成 (已通过风控检查)
        # - 0x0004: 交易所委托回报 (包括交易所委托拒绝、委托确认和撤单完成通知)
        # - 0x0008: 交易所成交回报
        # - 0x0010: 出入金委托执行报告 (包括出入金委托拒绝、出入金委托回报)
        # - 0x0020: 资金变动信息
        # - 0x0040: 持仓变动信息
        # - 0x0080: 市场状态信息
        # - 0x0100: 通知消息回报
        # - 0xFFFF: 所有回报
        # @see eOesSubscribeReportTypeT
        ('subscribeRptTypes', c_int32),
    ]


# 回报同步应答消息
class OesReportSynchronizationRspT(PrintableStructure):
    _fields_ = [
        # 服务端最后已发送或已忽略的回报数据的回报编号
        ('lastRptSeqNum', c_int64),
        # 待订阅的客户端环境号
        # - 大于0, 区分环境号, 仅订阅环境号对应的回报数据
        # - 小于等于0, 不区分环境号, 订阅该客户下的所有回报数据
        ('subscribeEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler', c_uint8 * 3),
        # 已订阅的回报消息种类
        ('subscribeRptTypes', c_int32),
    ]


# 测试请求报文
class OesTestRequestReqT(PrintableStructure):
    _fields_ = [
        # 测试请求标识符
        ('testReqId', c_char * OES_MAX_TEST_REQ_ID_LEN),
        # 发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('sendTime', c_char * OES_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler', c_char * 2),
    ]


# 测试请求的应答报文
class OesTestRequestRspT(PrintableStructure):
    _fields_ = [
        # 测试请求标识符
        ('testReqId', c_char * OES_MAX_TEST_REQ_ID_LEN),
        # 测试请求的原始发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('origSendTime', c_char * OES_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler1', c_char * 2),
        # 测试请求应答的发送时间 (timeval结构或形如'YYYYMMDD-HH:mm:SS.sss'的字符串)
        ('respTime', c_char * OES_MAX_SENDING_TIME_LEN),
        # 按64位对齐的填充域
        ('_filler2', c_char * 2),
        # 消息实际接收时间 (开始解码等处理之前的时间)
        ('_recvTime', STimespec32T),
        # 消息采集处理完成时间
        ('_collectedTime', STimespec32T),
        # 消息推送时间 (写入推送缓存以后, 实际网络发送之前)
        ('_pushingTime', STimespec32T),
    ]


# 批量委托请求的消息头
class OesBatchOrdersHeadT(PrintableStructure):
    _fields_ = [
        # 本批次的委托请求数量
        ('itemCount', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
    ]


# 批量委托请求的完整请求报文
# (只有请求报文, 没有独立的应答报文)
class OesBatchOrdersReqT(PrintableStructure):
    _fields_ = [
        # 批量委托请求的批次消息头
        ('batchHead', OesBatchOrdersHeadT),
        # 委托请求列表
        ('items', OesOrdReqT * 1),
    ]


# 修改密码请求报文
class OesChangePasswordReqT(PrintableStructure):
    _fields_ = [
        # 加密方法
        ('encryptMethod', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 登录用户名
        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
        # 之前的登录密码
        ('oldPassword', c_char * OES_PWD_MAX_LEN),
        # 新的登录密码
        ('newPassword', c_char * OES_PWD_MAX_LEN),
    ]


# 修改密码应答报文
class OesChangePasswordRspT(PrintableStructure):
    _fields_ = [
        # 加密方法
        ('encryptMethod', c_int32),
        # 按64位对齐的填充域
        ('_filler', c_int32),
        # 登录用户名
        ('username', c_char * OES_CLIENT_NAME_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在应答数据中原样返回)
        ('userInfo', UserInfo),
        # 客户端编号
        ('clientId', c_int16),
        # 客户端环境号
        ('clEnvId', c_int8),
        # 按64位对齐的填充域
        ('_filler2', c_int8),
        # 发生日期 (格式为 YYYYMMDD, 形如 20160830)
        ('transDate', c_int32),
        # 发生时间 (格式为 HHMMSSsss, 形如 141205000)
        ('transTime', c_int32),
        # 拒绝原因
        ('rejReason', c_int32),
    ]


# 期权账户结算单确认请求报文
class OesOptSettlementConfirmReqT(PrintableStructure):
    _fields_ = [
        # 客户代码
        ('custId', c_char * OES_CUST_ID_MAX_LEN),
        # 用户私有信息 (由客户端自定义填充, 并在回报数据中原样返回)
        ('userInfo', UserInfo),
    ]


# 回报消息的消息头定义
class OesRptMsgHeadT(PrintableStructure):
    _fields_ = [
        ('rptSeqNum', c_int64),  # 回报消息的编号
        ('rptMsgType', c_uint8),  # 回报消息的消息代码 @see eOesMsgTypeT
        ('execType', c_uint8),  # 执行类型 @see eOesExecTypeT
        ('bodyLength', c_int16),  # 回报消息的消息体大小
        ('ordRejReason', c_int32),  # 订单/撤单被拒绝原因
    ]


# 回报消息的消息体定义
class OesRptMsgBodyT(PrintableUnion):
    _fields_ = [
        ('ordInsertRsp', OesOrdCnfmT),  # OES委托响应-委托已生成
        ('ordRejectRsp', OesOrdRejectT),  # OES委托响应-业务拒绝
        ('ordCnfm', OesOrdCnfmT),  # 交易所委托回报
        ('trdCnfm', OesTrdCnfmT),  # 交易所成交回报
        ('fundTrsfRejectRsp', OesFundTrsfRejectT),  # 出入金委托拒绝
        ('fundTrsfCnfm', OesFundTrsfReportT),  # 出入金执行报告
        ('cashAssetRpt', OesCashAssetReportT),  # 资金变动回报信息
        ('stkHoldingRpt', OesStkHoldingReportT),  # 持仓变动回报信息 (股票)
        ('optHoldingRpt', OesOptHoldingReportT),  # 持仓变动回报信息 (期权)
        ('optUnderlyingHoldingRpt', OesOptUnderlyingHoldingReportT),  # 期权标的持仓变动回报信息
        ('notifyInfoRpt', OesNotifyInfoReportT),  # 通知消息回报信息
        ('optSettlementConfirmRpt', OesOptSettlementConfirmReportT),  # 期权账户结算单确认回报信息
        ('crdDebtCashRepayRpt', OesCrdCashRepayReportT),  # 融资融券直接还款执行报告
        ('crdDebtContractRpt', OesCrdDebtContractReportT),  # 融资融券合约变动回报信息
        ('crdDebtJournalRpt', OesCrdDebtJournalReportT),  # 融资融券合约流水回报信息
    ]


# 完整的回报消息定义
class OesRptMsgT(PrintableStructure):
    _fields_ = [
        ('rptHead', OesRptMsgHeadT),  # 回报消息的消息头
        ('rptBody', OesRptMsgBodyT),  # 回报消息的消息体
    ]


# 汇总的请求消息的消息体定义
class OesReqMsgBodyT(PrintableUnion):
    _fields_ = [
        # 委托申报请求报文
        ('ordReq', OesOrdReqT),
        # 撤单请求请求报文
        ('ordCancelReq', OesOrdCancelReqT),
        # 批量委托请求报文
        ('batchOrdersReq', OesBatchOrdersReqT),
        # 融资融券负债归还(除直接还款以外)请求报文
        ('crdRepayReq', OesCrdRepayReqT),
        # 融资融券直接还款请求报文
        ('crdCashRepayReq', OesCrdCashRepayReqT),
        # 出入金请求报文
        ('fundTrsfReq', OesFundTrsfReqT),
        # 修改密码请求报文
        ('changePasswordReq', OesChangePasswordReqT),
        # 期权账户结算单确认请求报文
        ('optSettlementConfirmReq', OesOptSettlementConfirmReqT),
        # 测试请求报文
        ('testRequestReq', OesTestRequestReqT),
        # 回报同步请求报文
        ('rptSyncReq', OesReportSynchronizationReqT),
    ]


OesOptSettlementConfirmRspT = OesOptSettlementConfirmBaseInfoT


# 汇总的应答消息的消息体定义
class OesRspMsgBodyT(PrintableUnion):
    _fields_ = [
        # 执行报告回报消息
        ('rptMsg', OesRptMsgT),
        # 市场状态消息
        ('mktStateRpt', OesMarketStateInfoT),
        # 测试请求的应答报文
        ('testRequestRsp', OesTestRequestRspT),
        # 回报同步应答报文
        ('reportSynchronizationRsp', OesReportSynchronizationRspT),
        # 修改密码应答报文
        ('changePasswordRsp', OesChangePasswordRspT),
        # 结算单确认应答报文
        ('optSettlementConfirmRsp', OesOptSettlementConfirmRspT),
    ]


# 统一的查询请求消息定义
class OesQryReqMsgT(PrintableUnion):
    _fields_ = [
        ('qryOrd', OesQryOrdReqT),  # 查询委托信息请求
        ('qryTrd', OesQryTrdReqT),  # 查询成交信息请求
        ('qryCashAsset', OesQryCashAssetReqT),  # 查询客户资金信息请求
        ('qryColoPeerCash', OesQryColocationPeerCashReqT),  # 查询两地交易COLO对端结点的资金信息请求
        ('qryStkHolding', OesQryStkHoldingReqT),  # 查询股票持仓信息请求
        ('qryOptHolding', OesQryOptHoldingReqT),  # 查询期权持仓信息请求
        ('qryCust', OesQryCustReqT),  # 查询客户信息请求
        ('qryInvAcct', OesQryInvAcctReqT),  # 查询证券账户请求
        ('qryComms', OesQryCommissionRateReqT),  # 查询客户佣金信息请求
        ('qryFundTrsf', OesQryFundTransferSerialReqT),  # 查询出入金信息请求
        ('qryLotWinning', OesQryLotWinningReqT),  # 查询新股配号、中签信息请求
        ('qryIssue', OesQryIssueReqT),  # 查询证券发行信息请求
        ('qryStock', OesQryStockReqT),  # 查询现货产品信息请求
        ('qryEtf', OesQryEtfReqT),  # 查询ETF申赎产品信息请求
        ('qryEtfComponent', OesQryEtfComponentReqT),  # 查询ETF基金成份证券信息请求
        ('qryOption', OesQryOptionReqT),  # 查询期权产品信息请求
        ('qryMktState', OesQryMarketStateReqT),  # 查询市场状态信息请求
        ('qryNotifyInfo', OesQryNotifyInfoReqT),  # 查询通知消息请求
        ('qryCounterCash', OesQryCounterCashReqT),  # 查询主柜资金信息请求
        ('qryOptPositionLimit', OesQryOptPositionLimitReqT),  # 查询期权限仓额度信息请求
        ('qryOptPurchaseLimit', OesQryOptPurchaseLimitReqT),  # 查询期权限购额度信息请求
        ('qryOptUnderlyingHolding', OesQryOptUnderlyingHoldingReqT),  # 查询期权标的持仓信息请求
        ('qryOptExerciseAssign', OesQryOptExerciseAssignReqT),  # 查询期权行权指派信息请求
        # 信用类查询请求
        ('qryCrdDebtContract', OesQryCrdDebtContractReqT),  # 查询融资融券合约信息请求
        ('qryCrdCustSecuDebtStats', OesQryCrdSecurityDebtStatsReqT),  # 查询客户单证券融资融券负债统计信息请求
        ('qryCrdCreditAsset', OesQryCrdCreditAssetReqT),  # 查询信用资产信息请求
        ('qryCrdCashRepay', OesQryCrdCashRepayReqT),  # 查询融资融券业务直接还券信息请求
        ('qryCrdCashPosition', OesQryCrdCashPositionReqT),  # 查询融资融券业务资金头寸信息 (可融资头寸信息) 请求
        ('qryCrdSecurityPosition', OesQryCrdSecurityPositionReqT),  # 查询融资融券业务证券头寸信息 (可融券头寸信息) 请求
        ('qryCrdExcessStock', OesQryCrdExcessStockReqT),  # 查询融资融券业务余券信息请求
        ('qryCrdDebtJournal', OesQryCrdDebtJournalReqT),  # 查询融资融券合约流水信息请求
        ('qryCrdInterestRateReq', OesQryCrdInterestRateReqT),  # 查询融资融券息费利率请求
        ('qryCrdUnderlyingInfoReq', OesQryCrdUnderlyingInfoReqT),  # 查询融资融券可充抵保证金证券及融资融券标的信息请求
        ('qryCrdDrawableBalanceReq', OesQryCrdDrawableBalanceReqT),  # 查询融资融券业务可取资金的请求
        ('qryCrdTransferOutMaxQtyReq', OesQryCrdCollateralTransferOutMaxQtyReqT),  # 查询融资融券担保品可转出的最大数量请求
    ]


# 统一的查询应答消息定义
class OesQryRspMsgT(PrintableUnion):
    _fields_ = [
        ('ordRsp', OesQryOrdRspT),  # 查询委托信息应答
        ('trdRsp', OesQryTrdRspT),  # 查询成交信息应答
        ('cashAssetRsp', OesQryCashAssetRspT),  # 查询客户资金信息应答
        ('qryColoPeerCashRsp', OesQryColocationPeerCashRspT),  # 查询两地交易COLO对端结点的资金信息应答
        ('stkHoldingRsp', OesQryStkHoldingRspT),  # 查询股票持仓信息应答
        ('optHoldingRsp', OesQryOptHoldingRspT),  # 查询期权持仓信息应答
        ('custRsp', OesQryCustRspT),  # 查询客户信息应答
        ('invAcctRsp', OesQryInvAcctRspT),  # 查询证券账户应答
        ('commsRateRsp', OesQryCommissionRateRspT),  # 查询客户佣金信息应答
        ('fundTrsfRsp', OesQryFundTransferSerialRspT),  # 查询出入金流水信息应答
        ('lotWinningRsp', OesQryLotWinningRspT),  # 查询新股配号、中签信息应答
        ('issueRsp', OesQryIssueRspT),  # 查询证券发行信息应答
        ('stockRsp', OesQryStockRspT),  # 查询现货产品信息应答
        ('etfRsp', OesQryEtfRspT),  # 查询ETF申赎产品信息应答
        ('etfComponentRsp', OesQryEtfComponentRspT),  # 查询ETF基金成份证券信息应答
        ('optionRsp', OesQryOptionRspT),  # 查询期权产品信息应答
        ('tradingDay', OesQryTradingDayRspT),  # 查询当前交易日信息应答
        ('mktStateRsp', OesQryMarketStateRspT),  # 查询市场状态信息应答
        ('notifyInfoRsp', OesQryNotifyInfoRspT),  # 查询通知消息应答
        ('clientOverview', OesClientOverviewT),  # 客户端总览信息
        ('counterCashRsp', OesQryCounterCashRspT),  # 客户主柜资金信息
        ('optPositionLimitRsp', OesQryOptPositionLimitRspT),  # 查询期权限仓额度信息应答
        ('optPurchaseLimitRsp', OesQryOptPurchaseLimitRspT),  # 查询期权限购额度信息应答
        ('optUnderlyingHoldingRsp', OesQryOptUnderlyingHoldingRspT),  # 查询期权标的持仓信息应答
        ('optExerciseAssignRsp', OesQryOptExerciseAssignRspT),  # 查询期权行权指派信息应答
        ('brokerParamsRsp', OesQryBrokerParamsInfoRspT),  # 查询券商参数信息应答
        ('applUpgradeRsp', OesQryApplUpgradeInfoRspT),  # 周边应用升级信息
        # 信用类查询应答
        ('crdDebtContractRsp', OesQryCrdDebtContractRspT),  # 查询融资融券合约信息应答
        ('crdCustSecuDebtStatsRsp', OesQryCrdSecurityDebtStatsRspT),  # 查询客户单证券融资融券负债统计信息应答
        ('crdCreditAssetRsp', OesQryCrdCreditAssetRspT),  # 查询信用资产信息应答
        ('crdCashRepayRsp', OesQryCrdCashRepayRspT),  # 查询融资融券业务直接还券信息应答
        ('crdCashPositionRsp', OesQryCrdCashPositionRspT),  # 查询融资融券业务资金头寸信息 (可融资头寸信息) 应答
        ('crdSecurityPositionRsp', OesQryCrdSecurityPositionRspT),  # 查询融资融券业务证券头寸信息 (可融券头寸信息) 应答
        ('crdExcessStockRsp', OesQryCrdExcessStockRspT),  # 查询融资融券业务余券信息应答
        ('crdDebtJournalRsp', OesQryCrdDebtJournalRspT),  # 查询融资融券合约流水信息应答
        ('crdInterestRateRsp', OesQryCrdInterestRateRspT),  # 查询融资融券息费利率应答
        ('crdCustUnderlyingInfoRsp', OesQryCrdUnderlyingInfoRspT),  # 查询融资融券可充抵保证金证券及融资融券标的信息应答
        ('crdDrawableBalanceRsp', OesQryCrdDrawableBalanceRspT),  # 查询融资融券业务可取资金的应答
        ('crdTransferOutMaxQtyRsp', OesQryCrdCollateralTransferOutMaxQtyRspT),  # 查询融资融券担保品及标的应答
    ]




#ifndef CLIENT_API_PACKETS_H
#define CLIENT_API_PACKETS_H


#include <extras/swf_oes/include/mds_api/mds_api.h>
#include <extras/swf_oes/include/oes_api/oes_api.h>


#define CLIENT_STRATEGY_INFO_NAME_MAX_LEN (64)
#define CLIENT_STRATEGY_INFO_PATH_MAX_LEN (1024)
#define CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN (2048)


#ifdef __cplusplus
extern "C" {
#endif


/**
 * 日志级别
 */
typedef enum _eClientApiLogLevel {
    CLIENT_API_LOG_LEVEL_TRACE,
    CLIENT_API_LOG_LEVEL_DEBUG,
    CLIENT_API_LOG_LEVEL_INFO,
    CLIENT_API_LOG_LEVEL_ERR,
    CLIENT_API_LOG_LEVEL_CRITICAL,
    CLIENT_API_LOG_LEVEL_OFF,
} eClientApiLogLevelT;


/**
 * 通知消息等级
 */
typedef enum _eClientApiNotifyLevel {
    CLIENT_API_NOTIFY_LEVEL_UNDEFINE = 0,  /**< 未定义 */
    CLIENT_API_NOTIFY_LEVEL_LOW = 1,       /**< 较低 */
    CLIENT_API_NOTIFY_LEVEL_GENERAL = 2,   /**< 一般 */
    CLIENT_API_NOTIFY_LEVEL_IMPORTANT = 3, /**< 重要 */
    CLIENT_API_NOTIFY_LEVEL_URGENT = 4,    /**< 紧急 */
} eClientApiNotifyLevelT;


/**
 * 通信消息的消息类型定义
 */
typedef enum _eClientApiMsgType {
    __CLIENTMSG_MIN,

    __CLIENT_API_MSG_BASE_COUNTER_START = 0x00010000,
    __CLIENT_API_MSG_BASE_COUNTER_END =
        __CLIENT_API_MSG_BASE_COUNTER_START + 0x1000,

    __CLIENT_API_MSG_BASE_MDS_START,
    __CLIENT_API_MSG_BASE_MDS_END = __CLIENT_API_MSG_BASE_MDS_START + 0x1000,

    __CLIENT_API_MSG_BASE_COUNTER_FINISHED_START,
    __CLIENT_API_MSG_BASE_COUNTER_FINISHED_END =
        __CLIENT_API_MSG_BASE_COUNTER_FINISHED_START + 0x1000,

    __CLIENT_API_MSG_BASE_MDS_FINISHED_START,
    __CLIENT_API_MSG_BASE_MDS_FINISHED_END =
        __CLIENT_API_MSG_BASE_MDS_FINISHED_START + 0x1000,

    __CLIENT_API_MSG_MERGE_MAX,

    // 策略心跳
    CLIENT_API_MSG_STRATEGY_EXE_LIVING,
    // 策略被动退出
    CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN,
    // 策略主动退出
    CLIENT_API_MSG_STRATEGY_EXE_QUITTED,
    // 客户端退出
    CLIENT_API_MSG_CLIENT_QUIT,

    // 策略通知
    CLIENT_API_MSG_STRATEGY_NOTIFY,
    // 策略委托
    CLIENT_API_MSG_STRATEGY_ORDER,

    CLIENT_API_MSG_QRY_ASSET,
    CLIENT_API_MSG_QRY_HOLD,
    CLIENT_API_MSG_QRY_ORD,
    CLIENT_API_MSG_QRY_TRD,

    __CLIENT_API_MSG_MAX
} eClientApiMsgTypeT;
/*----------------------------------------------------------------*/


/**
 * 消息头
 */
typedef struct _ClientApiMsgHead {
    uint8 msgFlag;      /**< 消息标志 */
    uint8 status;       /**< 状态码 */
    uint8 detailStatus; /**< 明细状态代码*/
    uint8 __fillter1;
    uint32 msgSize; /**< 消息大小 */

    int32 msgId;     /**< 消息代码 */
    int32 msgSeqNum; /**< 消息序号 */
} ClientApiMsgHeadT;


/* 结构体的初始化值定义 */
#define NULLOBJ_CLIENT_API_MSG_HEAD 0, 0, 0, 0, 0, 0, 0
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyInfoItem {
    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
    char path[CLIENT_STRATEGY_INFO_PATH_MAX_LEN];
    char notifymsg[CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN];

    uint8 execSts;
    uint8 isSelect;
    uint8 disuse;
    uint8 __fillter;
    // 精确到毫秒的时间戳,添加的时候获取,作为主键,用于交易数据匹配
    int32 timestampId;

    int64 pid;
    int64 lastLiveTime;
} ClientStrategyInfoItemT;


#define NULLOBJ_CLIENT_STRATEGY_INFO_ITEM_PKT {0}, {0}, {0}, 0, 0, 0, 0, 0, 0, 0
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyNotifyItem {
    int32 notifyId;
    uint8 notifyLevel;
    uint8 __fillter[3];

    int32 notifyTime;
    uint8 __fillter2[4];

    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
    char notifymsg[CLIENT_STRATEGY_NOTIFY_MSG_MAX_LEN];
} ClientStrategyNotifyItemT;


#define NULLOBJ_CLIENT_STRATEGY_NOTIFY_ITEM_PKT                                \
    0, 0, {0}, 0, {0}, {0}, { 0 }
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyOrdItem {
    int32 strategyOrdId;
    int32 strategyTimestampId;

    uint8 mktId;
    uint8 ordType;
    uint8 bsType;
    uint8 ordStatus; // 同oes订单状态
    uint8 isAutoSend;

    uint8 __filler[3];

    int32 ordRejReason;
    int32 exchErrCode;

    int32 ordQty;
    int32 ordPrice;

    int32 trdPrice;
    int32 __filler2;

    int32 cnfmQty;
    int32 canceledQty;

    int64 trdQty;
    int64 trdAmt;
    int64 trdFee;

    int64 __ordTimestamp; // 内部字段客户端使用

    char invAcctId[OES_INV_ACCT_ID_MAX_LEN];
    char securityId[OES_SECURITY_ID_MAX_LEN];
    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
} ClientStrategyOrdItemT;


#define NULLOBJ_CLIENT_STRATEGY_ORD_ITEM_PKT                                   \
    0, 0, 0, 0, 0, 0, 0, {0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0}, {0}, {  \
        0                                                                      \
    }
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyQuitItem {
    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
} ClientStrategyQuitItemT;


#define NULLOBJ_CLIENT_STRATEGY_QUIT_ITEM_PKT                                  \
    { 0 }
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyShutdownItem {
    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
} ClientStrategyShutdownItemT;


#define NULLOBJ_CLIENT_STRATEGY_SHUTDOWN_ITEM_PKT                              \
    { 0 }
/*----------------------------------------------------------------*/


/**
 *
 */
typedef struct _ClientStrategyLivingItem {
    char name[CLIENT_STRATEGY_INFO_NAME_MAX_LEN];
} ClientStrategyLivingItemT;


#define NULLOBJ_CLIENT_STRATEGY_LINING_ITEM_PKT                                \
    { 0 }
/*----------------------------------------------------------------*/


/*----------------------------------------------------------------
 * 流消息体完整定义
 *----------------------------------------------------------------*/
typedef union _ClientApiMsgBody {
    // 请求应答流数据
    ClientStrategyLivingItemT living;
    ClientStrategyQuitItemT quit;
    ClientStrategyShutdownItemT shutdown;

    ClientStrategyNotifyItemT notify;
    ClientStrategyOrdItemT order;

    // 交易流数据
    OesRptMsgT trdRpt;

    // 行情流数据
    MdsMktDataSnapshotT mktDataSnapshot;
    MdsL2TradeT trade;
    MdsL2OrderT mdOrder;

    char __data[1];
} ClientApiMsgBodyT;


/*----------------------------------------------------------------
 * 流消息完整定义
 *----------------------------------------------------------------*/
typedef struct _ClientApiStreamMsg {
    ClientApiMsgHeadT msgHead;
    ClientApiMsgBodyT msgBody;
} ClientApiStreamMsgT;


typedef int32 (*F_CLIENTAPI_ON_STREAM_MSG_T)(const ClientApiMsgHeadT *pMsgHead,
                                             void *pMsgItem,
                                             void *pCallbackParams);


#ifdef __cplusplus
}
#endif


#endif

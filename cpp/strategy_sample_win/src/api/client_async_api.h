
#ifndef CLIENT_ASYNC_API_H
#define CLIENT_ASYNC_API_H


#include <src/api/client_api_packets.h>


#ifdef __cplusplus
extern "C" {
#endif


/**
 * 初始化API接口
 *
 *
 * @param       pTrdStream      交易流地址
 * @param       pMktStream      行情流地址
 * @param       pReqStream      委托请求流地址
 * @param       pStrategyName   策略名称
 * @param       strategyId      策略ID
 * @param       strategyOrdId   策略委托序号
 * @param       timeoutMs       超时时间(毫秒)
 * @param       msgTimeoutMs
 * 回调函数超时时间(毫秒)(使用函数ClientAsyncApi_RunWithOutCallBack则不需要此参数)
 * @param       heartBtInt      心跳时间
 * @param       fnOnTrdMsgCallback
 * 注册的交易流回调函数(使用函数ClientAsyncApi_RunWithOutCallBack则不需要此参数)
 * @param       fnOnMdMsgCallback
 * 注册的行情流回调函数(使用函数ClientAsyncApi_RunWithOutCallBack则不需要此参数)
 * @param       pTrdCallBackParam
 * 交易回调函数自使用参数,作为回调函数参数(使用函数ClientAsyncApi_RunWithOutCallBack则不需要此参数)
 * @param       pMdCallBackParam
 * 行情回调函数自使用参数,作为回调函数参数(使用函数ClientAsyncApi_RunWithOutCallBack则不需要此参数)
 * @param       level               API日志级别
 * @return      非NULL成功否则失败。
 */
__SPK_DLL_EXPORT void *ClientAsyncApi_Init(
    const char *pTrdStream, const char *pMktStream, const char *pReqStream,
    const char *pStrategyName, int32 strategyId, int32 strategyOrdId,
    int32 timeoutMs, int32 msgTimeoutMs, int32 heartBtInt,
    F_CLIENTAPI_ON_STREAM_MSG_T fnOnTrdMsgCallback,
    F_CLIENTAPI_ON_STREAM_MSG_T fnOnMdMsgCallback, void *pTrdCallBackParam,
    void *pMdCallBackParam, uint8 level = CLIENT_API_LOG_LEVEL_DEBUG);


/**
 * 启动API, python不使用此接口
 * ClientAsyncApi_Run与ClientAsyncApi_RunWithOutCallBack不能同时使用，
 * 根据具体情况选择其中之一使用
 *
 * @param       pClientAsyncApiCtx              api上下文
 * @return      小于0失败否则成功。进程阻塞
 */
__SPK_DLL_EXPORT int32 ClientAsyncApi_Run(void *pClientAsyncApiCtx);


/**
 * 启动API, python语言使用此接口。
 * ClientAsyncApi_Run与ClientAsyncApi_RunWithOutCallBack不能同时使用，
 * 根据具体情况选择其中之一使用
 *
 * @param       pClientAsyncApiCtx              api上下文
 * @return      小于0失败否则成功。进程阻塞
 */
__SPK_DLL_EXPORT int32
ClientAsyncApi_RunWithOutCallBack(void *pClientAsyncApiCtx);


/**
 * 读取交易流数据,对于python语言使用此接口。
 *
 *
 * @param       pClientAsyncApiCtx      API上下文
 * @param       pMsg                    流消息
 * @param       timeoutMs               超时时间(毫秒)
 * @param       pCallbackParams         自定义回调函数参数
 * @return      小于0失败否则成功.使用独立线程调用，阻塞执行.
 */
__SPK_DLL_EXPORT bool ClientAsyncApi_WaitTrdMsg(ClientApiStreamMsgT *pMsg,
                                                int32 timeoutMs);


/**
 * 读取行情流数据,对于python语言使用此接口。
 *
 *
 * @param       pClientAsyncApiCtx      API上下文
 * @param       pMsg                    流消息
 * @param       timeoutMs               超时时间(毫秒)
 * @return      true: 获取到数据 false: 未获取数据
 */
__SPK_DLL_EXPORT bool ClientAsyncApi_WaitMdMsg(ClientApiStreamMsgT *pMsg,
                                               int32 timeoutMs);


/**
 * 发送委托
 *
 *
 * @param       pClientAsyncApiCtx  API上下文
 * @param       psecurityId         证券代码
 * @param       mktId               证券市场代码 (@eOesMarketIdT)
 * @param       bsType              买卖类型 (@eOesBuySellTypeT)
 * @param       strategyOrdId       策略委托序号, 策略自己维护的编号, 用于匹配
 * @param       ordQty              委托数量
 * @param       ordPrice            委托价格(单位精确到元后四位, 即1元=10000)
 * @param       isAutoSend
 * 是否自动发送至柜台(1:自动发送至柜台,0:仅缓存至客户端,需要手动发送)
 * @return      小于0失败否则成功。
 */
__SPK_DLL_EXPORT int32 ClientAsyncApi_SendOrderReq(void *pClientAsyncApiCtx,
                                                   const char *pSecurityId,
                                                   uint8 mktId, uint8 bsType,
                                                   int32 strategyOrdId,
                                                   int32 ordQty, int32 ordPrice,
                                                   uint8 isAutoSend);


/**
 * 发送通知消息
 *
 *
 * @param       pClientAsyncApiCtx  API上下文
 * @param       pMsg                通知消息内容
 * @param       msgLevel            通知消息等级(@eClientApiNotifyLevelT)
 * @return      小于0失败否则成功。
 */
__SPK_DLL_EXPORT int32 ClientAsyncApi_SendNotifyMsg(void *pClientAsyncApiCtx,
                                                    const char *pMsg,
                                                    uint8 msgLevel);


/**
 * 发送策略退出消息(策略主动退出)
 *
 *
 * @param       pClientAsyncApiCtx      API上下文
 * @return      小于0失败否则成功。
 */
__SPK_DLL_EXPORT int32 ClientAsyncApi_SendQuitedMsg(void *pClientAsyncApiCtx);


/**
 * 销毁API接口
 *
 *
 * @param       pClientAsyncApiCtx      API上下文
 * @return      小于0失败否则成功
 */
__SPK_DLL_EXPORT int32 ClientAsyncApi_Destory(void *pClientAsyncApiCtx);


/**
 * 是否为本策略订单
 *
 *
 * @param       userInfo      委托确认和成交确认中的userinfo字段
 * @param       strategyId    策略ID
 * @return      1:是 0:否
 */
__SPK_DLL_EXPORT bool ClientAsyncApi_IsOwnedByStrategy(int64 userInfo,
                                                       int32 strategyId);


#ifdef __cplusplus
}
#endif


#endif

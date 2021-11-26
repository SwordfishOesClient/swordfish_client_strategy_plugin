

#include <stdio.h>
#include <string>
#include <src/api/client_async_api.h>


static void* _clientAPiCtx = nullptr;
static volatile bool _isQuit = false;
static std::string _strategyName = "";
static int32 _strategyId;
static int32 _strategyOrdId = 0;
static int64 _mdMsgCount = 0;


static int32
_handleMd(const ClientApiMsgHeadT *pMsgHead,
               void *pMsgItem,
               void *pCallbackParams) {
    int32 rc = 0;

    if (_mdMsgCount > 100000) {
        _isQuit = true;
        rc = ClientAsyncApi_SendQuitedMsg(_clientAPiCtx);
        printf("发送策略主动退出消息, 设置退出标志且返回-1 rc: %d\n", rc);
        return -1;
    } else {
        if (pMsgHead->msgId == __CLIENT_API_MSG_BASE_MDS_START +  MDS_MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH ||
            pMsgHead->msgId == __CLIENT_API_MSG_BASE_MDS_START +
            MDS_MSGTYPE_L2_MARKET_DATA_SNAPSHOT) {
            MdsMktDataSnapshotT *pData = (MdsMktDataSnapshotT *) pMsgItem;
            if (0 == (_mdMsgCount % 50)) {
                rc = ClientAsyncApi_SendOrderReq(_clientAPiCtx,
                                                 pData->l2Stock.SecurityID,
                                                 pData->head.exchId == MDS_EXCH_SSE? OES_MKT_SH_ASHARE:OES_MKT_SZ_ASHARE,
                                                 OES_BS_TYPE_BUY,
                                                 _strategyOrdId++,
                                                 100,
                                                 pData->stock.TradePx,
                                                 1);
                printf("发送委托信息 rc: %d\n", rc);
            }
        }
    }
    return 0;
}


static int32
_handleTrd(const ClientApiMsgHeadT *pMsgHead,
               void *pMsgItem,
               void *pCallbackParams) {
    if (pMsgHead->msgId == __CLIENT_API_MSG_BASE_COUNTER_START + OESMSG_RPT_ORDER_INSERT) {
        OesRptMsgT* rpt = (OesRptMsgT* ) pMsgItem;
        OesOrdCnfmT* pData = &rpt->rptBody.ordInsertRsp;
        if (ClientAsyncApi_IsOwnedByStrategy(pData->userInfo.i64, _strategyId)) {
            ClientAsyncApi_SendNotifyMsg(_clientAPiCtx,
                (_strategyName + " 收到交易数据:" + pData->securityId).c_str(),
                CLIENT_API_NOTIFY_LEVEL_GENERAL);
        }
    }
    return 0;

}


static inline int32
_handleQuitMsg(const ClientApiMsgHeadT *pMsgHead,
               void *pMsgItem,
               void *pCallbackParams) {
    if (pMsgHead->msgId == CLIENT_API_MSG_CLIENT_QUIT) {
        _isQuit = true;
        printf("接收到客户端退出消息, 设置退出标志且返回 -1 msgId: %d\n", pMsgHead->msgId);
        return -1;
    }

    if (pMsgHead->msgId == CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN) {
        _isQuit = true;
        ClientAsyncApi_SendNotifyMsg(_clientAPiCtx,
                                     (_strategyName + " 被动退出").c_str(),
                                     CLIENT_API_NOTIFY_LEVEL_IMPORTANT);
        printf("接收到策略被动退出消息, 设置退出标志且返回 -1 msgId: %d\n", pMsgHead->msgId);
        return -1;
    }

    if (pMsgHead->msgId == CLIENT_API_MSG_STRATEGY_EXE_QUITTED) {
        _isQuit = true;
        printf("接收到策略主动退出消息, 设置退出标志且返回 -1 msgId: %d\n", pMsgHead->msgId);
        return -1;
    }
    return 0;
}


static int32
_OnMsgCallbackReadMdStream(const ClientApiMsgHeadT *pMsgHead,
                void *pMsgItem,
                void *pCallbackParams) {
    printf("接收到行情消息 msgId: %d\n", pMsgHead->msgId);
    int32 rc = _handleQuitMsg(pMsgHead, pMsgItem, pCallbackParams);
    if (rc < 0) {
        return rc;
    }

    _mdMsgCount++;

    // TODO 处理行情数据
    return _handleMd(pMsgHead, pMsgItem, pCallbackParams);
}


static int32
_OnMsgCallbackReadTrdStream(const ClientApiMsgHeadT *pMsgHead,
                void *pMsgItem,
                void *pCallbackParams) {
    printf("接收到交易消息 msgId: %d\n", pMsgHead->msgId - __CLIENT_API_MSG_BASE_COUNTER_START);
    int32 rc = _handleQuitMsg(pMsgHead, pMsgItem, pCallbackParams);
    if (rc < 0) {
        _isQuit = true;
        return rc;
    }

    // TODO 处理交易数据
    return _handleTrd(pMsgHead, pMsgItem, pCallbackParams);
}


int main(int argc, char **argv)
{
    if (argc != 8) {
out:
        fprintf(stderr, "./strategy_sample <trdStream> <mktStream> \
                <reqStream> <strategyName> <clEnvId> <strategyId> \
                <maxStrategyOrdId> \n");
        exit(EXIT_FAILURE);
    }
    int32 rc = 0;

    _strategyName = argv[4];
    _strategyId = std::stoi(argv[6]);
    _strategyOrdId = std::stoi(argv[7]) + 1;
    fprintf(stderr, "==== \n");

    _clientAPiCtx = ClientAsyncApi_Init(argv[1],
                                        argv[2],
                                        argv[3],
                                        _strategyName.c_str(),
                                        _strategyId,
                                        _strategyOrdId,
                                        5000,
                                        500,
                                        1000,
                                        _OnMsgCallbackReadTrdStream,
                                        _OnMsgCallbackReadMdStream,
                                        NULL, NULL,
                                        CLIENT_API_LOG_LEVEL_DEBUG);


    if (!_clientAPiCtx) {
        printf("ClientAsyncApi Init失败\n");
        goto out;
    }

    fprintf(stderr, "初始化CLIENT ASYNC API成功\n");

    rc = ClientAsyncApi_Run(_clientAPiCtx);
    if (rc < 0) {
        fprintf(stderr, "ClientAsyncApi run 失败\n");
        goto out;
    }
    fprintf(stderr, "CLIENT ASYNC API STOP 成功\n");

    ClientAsyncApi_Destory(_clientAPiCtx);
    fprintf(stderr, "销毁CLIENT ASYNC API成功");

    return EXIT_SUCCESS;

}

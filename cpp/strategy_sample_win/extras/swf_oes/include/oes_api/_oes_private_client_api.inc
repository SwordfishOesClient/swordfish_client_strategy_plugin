/*
 * Copyright 2020 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @file    _oes_private_client_api.inc
 *
 * 对客户端开放的OES内部接口
 *
 * @note    注意事项:
 * - 该文件中的接口仅提供给客户端内部使用, 请勿扩散
 *
 * @version 0.15.11.15  2020/11/12
 * @since   0.15.11.15  2020/11/12
 */


#ifndef __OES_PRIVATE_CLIENT_API_INC
#define __OES_PRIVATE_CLIENT_API_INC


#include    <oes_api/oes_api.h>


#ifdef __cplusplus
extern "C" {
#endif


/* ===================================================================
 * 内部接口别名 (避免在测试工具或样例代码等开源代码中直接使用内部接口)
 * =================================================================== */

/* 对客户端开放的内部接口 */
#define __OESAPI_QUERY_UPGRADE_INFO         OesApi_QueryApplUpgradeInfo
#define __OESAPI_ASSIGN_SOURCE_TYPE         __OesApi_SetSourceType
/* -------------------------           */


/* ===================================================================
 * 对客户端开放的内部接口函数声明
 * =================================================================== */

/**
 * 设置当前进程登录OES时使用的发送方代码
 *
 * @param   pSenderCompId       发送方代码
 */
void    OesApi_SetSenderCompId(
                const char *pSenderCompId);

/**
 * 返回当前进程登录OES时使用的发送方代码
 *
 * @return  发送方代码
 */
const char*
        OesApi_GetSenderCompId(void);

/**
 * 查询周边应用升级配置信息
 *
 * @param       pQryChannel     查询通道的会话信息
 * @param[out]  pApplUpgradeInfo
 *                              查询到的升级配置信息
 * @retval      =0              查询成功
 * @retval      <0              查询失败 (负的错误号)
 */
int32   OesApi_QueryApplUpgradeInfo(
                OesApiSessionInfoT *pQryChannel,
                OesApplUpgradeInfoT *pApplUpgradeInfo);

/**
 * 设置委托来源类型 (仅供客户端内部使用)
 *
 * @param   sourceType          委托来源类型 @see eOesSourceTypeT
 *                              - 0x21/33: 客户端
 */
void    __OesApi_SetSourceType(
                uint8 sourceType);

/**
 * 获取委托来源类型 (仅供客户端内部使用)
 *
 * @return  委托来源类型 @see eOesSourceTypeT
 */
uint8   __OesApi_GetSourceType(void);
/* -------------------------           */


#ifdef __cplusplus
}
#endif

#endif  /* __OES_PRIVATE_CLIENT_API_INC */

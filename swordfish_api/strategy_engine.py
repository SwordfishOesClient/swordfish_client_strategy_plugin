# -*- coding: utf-8 -*-
import sys
import platform
import threading
from ctypes import cast
from .client_api import *


class Engine(object):
    handle_td = None
    handle_md = None
    if platform.system() == 'Windows':
        client_api = ClientAPI('./swordfish_api/client_api.dll')
    elif platform.system() == 'Darwin':
        client_api = ClientAPI('./swordfish_api/libclient_api.dylib')
    else:
        raise Exception(f"不支持的操作系统{platform.system()}")
    is_quit = False
    trd_stream = ""
    mkt_stream = ""
    req_stream = ""
    strategy_name = ""
    cl_env_id = 1
    strategy_id = 0
    strategy_ord_id = 0


def init(handle_td, handle_md):
    Engine.handle_td = handle_td
    Engine.handle_md = handle_md
    Engine.trd_stream = sys.argv[1]
    Engine.mkt_stream = sys.argv[2]
    Engine.req_stream = sys.argv[3]
    Engine.strategy_name = sys.argv[4]
    Engine.cl_env_id = int(sys.argv[5])
    Engine.strategy_id = int(sys.argv[6])
    Engine.strategy_ord_id = int(sys.argv[7]) + 1
    return 0


def handle_quit_msg(msg_head, msg_item, callback_params):
    msg_id = msg_head.contents.msg_id
    if msg_id == CLIENT_API_MSG_CLIENT_QUIT:
        Engine.is_quit = True
        print(f"接收到客户端退出消息, 设置退出标志且返回 -1 msg_id: {msg_id}")
        return -1
    elif msg_id == CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN:
        Engine.is_quit = True
        Engine.client_api.client_async_api_send_notify_msg(Engine.strategy_name, f"{Engine.strategy_name} 被动退出",
                                                           CLIENT_API_NOTIFY_LEVEL_IMPORTANT)
        print(f"接收到策略被动退出消息, 设置退出标志且返回 -1 msg_id: {msg_id}")
        return -1
    elif msg_id == CLIENT_API_MSG_STRATEGY_EXE_QUITTED:
        Engine.is_quit = True
        print(f"接收到策略主动退出消息, 设置退出标志且返回 -1 msgId: {msg_id}")
        return -1
    return 0


def on_msg_callback_read_md_stream(msg_head, msg_item, callback_params):
    msg_head = cast(msg_head, POINTER(ClientApiMsgHeadT))
    print(f"接收到行情消息 msg_id: {msg_head.contents.msg_id}")
    rc = handle_quit_msg(msg_head, msg_item, callback_params)
    if rc < 0:
        return rc
    return Engine.handle_md(msg_head, msg_item, callback_params)


def on_msg_callback_read_trd_stream(msg_head, msg_item, callback_params):
    msg_head = cast(msg_head, POINTER(ClientApiMsgHeadT))
    print(f"接收到交易消息 msg_id: {msg_head.contents.msg_id}")
    rc = handle_quit_msg(msg_head, msg_item, callback_params)
    if rc < 0:
        return rc
    return Engine.handle_td(msg_head, msg_item, callback_params)


def do():
    Engine.client_api.client_async_api_init(Engine.trd_stream, Engine.mkt_stream, Engine.req_stream,
                                            Engine.strategy_name, Engine.strategy_id, Engine.strategy_ord_id,
                                            5000, 1000, CLIENT_API_LOG_LEVEL_DEBUG)
    if Engine.client_api.async_ctx is None:
        print("ClientAsyncApi Init失败")
        return -1
    wait_trd_msg = threading.Thread(target=Engine.client_api.client_async_api_wait_trd_msg,
                                    args=(on_msg_callback_read_trd_stream, 500, 0))
    wait_md_msg = threading.Thread(target=Engine.client_api.client_async_api_wait_md_msg,
                                   args=(on_msg_callback_read_md_stream, 500, 0))
    print("初始化CLIENT ASYNC API成功")

    wait_trd_msg.start()
    wait_md_msg.start()

    rc = Engine.client_api.client_async_api_run()
    if rc < 0:
        print("ClientAsyncApi run 失败")
        return -1

    print("CLIENT ASYNC API STOP 成功")

    Engine.client_api.client_async_api_destory()
    print("销毁CLIENT ASYNC API成功")

    wait_trd_msg.join()
    wait_md_msg.join()


def quit():
    Engine.is_quit = True
    rc = Engine.client_api.client_async_api_send_quited_msg(Engine.strategy_name)
    return rc


def send_order(security_id, mkt_id, bs_type, ord_qty, ord_price):
    Engine.strategy_ord_id += 1
    return Engine.client_api.client_async_api_send_order_req(Engine.strategy_name, security_id, mkt_id, bs_type,
                                                             Engine.strategy_id, Engine.strategy_ord_id, ord_qty,
                                                             ord_price)


def send_notify_msg(msg, msg_level):
    return Engine.client_api.client_async_api_send_notify_msg(Engine.strategy_name, msg, msg_level)


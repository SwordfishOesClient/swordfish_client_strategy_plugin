# -*- coding: utf-8 -*-
import sys
import platform
import threading
import traceback
from queue import Queue, Empty
from .client_api import *


class Engine(object):
    handle = None
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
    strategy_path = ""
    cl_env_id = 1
    strategy_id = 0
    strategy_ord_id = 0
    msg_queue = Queue()


def init(handle):
    Engine.handle = handle
    Engine.trd_stream = sys.argv[1]
    Engine.mkt_stream = sys.argv[2]
    Engine.req_stream = sys.argv[3]
    Engine.strategy_name = sys.argv[4]
    Engine.strategy_path = sys.argv[8]
    Engine.cl_env_id = int(sys.argv[5])
    Engine.strategy_id = int(sys.argv[6])
    Engine.strategy_ord_id = int(sys.argv[7])
    print("strategy_path:", Engine.strategy_path)
    Engine.client_api.client_async_api_init(Engine.trd_stream, Engine.mkt_stream, Engine.req_stream,
                                            Engine.strategy_name, Engine.strategy_path, Engine.strategy_id,
                                            Engine.strategy_ord_id, 5000, 1000, CLIENT_API_LOG_LEVEL_DEBUG)
    if Engine.client_api.async_ctx is None:
        print("ClientAsyncApi Init失败")
        return -1
    return 0


def on_msg_callback_read_md_stream():
    while not Engine.is_quit:
        msg = ClientApiStreamMsgT()
        if Engine.client_api.client_async_api_wait_md_msg(msg, 1000):
            Engine.msg_queue.put(msg)


def on_msg_callback_read_trd_stream():
    while not Engine.is_quit:
        msg = ClientApiStreamMsgT()
        if Engine.client_api.client_async_api_wait_trd_msg(msg, 1000):
            Engine.msg_queue.put(msg)


def process_msg():
    while not Engine.is_quit:
        try:
            msg = Engine.msg_queue.get(timeout=1)
            # print(f"接收到交易消息 msg_id: {msg.msg_head.msg_id}")
            msg_id = msg.msg_head.msg_id
            if msg_id == ClientApiMsgTypeT.CLIENT_API_MSG_CLIENT_QUIT.value:
                Engine.is_quit = True
                print(f"接收到客户端退出消息, 设置退出标志且返回 -1 msg_id: {msg_id}")
            elif msg_id == ClientApiMsgTypeT.CLIENT_API_MSG_STRATEGY_EXE_SHUTDOWN.value:
                Engine.is_quit = True
                Engine.client_api.client_async_api_send_notify_msg(f"{Engine.strategy_name} 被动退出",
                                                                   CLIENT_API_NOTIFY_LEVEL_IMPORTANT)
                print(f"接收到策略被动退出消息, 设置退出标志且返回 -1 msg_id: {msg_id}")
            elif msg_id == ClientApiMsgTypeT.CLIENT_API_MSG_STRATEGY_EXE_QUITTED.value:
                Engine.is_quit = True
                print(f"接收到策略主动退出消息, 设置退出标志且返回 -1 msg_id: {msg_id}")
            Engine.handle(msg)
        except Empty:
            pass
        except:
            print(traceback.format_exc())
            return


def do():
    wait_trd_msg = threading.Thread(target=on_msg_callback_read_trd_stream)
    wait_md_msg = threading.Thread(target=on_msg_callback_read_md_stream)
    process_msg_thread = threading.Thread(target=process_msg)
    print("初始化CLIENT ASYNC API成功")
    wait_trd_msg.start()
    wait_md_msg.start()
    process_msg_thread.start()

    Engine.client_api.client_async_api_add_strategy()

    rc = Engine.client_api.client_async_api_run()
    if rc < 0:
        print("ClientAsyncApi run 失败")
        return -1

    print("CLIENT ASYNC API STOP 成功")

    Engine.client_api.client_async_api_destory()
    print("销毁CLIENT ASYNC API成功")

    wait_trd_msg.join()
    wait_md_msg.join()
    process_msg_thread.join()
    return 0


def engine_quit():
    Engine.is_quit = True
    rc = Engine.client_api.client_async_api_send_quited_msg()
    return rc


def send_order(security_id, mkt_id, bs_type, ord_type, ord_qty, ord_price):
    Engine.strategy_ord_id += 1
    Engine.client_api.client_async_api_send_order_req(security_id, mkt_id, bs_type, ord_type,
                                                      Engine.strategy_ord_id, ord_qty,
                                                      ord_price, 1)
    return Engine.strategy_ord_id


def send_notify_msg(msg, msg_level):
    return Engine.client_api.client_async_api_send_notify_msg(msg, msg_level)


def is_owned_by_myself(user_info):
    return Engine.client_api.client_is_owned_by_strategy(user_info, Engine.strategy_id)


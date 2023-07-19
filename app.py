# encoding:utf-8

import os
import signal
import sys

from channel import channel_factory
from common.log import logger
from config import conf, load_config
from plugins import *

# 它在接收到指定的系统信号时保存用户数据，并优雅地退出程序。
def sigterm_handler_wrap(_signo):
    old_handler = signal.getsignal(_signo)

    def func(_signo, _stack_frame):
        logger.info("signal {} received, exiting...".format(_signo))
        #  保存用户数据
        conf().save_user_datas()
        if callable(old_handler):  #  check old_handler
            return old_handler(_signo, _stack_frame)
        sys.exit(0)

    signal.signal(_signo, func)


def run():
    try:
        # load config
        load_config()
        # ctrl + c    中断信号。在许多操作系统中，包括Unix和Linux，当你在命令行中按下 Ctrl+C 时，就会发送中断信号
        sigterm_handler_wrap(signal.SIGINT)
        # kill signal 进程终止的信号
        sigterm_handler_wrap(signal.SIGTERM)

        # create channel  ， 通道类型，支持：{wx,wxy,terminal,wechatmp,wechatmp_service,wechatcom_app}
        channel_name = conf().get("channel_type", "wx")

        if "--cmd" in sys.argv:
            channel_name = "terminal"

        if channel_name == "wxy":
            os.environ["WECHATY_LOG"] = "warn"
            # os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = '127.0.0.1:9001'

        # 根据通道类型创建通道
        channel = channel_factory.create_channel(channel_name)
        if channel_name in ["wx", "wxy", "terminal", "wechatmp", "wechatmp_service", "wechatcom_app"]:
            PluginManager().load_plugins()

        # startup channel
        channel.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)


if __name__ == "__main__":
    run()

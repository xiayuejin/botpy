#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os.path

import botpy
from botpy.utils import YamlUtil
from botpy.types.message import MessageEmbedField, MessageEmbed
from botpy.types.ws_context import WsContext

test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))


async def _message_handler(context: WsContext, message: botpy.Message):
    """
    定义事件回调的处理

    :param context: WsContext 对象，包含 event_type 和 event_id
    :param message: 事件对象（如监听消息是Message对象）
    """
    await handle_send_embed(1, message.channel_id, message.id)


async def handle_send_embed(time, channel_id, msg_id):
    msg_api = botpy.BotMessageAPI(t_token, False)

    for i in range(time):
        await asyncio.sleep(1)
        # 构造消息发送请求数据对象
        embed = MessageEmbed()
        embed.title = "embed消息"
        embed.prompt = "消息透传显示"
        embed.fields = [
            MessageEmbedField(name="<@!1234>hello world", value="通知提醒"),
            MessageEmbedField(name="<@!1234>hello world", value="标题"),
        ]

        send = botpy.MessageSendRequest(embed=embed, msg_id=msg_id, content="<@!1234>hello world")
        # 通过api发送回复消息
        botpy._log.info("send text message : %s" % i)
        await msg_api.post_message(channel_id, send)


if __name__ == "__main__":
    # async的异步接口的使用示例
    t_token = botpy.Token(test_config["token"]["appid"], test_config["token"]["token"])
    qqbot_handler = botpy.Handler(botpy.HandlerType.AT_MESSAGE_EVENT_HANDLER, _message_handler)
    botpy.async_listen_events(t_token, False, qqbot_handler)

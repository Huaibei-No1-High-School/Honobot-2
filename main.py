from mirai import *
import asyncio

from FDHolder import FDHolder
from KWD import KWD
from antirxbot import antirxbot
from sing import Sing
from whois import Whois

qq = 3185672511  # 字段 qq 的值
authKey = '123456987'  # 字段 authKey 的值
mirai_api_http_locate = 'vpn.orangecheers.top:23333/'  # httpapi所在主机的地址端口,如果 setting.yml 文件里字段 "enableWebsocket" 的值为 "true" 则需要将 "/" 换成 "/ws", 否则将接收不到消息.

miraibot = Mirai(f"mirai://{mirai_api_http_locate}?authKey={authKey}&qq={qq}", websocket=True)

AppList = []
@miraibot.receiver("GroupMessage")
async def event_gm(app: Mirai, event: GroupMessage):
    print(event.sender.group.id)
    global AppList
    for hoapp in AppList:
        await hoapp.recv(app,event)
    pass



if __name__ == "__main__":
    print("????")
    AppList.append(FDHolder())
    AppList.append(KWD())
    AppList.append(Whois())
    AppList.append(Sing())
    AppList.append(antirxbot())
    miraibot.run()






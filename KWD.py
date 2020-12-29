from mirai import *
from myemail import email

from HApp import HApp
from sing import Sing


class KWD(HApp):
    def __init__(self):
        self.white = True
        self.whitelist = [
            776324219,
            341475083,
            614123891,
        ]
    async def recv(self, app: Mirai, event: GroupMessage):
        if HApp.isblocked(self,event.sender.group.id):
            return
        str = event.messageChain.toString()
        if str.__contains__("一键邦邦"):
            print(event.sender.group)
            await app.sendGroupMessage(event.sender.group,[
                At(target=992951869),
                At(target=1127659190),
                At(target=1009878658),
                At(target=649737381),
                At(target=78497388),
                At(target=3504879459),
                At(target=764806602),
            ])
        if "让国歌堕入黑暗" in str:
            #email()
            await app.sendGroupMessage(event.sender.group, [
                Plain("关闭 星空凛的台灯 成功!")
            ])
        if "让国歌堕入黑暗" in str:
            #email()
            await app.sendGroupMessage(event.sender.group, [
                Plain("关闭 星空凛的台灯 成功!")
            ])
        if str[0:5] == "果果别唱了":
            if Sing.locked == False:
                await app.sendGroupMessage(event.sender.group, [
                    Plain('你耳朵聋了🐎，👴唱啥了')
                ])
            else:
                Sing.stopsignal = True
                await app.sendGroupMessage(event.sender.group, [
                    Plain('👴不唱了')
                ])
        print(event.messageChain)
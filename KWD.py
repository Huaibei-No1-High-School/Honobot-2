from mirai import *

from HApp import HApp


class KWD(HApp):
    HApp.white = True;
    HApp.whitelist = [
        776324219,
        341475083,
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
    pass
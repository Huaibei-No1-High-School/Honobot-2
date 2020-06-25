import random

from mirai import *

from HApp import HApp


class Whois(HApp):
    def __init__(self):
        self.li = []
        HApp.white = True
        HApp.whitelist = [
            776324219,
            341475083,
        ]
        self.li.append([[Plain(text="谷梦龙")],1919810])
        self.superuser = 992951869

    async def recv(self, app: Mirai, event: GroupMessage):
        if HApp.isblocked(self, event.sender.group.id):
            return
        if event.messageChain.toString() == "/*":
            msg = []
            cnt = 0
            for i in self.li:
                msg.append(Plain(text=str(cnt)+":"))
                msg.extend(i[0])
                msg.append(Plain(text="->from " + str(i[1]) + "\n"))
                cnt = cnt + 1
            await app.sendGroupMessage(event.sender.group, msg)
        if event.messageChain.toString()[0:2] == "/-":
            tstr = event.messageChain.toString()[2:]
            msg = [Plain(text="删除:\n")]
            try:
                index = int(tstr)
                if event.sender.id != self.li[index][1] and event.sender.id != self.superuser:
                    await app.sendGroupMessage(event.sender.group, [Plain(text="Permission Denied!\n删除失败！\n"),Image.fromFileSystem("./sb.gif")])
                else:
                    msg.extend(self.li[index][0])
                    msg.append(Plain(text="\n成功！\n"))
                    msg.append(Image.fromFileSystem("./cg.jpg"))
                    await app.sendGroupMessage(event.sender.group, msg)
            except BaseException:
                pass

        if ("谁是" not in event.messageChain.toString()) and ("是谁" not in event.messageChain.toString()):
            return
        nmsg = []
        nmc = []
        for msg in [i for i in event.messageChain][1:]:
            if type(msg) == Plain:
                tstr = msg.toString()
                twstr = tstr
                tstr = tstr.replace("我","005fga果果zkafc31")
                tsrt = tstr.replace("你","我")
                tstr = tstr.replace("005fga果果zkafc31", "你")
                print(tstr)
                if "谁是" in tstr:
                    nmsg.append(Plain(text=tstr.split("谁是")[0]))
                    nmsg.extend(self.li[random.randint(0,len(self.li)-1)][0])
                    nmsg.append(Plain(text="是"))
                    nmsg.append(Plain(text=tstr.split("谁是")[1]))
                    nmc.append(Plain(text=twstr.replace("谁是","")))
                elif "是谁" in tstr:
                    nmsg.append(Plain(text=tstr.split("是谁")[0]))
                    nmsg.append(Plain(text="是"))
                    nmsg.extend(self.li[random.randint(0, len(self.li) - 1)][0])
                    nmsg.append(Plain(text=tstr.split("是谁")[1]))
                    nmc.append(Plain(text=twstr.replace("是谁","")))
                else:
                    nmsg.append(Plain(text=tstr))
                    nmc.append(Plain(text=twstr))
            else:
                nmsg.append(msg)
                nmc.append(msg)
        
        self.li.append([nmc,event.sender.id])
        await app.sendGroupMessage(event.sender.group,nmsg)


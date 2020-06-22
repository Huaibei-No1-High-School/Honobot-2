from typing import List

from mirai import *

from FD import FD
from HApp import HApp


class FDHolder(HApp):
    FDList: List[FD] = dict()

    def __init__(self):
        HApp.white = True
        HApp.whitelist = [
            341475083,
            776324219,
        ]

    async def recv(self, app: Mirai, event: GroupMessage):
        if HApp.isblocked(self, event.sender.group.id):
            return

        if not event.sender.group.id in self.FDList:
            print("Not")
            self.FDList[event.sender.group.id] = FD()

        await self.FDList[event.sender.group.id].recv(app, event)

    pass

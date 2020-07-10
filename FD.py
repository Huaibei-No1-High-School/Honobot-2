from typing import List

from mirai import *


class FD():
    la: List[MessageChain] = []

    def __init__(self):
        self.la = []

    async def recv(self, app: Mirai, event: GroupMessage):
        self.la.append(event.messageChain)
        if len(self.la) >= 3 and self.la[len(self.la) - 2].toString() == self.la[len(self.la) - 1].toString() and self.la[len(self.la) - 2].toString() == self.la[len(self.la) - 3].toString():
            return

        if len(self.la) >= 2 and self.la[len(self.la) - 2].toString() == self.la[len(self.la) - 1].toString():
            await app.sendGroupMessage(event.sender.group, [i for i in event.messageChain][1:])

        if len(self.la) >= 200:
            self.la.clear()

    pass

from HApp import HApp
from mirai import *
import random

class antirxbot(HApp):
	def __init__(self):
		self.white = True
		self.whitelist = [
			337681195,
			341475083
		]

	async def recv(self, app: Mirai, event: GroupMessage):
		if HApp.isblocked(self, event.sender.group.id):
			return
		if(event.sender.id == 992951869):
			return
		print("ininininininininiinninininininininini")
		str = event.messageChain.toString()
		print(str[0:7])
		if str[0:7] == "/teach " or str[0:7] == "/force ":
			tli = list(event.messageChain)[1:]
			await app.sendGroupMessage(event.sender.group, [
				Plain("/delete " + tli[0].text[7:])
			])

		altern = ["太贵了", "太远了", "不好吃", "不想吃", "人太多"]
		if "恰啥" in str:
			await app.sendGroupMessage(event.sender.group, [
				Plain(altern[random.randint(0, 5)])
			])
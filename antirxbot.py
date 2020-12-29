from HApp import HApp
from mirai import *

class antirxbot(HApp):
	def __init__(self):
		self.white = True
		self.whitelist = [
			#337681195,
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
		if str[0:7] == "/teach ":
			tli = list(event.messageChain)[1:]
			await app.sendGroupMessage(event.sender.group, [
				Plain("/delete " + tli[0].text[7:])
			])
		elif str[0:8] == "/delete ":
			tli = list(event.messageChain)[1:]
			await app.sendGroupMessage(event.sender.group, [
				Plain("/teach " + tli[0].text[8:])
			])
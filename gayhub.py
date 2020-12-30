import httpx as requests
from mirai import *


class Gay(object):
    def __init__(self):
        print("Plugin (gayhub) is Loaded")
        self.__username = ''
        self.__gayURL = 'https://api.github.com/users/{}/repos'.format(self.__username)
        self.__result = ''
        self.__msg = ''


    def __makeData(self):
        try:
            self.__result = requests.get(url=self.__gayURL, timeout=5).json()
            result = self.__result
            try:
                a = 0
                for i in result:
                    description = str(i['description'])
                    name = str(i['name'])
                    if a > 4:
                        break
                    if description is None:
                        continue

                    if len(description) > 20:
                        description = description[0:21] + '...'

                    if len(name) > 20:
                        name = name[0:21] + '...'

                    self.__msg += "仓库名称: " + str(name) + ' | ' + "STAR: " + str(
                        i['stargazers_count']) + " | 仓库描述: " + str(description) + '\n'
                    a += 1
            except TypeError as ee:
                self.__msg = str('Not Found User!')

        except TimeoutError as e:
            self.__msg = str(e)

    async def recv(self, app: Mirai, event: GroupMessage):
        resp = event.messageChain.to_string()
        if 'github' in resp:
            self.__username = resp.strip().replace('github', '')
        self.__gayURL = 'https://api.github.com/users/{}/repos'.format(self.__username)
        self.__makeData()
        await app.sendGroupMessage(event.sender.group, [
            Plain(self.__msg + '...')
        ])


if __name__ == '__main__':
    print(Gay('mzdluo123').getMsg())

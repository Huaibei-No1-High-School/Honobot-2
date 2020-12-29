from HApp import HApp
import requests, json, re, datetime, time
import base64
from mirai import *
from qqmusic import *

class Sing(HApp):
    locked = False
    stopsignal = False
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
        if str[0:4] != "果果唱歌":
            return
        if Sing.locked == True:
            await app.sendGroupMessage(event.sender.group, [
                Plain("还没唱完来 等我唱完")
            ])
            return
        Sing.locked = True
        name = str[4:]
        _,mid = qqMusicMain(name)
        print(mid)
        await Sing.SingSong(mid[0],event,app)

    @staticmethod
    async def SingSong(songmid,event: GroupMessage,app: Mirai):
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'origin': 'https://y.qq.com',
            'referer': 'https://y.qq.com/portal/player.html',
        }
        sess = requests.Session()
        res = sess.get(headers=headers,
                       # data=data,
                       url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?songmid=' + songmid + '&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')

        lrc = base64.b64decode(res.json()['lyric']).decode('utf-8')
        print(lrc)
        lrc = lrc.splitlines()
        tlrc = []
        times = [datetime.timedelta(0, 0, 0)]
        for i in lrc:
            mres = re.search(r'\[[0-9]*:[0-9]*\.[0-9]*\]', i)
            if mres != None:
                # print(mres.group())
                tlrc.append(i)
                strtime = mres.group().replace('[', '').replace(']', '')
                tmin = int(strtime.split(':')[0])
                tsec = int(strtime.split(':')[1].split('.')[0])
                tmsec = int(strtime.split('.')[1])
                print(tmin, tsec, tmsec)
                ntime = datetime.timedelta(0, tmin * 60 + tsec, tmsec * 1000)
                times.append(ntime)

        print(tlrc)
        for i in range(0, len(times) - 1):
            span = times[i + 1] - times[i]
            print(times[i + 1], times[i])
            print(span.seconds + span.microseconds / 1000000)
            time.sleep(span.seconds + span.microseconds / 1000000)
            print(tlrc[i].split(']')[1])
            if tlrc[i].split(']')[1] == "":
                continue
            if Sing.stopsignal == True:
                Sing.stopsignal = False
                break
            await app.sendGroupMessage(event.sender.group, [
                Plain(tlrc[i].split(']')[1])
            ])
        Sing.locked = False

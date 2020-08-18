# name: qqMusic.py
__author__ = "xush2014@hotmail.com"
# -*- coding: utf-8 -*-
import requests, json
from lxml import etree
search = ''
musicUrl = 'https://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid='
def getSongURL(url, songName, singer):
	header2 = {
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
		'referer': 'https://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid=003aVkV81dHjYc',
		'cookie': 'yqq_stat = 0;pgv_pvi = 838125568;pgv_si = s2524780544;pgv_info = ssid = s1399264704;ts_last = y.qq.com /;ts_refer = ADTAGmyqq;ts_uid = 5369977090;pgv_pvid = 3517769994;userAction = 1',

	}
	result = requests.get(url, headers=header2).text
	result = etree.HTML(result)
	result = result.xpath('//*[@id="h5audio_media"]/@src')
	try:
		return singer + '  ' + songName + ' ' + result[0]
	except:
		return ''


def qqMusicMain(search):
	# search = '鎭嬬埍瑁佸垽'
	songIDUrl = 'https://c.y.qq.com/soso/fcgi-bin/search_for_qq_cp?_=1592730823167&g_tk=204993107&uin=&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&g_tk_new_20200303=204993107&w=' + search + '&zhidaqu=1&catZhida=1&t=0&flag=1&ie=utf-8&sem=1&aggr=0&perpage=20&n=20&p=1&remoteplace=txt.mqq.all'
	header = {
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
		'origin': 'https://i.y.qq.com',
		'referer': 'https://i.y.qq.com/n2/m/index.html',
	}
	result = requests.get(url=songIDUrl, headers=header).json()['data']['song']['list']
	songstring = ''
	string = ''
	# print(type(result))
	num = 1
	#print(result)
	mid = []
	for item in result:
		# print(item['songname'] + '\t' + musicUrl + item['songmid'])
		songstring = musicUrl + item['songmid']
		print(item['songmid'])
		mid.append(item['songmid'])
		singer_all = item['singer']
		for i in singer_all:
			singer = i['name']
			break
		string = string + getSongURL(songstring, songName=item['songname'], singer=singer) + '\n'
		num = num + 1
		if num > 5:
			break
	# print(string)
	return string,mid

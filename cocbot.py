#属性投掷

import requests
import urllib
import re
import bs4
import random
import logging

req=requests.Session()
req.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


def cocbot(item):
    #sender = item.fetchPreviousSiblings()[0]
    #sender = sender.text
    #item = item.text

    command = ''
    reply = ''

    sender = '没有'
    pattern = re.compile(r'#coc\s?([0-9]*)')
    match = pattern.match(item)
    print(match.groups())
    coms = [(3,6,0),(3,6,0),(3,6,0),(3,6,0),(3,6,0),(2,6,6),(2,6,6),(3,6,3),(1,10,0)]
    prop = ['力量 ',' 体质 ',' 意志 ',' 敏捷 ',' 外貌 ' ,' 智力 ',' 体型 ',' 教育 ',' 资产 ']
    if not match:
        reply = '命令格式错误' 
    else:
        x = (match.group(1) == '' and 1) or int(match.group(1))
        if (x < 1 or x > 10):
            reply = '参数错误'
        else:
            for k in range(x):
                for i in range(9):
                    (x,y,z) = coms[i]
                    reply += prop[i]
                    val = z
                    for j in range(x):
                        val += random.randint(1,y)
                    reply += str(val)
                reply += '\\n'
            command = '1'

    if command != '':
        reply = '* ' + sender + ' 投掷coc 6版 属性 :\\n' + reply; 
    
    #send(reply)
    #print('收到命令：',item,'已回复:',reply)
    
    print(reply)

cocbot('#coc5')
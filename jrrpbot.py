#jrrp

import requests
import urllib
import re
import bs4
import random
import logging

req=requests.Session()
req.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


def jrrpbot(item):
    #sender = item.fetchPreviousSiblings()[0]
    #sender = sender.text
    #item = item.text

    command = ''
    reply = ''

    sender = '没有'
    pattern = re.compile(r'#jrrp')
    match = pattern.match(item)
    if not match:
        reply = '命令格式错误' 
    else:
        x = random.randint(1,100)
        reply = str(x) + '% !\\n' + '|' * x
        command = '1'

    if command != '':
        reply = '* ' + sender + ' 今天的运势指数是 ' + reply; 
    
    #send(reply)
    #print('收到命令：',item,'已回复:',reply)
    
    print(reply)

jrrpbot('#jrrp')
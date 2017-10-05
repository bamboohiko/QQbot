#基础的骰娘机器人

import requests
import urllib
import re
import bs4
import random
import logging

req=requests.Session()
req.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


def dicebot(item):
    #sender = item.fetchPreviousSiblings()[0]
    #text = item.text.replace('#r ','',1)
    sender = '没有'
    
    text = item.replace('#r ','',1)
    coms = text.split("+")
    reply = ""
    comsum = 0
    for com in coms:
        com = ' ' + com
        if com.split('d')[0].isspace():
            x = 1
        else:
            x = int(com.split('d')[0])
        y = int(com.split('d')[1])
        print(x,y)
        reply += ' ('
        for i in range(x):
            j = random.randint(1,y)
            comsum += j
            reply += str(j) + ','
        reply = reply[:-1] + ') +'
    reply = reply[:-2] + ' = ' + str(comsum)
    reply = '* ' + sender + ' 投掷 :' + text + ' =' + reply; 
    
    #send(reply)
    print(reply)
    
    print('收到命令：',text,'已回复:',reply)

dicebot('#r 2d100+d100')
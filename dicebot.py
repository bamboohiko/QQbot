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
    #sender = sender.text
    #item = item.text
    command = ''
    reply = ''

    sender = '没有'
    pattern = re.compile(r'#r\s*(([0-9]*)d([0-9]*)\+?)+\s*(?P<hint>\S*)')
    match = pattern.match(item)
    if not match:
        reply = '命令格式错误'    
    else:
        hint = match.group(4);
        pattern = re.compile(r'((?P<x>[0-9]*)d(?P<y>[0-9]*)\+?)')
        coms = pattern.findall(item[:match.start(4)])

        comsum = 0
        
        for com in coms:
            print(com)
            x = (com[1] == '' and 1) or int(com[1])
            y = (com[2] == '' and 100) or int(com[2])
            if (x < 1 or x > 100 or y < 1 or y > 10000):
                command = ''
                reply = '参数错误'
                break
            command += str(x) + 'd' + str(y) + '+'
            reply += ' ('
            for i in range(x):
                j = random.randint(1,y)
                comsum += j
                reply += str(j) + ','
            reply = reply[:-1] + ') +'
    
    if command != '':
        reply = reply[:-2] + ' = ' + str(comsum)
        reply = '* ' + sender + ' 投掷 ' + hint + ': ' + command[:-1] + ' =' + reply; 
    
    #send(reply)
    #print('收到命令：',item,'已回复:',reply)
    
    print(reply)

dicebot('#rabdfaf')
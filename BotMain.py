#基于chrome引擎的qq骰子机器人，只适用于单个对话

#骰子主程序

from selenium import webdriver
from datetime import datetime
import time
import bs4
import re
import random
import logging

#浏览器引擎
obj = webdriver.Chrome('D:\code\chromedriver_win32\chromedriver.exe')

#命令符
target = '#'

#以下是命令调用函数

#普通的骰子
def dicebot(item):
    print(dicebot)
    sender = item.fetchPreviousSiblings()[0]
    text = item.text.replace('#r ','',1)
    #sender = '没有'
    #text = item.replace('#r ','',1)
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
        reply += ' ('
        for i in range(x):
            j = random.randint(1,y)
            comsum += j
            reply += str(j) + ','
        reply = reply[:-1] + ') +'
    reply = reply[:-2] + ' = ' + str(comsum)
    reply = '* ' + sender.text + ' 投掷 :' + text + ' =' + reply; 
    send(reply)
    #print(reply)
    print('收到命令：',text,'已回复:',reply)

#命令列表,函数放在包中
targetDic = {"r":dicebot}
#"jrrp":fatebot,"coc":cocbot

#发送信息
def send(text):
    global obj
    obj.execute_script('b=document.getElementById("chat_textarea");b.value="'+text+'"')
    obj.execute_script('c=document.getElementById("send_chat_btn");c.click()')

#读取对话列表
def readChat():
    global obj
    bs = bs4.BeautifulSoup(obj.page_source,'lxml')
    lis = bs.findAll('p',{'class':re.compile('chat_content |chat_nick')})
    return lis

#读取对话列表并提取有命令符的消息
def readTargetChat():
    global target
    messageList = []
    lis = readChat()
    for message in lis:
        if message.text.find(target) == 0:
            messageList.append(message)
    return messageList

#控制回复次数和回复间隔，未使用
def replydecorater(func):
    def funcx(item):
        global maxreply
        func(item)
        if maxreply<0:
            print('达到回复次数上限')
            return False
        else:
            maxreply=maxreply-1
            time.sleep(0.1)
    return funcx

#在对话中检索未处理信息并进行处理
def monitor():
    print('monitor')
    global target
    global targetDic
    global timeCnt
    tit = obj.find_element_by_id("panelTitle-5")
    print('%s 群名称: %s' % (datetime.now().strftime('%H:%M:%S'),tit.text))
    send('bot已启动')
    oldMessageList = readTargetChat()
    while True:
        newTit = obj.find_element_by_id("panelTitle-5")
        if (newTit != tit):
            print('%s %s监听结束' % (datetime.now().strftime('%H:%M:%S'),tit.text))
            break
        newMessageList = readTargetChat()
        #对比新旧信息序列
        if len(oldMessageList) == len(newMessageList):
            print(datetime.now().strftime('%H:%M:%S'))
        elif len(oldMessageList) < len(newMessageList):
            dif = len(newMessageList) - len(oldMessageList)
            for i in range(int(dif)):
                item = newMessageList[-i-1]
                print('%s NewMessage:%s' % (datetime.now().strftime('%H:%M:%S'),item.text))
                try:
                    check = 0
                    #检索命令并进行调用
                    for j in targetDic:
                        if item.text.find(j) == 1:
                            check = 1
                            repMeth = targetDic[j]
                            repMeth(item)
                            break
                    if check == 0:
                        #提示信息，尚未添加
                        replyHintMessage(item)
                except Exception as e:
                    send('因为奇怪的原因坏掉了QAQ:' + str(e))
                    #print('因为奇怪的原因坏掉了QAQ:' + str(e))
        else:
            print('%s %s监听结束' % (datetime.now().strftime('%H:%M:%S'),tit.text))
            break
        time.sleep(1)
        oldMessageList = newMessageList

#选择对话
def init():
    print('init')
    global obj
    global interval
    interval = input("选择会话后按回车键继续：")
    print(interval)
    #a = obj.find_elements_by_tag_name('li')
    #b = readChat()
    #print('TalkListLength:',len(a),'MessageListLength:',len(b));

#def __init__(self):
#global obj

obj.maximize_window()
obj.get('http://w.qq.com')
while True:
    #try:
        init()
        time.sleep(2)
        monitor()
    #except Exception as e:
    #    print('%s 错误: %s' % (datetime.now().strftime('%H:%M:%S'),str(e)))
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file         mouse_weixin.py
# @author       ymm
# @brief        微信界面指定位置的自动单击
# @date         2016-10-13  
# @History
# 1. 2016-10-13  author ymm    初步完成
# 2. 2016-10-17  author ymm    添加指定时间自动运行指定次数
# 3. 2016-10-18  author ymm    添加显示桌面+运行微信界面，并使用微信正常窗口

from pymouse import PyMouse
from pykeyboard import PyKeyboard

import time

m = PyMouse()
k = PyKeyboard()

#display desktop
x_dim, y_dim = m.screen_size()
m.click(x_dim, y_dim, 1)

time.sleep(1)

#weixin
#Screen_location x:346 y:789
x = 346
y = 789
#double click
m.click(x, y, 1, n=2)

time.sleep(5)

#x_dim, y_dim = m.screen_size()
#m.click(x_dim/2, y_dim/2, 1)
#k.type_string('Hello, World!')

a = "2016-10-17 23:59:59"
#a = "2016-10-13 15:02:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print timeStamp

while 1:
    now = int(time.time())
    if now >= timeStamp:
        print "come on"
        break
    else:
        print now
    time.sleep(1)


#x = 1341
#y = 836
x = 1092
y = 728
i = 0
while i < 5000:
    #print i
    m.click(x, y)
    i = i+1

now = int(time.time())
print now
#exit(0)

#Screen_location x:1341 y:836
print "sleep 1"
time.sleep(1)
m.click(x, y)

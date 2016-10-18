#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @file         mouse_weixin.py
# @author       ymm
# @brief        微信界面指定位置的自动单击
# @date         2016-10-13  
# @History
# 1. 2016-10-13  author ymm    初步完成

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
m.click(x_dim/2, y_dim/2, 1)
k.type_string('Hello, World!')

#Screen_location x:1341 y:836
x = 1341
y = 836
m.click(x, y)

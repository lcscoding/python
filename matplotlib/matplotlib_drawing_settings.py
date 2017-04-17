#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/4/17 11:34
# @Author : sixu
# @Site : https://github.com/sixu2/python.git
# @File : matplotlib_drawing_settings.py
# @Software: PyCharm Community Edition

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体   加入这两行可以显示中文

fig=plt.figure(figsize = (16,12))
##在matplotlib下，一个Figure对象可以包含多个子图（Axes）：
##ax1 = fig.add_subplot(2, 2, 1)  ##分成2x2，占用第一个，即第一行第一列的子图
##ax2 = fig.add_subplot(2, 2, 2)  ##分成2x2，占用第二个，即第一行第二列的子图
##ax3 = fig.add_subplot(2, 1, 2)  ##分成2x1，占用第二个，即第二行
font_size=30

plt.plot(range(5), range(5), 'bx--', label = 'legend1', markersize = 13, linewidth=3)
plt.plot(range(5), range(5, 10), label = u'图例2', color = 'b', marker = '*', markersize = 13, linestyle = '-.', linewidth = 5)
plt.plot(range(5), range(10, 15), label = r'$\mu=0.25$', c = 'r', linewidth=6)
plt.plot(range(5), np.linspace(15, 20, 5), 'c-', range(5), np.linspace(20, 25, 5, endpoint=True), 'ro', linewidth=2,markersize=8, label = 'legend5')

plt.xticks((0,1,2,3,4),('VL','L','M','H','VH'), fontsize = font_size)  ##X轴刻度信息
plt.xlim(-1,5)  ##X轴的范围
plt.ylim(-5,30)
plt.xlabel("xlabel", fontsize = font_size)  ##X轴的名称
plt.ylabel("ylabel", fontsize = font_size)
plt.title("plt_title", fontsize = font_size)  ##子图的标题
plt.text(3, 16, 'you can text here', size = 30)  ##图片上书写文字

plt.grid(True)  ##网格
plt.legend(loc = 'upper left', fontsize = font_size, ncol = 2)  ##具体的位置设定可以参考 help(plt.legend)  设置图例
##plt.legend([str(x) for x in range(5)], loc = 'upper left', fontsize = 20, ncol = 2)  ##更改图例的名称
fig.suptitle('figure title', fontsize = font_size)
plt.show()
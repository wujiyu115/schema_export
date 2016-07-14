# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 19:55:13
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 19:28:39


# import Tkinter
# top = Tkinter.Tk()
# # 进入消息循环
# top.mainloop()


import csv
with open('eggs.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

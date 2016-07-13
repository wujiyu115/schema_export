# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 19:58:14
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 20:09:17

class BaseExport(object):
	headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra','Comment']

	"""docstring for BaseExport"""
	def __init__(self):
		super(BaseExport).__init__()

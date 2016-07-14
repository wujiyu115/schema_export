# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 19:58:14
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 11:12:14

class BaseExport(object):
	# headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra','Comment']
	headings = [u'名称', u'数据类型', u'允许空值', u'主键', u'默认值', u'额外信息',u'说明']

	"""docstring for BaseExport"""
	def __init__(self):
		super(BaseExport).__init__()

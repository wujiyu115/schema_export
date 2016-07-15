# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-14 14:22:39
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-15 09:57:27

class BaseFormat(object):

	"""docstring for BaseFormat"""
	def __init__(self,filename,headings):
		self.filename = filename
		self.headings = headings
		self.outname = self.concat_name(self.filename)


	def concat_name(self,filename):
		return   "%s.%s"%( filename ,self.suffix)

	def write(self, data):
		self.handle_data(data)
		pass

	def handle_data(self,data):
		for table,table_info in data.iteritems():
			if table_info.columns:
				table_info.columns.insert(0,self.headings)

	def save(self):
		pass
# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-14 14:22:39
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 15:20:42

class BaseFormat(object):

	"""docstring for BaseFormat"""
	def __init__(self,filename):
		self.filename = filename
		self.outname = self.concat_name(self.filename)


	def concat_name(self,filename):
		return   "%s.%s"%( filename ,self.suffix)

	def write(self,  headings, data):
		pass

	def save(self):
		pass
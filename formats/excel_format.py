#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2013-12-23

@author: mingdong.li

excel option
xlrd : reading data and formatting information from Excel files
xlwt : writing data and formatting information to Excel files
xlutils : both xlrd and xlwt
'''
from xlrd import open_workbook
from xlwt import Workbook,easyxf
from xlutils.copy import copy
from base_format import BaseFormat


class ExcelFormat(BaseFormat):

	def __init__(self, filename,headings):
		self.suffix = "xls" #后缀
		super(ExcelFormat, self).__init__(filename,headings)

		self.book = Workbook(encoding='utf-8')


	def addSheet(self, sheet_name):
		return self.book.add_sheet(sheet_name)

	def write(self, sheet,  data):
		super(ExcelFormat, self).write(data)
		heading_xf = easyxf('font: bold on; align: wrap off, vert centre, horiz center')
		title_xf = easyxf('font: bold on, color blue; align: wrap on, vert bottom, horiz center; border: left thin, right thin, top thin, bottom thin')
		data_xfs = easyxf('font: bold off; align: wrap off, vert centre, horiz left; border: left thin, right thin, top thin, bottom thin')

		rowx=0
		# heading_xf = easyxf()
		# title_xf = easyxf()
		# data_xfs =easyxf()

		maxCol = len(self.headings)-1
		# for colx, value in enumerate(self.headings):
		# 	sheet.write(rowx, colx, value, heading_xf)
		# 	maxCol = colx

		sheet.set_panes_frozen(True) # frozen headings instead of split panes
		sheet.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
		sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there

		for table,table_info in data.iteritems():
			rowx += 1
			sheet.write_merge(rowx, rowx, 0, maxCol, table, title_xf)
			for d_row,columns in enumerate(table_info.columns or [] ):
				rowx += 1
				for colx, value in enumerate(columns ):
					if d_row == 0 :
						sheet.write(rowx, colx, value, heading_xf)
					else:
						sheet.write(rowx, colx, value, data_xfs)
			rowx += 1

		return rowx

	def save(self):
		self.book.save(self.outname)



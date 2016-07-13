# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-12 18:56:20
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 15:43:04


from formats.excel_util import ExcelUtil
from db.db_info import MySqlDbData

c = MySqlDbData()

def export_xls(xls_name):
	entu = ExcelUtil(xls_name)
	headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
	sheets = c.getDB() # 每个数据库作为一个sheet表格
	datas = {}
	for sheet in sheets:
		datas =c.getDatas(sheet)
		sheet = entu.addSheet(sheet)
		entu.write(sheet, headings, datas)
	entu.save()




# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-12 18:56:20
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 11:11:23


from formats.excel_util import ExcelUtil
from db.db_info import MySqlDbData
from export_base import BaseExport

c = MySqlDbData()

def export_xls(xls_name,db):
	entu = ExcelUtil(xls_name)
	sheets = c.getDB() # 每个数据库作为一个sheet表格
	sheets =[db]
	datas = {}
	for sheet in sheets:
		datas =c.getDatas(sheet)
		sheet = entu.addSheet(sheet)
		entu.write(sheet, BaseExport.headings, datas)
	entu.save()




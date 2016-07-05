#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: export_excel.py
Author: tdoly
Description: export excel
'''
from excel_util import ExcelNoTemplateUtils
from client import DictClient

class DbData(object):
	def __init__(self, dbname="localhost"):
		self.client = DictClient(dbname)

	def getDB(self):
		result = [database[0] for database in self.client.execute("show databases")]
		if result:
			for ignore in ["information_schema", "mysql", "performance_schema"]:
				result.remove(ignore)
		return result

	def getTable(self, database):
		if database:
			self.client.execute("use %s" % database)
			return [tables[0] for tables in self.client.execute("show tables")]

	def getColumn(self, table):
		if table:
			return [list(column) for column in self.client.execute("desc %s" % table)]

	def getDatas(self, sheet):
		datas = {}
		if sheet:
			tables = self.getTable(sheet)
			if tables:
				for table in tables:
					columns = self.getColumn(table)
					datas[table] = columns
		return datas

c = DbData()

def export():
	entu = ExcelNoTemplateUtils('dbdict.xls')
	heading_xf = entu.ezxf('font: bold on; align: wrap off, vert centre, horiz center')
	title_xf = entu.ezxf('font: bold on, color blue; align: wrap on, vert bottom, horiz center; border: left thin, right thin, top thin, bottom thin')
	data_xfs = entu.ezxf('font: bold off; align: wrap off, vert centre, horiz left; border: left thin, right thin, top thin, bottom thin')

	headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
	sheets = c.getDB() # 每个数据库作为一个sheet表格
	datas = {}
	for sheet in sheets:
		datas =c.getDatas(sheet)
		sheet = entu.addSheet(sheet)
		entu.write(sheet, headings, datas, heading_xf, title_xf, data_xfs)

	entu.save()

if __name__ == '__main__':
	print "==export start=="
	export()
	print "==End=="

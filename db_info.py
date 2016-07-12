# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-12 18:56:20
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-12 20:35:08
from client import DictClient

class DbData(object):
	def __init__(self, dbname="localhost"):
		self.client = DictClient(dbname)


	##
	## @brief      得到所有的库名
	##
	## @param      self  The object
	##
	## @return     The db.
	##
	def getDB(self):
		result = [database[0] for database in self.client.execute("show databases")]
		if result:
			for ignore in ["information_schema", "mysql", "performance_schema"]:
				result.remove(ignore)
		return result


	##
	## @brief      Gets the table.
	##
	## @param      self      The object
	## @param      database  The database
	##
	## @return     The table.
	##
	def getTable(self, database):
		if database:
			self.client.execute("use %s" % database)
			return [tables[0] for tables in self.client.execute("show tables")]


	##
	## @brief      Gets the column.
	##
	## @param      self   The object
	## @param      table  The table
	##
	## @return     The column.
	##
	def getColumn(self, table):
		if table:
			return [list(column) for column in self.client.execute("desc %s" % table)]


	##
	## @brief      Gets the datas.
	##
	## @param      self   The object
	## @param      sheet  The sheet
	##
	## @return     The datas.
	##
	def getDatas(self, sheet):
		datas = {}
		if sheet:
			tables = self.getTable(sheet)
			if tables:
				for table in tables:
					columns = self.getColumn(table)
					datas[table] = columns
		return datas


class MySqlDbData(DbData):
	"""docstring for MySqlDbData"""
	def __init__(self):
		super(MySqlDbData, self).__init__()

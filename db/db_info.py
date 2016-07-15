# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-12 18:56:20
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-15 09:34:44
from db_client import mymysqldb
from configutil import ConfigUtil

class  DbBean(object):
	def __init__(self):
		self.dbname = None
		self.tables =  {}

class  TableBean(object):
	def __init__(self,table,table_desc,columns):
		self.table = table #表名
		self.table_desc = table_desc #表注释
		self.columns =  columns #表字段信息

class ColumnBean(object):
	def __init__(self):
		self.column_name = None

class DbData(object):
	def __init__(self):
		database_info = ConfigUtil.instance().get_mysql_database()
		self.client = mymysqldb(*database_info)
		self.ignore_db = ["information_schema", "mysql", "performance_schema"]


	## @brief      得到所有的库名
	## @param      self  The object
	## @return     The db.
	def getDB(self):
		result = [database[0] for database in self.client.execute("show databases")]
		if result:
			for ignore in self.ignore_db:
				result.remove(ignore)
		return result


	## @brief      根据数据库得到所有表
	## @param      self      The object
	## @param      database  The database
	## @return     The tables.
	def getTable(self, database):
		if database:
			self.client.execute("use %s" % database)
			return [tables[0] for tables in self.client.execute("show tables")]
		return None

	## @brief      得到所有的列
	## @param      self   The object
	## @param      table  The table
	## @return     The column.
	# def getColumn(self, table):
	# 	if table:
	# 		return [list(column) for column in self.client.execute("desc %s" % table)]

	## @brief      得到所有的列
	## @param      self   The object
	## @param      table  The table
	## @return     The column.
	def getColumn(self, table):
		if table:
			columns =  [list(column) for column in self.client.execute("SHOW FULL FIELDS FROM %s" % table)]
			for column in columns:
				column.pop(7) #privileges
				column.pop(2) #collation
			return columns
		return None


	## @brief      得到表信息,最后一列是注释
	## @param      self   The object
	## @return     The tableinfo.
	def getTableInfo(self):
		tableinfo_result = {}
		tabelinfos =  [list(tabelinfo) for tabelinfo in self.client.execute("SHOW TABLE STATUS ")]
		for tabelinfo in tabelinfos:
			tableinfo_result[tabelinfo[0]] = tabelinfo[-1]
		return tableinfo_result

	## @brief      得到全部数据
	## @param      self   The object
	## @param      dbname  The dbname
	## @return     The datas.
	'''
	{
	'two':
		{
			"table_desc":"table_desc",
			"table":"table",
			"columns":
			 [
				 ['ID', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'one ID'],
				 ['NAME', 'varchar(128)', 'NO', '', 'NULL', '', ''],
				 ['DATE', 'datetime', 'NO', '', 'NULL', '', '']],
			 ]
		}
	}
	'''
	def getDatas(self, dbname):
		datas = {}
		tables = self.getTable(dbname)
		tablesinfos = self.getTableInfo()
		for table in tables or []:
			columns = self.getColumn(table)
			for column in tablesinfos:
				table_desc = tablesinfos[table]
				tb = TableBean(table,table_desc,columns)
			datas[table] = tb
		return datas

	## @brief    关闭数据库连接
	## @param      self  The object
	## @return     { description_of_the_return_value }
	def close(self):
		if self.client:
			self.client.close()


	def get_db_name(self):
		return self.client.get_db_name()

class MySqlDbData(DbData):
	"""docstring for MySqlDbData"""
	def __init__(self):
		super(MySqlDbData, self).__init__()

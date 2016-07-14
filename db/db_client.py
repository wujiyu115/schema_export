#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb
import traceback
from util.mylog import error

class mymysqldb(object):

	def __init__(self, host, user, passwd, db, port):
		self.host = str(host)
		self.user = str(user)
		self.passwd = str(passwd)
		self.db = str(db)
		self.port = int(port)
		self.charset = "utf8"
		self.conn = None
		# print(self.host,self.user,self.passwd,self.db,self.port)

	def build_conn(self):
		ret =None
		try:
			ret = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port,connect_timeout=20,charset=self.charset)
		except Exception, e:
			error(traceback.format_exc())
		return ret

	def get_conn(self):
		if self.conn == None:
			self.conn = self.build_conn()
		else:
			try:
				# fix reconnect
				self.conn.ping()
			except Exception, e:
				self.close_conn()
				# print("error",e)
				error(traceback.format_exc())
				self.conn = self.build_conn()
		return self.conn

	def close_conn(self):
		if self.conn:
			self.conn.close()
			self.conn = None

	def excute_sql(self, sql):
		conn = self.get_conn()
		if conn == None:
			return 0

		try:
			conn.autocommit(True)
			cur = conn.cursor()
			result = cur.execute(sql)
			cur.close()
			return result
		except:
			error(traceback.format_exc())
			self.close_conn()
			return 0

		return 0

	# def execute(self, sql):

	# 	conn = self.get_conn()
	# 	if conn == None:
	# 		return None

	# 	try:
	# 		cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
	# 		cur.execute(sql)
	# 		result = cur.fetchall()
	# 		cur.close()
	# 		return result
	# 	except:
	# 		error(traceback.format_exc())
	# 		self.close_conn()
	# 		return None

	# 	return None


	def escape_string(self, string):
		result = ''

		for c in string:
			escape = None
			char_num = ord(c)

			if char_num == 0:
				escape = '0'
			elif char_num == ord('\''):
				escape = '\''
			elif char_num == ord('"'):
				escape = '"'
			elif char_num == ord('\b'):
				escape = 'b'
			elif char_num == ord('\n'):
				escape = 'n'
			elif char_num == ord('\r'):
				escape = 'r'
			elif char_num == ord('\t'):
				escape = 't'
			elif char_num == 26:
				escape = 'Z'
			elif char_num == ord('\\'):
				escape = '\\'
			elif char_num == ord('%'):
				escape = '%'

			if escape:
				result = result + '\\' + escape
			else:
				result = result + c

		return result

	def close(self):
		if self.conn:
			self.conn.close()

	def execute(self, query, args=None):
		conn = self.get_conn()
		cur =conn.cursor()
		cur.execute(query, args)
		rows = cur.fetchall()
		cur.close()
		return rows

	def get_db_name(self):
		return self.db
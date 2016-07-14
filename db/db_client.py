#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

"""
the arguments use to create a connetcion to the database.

	"host": host to connect
	"user": user to connect as
	"passwd": password to user
	"db": database to use
	"port": TCP/IP port to connect to, default port is 3306
	"charset": # If supplied, the connection character set will be changed to this character set
	"use_unicode": If True, text-like columns are returned as unicode objects using the connection's character set.Otherwise, text-like columns are returned as strings.
	"ignore_db": set the name of database and you don't want to generate the database dictionary
"""


class DictClient(object):

	"""docstring for Client"""

	def __init__(self):
		self.con = DictClient.conn(self)


	def conn(self):
		settings = {
			"host": "10.105.60.80",
			# "host": "127.0.0.1",
			"user": "root",
			"passwd": "12345678",
			# "passwd": "root",
			"db": "mysql",
			"port": 3306,
			"charset": "utf8",
			"use_unicode": False,
		}

		host = settings.get("host")
		user = settings.get("user")
		passwd = settings.get("passwd")
		db = settings.get("db")
		port = settings.get("port")
		charset = settings.get("charset")
		use_unicode = settings.get("use_unicode")

		conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset, use_unicode=use_unicode)

		return conn

	def cursor(self):
		return self.con.cursor()

	def execute(self, query, args=None):
		cur = DictClient.cursor(self)
		cur.execute(query, args)
		rows = cur.fetchall()
		cur.close()
		return rows

	def close(self):
		if self.con:
			self.con.close()

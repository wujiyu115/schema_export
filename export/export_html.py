# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 20:41:32
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 10:04:55

from formats.html_util import render_template
from db.db_info import MySqlDbData
from export_base import BaseExport

c = MySqlDbData()

def export_html(filename,db):
	recordset =c.getDatas(db)
	context = {
		'dbname': db,
		'recordset': recordset,
		'headings':BaseExport.headings
	}
	with open(filename, 'w') as f:
		html = render_template('teamplate.html', context)
		f.write(html)


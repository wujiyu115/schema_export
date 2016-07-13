# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 20:41:32
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 20:44:28

from formats.html_util import render_template
from db.db_info import MySqlDbData
from export_base import BaseExport

c = MySqlDbData()

def export_html(filename,db):
	doc = PdfUtil(filename)
	recordset =c.getDatas(db)
	doc.write(BaseExport.headings,recordset)
	doc.save()

def create_index_html():
	fname = "output.html"
	urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
	context = {
		'urls': urls
	}
	#
	with open(fname, 'w') as f:
		html = render_template('template.html', context)
		f.write(html)

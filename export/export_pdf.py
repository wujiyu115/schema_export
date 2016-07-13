# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:22:52
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 15:43:15

from formats.pdf_util import PdfUtil
from db.db_info import MySqlDbData


c = MySqlDbData()

def export_pdf(filename):
	doc = PdfUtil(filename)
	headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
	sheet="bee_char"
	recordset =c.getDatas(sheet)
	c.close()
	doc.write(headings,recordset)
	doc.save()
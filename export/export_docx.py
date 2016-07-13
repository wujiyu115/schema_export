# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:22:52
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 15:44:08

from formats.docx_util import DocUtil
from db.db_info import MySqlDbData


c = MySqlDbData()

def export_doc(filename):
	doc = DocUtil(filename)
	headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
	sheet="bee_char"
	recordset =c.getDatas(sheet)
	c.close()
	doc.write(headings,recordset)
	doc.save()
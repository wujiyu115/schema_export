# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:22:52
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 20:13:56

from formats.docx_util import DocUtil
from db.db_info import MySqlDbData
from export_base import BaseExport

c = MySqlDbData()

def export_doc(filename,db):
	doc = DocUtil(filename)
	recordset =c.getDatas(db)
	c.close()
	doc.write(BaseExport.headings,recordset)
	doc.save()
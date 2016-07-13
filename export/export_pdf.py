# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:22:52
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 20:42:21

from formats.pdf_util import PdfUtil
from db.db_info import MySqlDbData
from export_base import BaseExport

c = MySqlDbData()

def export_pdf(filename,db):
	doc = PdfUtil(filename)
	recordset =c.getDatas(db)
	doc.write(BaseExport.headings,recordset)
	doc.save()
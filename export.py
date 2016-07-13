# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:12:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 20:43:59

from export.export_excel import export_xls
from export.export_docx import export_doc
from export.export_pdf import export_pdf
from export.export_html import export_html,create_index_html

if __name__ == '__main__':
	print "==export start=="
	# export_xls("database.xls","bee_char")
	# export_doc("database.docx","bee_char")
	# export_pdf("database.pdf","xyqhook")
	create_index_html()
	print "==End=="
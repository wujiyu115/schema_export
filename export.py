# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:12:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 16:39:33

from export.export_excel import export_xls
from export.export_docx import export_doc
from export.export_pdf import export_pdf

if __name__ == '__main__':
	print "==export start=="
	export_xls("database.xls")
	# export_doc("database.docx")
	# export_pdf("database.pdf")
	print "==End=="
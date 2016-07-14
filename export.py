# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:12:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 11:23:15

from export.export_excel import export_xls
from export.export_docx import export_doc
from export.export_pdf import export_pdf
from export.export_html import export_html
from util.mylog import install_log,info,debug

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	install_log()
	info( "==export start==")
	export_xls("database.xls","bee_char")
	# export_doc("database.docx","bee_char")
	# export_pdf("database.pdf","bee_char")
	# export_html("database.html","bee_char")
	info(  "==End==")
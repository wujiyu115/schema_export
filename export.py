# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:12:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 19:35:09

from export.export_base import *
from util.mylog import install_log,info,debug

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	install_log()
	# info( "==export start==")
	datasource =  MySqlDbData()
	all_exports =  [XlsExport(datasource),DocExport(datasource),HtmlExport(datasource),PdfExport(datasource),CSVExport(datasource)]
	#文件名,数据库名
	all_exports[4].export("database")
	# info(  "==End==")
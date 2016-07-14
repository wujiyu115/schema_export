# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 14:12:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 18:16:42

from export.export_base import *
from util.mylog import install_log,info,debug

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	install_log()
	# info( "==export start==")
	datasource =  MySqlDbData()
	all_exports =  [XlsExport(datasource),DocExport(datasource),HtmlExport(datasource),PdfExport(datasource)]
	#文件名,数据库名
	all_exports[1].export("database","hj_game_stat_lyx_s")
	# info(  "==End==")
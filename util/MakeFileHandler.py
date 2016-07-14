#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
from fileutil import mkdir_p


class MakeFileHandler(logging.handlers.TimedRotatingFileHandler):
	def __init__(self,filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):
		mkdir_p(os.path.dirname(filename))
		log_path =os.path.splitext(filename)
		log_file = '%s-%s%s'%(log_path[0],time.strftime("%Y-%m-%d", time.localtime()), log_path[1])
		logging.handlers.TimedRotatingFileHandler.__init__(self, log_file, when, interval, backupCount, encoding, delay, utc)
		# logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import logging
import logging.handlers
import logging.config
import yaml
import traceback

from util.codecutil import stdout_encoding
from configutil import ConfigUtil


LEVEL_INFO ="info"
LEVEL_DEBUG ="debug"
LEVEL_WARNING ="warn"
LEVEL_ERROR ="error"
LEVEL_CRITICAL ="critical"

#handler
ROOT_LOGGER ="root"
ROOT_TORNADO ="tornado"

def __log(level_func, message,logger_name):
	try:
		logger = logging.getLogger(logger_name)
		getattr(logger,level_func)(message)
	except:
		print(traceback.format_exc())
		pass

def info(message,logger_name="root"):
	__log(LEVEL_INFO, message,logger_name)


def debug(message,logger_name="root"):
	__log(LEVEL_DEBUG, message,logger_name)


def warn(message,logger_name="root"):
	__log(LEVEL_WARNING, message,logger_name)


def error(message,logger_name="root"):
	__log(LEVEL_ERROR, message,logger_name)

def critical(message,logger_name="root"):
	__log(LEVEL_CRITICAL, message,logger_name)


def blank(logger_name="root"):
	__log(LEVEL_INFO, '',logger_name)


def install_log():
	log_level =   str(ConfigUtil.instance().log_level if hasattr(ConfigUtil.instance(),"log_level") else "INFO")
	# 分割log
	if sys.hexversion>0x20700f0:
		logging.config.dictConfig(yaml.load(open(ConfigUtil.instance().loggingyaml, 'r')))
	else:
		log_file = 'logging.%s-%d.log'%(time.strftime("%Y-%m-%d--%H-%M-%S", time.localtime()), os.getpid())
		timelog = logging.handlers.TimedRotatingFileHandler(log_file,'midnight', 1, 0)
		logger.addHandler(timelog)
	logger = logging.getLogger()
	logger.setLevel(log_level)

	stdout_encoding()


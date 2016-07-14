#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2016-03-15 20:43:04
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-06-21 11:15:06
import threading
import os,ConfigParser


class ConfigUtil(object):
	_instance_lock = threading.Lock()

	@staticmethod
	def instance():
		if not hasattr(ConfigUtil, "_instance"):
			with ConfigUtil._instance_lock:
				if not hasattr(ConfigUtil, "_instance"):
					ConfigUtil._instance = ConfigUtil()
		return ConfigUtil._instance


	def __init__(self):
		pass

	def setConfigFile(self,fixed_config_file="configs/config.conf"):
		self.fixed_config_file = fixed_config_file

		root_path = os.path.split(os.path.realpath(__file__))[0] +"/"
		#固定值配置
		fixed_config = ConfigParser.ConfigParser()
		fixed_path =  root_path+self.fixed_config_file
		fixed_config.read(fixed_path)

		for section in fixed_config.sections():
			for p, value in fixed_config.items(section):
				if value.isdigit():
					setattr(self,p,int(value))
				else:
					if value=="true" or value=="false" :
						setattr(self,p,fixed_config.getboolean(section,p))
					else:
						setattr(self,p,str(value).strip())

		if self.vip_configs!=None:
			self.vip_configs = str.split(self.vip_configs,",")

	def getProcesses(self):
		return self.processes

	def getDBConfig(self):
		return self.host,self.user,self.passwd,self.db,self.port

ConfigUtil.instance().setConfigFile()

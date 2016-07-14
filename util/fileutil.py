# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-14 11:34:04
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 11:34:14
import os
import errno

def mkdir_p(path):
	"""http://stackoverflow.com/a/600612/190597 (tzot)"""
	try:
		os.makedirs(path, exist_ok=True)  # Python>3.2
	except TypeError:
		try:
			os.makedirs(path)
		except OSError as exc: # Python >2.5
			if exc.errno == errno.EEXIST and os.path.isdir(path):
				pass
			else: raise
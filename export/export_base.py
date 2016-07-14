# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 19:58:14
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 16:11:24
from formats.docx_format import DocFormat
from formats.excel_format import ExcelFormat
from formats.html_format import HtmlFormat
from formats.pdf_format import PdfFormat
from db.db_info import MySqlDbData
from util.fileutil import mkdir_p
from configutil import ConfigUtil
import os

class BaseExport(object):

	"""docstring for BaseExport"""
	def __init__(self,datasource):
		super(BaseExport,self).__init__()
		# self.headings = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra','Comment']
		self.headings = [u'名称', u'数据类型', u'允许空值', u'主键', u'默认值', u'额外信息',u'说明']
		self.datasource =  datasource

	def export(self,outfilename,dbname):
		outputdir = ConfigUtil.instance().outputdir
		outpath =os.path.join(os.getcwd(), outputdir)
		mkdir_p(outpath)
		outpath = os.path.join(outpath,outfilename)
		return outpath

class XlsExport(BaseExport):
	"""docstring for XlsExport"""
	def __init__(self,datasource):
		super(XlsExport, self).__init__(datasource)

	def export(self,outfilename,dbname):
		outpath= super(XlsExport, self).export(outfilename,dbname)
		entu = ExcelFormat(outpath)
		sheets =[dbname]
		datas = {}
		for sheet in sheets:
			datas =self.datasource.getDatas(sheet)
			sheet = entu.addSheet(sheet)
			entu.write(sheet, self.headings, datas)
		self.datasource.close()
		entu.save()

class DocExport(BaseExport):
	"""docstring for DocExport"""
	def __init__(self,datasource):
		super(DocExport, self).__init__(datasource)

	def export(self,outfilename,dbname):
		outpath= super(DocExport, self).export(outfilename,dbname)
		doc = DocFormat(outpath)
		recordset =self.datasource.getDatas(dbname)
		self.datasource.close()
		doc.write(self.headings,recordset)
		doc.save()

class HtmlExport(BaseExport):
	"""docstring for HtmlExport"""
	def __init__(self,datasource):
		super(HtmlExport, self).__init__(datasource)

	def export(self,outfilename,dbname):
		outpath=super(HtmlExport, self).export(outfilename,dbname)
		htmlformat = HtmlFormat(outpath)
		recordset =self.datasource.getDatas(dbname)
		self.datasource.close()
		context = {
			'dbname': dbname,
			'recordset': recordset,
			'headings':self.headings
		}
		htmlformat.write(self.headings,context)
		htmlformat.save()

class PdfExport(BaseExport):
	"""docstring for PdfExport"""
	def __init__(self,datasource):
		super(PdfExport, self).__init__(datasource)

	def export(self,outfilename,dbname):
		outpath=super(PdfExport, self).export(outfilename,dbname)
		doc = PdfFormat(outpath)
		recordset =self.datasource.getDatas(dbname)
		self.datasource.close()
		doc.write(self.headings,recordset)
		doc.save()



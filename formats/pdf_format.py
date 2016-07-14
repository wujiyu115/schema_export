# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 15:03:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 17:42:16
import os

from reportlab.lib import fonts,colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from base_format import BaseFormat
from configutil import ConfigUtil

# ttf=os.path.join(os.getcwd(), 'templates',"simsun.ttf")
ttf=ConfigUtil.instance().pdfttf
ttfname = 'sim'
pdfmetrics.registerFont(TTFont(ttfname,ttf))

fonts.addMapping(ttfname, 0, 0,ttfname)
fonts.addMapping(ttfname, 0, 1, ttfname)

class PdfFormat(BaseFormat):

	def __init__(self, filename):
		self.suffix = "pdf" #后缀
		super(PdfFormat, self).__init__(filename)

		self.doc = SimpleDocTemplate(self.outname, pagesize=letter)
		self.elements = []


	def write(self,  headings, data):
		styles=getSampleStyleSheet()
		styles.add(ParagraphStyle(name='Justify', alignment=TA_CENTER))
		styles['Justify'].fontName =ttfname
		head_len = len(headings)
		for db_name,items in data.iteritems():
			items.insert(0,headings)
			rows = len(items)
			t=Table(items,head_len*[1*inch], rows*[0.3*inch])
			t.setStyle(TableStyle([
					('FONT', (0,0), (-1,-1),ttfname),
					('FONTSIZE', (0, 0), (-1, -1), 7),
					('ALIGN',(0,0),(-1,-1),'CENTER'),
					('VALIGN',(0,0),(-1,-1),'MIDDLE'),
					('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
					('BOX', (0,0), (-1,-1), 0.25, colors.black),
					]))
			self.elements.append(Spacer(1, 20))
			self.elements.append(Paragraph(db_name, styles["Justify"]))
			self.elements.append(Spacer(1, 20))
			self.elements.append(t)

	def save(self):
		self.doc.build(self.elements)




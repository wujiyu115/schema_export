# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 15:03:26
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-13 16:03:05
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

class PdfUtil():

	def __init__(self, filename):
		self.filename = filename
		self.doc = SimpleDocTemplate(self.filename, pagesize=letter)
		self.elements = []


	def write(self,  headings, data):
		styles=getSampleStyleSheet()
		styles.add(ParagraphStyle(name='Justify', alignment=TA_CENTER))
		head_len = len(headings)
		for db_name,items in data.iteritems():
			items.insert(0,headings)
			rows = len(items)
			t=Table(items,head_len*[1*inch], rows*[0.3*inch])
			t.setStyle(TableStyle([
					('FONTSIZE', (0, 0), (-1, -1), 7),
					('ALIGN',(0,0),(-1,-1),'CENTER'),
					('VALIGN',(0,0),(-1,-1),'MIDDLE'),
					('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
					('BOX', (0,0), (-1,-1), 0.25, colors.black),
					]))
			self.elements.append(Spacer(1, 12))
			self.elements.append(Paragraph(db_name, styles["Normal"]))
			self.elements.append(Spacer(1, 12))
			self.elements.append(t)

	def save(self):
		self.doc.build(self.elements)




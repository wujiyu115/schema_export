# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 15:11:53
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-15 10:22:02
import csv
from base_format import BaseFormat
class CSVFormat(BaseFormat):

	def __init__(self, filename,headings):
		self.suffix = "csv" #后缀
		super(CSVFormat, self).__init__(filename,headings)


	def create_space_row(self, headings):
		row = []
		for x in headings:
			row.append(",")
		return row

	def write(self,  data):
		super(CSVFormat, self).write(data)
		headings = self.headings
		with open(self.outname, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(headings)
			for db_name,table_info in data.iteritems():
				table_caption = db_name
				if table_info.table_desc   :
					table_caption = '%s(%s)'%(db_name,table_info.table_desc)
				spamwriter.writerow([table_caption])
				for column in table_info.columns or []:
					spamwriter.writerow(column)
				spamwriter.writerow(self.create_space_row(headings))


	def save(self):
		pass
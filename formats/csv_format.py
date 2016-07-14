# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 15:11:53
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 19:39:07
import csv
from base_format import BaseFormat
class CSVFormat(BaseFormat):

	def __init__(self, filename):
		self.suffix = "csv" #后缀
		super(CSVFormat, self).__init__(filename)


	def create_space_row(self, headings):
		row = []
		for x in headings:
			row.append(",")
		return row

	def write(self, headings, data):

		with open(self.outname, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(headings)
			for table,columns in data.iteritems():
				spamwriter.writerow([table])
				for column in columns:
					spamwriter.writerow(column)
				spamwriter.writerow(self.create_space_row(headings))


	def save(self):
		pass
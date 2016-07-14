# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 20:27:03
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 16:10:55
import os
from base_format import BaseFormat
from jinja2 import Environment, FileSystemLoader

PATH=os.path.join(os.getcwd(), 'templates')
TEMPLATE_ENVIRONMENT = Environment(
	autoescape=False,
	loader=FileSystemLoader(PATH),
	trim_blocks=False)



class HtmlFormat(BaseFormat):

	def __init__(self, filename):
		self.suffix = "html" #后缀
		super(HtmlFormat, self).__init__(filename)

		self.html_data = None

	def render_template(self,template_filename, context):
		return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


	def write(self,  headings, context):
		self.html_data = self.render_template('teamplate.html', context)

	def save(self):
		with open(self.outname, 'w') as f:
			f.write(self.html_data)


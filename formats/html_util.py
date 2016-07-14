# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 20:27:03
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 11:13:21
import os
from jinja2 import Environment, FileSystemLoader

PATH=os.path.join(os.getcwd(), 'templates')
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(PATH),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)



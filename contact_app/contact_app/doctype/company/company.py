# -*- coding: utf-8 -*-
# Copyright (c) 2020, Abizeyimana Victor and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
# from frappe.website.website_generator import WebsiteGenerator
# from frappe import _

class company(Document):
	pass


# # subclass from WebsiteGenerator, not Document
# class company(WebsiteGenerator):
# 	website = frappe._dict(
# 		template = "templates/generators/company.html",
# 		# condition_field = "published",
# 		page_title_field = "company_name",
# 	)
# 	def validate(self) :
#         if not self.route:        #pylint: disable=E0203
#             self.route = "company/" + "-"
#                      .join(self.title.split(" "))

# 	def get_context(self, context):
# 		# show breadcrumbs
# 		context.parents = [{'name': 'jobs', 'title': _('All Jobs') }]
# 		context.no_cache = 1
# 		context.show_sidebar = True
# 		context.title = self.title
# 		context['list'] = frappe.get_doc('company', frappe.form_dict.get('name'))

# 	def get_list_context(context):
# 		context.title = _("Jobs")
# 		context.introduction = _('Current Job Openings')
# 		# context.get_list = get_encounter_list #  query return the data to be render in lest 
# 		# context.row_template = "contact_app/doctype/company/templates/company_row.html"
# 		# context.result_heading_template = "yourcusutomapp/module/doctype/doctypename/templateresult_heading_template.html"


# 	def get_encounter_list(doctype, txt, filters, limit_start, limit_page_length = 20, order_by='modified desc'):
# 		# sql or orm query  you get data  as_dict = True
# 		company_list = frappe.get_list('CRMContact', start=0, page_length=20, fields="*", order_by='creation desc')
# 		return company_list
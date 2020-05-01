from __future__ import unicode_literals
import frappe, json
from frappe import _
import frappe.www.list
from frappe.utils.file_manager import save_file

no_cache = 1
no_sitemap = 1

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

# 	# context['list'] = frappe.get_doc('company', frappe.form_dict.get('name'))
# 	context.parents = [dict(route='/me', label='My Account')] 
# 	# context['Gender'] = frappe.get_all('Gender')
#     # frappe.get_list(doctype, filters, fields, order_by)

# @frappe.whitelist()
# def get_company_list(doctype):
# 	# company_list = frappe.get_all(doctype, fields=['*'])
# 	company_list = frappe.get_list('company', start=0, page_length=20, fields="*", order_by='creation desc')
# 	return company_list
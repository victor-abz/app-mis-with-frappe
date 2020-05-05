from __future__ import unicode_literals
import frappe, json
from frappe import _
import frappe.www.list
from frappe.utils.file_manager import save_file
import datetime
from datetime import timedelta
from datetime import datetime as dt
from frappe.utils import (add_days, getdate, formatdate, date_diff,
	add_years, get_timestamp, nowdate, flt, cstr, add_months, get_last_day)
from six import iteritems, string_types

no_cache = 1
no_sitemap = 1

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context['Appointments'] = frappe.db.get_all('Appointment',
			fields=['*'],
            order_by='scheduled_time desc',
            start=0,
            page_length=20,
            filters={
                'status': 'Open',
				'scheduled_time': ['>=', dt.now()],
				'scheduled_time': ['<=', dt.now() + timedelta(days=7)  ],
            }
		)
	context['companies'] = frappe.db.get_all('company',
			fields=['*'],
            order_by='company_name asc',
            start=0,
            page_length=5,
		)

@frappe.whitelist()
def get_communication_data(doctype):
	company = frappe.db.get_list( doctype,
			# fields=['communication_date'],
			fields=['count(name) as count', 'communication_date'],
			group_by='date(creation)',
			order_by='communication_date asc',
            start=0,
            page_length=60,
			filters={
                'sent_or_received': 'Sent',
				'communication_date': ['<=', dt.now()],
            }
			
		)
	return company

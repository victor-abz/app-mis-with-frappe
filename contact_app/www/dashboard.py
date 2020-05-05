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
            start=0,
            page_length=60,
			filters={
                'sent_or_received': 'Sent',
            }
			
		)
	return company

# @frappe.whitelist()
# def get_timeline_data(doctype, name):
# 	'''returns timeline data for the past one year'''
# 	from frappe.desk.form.load import get_communication_data

# 	out = {}
# 	fields = 'date(creation), count(name)'
# 	after = add_years(None, -1).strftime('%Y-%m-%d')
# 	group_by='group by date(creation)'

# 	data = get_communication_data(doctype, name, after=after, group_by='group by date(creation)',
# 		fields='date(C.creation) as creation, count(C.name)',as_dict=False)

# 	# fetch and append data from Activity Log
# 	data += frappe.db.sql("""select {fields}
# 		from `tabActivity Log`
# 		where (reference_doctype="{doctype}" and reference_name="{name}")
# 		or (timeline_doctype in ("{doctype}") and timeline_name="{name}")
# 		or (reference_doctype in ("Quotation", "Opportunity") and timeline_name="{name}")
# 		and status!='Success' and creation > {after}
# 		{group_by} order by creation desc
# 		""".format(doctype=frappe.db.escape(doctype), name=frappe.db.escape(name), fields=fields,
# 			group_by=group_by, after=after), as_dict=False)

# 	timeline_items = dict(data)

# 	for date, count in iteritems(timeline_items):
# 		timestamp = get_timestamp(date)
# 		out.update({ timestamp: count })

# 	return out
from __future__ import unicode_literals
import frappe, json
from frappe import _
import frappe.www.list
from frappe.utils.file_manager import save_file
from frappe.core.doctype.communication.email import make

no_cache = 1
no_sitemap = 1

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context['company'] = frappe.get_doc('company', frappe.form_dict.get('name'))
	context.parents = [{'route': 'me', 'title': _('My Account') }, {'route': 'company', 'title': _('All companies') }]
	context['Gender'] = frappe.get_all('Gender')

@frappe.whitelist()
def add_company_contact(company, inputFirstName,inputLastName,inputEmail,inputGender,inputPosition,inputPhone):
	company = frappe.get_doc('company', company)
	company.append('contacts', {
		'first_name': inputFirstName,
		'last_name': inputLastName,
		'email_id': inputEmail,
		'gender': inputGender,
		'position': inputPosition,
		'phone_number': inputPhone
	})
	company.save()
	return company

@frappe.whitelist()
def attach_file_to_contact(filedata, contact_name):
	if filedata:
		fd_json = json.loads(filedata)
		fd_list = list(fd_json["files_data"])
		for fd in fd_list:
			filedoc = save_file(fd["filename"], fd["dataurl"],
				"CRMContact", contact_name, decode=True, is_private=1).file_url
		
		contact = frappe.get_doc("CRMContact", contact_name)
		contact.image = filedoc
		contact.save(ignore_permissions=True)

@frappe.whitelist()
def send_email(email_address):
	frappe.sendmail(recipients=email_address,
		subject="Subject of the email",
		message= "Content of the email")


@frappe.whitelist()
def send_email(emailForm, company_id, email_id):
	msg=json.loads(emailForm)
	comm = make(
		doctype = "company",
		name = company_id,
		subject = msg.get('subject'),
		content = msg.get('body'),
		sender = 'svicky.shema@gmail.com',
		recipients = email_id,
		communication_medium = "Email",
		sent_or_received = "Sent",
		send_email = True
	)
	return comm
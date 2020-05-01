# -*- coding: utf-8 -*-
# Copyright (c) 2020, Abizeyimana Victor and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import urllib
from collections import Counter
from datetime import timedelta

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_url, getdate
from frappe.utils.verified_command import verify_request, get_signed_params


class Appointment(Document):
	def find_customer_by_email(self):
		customer_list = frappe.get_list(
			'CRMContact', filters={'email_id': self.customer_email}, ignore_permissions=True
		)
		if customer_list:
			return customer_list[0].name
		frappe.msgprint('Please input a correct contact email')

	def before_insert(self):
		customer = self.find_customer_by_email()
		self.appointment_with = "CRMContact"
		self.party = customer

	def after_insert(self):
		self.create_calendar_event()

	def on_change(self):
		# Sync Calendar
		if not self.calendar_event:
			return
		cal_event = frappe.get_doc('Event', self.calendar_event)
		cal_event.starts_on = self.scheduled_time
		cal_event.save(ignore_permissions=True)


	def create_calendar_event(self):
		if self.calendar_event:
			return
		appointment_event = frappe.get_doc({
			'doctype': 'Event',
			'subject': ' '.join(['Appointment with', self.customer_name]),
			'starts_on': self.scheduled_time,
			'status': 'Open',
			'type': 'Public',
			'send_reminder': frappe.db.get_single_value('Appointment Booking Settings', 'email_reminders'),
			'event_participants': [dict(reference_doctype=self.appointment_with, reference_docname=self.party)]
		})
		appointment_event.insert(ignore_permissions=True)
		self.calendar_event = appointment_event.name
		self.save(ignore_permissions=True)


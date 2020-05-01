from __future__ import unicode_literals
import frappe, json
from frappe import _
import frappe.www.list
from frappe.utils.file_manager import save_file

no_cache = 1
no_sitemap = 1

def boot_session(bootinfo):
    bootinfo['home_page'] = 'dashboard'
    return bootinfo
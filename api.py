from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def hello():
    hello_world = ['Hello','world','Me']
    return hello_world
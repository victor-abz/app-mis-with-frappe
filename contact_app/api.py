from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def hello(name):
    hello_world = ['Hello','world','Me', name]
    return hello_world

@frappe.whitelist(allow_guest=True)
def john(name):
    hello_world = ['Hello', name]
    return hello_world

@frappe.whitelist(allow_guest=True)
def _get_company(id):
    hello_world = ['Hello', name]
    return hello_world
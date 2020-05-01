import frappe

def get_context(context):
    context['body'] = 'This is a custom homepage'

def add_users_to_context(context):
    context['users'] = frappe.get_all('User')
import frappe
data = []
def get_context(context):
    context.users = data
# data = []
# def get_context(context):
#         context.users = data

@frappe.whitelist()
def get_value(value):
        global data
        data = frappe.get_list("Registration Form", fields=["firstname", "lastname"], filters={"email": value})
        
        data.append(data)

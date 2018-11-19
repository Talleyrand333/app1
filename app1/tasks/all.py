import frappe

def setter():
    doc=frappe.get_doc("Vehicle","ML 350-2013_HU-432-REH")
    doc.odometer_2=10
    return

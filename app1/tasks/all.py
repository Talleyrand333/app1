from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate


def setter():
    print("Starting Operation")
    doc=frappe.get_doc("Vehicle","Pathfinder-2016_YI-896-JJN")
    doc.odometer_2=1414
    doc.save()
    print("Done")

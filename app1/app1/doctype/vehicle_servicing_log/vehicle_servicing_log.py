# -*- coding: utf-8 -*-
# Copyright (c) 2018, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VehicleServicingLog(Document):
	pass

	def autoname(self):
		vehicle_=frappe.get_doc("Vehicle",self.vehicle)
		license_plate=vehicle_.license_plate
		start_date=self.service_date
		name2=start_date+"_"+license_plate
		self.name=name2
		return

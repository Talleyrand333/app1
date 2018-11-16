# -*- coding: utf-8 -*-
# Copyright (c) 2018, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VehicleModel(Document):
	pass
	def autoname(self):
		"""This function changes the default naming series of the vehicle model when it is created"""
		name_1=self.name1
		year_1=self.model_year
		self.vmn=name_1+"-"+str(year_1)
		self.name=self.vmn
		return self.name

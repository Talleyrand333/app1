from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Backup"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Azure Storage Backup Settings",
					"description": _("Azure Storage Backup Settings"),
				},
			]
		}
	]

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Workflow"),
			"icon": "fa fa-random",
			"items": [
				{
					"type": "doctype",
					"name": "Workflow Notification",
				},
			]
		},
	]

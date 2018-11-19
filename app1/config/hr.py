from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Fleet Management"),
            "items":[
                {
                    "type": "doctype",
                    "name": "Vehicle Request"
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Make"
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Model"
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Servicing Log"
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Trip Log"
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Type"
                },

            ]
        },

    ]

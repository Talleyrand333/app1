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
            ]
        },

    ]

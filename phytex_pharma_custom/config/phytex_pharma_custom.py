from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Reports"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"name": "Customer Ledger Statement",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Supplier Ledger Statement",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
			]
		},

	]

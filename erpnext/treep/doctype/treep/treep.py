# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe import exceptions


class Treep(Document):
	def validate(self):
		if frappe.db.exists(self.doctype, self.name):
			duplicate_error_message = _("Please kindly choose another day to schedule Treep")
			frappe.throw(duplicate_error_message, title=_("DATE ALREADY BOOKED"))
	# def on_save(doc):
	# 	if frappe.db.exists(doc.doctype,doc.name):
	# 		duplicate_error_message = _("Please Kindly choose another day to schedule Treep")
	# 		frappe.throw(duplicate_error_message, title= _("DATE ALREADY BOOKED"))

	

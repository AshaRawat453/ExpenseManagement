# Copyright (c) 2024, asha rawat and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class LeaveApplication(Document):
     def validate(self):
        # Check if both start_date and end_date are provided
        if self.start_date and self.end_date:
            # Calculate the number of days between start_date and end_date (inclusive)
            self.total_days = date_diff(self.end_date, self.start_date) + 1  # +1 to include both dates
        else:
            frappe.throw("Please provide both Start Date and End Date")

import frappe


def daily_maintenance():
    frappe.log_error(
        title="Daily Maintenance",
        message="Daily maintenance task executed successfully."
    )

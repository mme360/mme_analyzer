import frappe


def execute():
    for page_name in ["analyzer", "calibration-log"]:
        if frappe.db.exists("Page", page_name):
            frappe.delete_doc("Page", page_name, force=True, ignore_permissions=True)

app_name = "mme_analyzer"
app_title = "MME Analyzer"
app_publisher = "MME360"
app_description = "Analyzer support and monitoring app for ERPNext"
app_license = "MIT"

required_apps = ["erpnext"]

after_install = "mme_analyzer.install.after_install"

add_to_apps_screen = [
    {
        "name": "mme_analyzer",
        "title": "MME Analyzer",
        "route": "/desk/mme-analyzer",
        "has_permission": "frappe.session.user != 'Guest'"
    }
]

fixtures = []

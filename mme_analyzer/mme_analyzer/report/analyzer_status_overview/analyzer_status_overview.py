def execute(filters=None):
    columns = [
        {"label": "Analyzer", "fieldname": "name", "fieldtype": "Link", "options": "Analyzer", "width": 180},
        {"label": "Analyzer Name", "fieldname": "analyzer_name", "fieldtype": "Data", "width": 180},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 180},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": "Health Score", "fieldname": "health_score", "fieldtype": "Int", "width": 120},
        {"label": "Last Sync", "fieldname": "last_sync", "fieldtype": "Datetime", "width": 180}
    ]
    data = []
    return columns, data

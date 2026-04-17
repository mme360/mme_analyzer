# Install mme_analyzer on mme-care-portal-v16

## Bench
`mme-care-portal-v16`

## Site
`mme360.u.frappe.cloud`

## Assumptions
- ERPNext is already installed
- Marley is already installed
- This custom app will be added on top of the existing stack

## Steps
1. Get the app code into the bench apps directory.
2. Ensure the app folder name is `mme_analyzer`.
3. Run migrations after adding the app.
4. Install the app on the site.

## Typical commands
```bash
cd ~/frappe-bench
bench --site mme360.u.frappe.cloud install-app mme_analyzer
bench --site mme360.u.frappe.cloud migrate
bench restart
```

## After install
- Open Desk
- Search for `MME Analyzer`
- Open the workspace
- Verify DocTypes are visible:
  - Analyzer
  - Customer Site
  - QC Log
  - Calibration Log
  - Maintenance Log
  - Support Incident
  - Alert Rule

## Next build targets
- workspace polish
- role permissions
- dashboard cards
- analyzer health logic
- support automation

# Installation and Setup Guide for Lydinc HR Custom Module

## Prerequisites

- Odoo 19 installed and running
- Access to Odoo database with admin rights
- HR and HR Holidays modules installed

## Installation Steps

### 1. Module Location

The module is already located at:
```
D:\odoo_project\odoo_space\lydinchr\
```

### 2. Update Odoo Configuration

Ensure your `odoo.conf` file includes the addons path:
```
addons_path = D:\odoo_project\odoo_space\addons,D:\odoo_project\odoo_space
```

### 3. Restart Odoo Server

After placing the module, restart your Odoo server:
```bash
# If running from command line
python odoo-bin -c odoo.conf

# Or restart your Odoo service
```

### 4. Update Apps List

1. Log in to Odoo as Administrator
2. Activate Developer Mode:
   - Settings > General Settings > Developer Tools > Activate Developer Mode
3. Go to Apps menu
4. Click "Update Apps List"
5. Confirm the update

### 5. Install the Module

1. In the Apps menu, remove the "Apps" filter
2. Search for "Lydinc HR Custom" or "lydinchr"
3. Click the "Install" button

### 6. Verify Installation

After installation, you should see:
- New menu item: **Lydinc HR**
- Extended employee forms with new tabs
- Enhanced leave request forms
- Employee Properties menu

## Post-Installation Configuration

### Setting Up Security Groups

1. Go to Settings > Users & Companies > Groups
2. Find "HR Custom User" and "HR Custom Manager" groups
3. Assign users to appropriate groups:
   - **HR Custom User**: Regular HR staff (read-only access to properties)
   - **HR Custom Manager**: HR managers (full access)

### Configuring Employee Information

1. Navigate to Employees app
2. Open an employee record
3. Fill in the new fields:
   - Badge Number
   - Joining Date
   - Salary Information (in Salary Information tab)
   - Emergency Contact (in Emergency Contact tab)

### Creating Employee Properties

1. Go to Lydinc HR > Employee Properties
2. Create property records for:
   - Equipment (laptops, phones)
   - Documents (contracts, certificates)
   - Assets (keys, cards)
   - Credentials (access badges)

## Troubleshooting

### Module Not Appearing in Apps List

- Check if the module path is correct in odoo.conf
- Ensure __manifest__.py exists and is properly formatted
- Check server logs for errors

### Installation Fails

- Verify all dependencies (base, hr, hr_holidays) are installed
- Check database permissions
- Review server logs for specific errors

### Access Rights Issues

- Ensure users are assigned to appropriate security groups
- Check that ir.model.access.csv is loaded correctly
- Verify security groups are created

## Upgrading the Module

To upgrade after making changes:

1. Make your changes to the module files
2. Restart Odoo server
3. Go to Apps menu
4. Search for "Lydinc HR Custom"
5. Click "Upgrade"

Or use command line:
```bash
python odoo-bin -c odoo.conf -u lydinchr -d your_database_name
```

## Uninstallation

To uninstall the module:

1. Go to Apps menu
2. Search for "Lydinc HR Custom"
3. Click "Uninstall"
4. Confirm the uninstallation

**Note**: Uninstalling will remove all custom data (employee properties, extended fields data).

## Database Backup

Before installing or upgrading, it's recommended to backup your database:

```bash
# From Odoo interface:
Settings > Database Manager > Backup

# Or from command line:
pg_dump your_database_name > backup.sql
```

## Support

For issues or questions, contact the module developer.

## Next Steps

After successful installation:
1. Configure employee information with extended fields
2. Start tracking employee properties
3. Use enhanced leave management features
4. Plan for future enhancements based on your needs


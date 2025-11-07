# Lydinc HR Custom Module

## Overview

This custom Odoo 19 module extends the standard HR functionality to provide enhanced employee management capabilities, property tracking, and leave management features.

## Features

### 1. Extended Employee Information
- **Badge Number**: Track employee badge/ID numbers
- **Joining Date**: Record when employees joined the company
- **Salary Components**:
  - Basic Salary
  - Housing Allowance
  - Transport Allowance
  - Other Allowances
  - Automatic Total Salary Calculation
- **Emergency Contact Information**:
  - Emergency contact name
  - Relationship
  - Phone number
  - Address

### 2. Employee Property Tracking
- Track equipment, documents, assets, and credentials assigned to employees
- Property categories:
  - Equipment (laptops, phones, etc.)
  - Documents (certificates, contracts, etc.)
  - Assets (company property)
  - Credentials (access cards, keys, etc.)
  - Other
- Property status tracking: Assigned, Returned, Lost, Damaged
- Assignment and return date tracking
- Notes and detailed descriptions

### 3. Enhanced Leave Management
- Emergency leave flag
- Detailed leave reason
- Contact information during leave
- Address during leave
- Backup employee assignment
- Approval tracking (who approved and when)
- Rejection reason tracking

## Installation

1. Copy the `lydinchr` folder to your Odoo addons directory
2. Update the addons list: Go to Apps > Update Apps List
3. Search for "Lydinc HR Custom"
4. Click "Install"

## Dependencies

- `base` - Odoo Base Module
- `hr` - Human Resources
- `hr_holidays` - Time Off (Leave Management)

## Module Structure

```
lydinchr/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── employee_property.py      # Employee property tracking model
│   ├── hr_employee.py             # Extended employee model
│   └── hr_leave_custom.py         # Extended leave model
├── views/
│   ├── employee_property_views.xml
│   ├── hr_employee_views.xml
│   └── hr_leave_views.xml
├── security/
│   ├── lydinchr_security.xml      # Security groups
│   └── ir.model.access.csv        # Access rights
├── data/
│   └── employee_property_data.xml # Initial data
└── static/
    └── description/
        └── icon.png               # Module icon
```

## Usage

### Managing Employee Information

1. Navigate to **Employees** app
2. Open any employee form
3. New tabs available:
   - **Salary Information**: Enter salary components
   - **Emergency Contact**: Add emergency contact details
   - **Properties**: View assigned properties

### Managing Employee Properties

1. Navigate to **Lydinc HR > Employee Properties**
2. Create new property records
3. Assign to employees
4. Track status (Assigned, Returned, Lost, Damaged)
5. Use filters to find specific properties

### Enhanced Leave Requests

1. Navigate to **Time Off** app
2. Create a leave request
3. Additional fields available:
   - Emergency Leave toggle
   - Detailed reason
   - Contact information during leave
   - Backup employee

## Security Groups

- **HR Custom User**: Read-only access to employee properties
- **HR Custom Manager**: Full access to all features

## Version

- **Version**: 19.0.1.0.0
- **Odoo Version**: 19.0
- **License**: LGPL-3

## Author

Lee - Lydinc

## Support

For support or questions, please contact the module author.

## Future Enhancements

This is a basic CRUD implementation. Future updates may include:
- Workflow automations
- Custom reports and dashboards
- Integration with payroll
- Document management features
- Performance evaluation tracking
- Training and certification management


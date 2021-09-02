# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd.
#See LICENSE file for full copyright and licensing details.

{
    'name': 'Account Asset Disposal',

    'version': '1.0',
    'currency': 'EUR',
    
            'price': 10.0,

    'depends': [
            'account',
            'account_asset_disposal_ce',
            'odoo_account_asset_extend_ce',
                ],    
    'license': 'Other proprietary',
    'summary': """Account Asset Disposal Process""",
    'description': """
Odoo Disposal Extend
Odoo Disposal Extend
Disposal Number
Asset Disposal Report
Asset Disposal Analysis Report
Asset Pivot Report
Asset Disposal Reason
Disposal Number and Reason
Asset Disposal Qweb Report
Disposal Report
Asset Disposal PDF Report
Account Asset Disposal
This module enables the feature to dispose the asset. User can use two below methods to dispose any asset.
Sales Dispose
Asset Write-Off
This will allow user to dispose asset of company directly from Asset form. We have provide new tab under Asset form. 
You can see blog of our here on this: http://www.probuse.com/blog/erp-functional-27/post/asset-disposal-write-off-69 
**Note: This module only support Invoice sales of Asset not Cash sales.
asset close
asset dispose
asset disposal
account asset
account asset disposal
disposal process
process disposal
Asset Disposal
Dispose Assets

    """,
    'category' : 'Accounting',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpg'],
#    'live_test_url': 'https://youtu.be/ah0FZVSjlTk',
    'data':[
        'data/disposal_sequence.xml',
        'views/asset_view.xml',
        'report/disposal_report.xml',
        'report/asset_disposal_report.xml',
        'views/asset_menu_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

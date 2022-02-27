# -*- coding: utf-8 -*-
{
    'name': 'Templates Menu Technical',
    'version': '1.0',
    'summary': 'Create new menuitem with templates (qweb views) of reports.',
    'sequence': 15,
    'description': """
Templates Menu Technical
====================
Create new menuitem with templates (qweb views) of reports.
    """,
    'category': 'Settings/Technical',
    'website': '',
    'depends': ['base', ],
    'data': [
        'views/views.xml',
        'views/menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
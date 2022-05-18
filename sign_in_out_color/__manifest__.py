# -*- coding: utf-8 -*-
# Copyright 2017 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Sign in and Sign out color change",
    'description': """
        This module is used to change the colors of
        Sign in and Sign out buttons in Attendance.
    """,
    'author': "Sodexis, Inc <dev@sodexis.com>",
    'website': "http://sodexis.com/",
    'category': 'Human Resources',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'web',
        'hr_attendance'
    ],
    'data': [
        'views/sign_in_out_view.xml'
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
}

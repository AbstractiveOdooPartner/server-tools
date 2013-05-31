# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Templates for email templates",
    "version": "1.0",
    "author": "Therp BV",
    "category": 'Tools',
    'complexity': "expert",
    "description": """If an organisation's email layout is a bit more
complicated, changes can be tedious when having to do that across several email
templates. So this addon allows to define templates for mails that is referenced
by other mail templates.
This way we can put the layout parts into the template template and only content
in the other templates. Changing the layout is then only a matter of changing
the template template.


Usage:
Create an email template with the related document model 'Email Templates'. Now
most of the fields gray out and you can only edit body_text and body_html. Be
sure to use ${body_text} and ${body_html} respectively in your template
template.

Then select this newly created template templates in one of your actual
templates.""",
    'website': 'http://therp.nl',
    'images': [],
    'depends': ['email_template'],
    'data': [
        'view/email_template.xml',
    ],
    "license": 'AGPL-3',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

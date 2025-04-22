# -*- coding: utf-8 -*-
{
    'name': "Retail Promotions",

    'summary': """
        Daka's Management Module for Managing Discounts in the Retail Sector""",

    'description': """
        Daka is a retail company specializing in technology, 
        household products, white goods, and other items.

        This module allows you to manage the different discounts 
        assigned to each product, making it easier to generate sales
        orders and speeding up the company's internal processes.
        
        This module gives you:
        - All the products in the system.
        - The ability to create and manage discounts for each product.
        """,

    'author': "Sebastian Osto",
    'website': "https://www.tiendasdaka.com/",
    'category': 'Sales/Promotions/Discounts',
    'version': '0.1',
    'icon': '/retail_promotions/static/description/icon.png',

    'depends': ['base','product','sale'],

    'data': [
        #Security
        'security/ir.model.access.csv',
        #Views
        'views/promotion.xml',
        'views/menu.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
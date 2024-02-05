# -*- coding: utf-8 -*-
{
    'name': "Ejad",

    'summary': """Ejad Tec""",

    'author': "mostafa",
    'website': "mostafa",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'ejad_tec_task/static/src/js/payment_screen.js',
            'ejad_tec_task/static/src/js/models.js',
        ],
    },
    # always loaded
    'data': [

    ],

}

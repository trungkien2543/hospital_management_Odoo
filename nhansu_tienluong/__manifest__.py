{
    'name': 'Nhân sự & Tiền lương',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Tran khanh duy',
    'category': 'HR',
    'summary': 'Quản lý phụ cấp và tiền lương nhân sự',
    'description': 'Module quản lý phụ cấp và tiền lương cho nhân sự.',
    'data': [
        'security/ir.model.access.csv',
        'views/salary_views.xml',
    ],
    'installable': True,
    'application': True,
}

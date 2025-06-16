#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# إعدادات API
API_CONFIG = {
    # إعدادات theHarvester
    'theHarvester': {
        'api_keys': {
            'shodan': '',      # أدخل مفتاح API الخاص بـ Shodan
            'virustotal': '',  # أدخل مفتاح API الخاص بـ VirusTotal
            'hunter': '',      # أدخل مفتاح API الخاص بـ Hunter.io
        },
        'timeout': 60,        # مهلة الانتظار بالثواني
        'limit': 100          # الحد الأقصى للنتائج
    },
    
    # إعدادات SpiderFoot
    'spiderfoot': {
        'api_key': '',        # أدخل مفتاح API الخاص بـ SpiderFoot
        'server': 'http://127.0.0.1:5001',  # عنوان خادم SpiderFoot
        'timeout': 300,       # مهلة الانتظار بالثواني
        'modules': [          # الوحدات النشطة
            'sfp_hunter',
            'sfp_social',
            'sfp_email'
        ]
    },
    
    # إعدادات GHunt
    'ghunt': {
        'credentials_file': 'credentials.json',  # ملف بيانات اعتماد Google
        'timeout': 120,       # مهلة الانتظار بالثواني
        'max_results': 50     # الحد الأقصى للنتائج
    },
    
    # إعدادات Sherlock
    'sherlock': {
        'timeout': 60,        # مهلة الانتظار بالثواني
        'max_connections': 20, # الحد الأقصى للاتصالات المتزامنة
        'proxy': {            # إعدادات البروكسي (اختياري)
            'http': '',       # مثال: http://proxy.example.com:8080
            'https': ''       # مثال: https://proxy.example.com:8080
        }
    }
}

# إعدادات عامة
GENERAL_CONFIG = {
    'output_dir': 'results',  # مجلد حفظ النتائج
    'debug': False,           # وضع التصحيح
    'log_level': 'INFO',      # مستوى السجلات
    'user_agent': 'Sayer/1.0' # عميل المستخدم
}

# دالة للحصول على إعدادات أداة معينة
def get_tool_config(tool_name):
    if tool_name in API_CONFIG:
        return API_CONFIG[tool_name]
    return None

# دالة للتحقق من صحة مفاتيح API
def validate_api_keys():
    missing_keys = []
    
    # التحقق من مفاتيح theHarvester
    for key_name, key_value in API_CONFIG['theHarvester']['api_keys'].items():
        if not key_value:
            missing_keys.append(f'theHarvester - {key_name}')
    
    # التحقق من مفتاح SpiderFoot
    if not API_CONFIG['spiderfoot']['api_key']:
        missing_keys.append('SpiderFoot API key')
    
    return missing_keys

# دالة لتحديث مفتاح API
def update_api_key(tool_name, key_name, key_value):
    if tool_name == 'theHarvester':
        API_CONFIG['theHarvester']['api_keys'][key_name] = key_value
    elif tool_name == 'spiderfoot':
        API_CONFIG['spiderfoot']['api_key'] = key_value
    else:
        return False
    return True
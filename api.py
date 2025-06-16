#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import get_tool_config, validate_api_keys, GENERAL_CONFIG

class SayerAPI:
    def __init__(self):
        self.logger = self._setup_logging()
        self.config = GENERAL_CONFIG
        self._validate_setup()
    
    def _setup_logging(self):
        """إعداد نظام التسجيل"""
        logger = logging.getLogger('SayerAPI')
        logger.setLevel(logging.getLevelName(GENERAL_CONFIG['log_level']))
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def _validate_setup(self):
        """التحقق من صحة الإعداد"""
        missing_keys = validate_api_keys()
        if missing_keys:
            self.logger.warning(
                'مفاتيح API مفقودة: %s', ', '.join(missing_keys)
            )
    
    async def run_harvester(self, target):
        """تشغيل theHarvester"""
        config = get_tool_config('theHarvester')
        try:
            # تنفيذ البحث باستخدام theHarvester
            # يتم تنفيذ الكود الفعلي هنا
            pass
        except Exception as e:
            self.logger.error('خطأ في theHarvester: %s', str(e))
            return {'status': 'error', 'message': str(e)}
    
    async def run_spiderfoot(self, target):
        """تشغيل SpiderFoot"""
        config = get_tool_config('spiderfoot')
        try:
            # تنفيذ البحث باستخدام SpiderFoot
            # يتم تنفيذ الكود الفعلي هنا
            pass
        except Exception as e:
            self.logger.error('خطأ في SpiderFoot: %s', str(e))
            return {'status': 'error', 'message': str(e)}
    
    async def run_ghunt(self, target):
        """تشغيل GHunt"""
        config = get_tool_config('ghunt')
        try:
            # تنفيذ البحث باستخدام GHunt
            # يتم تنفيذ الكود الفعلي هنا
            pass
        except Exception as e:
            self.logger.error('خطأ في GHunt: %s', str(e))
            return {'status': 'error', 'message': str(e)}
    
    async def run_sherlock(self, target):
        """تشغيل Sherlock"""
        config = get_tool_config('sherlock')
        try:
            # تنفيذ البحث باستخدام Sherlock
            # يتم تنفيذ الكود الفعلي هنا
            pass
        except Exception as e:
            self.logger.error('خطأ في Sherlock: %s', str(e))
            return {'status': 'error', 'message': str(e)}
    
    async def search(self, target):
        """تنفيذ البحث باستخدام جميع الأدوات"""
        start_time = time.time()
        results = {
            'target': target,
            'timestamp': start_time,
            'tools': {}
        }
        
        # تنفيذ البحث بشكل متوازي
        tasks = [
            self.run_harvester(target),
            self.run_spiderfoot(target),
            self.run_ghunt(target),
            self.run_sherlock(target)
        ]
        
        # انتظار اكتمال جميع المهام
        completed_tasks = await asyncio.gather(*tasks, return_exceptions=True)
        
        # معالجة النتائج
        tool_names = ['theHarvester', 'spiderfoot', 'ghunt', 'sherlock']
        for tool_name, result in zip(tool_names, completed_tasks):
            if isinstance(result, Exception):
                results['tools'][tool_name] = {
                    'status': 'error',
                    'message': str(result)
                }
            else:
                results['tools'][tool_name] = result
        
        # إضافة وقت التنفيذ الإجمالي
        results['execution_time'] = time.time() - start_time
        
        # حفظ النتائج
        self._save_results(results)
        
        return results
    
    def _save_results(self, results):
        """حفظ نتائج البحث"""
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f"{self.config['output_dir']}/results_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4)
            self.logger.info('تم حفظ النتائج في: %s', filename)
        except Exception as e:
            self.logger.error('خطأ في حفظ النتائج: %s', str(e))

# مثال على الاستخدام
if __name__ == '__main__':
    import asyncio
    
    async def main():
        api = SayerAPI()
        target = 'example.com'
        results = await api.search(target)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    
    asyncio.run(main())
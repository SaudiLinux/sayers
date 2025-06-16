=== أداة Sayer - دليل الاستخدام ===

الوصف:
------
Sayer هي أداة متكاملة تجمع بين أربع أدوات OSINT قوية (theHarvester, SpiderFoot, GHunt, Sherlock) في واجهة موحدة وسهلة الاستخدام. تقوم الأداة بتنفيذ عمليات البحث بشكل متوازي لتوفير الوقت وتحسين الأداء.

المتطلبات الأساسية:
-----------------
1. Python 3.6 أو أحدث
2. pip (مدير حزم Python)
3. Git (لتحميل الأدوات)

خطوات التثبيت:
-------------
1. تثبيت المكتبات الأساسية:
   ```
   pip install -r requirements.txt
   ```

2. تثبيت الأدوات المطلوبة:

   أ. theHarvester:
   ```
   git clone https://github.com/laramies/theHarvester
   cd theHarvester
   python setup.py install
   cd ..
   ```

   ب. SpiderFoot:
   ```
   git clone https://github.com/smicallef/spiderfoot.git
   cd spiderfoot
   pip install -r requirements.txt
   cd ..
   ```

   ج. GHunt:
   ```
   git clone https://github.com/mxrch/GHunt
   cd GHunt
   pip install -r requirements.txt
   cd ..
   ```

   د. Sherlock:
   ```
   git clone https://github.com/sherlock-project/sherlock.git
   cd sherlock
   python -m pip install -r requirements.txt
   cd ..
   ```

إعداد مفاتيح API:
---------------
1. افتح ملف `config.py` في محرر النصوص

2. قم بإضافة مفاتيح API المطلوبة:
   - theHarvester:
     * Shodan API key (https://account.shodan.io)
     * VirusTotal API key (https://www.virustotal.com/gui/join-us)
     * Hunter.io API key (https://hunter.io/users/sign_up)

   - SpiderFoot:
     * قم بتعيين مفتاح API الخاص بـ SpiderFoot
     * تأكد من تشغيل خادم SpiderFoot على المنفذ 5001

   - GHunt:
     * قم بإعداد ملف credentials.json الخاص بـ Google

3. تخصيص الإعدادات (اختياري):
   - تعديل مهل الانتظار
   - تحديد عدد النتائج
   - إعداد البروكسي
   - تغيير مجلد حفظ النتائج

طريقة الاستخدام:
--------------
الصيغة العامة:
```
python sayer.py [الهدف]
```

أمثلة على الاستخدام:
-----------------
1. البحث عن نطاق:
   ```
   python sayer.py example.com
   ```

2. البحث عن بريد إلكتروني:
   ```
   python sayer.py user@example.com
   ```

3. البحث عن اسم مستخدم:
   ```
   python sayer.py username
   ```

المميزات:
--------
1. تشغيل متوازي للأدوات:
   - تعمل جميع الأدوات في نفس الوقت
   - تحسين سرعة التنفيذ الإجمالية
   - عرض تقدم كل أداة بشكل منفصل

2. معالجة الأخطاء:
   - استمرار العمل حتى مع فشل بعض الأدوات
   - عرض تفاصيل الأخطاء لكل أداة
   - تقرير شامل عن حالة التنفيذ

3. النتائج:
   - حفظ جميع النتائج في ملف JSON
   - تضمين حالة تنفيذ كل أداة
   - عرض ملخص نهائي ملون
   - حساب الوقت الإجمالي للتنفيذ

ملاحظات مهمة:
------------
1. تأكد من إعداد جميع مفاتيح API المطلوبة في ملف config.py
2. تحقق من تشغيل خدمات API قبل بدء البحث
3. راجع رسائل الخطأ في حالة فشل أي أداة
4. يمكن إيقاف البحث في أي وقت باستخدام Ctrl+C

معلومات المطور:
-------------
المطور: SaudiLinux
البريد الإلكتروني: SaudiCrackers@gmail.com

الدعم والمساعدة:
--------------
إذا واجهتك أي مشكلة، تأكد من:
1. تثبيت جميع المتطلبات بشكل صحيح
2. إعداد مفاتيح API بشكل صحيح
3. توفر اتصال إنترنت مستقر
4. صلاحيات الوصول المناسبة للمجلدات
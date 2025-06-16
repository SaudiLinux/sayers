=== Sayer - أداة OSINT متكاملة ===

المتطلبات الأساسية:
---------------
- Python 3.6 أو أحدث
- pip (مدير حزم Python)

التثبيت:
--------
1. قم بتثبيت المكتبات المطلوبة:
   pip install -r requirements.txt

2. قم بتثبيت الأدوات المطلوبة:
   - theHarvester:
     git clone https://github.com/laramies/theHarvester
     cd theHarvester
     python setup.py install

   - SpiderFoot:
     git clone https://github.com/smicallef/spiderfoot.git
     cd spiderfoot
     pip install -r requirements.txt

   - GHunt:
     git clone https://github.com/mxrch/GHunt
     cd GHunt
     pip install -r requirements.txt

   - Sherlock:
     git clone https://github.com/sherlock-project/sherlock.git
     cd sherlock
     python -m pip install -r requirements.txt

كيفية الاستخدام:
--------------
python sayer.py [الهدف]

أمثلة:
------
- البحث عن نطاق:
  python sayer.py example.com

- البحث عن بريد إلكتروني:
  python sayer.py user@example.com

- البحث عن اسم مستخدم:
  python sayer.py username

المميزات:
--------
- تكامل مع theHarvester للبحث عن معلومات النطاق
- تكامل مع SpiderFoot لجمع المعلومات الاستخباراتية
- تكامل مع GHunt للبحث في خدمات Google
- تكامل مع Sherlock للبحث عن حسابات وسائل التواصل الاجتماعي
- حفظ النتائج في ملف JSON
- واجهة ملونة وسهلة الاستخدام

المطور:
------
SaudiLinux
البريد الإلكتروني: SaudiCrackers@gmail.com

ملاحظات:
--------
- تأكد من تثبيت جميع المتطلبات قبل تشغيل الأداة
- قد تحتاج بعض الأدوات إلى تكوين إضافي (مثل مفاتيح API)
- يمكن أن تستغرق عملية البحث بعض الوقت حسب الهدف
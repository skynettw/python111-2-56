from django.contrib import admin
from mysite import models         # 從mysite資料夾底下匯入models.py裡面所有的類別
admin.site.register(models.HBicycleData)
admin.site.register(models.NKUSTnews)
admin.site.register(models.PhoneMaker)
admin.site.register(models.PhoneModel)

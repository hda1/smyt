from django.contrib import admin
from django.db import models

from models import createModels
from utils import test

test()

createModels()

app = models.get_app(__package__)
app_models = models.get_models(app_mod=app)

for Model in app_models:
    #print 'Admin Model = ', Model._meta.fields[1]
    if Model.__name__ != 'MetaModel':
        class ModelAdmin(admin.ModelAdmin):
            pass
        admin.site.register(Model, ModelAdmin)


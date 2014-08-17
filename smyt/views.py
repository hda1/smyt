# -*- coding: utf-8 -*-

import os

from django.db.models import get_app, get_models
from django.shortcuts import render_to_response

def index(request):
    models = []
    for model in get_models(get_app(__package__)):
        print 'model.__name__ = ', model.__name__
        print 'model._meta.verbose_name = ', model._meta.verbose_name
        print 'model._meta.verbose_name_plural = ', model._meta.verbose_name_plural
        
        models.append({
            'name': model._meta.verbose_name_plural,

        })
        
    return render_to_response("index.html", locals())

def load(request):
    #print os.path.dirname(__file__)
        
        #for key in key.iterkeys():
    
    #for obj in serializers.deserialize("yaml", data):
    #   print obj
    
    #from django.core.management import call_command
    #call_command('loaddata', '/fixtures/initial_data.yaml')
    #call_command('syncdb')
    
    return render_to_response("index.html", locals())

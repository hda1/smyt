# -*- coding: utf-8 -*-

import os

from django.db.models import get_app, get_models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

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

def json(request):
    
    return HttpResponse(simplejson.dumps(result))

def load(request):
    
    return render_to_response("index.html", locals())

# -*- coding: utf-8 -*-

import os

from django.shortcuts import render_to_response


#from .settings import MEDIA_ROOT

#from smanuals.manual.models import Section

def index(request):
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

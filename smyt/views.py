# -*- coding: utf-8 -*-

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import get_app, get_model, get_models
from django.http import HttpResponse
from django.views.generic import TemplateView, View

class IndexView(TemplateView):
        
    def get_context_data(self, **kwargs):
        models = []
        for model in get_models(get_app(__package__)):
            print 'model.__name__ = ', model.__name__
            models.append({
                           'name': model._meta.verbose_name_plural,
                           'url': model.__name__,
            })
        return {
            'models': models,
        }
        
    template_name = "index.html"

class JsonView(View):
    
    def get(self, request, model_name = None, *args, **kwargs):
        model = get_model(__package__, model_name)
        rows = []
        rows.append([x.verbose_name for x in model._meta.fields])
        items = model.objects.all()
        for item in items:
            row = []
            [row.append(getattr(item, x.attname)) for x in item._meta.fields]
            rows.append( row )
        return HttpResponse(json.dumps(rows, cls = DjangoJSONEncoder), content_type = "application/json")
    

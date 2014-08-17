# -*- coding: utf-8 -*-
from django.db import models
import yaml

class MetaModel():
    class Meta:
        pass

    def create(self, name, fields = {}, meta = {}):
        fields['__module__'] = self.__module__
       
        for key, value in meta.iteritems():        
            setattr(self.Meta, key, value)
            
        return type(name, (models.Model, MetaModel, ), fields)
    
    def __unicode__(self):
        return self._meta.fields[1].value_to_string(self)
        
def createModels():
    
    resultAttr = {}
    resulFields = {}
    
    data = yaml.load(open('/home/sam/Aptana Studio 3 Workspace/smyt/test.yml', "r"))
    
    for key in data.keys():

        f = MetaModel()
        resulFields.clear()

        for field in data[key]['fields']:
            typesOfField = {'char':models.CharField(max_length = 50, verbose_name=field['title']), 
                            'int':models.IntegerField(verbose_name=field['title']), 
                            'date':models.DateField(verbose_name=field['title'])}

            resulFields[field['id']] = typesOfField.get(field['type'], models.CharField(max_length = 50, verbose_name=data[key]['title']))
            resultAttr['verbose_name_plural'] = data[key]['title']

        f.create(key, resulFields, resultAttr)

        f = None


    
    
        
        
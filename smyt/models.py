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
        
def createModels():
    

    resultAttr = {}
    resulFields = {}
    
    data = yaml.load(open('/home/sam/Aptana Studio 3 Workspace/smyt/test.yml', "r"))
    for key, value in data.iteritems(): # for users, rums
        f = MetaModel()
        resulFields.clear()

        #print type(value['fields']), value['fields'][0]['id']


        for field in value['fields']:
            typesOfField = {'char':models.CharField(max_length = 50, verbose_name=field['title']), 
                            'int':models.IntegerField(verbose_name=field['title']), 
                            'date':models.DateField(verbose_name=field['title'])}

            resulFields[field['id']] = typesOfField.get(field['type'], models.CharField(max_length = 50, verbose_name=value['title']))
            resultAttr['verbose_name_plural'] = value['title']
        
        
        
        #resulFields[field['id']]
        #def __unicode__(self):
        #    return eval('self.' + value['fields'][0]['id'])
        
        #f.__unicode__ = __unicode__
        print 'key =', key
        ff = f.create(key, resulFields, resultAttr)
        
        def __unicode__(self):
            return eval('self.' + value['fields'][0]['id'])
        
        ff.__unicode__ = __unicode__
        
        print 'id =', value['fields'][0]['id']
        
        #models.Model.
        f = None
        #print ff.__subclasses__()
        #print 'ff', getattr(ff, value['fields'][0]['id'])
        #print  type(value['fields'][0]['id']), value['fields'][0]['id']
        
        #ff.setUnicode()
        #print ff.__unicode__(ff)
        
    from django.core.management import call_command
    call_command('syncdb', interactive=False)    
        
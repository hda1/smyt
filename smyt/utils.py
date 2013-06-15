import yaml
from models import createModels
        
def parse():
    data = yaml.load(open('/home/sam/Aptana Studio 3 Workspace/smyt/test.yml', "r"))
        #print data
    for key in data.iteritems():
            #print key
        title, fields = key
        print title
           #print "    ", 
           #print fields
        for field in fields.iteritems():
            print field
        
#        createModel(title, fields)
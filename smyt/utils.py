import commands
import os
#import yaml

from settings import rel

def test():
    app_name = __name__.split('.')[0]
    print 'app_name = ', app_name, type(app_name)
    
    print 'rel = ', os.path.dirname(rel())
    
    path = os.path.join(os.path.dirname(rel()), 'manage.py').replace('Aptana Studio 3 Workspace', "'Aptana Studio 3 Workspace'")
    print 'path = ', path
    
    if app_name in commands.getoutput(path+ ' migrate --list'):
        print commands.getoutput(path+ ' migrate --list')
    else:
        print commands.getoutput(path+ ' syncdb')
        print commands.getoutput(path+ ' schemamigration ' + app_name + ' --initial')
        print commands.getoutput(path+ ' migrate --fake')

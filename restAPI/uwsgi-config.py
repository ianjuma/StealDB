#!/usr/bin/env python
# -*- coding: utf-8 -
import os
import sys
from subprocess import call


print 'OS Name', os.name
print 'Platform', sys.platform
print 'Parent PID -->', os.getppid()
print 'Process ID -->', os.getpid()

if (os.name == 'posix'):
    print 'Kernel Version -->', os.system('uname -r')
else:
    pass


# options --> -p is buggy use --processes instead / workers
#           --single-interpreter
# Not a good option for UWSGI --daemonize it
call(
    ['uwsgi', '-T', '--threads', '10', '--master', '--processes', '4', '--workers', '3', '--socket', '127.0.0.1:8000', '-w',
     'flask_render:app', '--protocol', 'http'])

#call(['uwsgi', '-s', '127.0.0.1:8000', '-w', 'flask_render:app',
#     '--processes', '=4', '--workers', '4', '--protocol', 'http'])
# sudo /usr/local/bin/uwsgi -s 127.0.0.1:8000 --module flask_render --callable
# app --master --processes=4 --protocol http

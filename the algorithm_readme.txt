DRF_Django_Automation Tool

Create folder
navigate to that folder
pipenv install django
activate pipenv - pipenv shell
create django project
python manage.py createsuperuser --username admin --email admin@example.com



[way to select the the python intrpreter in vscode]

install the following
*ipython
*debugtool
*drf
show guide for the settings.py file for the following
*drf
*debugtool


histyory of commands

  Id CommandLine
  -- -----------
   1 pipenv install djangorestframework
   2 pipenv install ipython
   3 pipenv install django-debug-toolbar
   4 cd .\resturant\
   5 ls
   6 python.exe .\manage.py migrate
-------------------------------------------------debug toolbar process
orgnize 
install
Add "debug_toolbar" to your INSTALLED_APPS setting:
path('__debug__/', include('debug_toolbar.urls')),
'debug_toolbar.middleware.DebugToolbarMiddleware',
INTERNAL_IPS = [
    '127.0.0.1',
]
---------------------------------------------
drf process
'rest_framework', to your INSTALLED_APPS setting:




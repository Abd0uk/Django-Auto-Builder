# Django_automation_creation (django_autocreate)

import os
# folder_name = input('Please enter the folder name> ')

pipenv_install_commands = ['pipenv install django',
            'pipenv install ipython',
            'pipenv install djangorestframework',
            'pipenv install django-debug-toolbar',
            'pipenv graph']


def create_navigate_folder(foldername):
    os.mkdir(foldername)
    os.chdir(foldername)
    cwd = os.getcwd()
    gwd = f'Folder path is -> "{cwd}"\n'
    note =  "\nNote: the path has space so please use it with double qutation\n"
    if ' ' in cwd: 
        print(note+gwd)
    else:
        print(gwd)
    return cwd
    
    
# to install dependencies (pipenv_install_commands)
def excute(commands):
    for command in commands:
        os.system(command)
    


from shutil import copytree, ignore_patterns, copyfile

import os
path = os.getcwd()
#os.mkdir(f'{path}/dist')
#os.mkdir(f'{path}/dist/img')
try:
    copyfile(f'{path}/setup.ini', f'{path}/dist/setup.ini')
    copytree(f'{path}/img', f'{path}/dist/img', ignore=ignore_patterns('*.pyc', 'tmp*'))
except FileExistsError:
    print('Directory already created')
    pass
except FileNotFoundError:
    print('Source directory not found')
    pass

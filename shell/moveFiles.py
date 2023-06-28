from shutil import copytree, ignore_patterns, copyfile

import os
path = os.getcwd()
try:
    os.mkdir(f'{path}/dist')
    os.mkdir(f'{path}/dist/img/aws')
    os.mkdir(f'{path}/dist/img/ff')
    os.mkdir(f'{path}/dist/img/mutl')
    os.mkdir(f'{path}/dist/img/ru')
except any:
    print('directoy exits')

try:
    copyfile(f'{path}/setup.ini', f'{path}/dist/setup.ini')
    copytree(f'{path}/img/aws', f'{path}/dist/img/aws', ignore=ignore_patterns('*.pyc', 'tmp*'))
    copytree(f'{path}/img/ff', f'{path}/dist/img/ff', ignore=ignore_patterns('*.pyc', 'tmp*'))
    copytree(f'{path}/img/mutl', f'{path}/dist/img/mutl', ignore=ignore_patterns('*.pyc', 'tmp*'))
    copytree(f'{path}/img/ru', f'{path}/dist/img/ru', ignore=ignore_patterns('*.pyc', 'tmp*'))
except FileExistsError:
    print('Directory already created')
    pass
except FileNotFoundError:
    print('Source directory not found')
    pass

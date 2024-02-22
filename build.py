import os
import fs
from distutils.dir_util import copy_tree
# Preparing shell

os.system('cls' if os.name == 'nt' else 'clear')
os.system('title Building...')
print('Building...')
# Preparing directories directory 

## The dist directory
if os.path.exists('dist'):
    ## Clearing the dist directory
    fs.clear_dir('dist')
else:
    os.mkdir('dist')

## The build directory
## If the directory already exists, remove all files and subdirectories in it recursively
## If the directory does not exist, create it
if not os.path.exists('build'):
    os.mkdir('build')

if os.path.exists('build/document'):
    ## Clearing the build directory
    fs.clear_dir('build/document')
else:
    os.mkdir('build/document')

# Document

import document.build as document

## Running the build function in the document.build module

document.build()

# Copying the static files into the dist directory

os.system('copy /Y "static\\*" "dist"')
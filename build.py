import os
from distutils.dir_util import copy_tree

# Preparing dist directory 

## If the directory already exists, remove all files and subdirectories in it recursively
## If the directory does not exist, create it

if os.path.exists('dist'):
    for root, dirs, files in os.walk('dist', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
else:
    os.mkdir('dist')

# Document

import document.build as document

## Running the build function in the document.build module

document.build()

# Copying static files
    
## Copying all files and subdirectories from the static directory to the dist directory

copy_tree('static', 'dist')
import os

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



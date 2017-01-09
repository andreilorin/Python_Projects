import os
import shutil

sourcepath = 'C:/Users/Lorin/Desktop'
source = os.listdir(sourcepath)
pythonpath = 'D:/PythonProgramming'
musicpath = 'D:/Music'
sitepath = 'D:/WebsiteImages'

for files in source:
    if files.endswith('.py'):
        shutil.move(os.path.join(sourcepath, files), os.path.join(pythonpath, files))
    elif files.endswith('.mp3'):
        shutil.move(os.path.join(sourcepath, files), os.path.join(musicpath, files))
    elif files.endswith('.png') or files.endswith('.jpg'):
        shutil.move(os.path.join(sourcepath, files), os.path.join(sitepath, files))

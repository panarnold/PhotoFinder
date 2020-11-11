#! python
# photoFinder.py - script, that will find&print absolute path to every "photofolder" on a Disc/directory
# usage: photoFinder.py <Disc or Directory >
# e.g: photoFinder.py C:\
# e.g: photoFinder.py C:\exampleFolder\GiveMeJobPlease
# XI 2020 Arnold Cytrowski

import os, sys
from PIL import Image

if len(sys.argv) != 2:
    print('Sorry. Here is the proper usage: type "python photoFinder.py <directoryname>"')
    exit(0)

dir = sys.argv[1]

for foldername, subfolders, filenames in os.walk(dir):
    num_of_photos = 0
    num_no_photos = 0
    for filename in filenames:
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            num_no_photos += 1
            continue

        try:
            image = Image.open(os.path.join(foldername, filename))
        except:
            continue

        width, height = image.size

        if width > 1000 and height > 1000:
            num_of_photos += 1
        else:
            num_no_photos += 1

    if num_no_photos > num_no_photos:
        print(os.path.abspath(foldername))

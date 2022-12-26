#!/usr/bin/python
from PIL import Image
import os, sys

target_path = "kutu_daun"
path = "C:/Users/Lenovo/3D Objects/New folder/dataset/" + target_path + "/"
dirs = os.listdir(path)

destination = path + "resize/"

i = 1

for item in dirs:
    if os.path.isfile(path + item):
        im = Image.open(path + item)
        f, e = os.path.splitext(path + item)
        im_resize = im.resize((224, 224), Image.ANTIALIAS)
        # im_resize.save(f + destination + str(i) + '.jpg', 'JPEG', quality=90)
        im_resize.save(destination + str(i) + '.jpg', 'JPEG', quality=90)
        i = i + 1
        print("succes resize: ", f)

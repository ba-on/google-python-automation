#!/usr/bin/env python3

# TODO: Test tomorrow with fresh lab, too tired to continue past 3:00AM

import os
from PIL import Image 

IMG_SOURCE = '/home/student-04-8997365d472f/supplier-data/images/'

for image in os.listdir(IMG_SOURCE):
    if image.endswith('.tiff'):
        file, ext = os.splitext(image)
        new_im = Image.open(image)
        new_im.convert("RGB").resize((600, 400)).save(IMG_SOURCE + file + '.jpeg', "JPEG")


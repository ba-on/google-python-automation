#!/usr/bin/env python3

import os
from PIL import Image 

IMG_SOURCE = '/home/student-04-8997365d472f/supplier-data/images/'

for image in os.listdir(IMG_SOURCE):
    if image.endswith('.tiff'):
        
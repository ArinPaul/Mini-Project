import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

data = 'Images'
category = ['MANGO']

flat_data = []
target = []

for i in category:
    path = os.path.join(data, i)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path,img))
        img_resize = resize(img_array,(50,50,3))
        
        flat_data.append(img_resize.flatten())
        target.append(i)
        
    




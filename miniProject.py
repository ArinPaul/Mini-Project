import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

data = '/Images'
category = ['MANGO']

for i in category:
    path = os.path.join(data, i)
    print(path)



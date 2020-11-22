import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

data = 'Images'
category = ['men','women']

flat_data = []
label = []

for i in category:
    path = os.path.join(data, i)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path,img))
        img_resize = resize(img_array,(300,300,3))
        
        flat_data.append(img_resize.flatten())
        label.append(i)
        
x_train,x_test,y_train,y_test = train_test_split(flat_data,label,random_state = 0)
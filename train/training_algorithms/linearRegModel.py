# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:03:35 2018

@author: Swarit
"""

from sklearn import linear_model
from PIL import Image
#to import image data

def getTestData():
    test_image_i = []
    try:
        img = Image.open("E:\\python ml\\coloring_images_ml\\test\\test_input_images\\abc.jpg") 
        w, h = img.size
            
        for i in range(0,w):
            for j in range(0,h):
                pixelI = img.getpixel((i,j))#input pixel getpixel() returns tuple always    
                test_image_i.append(pixelI)
        return test_image_i
    except:
        print("Image error.")

from coloring_images_ml.train import training_data_access

train_input, train_predict = training_data_access.get_train_data()

model = linear_model.LinearRegression()
model.fit(train_input, train_predict)

test_input = getTestData()
#print(test_input)
test_predict = model.predict(test_input)#returns list of prediction to make image

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:08:00 2018

@author: Swarit
"""
from sklearn import linear_model
#to import image data
from coloring_images_ml.train import training_data_access
from PIL import Image

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

train_input, train_predict = training_data_access.get_train_data()

model = linear_model.Ridge(alpha=0.5, normalize=True)
model.fit(train_input, train_predict)

test_input = getTestData()
test_predict = model.predict(test_input)
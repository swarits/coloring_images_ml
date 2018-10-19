# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:57:08 2018

@author: Swarit
"""
from PIL import Image

def get_train_data():
    #trainData = []#list tuples 2-D
    train_input_data = []
    train_predict_data = []
    try:
        train_imageI = Image.open("E:\\python ml\\coloring_images_ml\\train\\training_data\\input_images\\butterfly.jpg")
        train_imageP = Image.open("E:\\python ml\\coloring_images_ml\\train\\training_data\\predict_images\\butterfly.jpg")     
        train_input_data = list(train_imageI.getdata())
        train_predict_data = list(train_imageP.getdata())
        
        return train_input_data, train_predict_data
    except:
        print("Image error.")
        #trainImageP.show()


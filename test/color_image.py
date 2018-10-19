# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:41:52 2018

@author: Swarit
"""
from PIL import Image
import glob
"""
def get_test_data(current_img):
    test_image_i = []
    try:
        img = Image.open("E:\\python ml\\coloring_images_ml\\test\\test_input_images\\abc.jpg")
        w, h = img.size
            
        for i in range(0,h):
            for j in range(0,w):
                pixelI = img.getpixel((i,j))#input pixel getpixel() returns tuple always    
                test_image_i.append((pixelI[0], pixelI[1], pixelI[2]))
        return test_image_i #rowise return of rgb values in list
    except:
        print("Image error")
"""

def save_current_image(img, res):
    result = Image.new(img.mode, img.size)
    width, height = img.size
    count = 0
    for i in range(0,width):
        for j in range(0,height):
            r = int(res[count][0])
            g = int(res[count][1])
            b = int(res[count][2])
            result.putpixel( (i,j), (r,g,b) )
            count = count+1
    result.save("E:\\python ml\\coloring_images_ml\\result\\abc.jpg")
    
def lr_prediction():
    from coloring_images_ml.train.training_algorithms import linearRegModel
    for current_img in glob.glob("E:\\python ml\\coloring_images_ml\\test\\test_input_images\\*.jpg"):
        #test_input = get_test_data(current_img)#list      
        #test_predict = linearRegModel.model.predict(test_input)#2d list rgb
        save_current_image(Image.open(current_img), linearRegModel.test_predict)

def rr_prediction():
    from coloring_images_ml.train.training_algorithms import ridgeRegModel
    for current_img in glob.glob("E:\\python ml\\coloring_images_ml\\test\\test_input_images\\*.jpg"):
        save_current_image(Image.open(current_img), ridgeRegModel.test_predict)
        
def lassor_prediction():
    from coloring_images_ml.train.training_algorithms import lassoRegModel
    for current_img in glob.glob("E:\\python ml\\coloring_images_ml\\test\\test_input_images\\*.jpg"):
        save_current_image(Image.open(current_img), lassoRegModel.test_predict)



# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:14:57 2018

@author: Swarit
"""
#main program to choose type of algorithm for the prediction

def color_using_linearregression():
    from coloring_images_ml.test import color_image
    color_image.lr_prediction()
     
def color_using_ridgeregression():
    from coloring_images_ml.test import color_image
    color_image.rr_prediction()
    
def color_using_lassoregression():
    from coloring_images_ml.test import color_image
    color_image.lassor_prediction()
    
def main_function():
    choice = int(input("Enter 1(Linear Regression) 2(Ridge Regression) 3(Lasso Regression)"))
    if choice == 1:
        color_using_linearregression()
    elif choice==2:
        color_using_ridgeregression()
    elif choice==3:
        color_using_lassoregression()
        
main_function()
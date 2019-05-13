#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: abqader

Synthetic dataset creation. Overlays logos on top of images. Helps for object detection and recognition.. 
Also outputs CSV for Tensorflow object segmentation training. Follows CSVTrainer spec. 
"""
from PIL import Image
from random import randint
import os
import argparse
import csv
import BoundingBox as bx
        
def resizer(imgx, filename):
    """
    Returns: image array. Saves a resized file. 
    
    Parameter:  imgx: a path to the image you want to resize
                filename: path to where to save resized images
    Precondition:   imgx exists and is a string | filename is a path that exists
    """
    img = Image.open(imgx)
    
    basewidth = 100
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)  
    img.save(filename)
    return(img)


def transposer(foregroundImage,label):
    """
    Returns: an image array of 2 transposed images. Also saves the image to a path provided. 
    
    Parameter:  backgroundX: path to the dataset that will be the background images
                foregound : path to the image that will be on top of the background image
                filename: path of where you want the image to be saved
    Precondition:   backgroundX is a path that exists of a directory of images. 
                    foreground: is a path that exists of a TRANSPARENT image
                    filename: path that exists to save 
    """
    
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    backgroundX = dir_path + '/backgroundDirectory/'
    iterationer = 0
    filer = []

    for backgroundF in os.listdir(backgroundX):
        if backgroundF == '.DS_Store':
            continue 
        x = (randint(0, 100))
        y = (randint(0, 100))
        
        backgroundImage = backgroundX + (backgroundF )
        filename = dir_path + '/syntheticImages/' +str(iterationer) + '.jpg'
        
        background = Image.open(backgroundImage).convert("RGBA")
        foreground = Image.open(foregroundImage).convert("RGBA")
        background.paste(foreground, (x, y), foreground)
        background = background.convert("RGB")
        background.save(filename)
        
        width,height=foreground.size
        topLeft = (x,y)
        topRight = (x + width, y)
        bottomLeft = (x, y+ height)
        bottomRight = (x + width, y + height)
        
        text = writeLabel(topLeft, topRight, bottomLeft, bottomRight, iterationer, label)
        filer.append(text)
        iterationer = iterationer + 1
    
    csvWrite(filer, label)
    
    
def writeLabel(tl, tr, bl, br, iterx, logo):
   
    coord = (tl,tr,bl,br)
    bbox = bx.BoundingBox(coord)
    bbox = bbox.toArray()
    
    dirp = os.path.dirname(os.path.realpath(__file__))
    
    pathToImages = dirp + '/syntheticImages/' +str(iterx) + '.jpg'
    text = [pathToImages, str(bbox[0]), str(bbox[1]), str(bbox[2]), str(bbox[3]), logo]
    return(text)
    
    
def csvWrite(myData, label):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filePath = dir_path + '/csvFiles/' + str(label) + '.csv'
    filePathLabelFile = dir_path + '/csvFiles/' + 'label.csv'
    myDataLabel = [label, '0']
    myFile = open(filePath, 'w')  
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerows(myData)
    myFileX = open(filePathLabelFile, 'w')  
    with myFileX:  
        writer = csv.writer(myFileX)
        writer.writerow(myDataLabel)        


ap = argparse.ArgumentParser()#
ap.add_argument("-l", "--logo", required=True, help="Path to the logo image")
ap.add_argument("-x", "--label", required=True, help="Label (logo name)")


args = vars(ap.parse_args())
#
transposer(args["logo"], args["label"])

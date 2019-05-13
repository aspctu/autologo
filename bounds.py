#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:20:09 2018

@author: abqader
"""

import augmentor as ag
from imgaug import augmenters as iaa
import numpy as np
from PIL import Image

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "True")

def save(imageArray):
    cnt = 0
    for image in imageArray:
        im = Image.fromarray(image)
        im.save('/Users/abqader/Downloads/imagesCV/im' + str(cnt) + '.png')
        cnt += 1
        
def scaleImages(bottomCap, upperCap, image):
    scaleL, val = ag.scale('test', bottomCap)
    scaleH, val = ag.scale('test', upperCap)
    seqL = iaa.Sequential([scaleL])
    seqH = iaa.Sequential([scaleH])
    weak = (seqL.augment_image(image))
    extreme = (seqH.augment_image(image))
    return(weak, extreme)
    
def scaleImagesArray(bottomCap, upperCap, image, num = 6):
    images = []
    scaleValues = np.linspace(bottomCap, upperCap, num)
    
    # Create the first set of images with reduced scale 
    for value in scaleValues:
        scale, val = ag.scale('test', value)
        seq = iaa.Sequential([scale])
        newImage = (seq.augment_image(image))
        images.append(newImage)
    return(images)
    
def blurImages(bottomCap, upperCap, image):
    scaleL, val = ag.gaussian_blur('test', bottomCap)
    scaleH, val = ag.gaussian_blur('test', upperCap)
    seqL = iaa.Sequential([scaleL])
    seqH = iaa.Sequential([scaleH])
    weak = (seqL.augment_image(image))
    extreme = (seqH.augment_image(image))
    return(weak, extreme)
    
def blurImagesArray(bottomCap, upperCap, imageAr, num=10):
    imagesBlurred = []
    gaussianBlurValues = np.linspace(bottomCap, upperCap)
    for image in imageAr:
    # Create the first set of images with reduced scale 
        for value in gaussianBlurValues:
            blur, val = ag.gaussian_blur('test', value)
            seq = iaa.Sequential([blur])
            newImage = (seq.augment_image(image))
            imagesBlurred.append(newImage)
    return(imagesBlurred)

def warpImages(bottomCap, upperCap, image):
    scaleL, val = ag.affine_warp('test', bottomCap)
    scaleH, val = ag.affine_warp('test', upperCap)
    seqL = iaa.Sequential([scaleL])
    seqH = iaa.Sequential([scaleH])
    weak = (seqL.augment_image(image))
    extreme = (seqH.augment_image(image))
    return(weak, extreme)
    
def warpImagesArray(bottomCap, upperCap, imageAr, num = 6):
    images = []
    scaleValues = np.linspace(bottomCap, upperCap, num)
    for image in imageAr:
    # Create the first set of images with reduced scale 
        for value in scaleValues:
            scale, val = ag.affine_warp('test', value)
            seq = iaa.Sequential([scale])
            newImage = (seq.augment_image(image))
            images.append(newImage)
    return(images)



# Read image in (logo)
image = np.array(Image.open('/Users/abqader/Downloads/Chicago-Ventures.png'))

# Set values to produce scale measurements 
bottomCap = .1
upperCap = .7

weakImage, extremeImage = scaleImages(bottomCap, upperCap, image)

Image.fromarray(weakImage).show()

weakImageAns = input('Valid? ')

Image.fromarray(extremeImage).show()
extremeImageAns = input('Valid? ')
while(str2bool(weakImageAns) == False):
    bottomCap += .1
    weakImage, extremeImage = scaleImages(bottomCap, upperCap, image)
    Image.fromarray(weakImage).show()
    weakImageAns = input('Valid? ')
print('Done with lower end val')
while(str2bool(extremeImageAns) == False):
    upperCap -= .1
    weakImage, extremeImage  = scaleImages(bottomCap, upperCap, image)
    Image.fromarray(extremeImage).show()
    extremeImageAns = input('Valid? ')
print('Done with higher end val')
print('upperCap ', upperCap)
print('bottomCap ', bottomCap)

scaledImages = scaleImagesArray(bottomCap, upperCap, image)

# At this point, we have 6 images of the logo in varying scales 
blurbottomCap = 1.0
blurupperCap = 5.0

weakImage, _ = blurImages(blurbottomCap, blurupperCap, scaledImages[0])
_, extremeImage = (blurImages(blurbottomCap, blurupperCap, scaledImages[(len(scaledImages)-1)]))


Image.fromarray(weakImage).show()

weakImageAns = input('Valid? ')

Image.fromarray(extremeImage).show()
extremeImageAns = input('Valid? ')

while(str2bool(weakImageAns) == False):
    blurbottomCap += .1
    weakImage, _ = blurImages(blurbottomCap, blurupperCap, image)
    Image.fromarray(weakImage).show()
    weakImageAns = input('Valid? ')
print('Done with lower end val')


while(str2bool(extremeImageAns) == False):
    blurupperCap -= .1
    _, extremeImage = blurImages(blurbottomCap, blurupperCap, image)
    Image.fromarray(extremeImage).show()
    extremeImageAns = input('Valid? ')
print('Done with higher end val')
print('blurupperCap ', blurupperCap)
print('blurbottomCap ', blurbottomCap)


imagesBlurred = blurImagesArray(bottomCap, upperCap, scaledImages)

warpBottomCap = .01
warpUpperCap = .05

weakImage, _ = warpImages(warpBottomCap, warpUpperCap, imagesBlurred[0])
_, extremeImage = (warpImages(warpBottomCap, warpUpperCap, imagesBlurred[(len(imagesBlurred)-1)]))


Image.fromarray(weakImage).show()

weakImageAns = input('Valid? ')

Image.fromarray(extremeImage).show()
extremeImageAns = input('Valid? ')

while(str2bool(weakImageAns) == False):
    warpBottomCap += .01
    weakImage, _ = warpImages(warpBottomCap, warpUpperCap, imagesBlurred)
    Image.fromarray(weakImage).show()
    weakImageAns = input('Valid? ')
print('Done with lower end val')


while(str2bool(extremeImageAns) == False):
    warpUpperCap -= .01
    _, extremeImage = warpImages(warpBottomCap, warpUpperCap, imagesBlurred)
    Image.fromarray(extremeImage).show()
    extremeImageAns = input('Valid? ')
print('Done with higher end val')
print('blurupperCap ', warpUpperCap)
print('blurbottomCap ', warpBottomCap)

imagesWarped = warpImagesArray(warpBottomCap, warpUpperCap, imagesBlurred)

save(imagesWarped)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abqader
"""

import imgaug
from imgaug import augmenters as iaa
import numpy as np
from PIL import Image

def show_image(imageArray):
    '''
    Converts Numpy array into an image
    
    imageArray : Numpy array of image
    
    Returns: PIL object of imageArray
    '''
    return(Image.fromarray(imageArray))
    
    
def brightness(origImage, value):
    '''
    Increases/decreases brightness of image 
    
    origImage: Array of image pixels as numpy array
    value: Value to add all pixels by 
    
    Returns: Augmented image array (with added/decreased brightess),
            value
    '''
    return(iaa.Add(value), value)
    
def scale(origImage, value):
    '''
    Increases/decreases size of image via percentage of orginal image
    
    origImage: Array of image pixels as numpy array
    value: Percent of original image to scale to (as a decimal like)
    
    Returns: Scaled image array, value
    '''
    return(iaa.Scale(value), value)
    
def flip_horizontal(origImage, value = None ):
    '''
    Flips the image horizontal 
    
    origImage: Array of image pixels as numpy array
    value: None 
    
    Returns: Augmented image array flipped horizontally, value
    '''
    return(iaa.Fliplr(1.0), value)

def flip_vertical(origImage, value = None):
    '''
    Flips the image vertical
    
    origImage: Array of image pixels as numpy array
    value: None 

    Returns: Augmented image array flipped vertically, value
    '''
    return(iaa.Flipud(1.0), value)

# Exprimental; further testing needed    
def superpixel_blurring(origImage, value):
    return(iaa.Superpixels(p_replace = (0.0, 0.5), n_segments=value), value)
    

def hue(origImage, value):
    '''
    Increases/decreeases the hue of the image
    
    origImage: Array of image pixels as numpy array
    value: Value to add/subtract hue by  

    Returns: Augmented image array with hue changed, value
    '''
    
    aug = iaa.Sequential([
            iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
            iaa.WithChannels(0, iaa.Add(value)),
            iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
    ])
    return(aug, value)
    
def saturation(origImage, value):
    '''
    Increases/decreeases the saturation of the image
    
    origImage: Array of image pixels as numpy array
    value: Value to add/subtract saturation by  

    Returns: Augmented image array with saturation changed , value
    '''
    
    aug = iaa.Sequential([
            iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
            iaa.WithChannels(1, iaa.Add(value)),
            iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
    ])
    return(aug, value)

def grayscale(origImage, value):
    '''
    Converts image to grayscale with color overlay 
    
    origImage: Array of image pixels as numpy array
    value: How much of the color overlay is needed 

    Returns: Augmented image array as grayscale , value
    '''
    assert 0.00 <= value <= 1.0, "Expected value to be in between 0 and 1, got %d." % (int(value),)
    return(iaa.Grayscale(alpha=value), value)
    
def gaussian_blur(origImage, value):
    return(iaa.GaussianBlur(sigma = value), value)

    
def median_blur(origImage, value):
    '''
    Blur an image by computing median values over neighbourhoods.
    
    origImage: Array of image pixels as numpy array
    value: Represents the length and height (value x value) of the blurring convolution

    Returns: Augmented image array with median blur, value
    '''
    assert value % 2 != 0, "Expected value to be odd, got %d. Add or subtract 1." % (int(value),)
    return(iaa.MedianBlur(k=value), value)
    
def sharpen(origImage, value):
    assert 0.0 <= value <= 1.0, "Expected value to be in between 0.0 and 1.0, got %d" % (int(value),)
    return(iaa.Sharpen(alpha=value, lightness=1.0), value)
    
def add_element_noise(origImage, value):
    '''
    Add values to the pixels of images with possibly different values for neighbouring pixels.

    origImage : Array of image pixels as numpy array
    value : Is a postive integer than is used as the upper bound to a random value generator for noise
    
    Returns: Augmented image array with added pixel noise
    '''
    return(iaa.AddElementwise((-value, value)), value)
    
def add_gaussian_noise(origImage, value):
    '''
    Add gaussian noise (aka white noise) to images.
    
    origImage: 
    
    '''
    return(iaa.AdditiveGaussianNoise(scale=(0, value*255)), value)
    


def dropout(origImage, value):
    '''
    Augmenter that sets a certain fraction of pixels in images to zero.

    '''
    
    return(iaa.Dropout(p=value), value)
    
def contrast_normalization(origImage, value):
    '''
    Augmenter that changes the contrast of images.
    
    '''
    return(iaa.ContrastNormalization(value), value)
    

def affine_warp(origImage, value, nb_size = 4):
    return((iaa.PiecewiseAffine(scale = value, nb_rows = nb_size, nb_cols=nb_size), value))

def elastic_distortion(origImage, value, sigma=0.25):
    return(iaa.ElasticTransformation(alpha=value, sigma=0.25), value)

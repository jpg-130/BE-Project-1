# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:37:22 2020

@author: JigDhwani
"""

#FUNCTION: return skin segmented images
def skin_segmentation(image):
    # define the upper and lower boundaries of the HSV pixel
    # intensities to be considered 'skin'
    lower = np.array([0, 48, 80], dtype = "uint8")
    upper = np.array([20, 255, 255], dtype = "uint8")
    
    # resize the frame, convert it to the HSV color space,
    # and determine the HSV pixel intensities that fall into
    # the speicifed upper and lower boundaries
    frame = imutils.resize(image, width = 400)
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)
    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(frame, frame, mask = skinMask)
    # show the skin in the image along with the mask
    cv2.imshow("images", np.hstack([frame, skin]))
    return skin

# SAVE SEGMENTED IMAGES
import glob
all_imgs = set(glob.glob('all_images/*/*/*'))
print(glob.glob('all_images/*/*/*'))

import os
path = os.path('all_images\\original\\negative')

path_original = 'all_images/original'
path_skin_segmentation = 'all_images/segmented_image'

#FUNCTION: create directory if not existing
def create_dir(directory):
if not os.path.exists(directory):
    os.makedirs(directory)
#make directory for segmented images
create_dir(path_skin_segmentation)

#FUNCTION: get all subdirectories in a directory
def get_subdirectory(current_dir):
    return [os.path.basename(x[0]) for x in os.walk(current_dir)][1:]
#subdirectories in path_original
print(get_subdirectory(path_original))


for dirname in os.listdir(path_original):
    for filename in os.listdir(os.path.join(path_original, dirname)):
        print(filename)

#save image at path
cv2.imwrite(path, image)

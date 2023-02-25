import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

#Translation
def translateImg(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

#-x-->Go Left
#-y-->Go Up
#x-->Go Right
#y-->Go Down

translated=translateImg(img,-250, 200)
cv.imshow('Translated Image',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint == None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions=(width,height)
    return cv.warpAffine(img, rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated Image',rotated)

rotated_rotated=rotate(img, -90)
cv.imshow('Rotated Image',rotated_rotated)

#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image',resized)

#Flipping
flip=cv.flip(img,0)
# flip=cv.flip(img,1) -->Flipping about y
# flip=cv.flip(img,-1)-->Flipping about x and y
cv.imshow('Flipping about x',flip)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped Image',cropped)

cv.waitKey(0)
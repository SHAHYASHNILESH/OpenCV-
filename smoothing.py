import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

#Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

#Gaussian
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median
#Higher value of Kernel size can result in smurging the image
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral
#Higher value of sigma space can result in smurging the image
bilateral=cv.bilateralFilter(img, 15,35,25)
cv.imshow('Bilateral Blur',bilateral)

cv.waitKey(0)
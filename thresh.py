import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholded Image',thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Thresholded Image',thresh_inv)

#Adaptive thresholding-->essentially computed optimal threshold value on the basis of the mean
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
cv.imshow('Adaptive Thresholded Image',adaptive_thresh)

adaptive_thresh_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Inverse Adaptive Thresholded Image',adaptive_thresh_inv)

cv.waitKey(0)
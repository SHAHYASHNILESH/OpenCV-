import cv2 as cv
import numpy as np

#Contours is boundary detection
#Contours is not similar to Edges

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale Image',gray)

blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#Thresholding is to binarize an image and convert it to binary form
#If the value is less than 125, then image will be 0(Black) and if the value is greater than 125,then image will be 1(White)
# ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresh Image',thresh)
# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(len(contours))

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

contours_drawn=cv.drawContours(blank, contours,-1,(0,0,244),thickness=1)
cv.imshow('Contours Drawn',contours_drawn)

cv.waitKey(0)
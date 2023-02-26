import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_image=cv.merge([b,g,r])
cv.imshow('Merged Image',merged_image)

cv.waitKey(0)

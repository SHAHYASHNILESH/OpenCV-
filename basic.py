import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#Converting image to Gray Scale Image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)

#Blur
#ksize is assigned always an odd value
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur Image',blur)

#Edge Cascades
canny=cv.Canny(blur,125,175)
cv.imshow('Edge Cascaded Image',canny)

#Dialating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated Image',dilated)

#Eroding Image
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded Image',eroded)

#Resize Image
#Shrinking Image-->INTER_AREA(Default)
#Increasing Image-->INTER_LINEAR OR INTER_CUBIC(Slower but gives better results)
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image',resized)

#Cropping Image
cropped=img[50:200,200:400]
cv.imshow('Cropped Image',cropped)

cv.waitKey(0)
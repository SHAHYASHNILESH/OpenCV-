import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#Paint the image a certain colour
blank[200:300,300:400]=0,0,255
#cv.imshow('Red',blank)

#Draw rectangle on Image
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

#Draw Circle on Image
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)

#Draw Line on Image
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=6)
cv.imshow('Line',blank)

#Put Text on Image
cv.putText(blank,'Hello World',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),2)
cv.imshow('Text',blank)

cv.waitKey(0)
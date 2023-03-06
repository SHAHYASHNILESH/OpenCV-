import cv2 as cv
import time
import os

wCam,hCam=640,480

cap=cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success,img=cap.read()
    cv.imshow('Image',img)
    cv.waitKey(1)
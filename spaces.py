import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

#OpenCV has Default Image as bgr
#MatplotLib has default Image as rgb

# plt.imshow(img)
# plt.show()

#BGR TO GRAY
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)

#BGR TO HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV Image',hsv)

#BGR TO LAB(L*A*B)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB Image',lab)

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB Image',rgb)

#HSV TO BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV->BGR',hsv_bgr)

#LAB TO BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB->BGR',lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)

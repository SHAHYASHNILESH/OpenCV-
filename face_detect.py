import cv2 as cv

#Haar Cascade is sensitive to noise

img=cv.imread('Photos/group 2.jpg')
cv.imshow('Group of 5 people',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray People',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Faces Detected',img)

cv.waitKey(0)
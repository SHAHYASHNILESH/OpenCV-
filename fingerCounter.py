import cv2 as cv
import time
import os
import handTracking as htm

wCam,hCam=640,480

cap=cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath="FingerImages"
myList=os.listdir(folderPath)
print(myList)
overlayList=[]
for imPath in myList:
    image=cv.imread(f'{folderPath}/{imPath}')
    # print(image)
    overlayList.append(image)

pTime=0
detector=htm.HandDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)

    if len(lmList)!=0:
        fingers=[]

        #Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #Four Fingers
        for id in range(1,5):
          if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
            fingers.append(1)
          else:
            fingers.append(0)
        #print(fingers)
        totalFingers=fingers.count(1)
        print(totalFingers)
        cv.rectangle(img,(20,225),(170,425),(0,255,0),cv.FILLED)
        cv.putText(img,str(totalFingers),(45,375),cv.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
        


    # h,w,c=overlayList[3].shape
    # img[0:h,0:w]=overlayList[3]
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img, str(int(fps)), (400, 70),
               cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Image',img)
    cv.waitKey(1)
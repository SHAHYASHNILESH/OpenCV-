import cv2 as cv

img=cv.imread('Photos/cat.jpg')

def rescaleFrame(frame,scale=0.75):
    #Works for Videos,images,Live Videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.imshow('Cat',img)
resized_img=rescaleFrame(img)
cv.imshow('Cat Resized',resized_img)
# cv.waitKey(0)

def changeRes(width,height):
    #Works for Live Videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
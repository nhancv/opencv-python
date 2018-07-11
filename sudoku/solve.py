
import cv2 as cv
import numpy as np
import letter_recog

#500x500
padding = 3
image = cv.imread("test2.jpg")[padding:-padding,padding:-padding]
height, width, channels = image.shape
cellW = width/9
cellH = height/9

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# gray = cv.GaussianBlur(gray, (11, 11), 0)
outerBox = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2)
outerBox = cv.bitwise_not(outerBox)

# cv.imshow('outerBox', outerBox)

y=2
x=4
box = outerBox[cellH*y + padding:cellH*(y+1) - padding, cellW*x + padding:cellW*(x+1) - padding]
# cv.imshow('box', box)
_, contours, _ = cv.findContours(box, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    [x,y,w,h] = cv.boundingRect(cnt)
    if(h>15):
	    # cv.rectangle(box,(x,y),(x+w,y+h),(255,255,255),1)
	    roi = box[y:y+h,x:x+w]
	    roismall = cv.resize(roi,(50,50))
	    cv.imshow('roismall', roismall)
	    letter_recog.recog(roismall)


for x in range(0, 9):
	box = outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)]

	# cv.imshow("box {0}".format(x+1), outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)])

cv.waitKey(0)
cv.destroyAllWindows()

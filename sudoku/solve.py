
import cv2
import numpy as np

#500x500
image = cv2.imread("test2.jpg")
height, width, channels = image.shape
cellW = width/9
cellH = height/9

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (11, 11), 0)
outerBox = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
outerBox = cv2.bitwise_not(outerBox)

cv2.imshow('outerBox', outerBox)

x=0
box = outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)]
cv2.imshow('box', box)


for x in range(0, 9):
	box = outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)]
	# cv2.imshow("box {0}".format(x+1), outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)])

cv2.waitKey(0)
cv2.destroyAllWindows()

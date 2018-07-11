
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

def n10():
	img = np.zeros((50, 50, 3), np.uint8)*255
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	roi = img[:,:]
	return roi

def getLetter(box):
    _, contours, _ = cv.findContours(box, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        [x,y,w,h] = cv.boundingRect(cnt)
        if(h>15):
            roi = box[y:y+h,x:x+w]
            roi = cv.resize(roi,(50,50))
            return roi
    return n10()

board = np.empty((0, 2500))
for i in range(0, 9):
	for j in range(0, 9):
		box = outerBox[cellH*i + padding:cellH*(i+1) - padding, cellW*j + padding:cellW*(j+1) - padding]
		roi = getLetter(box)
		board = np.append(board, [roi.ravel()], axis=0)
		# cv.imshow("box {0}x{1}".format(i, j), box)

result = letter_recog.recogBoard(board)
result = np.reshape(result, (-1, 9))
result = np.vectorize(lambda t: 0 if t == 10 else t)(result)
print(result)
# cv.waitKey(0)
# cv.destroyAllWindows()

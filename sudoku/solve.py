
import cv2 as cv
import numpy as np
import letter_recog
import su_board
#500x500
padding = 5

def preprocessImg(image):
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	# gray = cv.GaussianBlur(gray, (11, 11), 0)
	# outerBox = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2)
	ret,thresh = cv.threshold(gray,128,255,cv.THRESH_BINARY)
	outerBox = cv.bitwise_not(thresh)
	cv.imshow('thresh', outerBox)
	return outerBox

def n10():
	img = np.zeros((50, 50, 3), np.uint8)*255
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	roi = img[:,:]
	return roi

def getRoi(box):
    _, contours, _ = cv.findContours(box, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        [x,y,w,h] = cv.boundingRect(cnt)
        if(h > 15 and w > 5 and x > padding/2 and y > padding/2):
            roi = box[y:y+h,x:x+w]
            roi = cv.resize(roi,(50,50))
            return roi
    return n10()

def getBox(img, i, j): 
	height, width, channels = image.shape
	cellW = width/9
	cellH = height/9
	box = img[cellH*i + padding:cellH*(i+1) - padding, cellW*j + padding:cellW*(j+1) - padding]
	return box

if __name__ == '__main__':
	import getopt
	import sys

	args, dummy = getopt.getopt(sys.argv[1:], '', ['img='])
	args = dict(args)
	args.setdefault('--img', 'test3.jpg')

	#process image to board
	image = cv.imread(args['--img'])
	outerBox = preprocessImg(image)
	imgBoard = np.empty((0, 2500))
	for i in range(0, 9):
		for j in range(0, 9):
			box = getBox(outerBox, i,j)
			roi = getRoi(box)
			imgBoard = np.append(imgBoard, [roi.ravel()], axis=0)
			# cv.imshow("box {0}x{1}".format(i, j), roi)

	board = letter_recog.recogBoard(imgBoard)
	board = np.reshape(board, (-1, 9 if len(board) > 9 else len(board)))
	board = np.vectorize(lambda t: 0 if t == 10 else t)(board)
	print(board)

	#find solution depend on board
	if(su_board.solveSDKBoard(board) == True):
		print('result:')
		print(board)
	else:
		print('no solution')


	cv.waitKey(0)




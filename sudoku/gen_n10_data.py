import numpy as np
import cv2 as cv


fileName = "n10.data"

def gendata():
	img = np.zeros((50, 50, 3), np.uint8)*255
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	roi = img[:,:]
	roi_1 = np.append([10], roi)
	roi_2 = np.append([10], cv.bitwise_not(roi))
	res = np.array([roi_1,roi_2])
	np.savetxt(fileName, res, delimiter=',', fmt='%u')
	print("Generate data completed")
	# [10, cv.bitwise_not(roi)]])

gendata()


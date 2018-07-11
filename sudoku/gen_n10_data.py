import numpy as np
import cv2 as cv


fileName = "n10.data"

def gendata():
	img = np.zeros((50, 50, 3), np.uint8)*255
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	roi = img[:,:]
	res = np.array([10])
	res = np.append(res, roi)
	np.savetxt(fileName, [res], delimiter=',', fmt='%u')
	print("Generate data completed")

gendata()


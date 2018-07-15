
import cv2 as cv
import numpy as np

#500x500
padding = 5
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

def saveData(data, number=10):
    res = np.array([number])
    res = np.append(res, data)
    np.savetxt("n%s.data" % number, [res], delimiter=',', fmt='%u')

#For gen train data
def genData(img, i, j, num = 1):
	box = getBox(img, i,j)
	roi = getRoi(box)
	cv.imshow("roi {0}x{1}".format(i, j), roi)
	saveData(np.float32(np.array([roi.ravel()])), num)

if __name__ == '__main__':

	image = cv.imread("test3/test3.jpg")
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	# gray = cv.GaussianBlur(gray, (11, 11), 0)
	# outerBox = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2)
	ret,thresh = cv.threshold(gray,128,255,cv.THRESH_BINARY)
	outerBox = cv.bitwise_not(thresh)
	cv.imshow('thresh', outerBox)

	test1_pic = {'1':(2, 8),'2':(0, 6),'3':(0, 5),'4':(2, 0),'5':(1, 1),'6':(0,2),'7':(0,3),'8':(1,2),'9':(2,4)}
	test2_pic = {'1':(0, 0),'2':(1, 4),'3':(2, 8),'4':(2, 3),'5':(2, 4),'6':(1,2),'7':(2,0),'8':(2,1),'9':(2,2)}
	test3_pic = {'1':(7,4),'2':(6,6),'3':(4,5),'4':(7,3),'5':(7,8),'6':(6,1),'7':(5,0),'8':(8,4),'9':(7,5)}
	test4_pic = {'1':(7,4),'2':(7, 2),'3':(6, 8),'4':(8,4),'5':(1, 8),'7':(6,7),'8':(1,7),'9':(8,8)}
	a_dict = test3_pic
	for label in a_dict:
		i, j = a_dict[label]
		num =  int(label)
		genData(outerBox, i, j, num)


	cv.waitKey(0)

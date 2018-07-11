import numpy as np
import cv2 as cv


fileName = "digits.data"
np.savetxt(fileName, [])
f=open(fileName,'a')

def gendata(number):
	# create blank image - y, x
	img = np.zeros((50, 50, 3), np.uint8)*255
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	# setup text
	font = cv.FONT_HERSHEY_SIMPLEX
	font_scale = 0.55
	margin = 5
	thickness = 2
	color = (255, 255, 255)

	text = str(number)
	size = cv.getTextSize(text, font, font_scale, thickness)

	# get boundary of this text
	textsize = cv.getTextSize(text, font, 1, 2)[0]
	# get coords based on boundary
	textX = (img.shape[1] - textsize[0]) / 2
	textY = (img.shape[0] + textsize[1]) / 2
	# add text centered on image
	cv.putText(img, text, (textX, textY ), font, 1, (255, 255, 255), 2)
	# img = np.invert(img)
	# cv.imshow('img', img)
	_, contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
	    [x,y,w,h] = cv.boundingRect(cnt)
    	if(h > 15 and w > 5 and x > padding/2 and y > padding/2):
		    # cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),1)
		    roi = img[y:y+h,x:x+w]
		    roismall = cv.resize(roi,(50,50))
		    # cv.imshow('roismall', roismall)
		    res = np.array([number])
		    res = np.append(res, roismall.ravel())
		    np.savetxt(f, [res], delimiter=',', fmt='%u')

for x in range(1, 10):
	gendata(x)
	
print("Generate data completed")

f.close()


# cv.waitKey(0)
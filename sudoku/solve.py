
import cv2 as cv
import numpy as np
# import os
# os.system("letter_recog.py")


SZ=20
bin_n = 16 # Number of bins


affine_flags = cv.WARP_INVERSE_MAP|cv.INTER_LINEAR

## [deskew]
def deskew(img):
    m = cv.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img
## [deskew]

## [hog]
def hog(img):
    gx = cv.Sobel(img, cv.CV_32F, 1, 0)
    gy = cv.Sobel(img, cv.CV_32F, 0, 1)
    mag, ang = cv.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist
## [hog]
# help(cv.ml)


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

cv.imshow('outerBox', outerBox)

x=2
box = outerBox[cellH*x + padding:cellH*(x+1) -padding, cellW*x + padding:cellW*(x+1) - padding]
# cv.imshow('box', box)

svm = cv.ml.SVM_load("svm_data.dat")
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setType(cv.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)

# Preprocessing: this image is inverted compared to the training data
# Here it is inverted back
# img_predict = np.invert(box)

# Preprocessing: it also has a completely different size
# This resizes it to the same size as the training data
img_predict = cv.resize(box, (20, 20), interpolation=cv.INTER_CUBIC)
cv.imshow('img_predict', img_predict)
# Extract the features
img_predict_ready = np.float32(hog(deskew(img_predict)))
img_arr = np.array([img_predict_ready])
print(img_arr)

# Run the prediction
prediction = svm.predict(img_arr)[1]
print(prediction)

for x in range(0, 9):
	box = outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)]

	# cv.imshow("box {0}".format(x+1), outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)])

cv.waitKey(0)
cv.destroyAllWindows()

from glob import iglob
import cv2 as cv

image=cv.imread('Cat03.jpg')
image_gray=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh=cv.threshold(image_gray, 127, 255, 0)

cv.imshow('Image', thresh)
cv.waitKey(0)

contours, hierarchy=cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

image=cv.drawContours(image, contours, -1, (0,255,0), 4)

cv.imshow('image', image)
cv.waitKey(0)
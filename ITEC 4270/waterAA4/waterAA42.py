import cv2
import numpy

img = cv2.imread('num13.png')

whiteboundary = ([250, 250, 250], [255, 255, 255 ])
blueboundary =([235, 90, 10], [245, 100, 20 ])

lowerbluebgr = numpy.array(blueboundary[0], dtype='uint8')
upperbluebgr = numpy.array(blueboundary[1], dtype='uint8')

mask = cv2.InRange(img, lowerbluebgr, upperbluebgr)
outputimage = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("finding blue", numpy.hstack([img, outputimage]))

cv2.waitKey(0)
import cv2
import numpy as np
import matplotlib.pyplot as plt


#0. Load images
#imaExam1 = cv2.imread('Images/Cal_1.jpg',0)
imaExam2 = cv2.imread('Images/Cal_2.jpg',0)
#imaExam3 = cv2.imread('Images/Cal_3.jpg',0)

#1. Canny
can = cv2.Canny(imaExam2,20,150)
kernel = np.ones((5,5),np.uint8)
bordes = cv2.dilate(can, kernel)

#contorno
contour,_ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#dibujar contornos
objects = bordes.copy()
cv2.drawContours(objects, [max(contour, key = cv2.contourArea)], -1,255,thickness=-1)

#get labels
output = cv2.connectedComponentsWithStats(objects,4,cv2.CV_32S)
cantObj = output[0]
labels = output[1]
stats = output[2]

#Get ArgMax
mask = np.uint8(255*(np.argmax(stats[:,4][1:])+1==labels))
contours,_ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

#convexhull
hull = cv2.convexHull(cnt)
puntoConvex = hull[:,0,:]
m,n = mask.shape
ar = np.zeros((m,n))
mascara_convex = np.uint8(cv2.fillConvexPoly(ar, puntoConvex,1))


cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('images/A.jpg')
img2 = cv2.imread('images/B.jpg')

I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
umbral1,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
mascara1 = np.uint8((I<umbral1)+255)

J = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
umbral2,_ = cv2.threshold(J,0,255,cv2.THRESH_OTSU)
mascara2 = np.uint8((J<umbral2)+255)

cv2.imshow("Img1-COLOR",img1)
cv2.imshow("Img1-GRAY",I)
cv2.imshow("Img1-BINARY",mascara1)

cv2.imshow("Img2-COLOR",img2)
cv2.imshow("Img2-GRAY",J)
cv2.imshow("Img2-BINARY",mascara2)

suma1 = np.sum(img1)
min1 = np.min(img1)
max1 = np.max(img1)
prom1 = np.mean(img1)
var1 = np.var(img1)
de1 = np.sqrt(var1)

suma2 = np.sum(img2)
min2 = np.min(img2)
max2 = np.max(img2)
prom2 = np.mean(img2)
var2 = np.var(img2)
de2 = np.sqrt(var2)

data = I.flatten()
plt.hist(data, bins=100)
red1 = img1[:,:,0].flatten()
green1 = img1[:,:,1].flatten()
blue1 =  img1[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red1, bins=1000, histtype="stepfilled", color="red")
plt.hist(green1, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue1, bins=1000, histtype="stepfilled", color="blue")

data = J.flatten()
plt.hist(data, bins=100)
red2 = img2[:,:,0].flatten()
green2 = img2[:,:,1].flatten()
blue2 =  img2[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red2, bins=1000, histtype="stepfilled", color="red")
plt.hist(green2, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue2, bins=1000, histtype="stepfilled", color="blue")

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

file = "bankdetails.png"

im1 = cv2.imread(file,0)
im = cv2.imread(file)

ret,thresh_value = cv2.threshold(im1,180,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)

contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

plt.imshow(im)
cv2.namedWindow('detecttable', cv2.WINDOW_NORMAL)
cv2.imwrite('detecttable.jpg',im)


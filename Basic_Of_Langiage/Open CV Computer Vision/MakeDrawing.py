import cv2 
import numpy as np

img = np.zeros((512,512,3))
cv2.rectangle(img,pt1=(100,100),pt2=(200,200),color=(255,0,0),thickness=-1)
cv2.circle(img,center=(100,500),radius=50,color=(0,255,0),thickness=-1)
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(0,0,255))
cv2.imshow("window",img)
cv2.waitKey(0)
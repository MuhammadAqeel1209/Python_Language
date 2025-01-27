import numpy as np
import cv2

#Read the Images 👇👇👇
img = cv2.imread('img/one.jpeg')
# print(img)
# print(type(img))
# print(img.shape)

# cv2.imshow("window",img)
# cv2.waitKey(0)

# Convert to gray scale Image
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("window",imgGray)
# cv2.waitKey(0)

#Playing with RGC Color Channels

# img[:,:,0] = 0 # Blue Channel Completely Zero
# img[:,:,1] = 0 # Green Channel Completely Zero
# img[:,:,2] = 0 # Red Channel Completely Zero

# imgBlue = img[:,:,0] # Blue Channel Completely Zero
# imgGreen = img[:,:,1]# Green Channel Completely Zero
# imgRed =  img[:,:,2]# Red Channel Completely Zero

# imgcomb = np.hstack((imgBlue,imgGreen,imgRed))


# Resizing the image 
img_resize = cv2.resize(img,(256,256))
# print(img_resize.shape)

# Flip the Image --> Rotate the images
# img_flip = cv2.flip(img_resize,0) # 0 --> Total complete rotate Vertical Axis
# img_flip = cv2.flip(img_resize,1) # 1 -->  Horizontal Axis
# img_flip = cv2.flip(img_resize,-1) # -1 -->  Both Flips Horizaontal and Vertical Axis


# Crop the image 
img_crop = img[100 : 300 , 500 : 700]

cv2.imshow("window",img_crop)
cv2.waitKey(0)
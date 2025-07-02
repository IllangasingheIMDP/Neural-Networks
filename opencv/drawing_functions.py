import cv2
import numpy as np
#img =cv2.imread('lena.jpg',1)
#can create a image by numpy zero method
img = np.zeros([512,512,3],np.uint8)
#line on image
img=cv2.line(img,(0,0),(255,255),(255,30,0),2)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),2)
img=cv2.rectangle(img,(384,0),(0,384),(0,0,255),4) # pt1top left vertex.instead of tickness -1 fill
img =cv2.circle(img, (400,400),50,(0,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"First Image On opencv",(0,500),font,1,(100,40,60),2,cv2.LINE_AA)

#eclipse and polygon are here too
cv2.imshow('image',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
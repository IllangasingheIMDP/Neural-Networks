import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        width=int(cap.get(3))
        height=int(cap.get(4))
        
        
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #colors to extract
        
        lower_blue=np.array([90,50,50])
        upper_blue=np.array([130,255,255])
        # mask only contains pixels of the given range
        mask=cv2.inRange(hsv,lower_blue,upper_blue)
        
        result=cv2.bitwise_and(frame,frame,mask=mask)
        
        
        cv2.imshow('image',result)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
#one pixel image,this will create an one pizel image.
# BGR_color=np.array([[[255,0,0]]])
# x=cv2.cvtColor(BGR_color,cv2.COLOR_BGR2HSV)
# below is how you access one pixel
# x[0][0]








cap.release()
cv2.destroyAllWindows()
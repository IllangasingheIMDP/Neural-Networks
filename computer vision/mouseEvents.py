import cv2
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='X:'+str(x)+", Y:"+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,0,0),2)
        cv2.imshow('img',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(blue)+', '+str(green)+', '+str(red)
        cv2.putText(img,text,(x,y),font,0.5,(200,100,90),2)
        cv2.imshow('img',img)
    
    
#img = np.zeros((512,512,3),np.uint8)
img=cv2.imread('lena.jpg',1)
cv2.imshow('img',img)

cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
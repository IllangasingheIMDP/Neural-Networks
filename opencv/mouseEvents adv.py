import cv2
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        # This will create a connected graph
        #cv2.circle(img,(x,y),3,(100,100,100),-1)
        #points.append((x,y))
        #if len(points) >=2:
        #    cv2.line(img,points[-1],points[-2],(255,0,0),4)
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        color_image=np.zeros((512,512,3),np.uint8)
        color_image[:]=[blue,green,red] #fill every color
        
        
        cv2.imshow('color',color_image)
   
    
    
#img = np.zeros((512,512,3),np.uint8)
img=cv2.imread('lena.jpg',1)
cv2.imshow('img',img)
points=[]
cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
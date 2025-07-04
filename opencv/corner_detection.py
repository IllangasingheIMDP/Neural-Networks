import cv2
import numpy as np

img=cv2.imread('lena.jpg',1)
# img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)

#corner works great on gray scales
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)
#gives floating point values

corners =np.int0(corners)
#ravel flattens all.[[1,2],[2,4]]=[1,2,2,4]
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1=tuple(corners[i].ravel())
        corner2=tuple(corners[j].ravel())
        #random color
        color=tuple(map(lambda x:int(x),np.random.randint(0,255,size=3)))
        cv2.line(img,corner1,corner2,color,1)
        

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows
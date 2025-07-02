import cv2
import datetime
cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font=cv2.FONT_HERSHEY_PLAIN
        datet=str(datetime.datetime.now())
        text='Width :'+str(cap.get(3)) +"  Height:"+str(cap.get(4))
        
        frame = cv2.putText(frame,datet,(0,200),font,1,(0,255,0),1,cv2.LINE_AA)
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
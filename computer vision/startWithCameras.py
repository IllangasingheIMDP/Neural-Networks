import cv2
cap =cv2.VideoCapture(0) #input file name or avi/mp4 ,or index of camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('firstvid.avi',fourcc,20.0,(640,480)) #fourcc is codec.frame =20,size

while(cap.isOpened()):
    ret,frame=cap.read() #ret is true or false if frame is aving.
    if(ret==True):
        out.write(frame)
    #get
    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

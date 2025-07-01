import cv2
img = cv2.imread('lena.jpg',0) # 0,1,-1 specifies the way images read.1=loads a color image,0=gray scale,-1=including alpha channel
cv2.imshow('image show',img)
k=cv2.waitKey(5000) & 0xFF #key capturing 0xff for 64 bit
if k==27: #escape key
    cv2.destroyAllWindows() # all window
elif k==ord('s'):

#write image to file

    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()



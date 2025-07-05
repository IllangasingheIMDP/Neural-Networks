import cv2
import numpy as np

img=cv2.imread('soccer_practice.jpg',0)
img=cv2.resize(img,(0,0),fx=0.6,fy=0.6)
template=cv2.imread('shoe.png',0)
template=cv2.resize(template,(0,0),fx=0.6,fy=0.6)


#for gray scale it only contains (height,width)
#for color image it contains channels too.
h,w=template.shape


# cv2.TM_SQDIFF:        Sum of squared differences. Best match has minimum value.
# cv2.TM_SQDIFF_NORMED: Normalized version of TM_SQDIFF. Best match has minimum value.
# cv2.TM_CCORR:         Cross-correlation. Best match has maximum value.
# cv2.TM_CCORR_NORMED:  Normalized cross-correlation. Best match has maximum value.
# cv2.TM_CCOEFF:        Correlation coefficient. Best match has maximum value.
# cv2.TM_CCOEFF_NORMED: Normalized correlation coefficient. Best match has maximum value.

# Try with all an get the best

methods=[cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED]

for method in methods:
    img2=img.copy()
    
    result=cv2.matchTemplate(img2,template,method)
    #used convolution here
    # the rsult will contain a 2d array (like an image)
    # its shape will be (W-w+1,H-h+1)
    # W,H is the base image
    # w,h is template image
    min_val,max_val,min_loc,max_loc =cv2.minMaxLoc(result)
    print(min_loc,max_loc)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc
    bottom_right=(location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)  
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    
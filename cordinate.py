import cv2
import numpy as np
import sys
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print events
imo=cv2.imread(sys.argv[1],1)
im=np.array(imo)

def retrgb(event,x,y,flag,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print("x= ",x," y= ",y)		
        print ("************* \n")

cv2.imshow('win',imo)
cv2.setMouseCallback("win",retrgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

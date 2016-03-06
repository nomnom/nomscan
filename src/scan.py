#!/usr/bin/python


import cv2 as cv
import numpy as np

from camera import Camera

cam = Camera(1)

if (cam.IsOnline() == False):
   """Not Connected"""
   exit
   
print cam.GetAvailableUVCParameters()
   
#cam.SetFPS(10)
cam.SetResolution( (1024, 768))
cam.SetAutoFocus(False)
cam.SetAutoExposure(False)

focus = 128
exposure = 128
cam.SetFocus(focus)
cam.SetExposure(exposure)

camview = 'camera'
cv.namedWindow(camview)
cv.startWindowThread()

running = True
while running:
   
   frame = cam.Capture()
   cv.imshow(camview, frame)
   
   c = cv.waitKey(30) & 255
   
   if (int(c) == 27):
      running = False
      exit
   
   if (c == 82):    # up
      if focus < 255: 
         focus += 20
         cam.SetFocus(focus)
         
   elif(c == 84):   # down
      if focus > 0: 
         focus -= 20
         cam.SetFocus(focus)
      
   if (c == 81):    # left
      if exposure > 0: 
         exposure -= 20
         cam.SetExposure(exposure)
         
   elif(c == 83):   # right
     if exposure < 10000: 
         exposure += 20
         cam.SetExposure(exposure)
       

cv.destroyAllWindows()

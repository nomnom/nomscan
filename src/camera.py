import cv2 as cv
import numpy as np
  


class Camera(object):

    # constructor
    def __init__(self, video, size = (1024, 768)):
        
        
        self.video = video
        self.size = size
        if (isinstance(video, int) == True):
            self.isRealtime = True

        self.capt = cv.VideoCapture(video)
        if not self.capt:
            raise Exception("Capture source " + video +" not accessible")
        
     
        #self.intrinsics = # unity matrix?
        #self.extrinsics = # unity matrix?
        #self.undistortCoeffs = # default params
        self.undistorted = False
        
        #self.capt.set(CV_CAP_PROP.CAP_PROP_FOURCC, FourCC("MPEG"))
        
        self.SetResolution(size)
        self.Capture()
        
    # check if cam is available
    def IsOnline(self):
        if not self.isRealtime:
            return True
        
        if self.capt.isOpened():
            return True
        return False
            
            
    # get the next frame
    def Capture(self):
        retval, frame = self.capt.read()
        if not retval:
            return False
        self.frame = frame
        self.undistorted = False
        return GetFrame()
    
            
    # capture the current image
    def CaptureNow(self):
        if self.isRealtime: 
            return
        while self.Capture(): pass

    
    # access last frame        
    def GetFrame(self):
        if not self.undistorted:                    # undistort frame if not already
            self.frame = Undistort(self.frame);
            self.undistorted = True
        return self.frame
        
    
    # pixel geometrics
    def GetRay(pixelCoords):
        x = pixelCoords(0)
        y = pixelCoords(1)
        #TODO implement
        pass
        
        
    # set camera position in world (changes extrinsics)
    def Move(worldCoords):
        #TODO implement
        pass
        
        
    # position camera change extrinsics
    def LookAt(worldCoords):
        #TODO implement
        pass
        
        
    #
    # cam config
    #
    
    def SetResolution(self, size):
        self.capt.set(CV_CAP_PROP.CAP_PROP_FRAME_WIDTH, size[0])
        self.capt.set(CV_CAP_PROP.CAP_PROP_FRAME_HEIGHT, size[1])
        
    def SetFPS(self, fps):
        self.capt.set(CV_CAP_PROP.CAP_PROP_FPS, fps)
        
    def SetAutoFocus(enable):
        #TODO implement
        pass
            
    def SetFocus(focus):
        #TODO implement
        pass
        
    def SetAutoExposure(enable):
        #TODO implement
        pass
       
    def SetExposure(exposure):
        #TODO implement
        pass
        
    def SetIntrinsics(matrix):
        self.intrinsicsMatrix = matrix
    
    def SetExtrinsics(matrix):
        self.extrinsicsMatrix = matrix
        
    def GetExtrinsics():
        return self.extrinsicsMatrix
        
    def SetUndistort(coeffs):
        self.undistortCoeffs = coeffs
        
    #
    # helpers
    #
    
    # load and apply a complete cam config
    def LoadConfig(file):
        pass

    
    # undistort a frame
    def Undistort(frame):
        #TODO implement
        pass
    
    #
    #
    #
    def FourCC(chars):
        return (ord(chars[0]) +  (ord(chars[1]) << 8) + (ord(chars[2]) << 16) + (ord(chars[3]) << 24))


#############


class CameraCalibrator(object):

    MODES = {0, 'ManualChecker4', 
             1, 'ManualChecker8' }
        
        
    # runs selected calib method, sets distortion parameters, returns True/False on success/failure
    def Calibrate (camera, mode = 0):
        if (mode == 0):
            Calibrate_ManualChecker(camera, 4)
        elif (mode == 1):
            Calibrate_ManualChecker(camera, 8)
        # TODO more calibration methods

    def Calibrate_ManualChecker(numImages):
        # TODO implement default opencv checkerboard camera calibration routine
        pass
        
        
# copy for non-working cv constants
class CV_CAP_PROP:
    CAP_PROP_POS_MSEC = 0
    CAP_PROP_POS_FRAMES = 1
    CAP_PROP_POS_AVI_RATIO = 2
    CAP_PROP_FRAME_WIDTH = 3
    CAP_PROP_FRAME_HEIGHT = 4
    CAP_PROP_FPS = 5
    CAP_PROP_FOURCC = 6
    CAP_PROP_FRAME_COUNT = 7
    CAP_PROP_FORMAT = 8
    CAP_PROP_MODE = 9
    CAP_PROP_BRIGHTNESS = 10
    CAP_PROP_CONTRAST = 11
    CAP_PROP_SATURATION = 12
    CAP_PROP_HUE = 13
    CAP_PROP_GAIN = 14
    CAP_PROP_EXPOSURE = 15
    CAP_PROP_CONVERT_RGB = 16
    CAP_PROP_WHITE_BALANCE_BLUE_U = 17
    CAP_PROP_RECTIFICATION = 18
    CAP_PROP_MONOCHROME = 19
    CAP_PROP_SHARPNESS = 20
    CAP_PROP_AUTO_EXPOSURE = 21
    CAP_PROP_GAMMA = 22
    CAP_PROP_TEMPERATURE = 23
    CAP_PROP_TRIGGER = 24
    CAP_PROP_TRIGGER_DELAY = 25
    CAP_PROP_WHITE_BALANCE_RED_V = 26
    CAP_PROP_ZOOM = 27
    CAP_PROP_FOCUS = 28
    CAP_PROP_GUID = 29
    CAP_PROP_ISO_SPEED = 30
    CAP_PROP_BACKLIGHT = 32
    CAP_PROP_PAN = 33
    CAP_PROP_TILT = 34
    CAP_PROP_ROLL = 35
    CAP_PROP_IRIS = 36
    CAP_PROP_SETTINGS = 37
    CAP_PROP_BUFFERSIZE = 38
    CAP_PROP_AUTOFOCUS = 39


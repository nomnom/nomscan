import serial


class LEDs(object):
    
   def __init__(self, port, numLEDs):
      self.port = port
      self.count = numLEDs
      self.serial = serial.Serial(port, 115200);
      self.ledMap = range(numLEDs);    # identy map

   # check if device is online
   def IsConnected(self):
      if not self.serial.is_open():    # serial port not open
         return False
         
      if Ping():                       # device responding?
         return True
         
      return False
   
   #
   # LED Control
   #
   
   # get number of LED
   def GetNumLEDs(self):
      return self.count


   # set led color (0-1 rgb), values are linar in light if calibrated
   def Set(self, index, color):
      rawColor = Linearize(color)
      SetRaw(index, color)
      #TODO implement
      pass
      
      
   # apply calibration to color, if specified
   def Linearize(self, color):
      if not self.colorCalibration:   
         return color * 255            # map linear if no calibration was specified
   
      #TODO apply calibration
      return color
      
      
   # set raw (0-255 rgb)
   # command format: L 23 255 255 255
   def SetRaw(self, index, color):
      if self.ledMap:
         
      command = b'L ' + str(index) + b' ' + map(str, color).join(b' ')
      self.serial.write(command)
      
      
   # shut all leds off
   def Off(self):
      self.SendCommand(b'C\n')
      

   # write command to serial port
   def SendCommand(self, string):
      self.serial.write(string)
      
      
      
   #
   # LED Strip mapping
   #

   def LoadStripMap(self, file):
      #TODO
      # stripMap = 
      #SetStripMap(stripMap)
      pass
      
      
   # led strip map is a matrix with 8 columns and large enough to hold the max strip length over all eight strips
   # each entry in the map holds the index of the LED in the final logical led array
   def SetStripMap(self, stripMap)
      self.ledMap = self.CalcLEDMap(stripMap)
   
   # invert strip map (and do sanity check), produces an 1D array that holds the (octows2811-logical) led indice that are sent to the controller
   def CalcLEDMap(self, stripMap)
      # - construct output array by finding the next higher index
      # - error if number is duplicate or missing
      # - remember indices, return array
      pass

   #
   # Calibration
   #

   # load calibration table from file
   def LoadCalibration(self, file):
      #TODO implement
      pass
      
      
   # set calibration lookup table
   def SetCalibration(self, colorLUT):
      #TODO implement
      pass
      


# calibration routines
class LEDCalibrator(object):
   
   def __init__ (self, camera):
      self.camera = camera
      

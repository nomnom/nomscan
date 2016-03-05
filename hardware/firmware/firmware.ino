/*  
   http://www.pjrc.com/teensy/td_libs_OctoWS2811.html
   
  Required Connections
  --------------------
    pin 2:  LED Strip #1    OctoWS2811 drives 8 LED Strips.
    pin 14: LED strip #2    All 8 are the same length.
    pin 7:  LED strip #3
    pin 8:  LED strip #4    A 100 ohm resistor should used
    pin 6:  LED strip #5    between each Teensy pin and the
    pin 20: LED strip #6    wire to the LED strip, to minimize
    pin 21: LED strip #7    high frequency ringining & noise.
    pin 5:  LED strip #8
    pin 15 & 16 - Connect together, but do not useco
    pin 4 - Do not use
    pin 3 - Do not use as PWM.  Normal use is ok.
*/

#include <OctoWS2811.h>

const int numLEDs = 26;

DMAMEM int displayMemory[numLEDs*6];
int drawingMemory[numLEDs*6];

const int config = WS2811_GRB | WS2811_800kHz;

OctoWS2811 leds(numLEDs, displayMemory, drawingMemory, config);

void setup() {
  leds.begin();
  leds.show();
}

#define RED    0xFF0000
#define GREEN  0x00FF00
#define BLUE   0x0000FF
#define YELLOW 0xFFFF00
#define PINK   0xFF1088
#define ORANGE 0xE05800
#define WHITE  0xFFFFFF

void loop() 
{
  if (Serial.available() > 0) 
  {
    // read the first char (command char)
    byte c = Serial.read();
    int led = 0;
    switch (c)
    {
      case '\n': case '\r':
       leds.show();
       break;
       
      // clear
      case 'c': case 'C':
        Clear();
        break;
        
       // toggle led
       case 'W': case 'w':
        led = Serial.parseInt();
        ToggleColor(led, WHITE);
        break;

       case 'r': case 'R':
        led = Serial.parseInt();
        ToggleColor(led, RED);
        break;
        
       case 'g': case 'G':
        led = Serial.parseInt();
        ToggleColor(led, GREEN);
        break;

       case 'b': case 'B':
        led = Serial.parseInt();
        ToggleColor(led, BLUE);
        break;

       // ping - send byte back
       case 'p': case 'P':
          Serial.write(c);
          break;
       case 'n': case 'N':
       
       // bytestream
       case 's': case 'S':
        while (true)
        {
     
        
        }
        break;
    }

  }

}

void Clear()
{
  for (int i=0; i < numLEDs; i++) 
    leds.setPixel(i, 0);
}


void SetColor(int led, int color)
{
  if (led < 0 || led >= numLEDs)
   return;
  
  leds.setPixel(led, color);
}


void ToggleColor(int led, int color)
{
  if (led < 0 || led >= numLEDs)
   return;

  int currentColor = leds.getPixel(led);
  int newColor = currentColor ^ color;
  leds.setPixel(led, newColor);
}


int FromRGB(int red, int green, int blue)
{
  return red << 16 | green << 8 | blue;
}


int ToRGB(int color, int channel)
{
  return (color >> channel * 8) & 0xFF;
}

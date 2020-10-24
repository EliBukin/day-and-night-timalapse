#!/usr/bin/python

import time
import picamera
from picamera import PiCamera
from fractions import Fraction
#
import sys
from check_light_func import check_light
#
from time import sleep
from datetime import datetime
import os
import shutil

dest_photo = '/home/pi/Desktop/sysconfig_rpi-sputnik-portable-1/day-and-night-timelapse/timelapse/{timestamp:%a-%d.%m.%Y-%H-%M-%S}'+'_{counter:05d}.jpg'
dest_location = '/home/pi/Desktop/sysconfig_rpi-sputnik-portable-1/day-and-night-timelapse/timelapse/*'
ineligible_files = './ineligible_files/'

def helloday():
   print ('[INFO]: Switching to Day Mode')

def hellonight():
   print ('[INFO]: Switching to Night Mode')

### Night Mode
def night_mode():
   #camera = PiCamera(resolution=(1280, 720), framerate=Fraction(1, 6))
   camera = PiCamera(resolution=(1920, 1080), framerate=Fraction(1, 6))
   camera.shutter_speed = 6000000
   camera.iso = 800
   # Give the camera a good long time to set gains and
   # measure AWB (you may wish to use fixed AWB instead)
   sleep(5)
   camera.exposure_mode = 'off'
   # Finally, capture an image with a 6s exposure. Due
   # to mode switching on the still port, this will take
   # longer than 6 seconds
   #camera.capture('dark9.jpg')
   ###
   for filename in camera.capture_continuous(dest_photo):
      print('[INFO]: NM Captured %s' % filename)
      time.sleep(15) # interval in seconds
      check_light(dest_location)
      print ('[INFO]: light is ' + str(check_light.light))
      if check_light.light < 650:
         print ('[INFO]: '+(check_light.img +' is a night photo'))
      else:
         print ('[INFO]: '+(check_light.img +' is a day photo'))
         ineligible = os.path.basename(check_light.img)
         shutil.move(check_light.img, ineligible_files+ineligible)
         helloday()
         camera.close()
         day_mode()
         break

### Day Mode
def day_mode():
   with picamera.PiCamera() as camera:
      camera.start_preview()
      time.sleep(2)
      for filename in camera.capture_continuous(dest_photo):
         print ('[INFO]: DM Captured %s' % filename)
         time.sleep(25) # interval in seconds
         check_light(dest_location)
         print ('[INFO]: light is ' + str(check_light.light))
         if check_light.light < 240:
            print ('[INFO]: '+(check_light.img +' is a night photo'))
            ineligible = os.path.basename(check_light.img)
            shutil.move(check_light.img, ineligible_files+ineligible)
            hellonight()
            camera.close()
            night_mode()
            break
         else:
            print ('[INFO]: '+(check_light.img +' is a day photo'))

day_mode()

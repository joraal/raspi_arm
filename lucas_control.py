# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

from Tkinter import *


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


# define the gui


class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		scale1 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update1)
		scale1.grid(row=0)

		scale2 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update2)
		scale2.grid(row=0)

		scale3 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update3)
		scale3.grid(row=0)
		
		scale4 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update4)
		scale4.grid(row=0)
		
		scal5 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update5)
		scale5.grid(row=0)
		
		scal6 = Scale(frame, from_=0, to=180,
		orient=HORIZONTAL, command=self.update6)
		scal6.grid(row=0)
		
	def update1(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(0, 0, pulse_len)


	def update2(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(1, 0, pulse_len)
		
	def update3(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(2, 0, pulse_len)
		
	def update4(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(3, 0, pulse_len)
		
	def update5(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(4, 0, pulse_len)
		
	def updat6(self, angle):
		pulse_len = int(float(angle) * 500.0 / 180.0) + 110
		pwm.set_pwm(5, 0, pulse_len)
		
		

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()



#print('Moving servo on channel 0, press Ctrl-C to quit...')
#while True:
    # Move servo on channel O between extremes.
 #   pwm.set_pwm(0, 0, servo_min)
  #  time.sleep(1)
   # pwm.set_pwm(0, 0, servo_max)
    #time.sleep(1)

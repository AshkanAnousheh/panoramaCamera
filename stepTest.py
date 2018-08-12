import RPi.GPIO as GP
from time import sleep
#from picamera import PiCamera


GP.setmode(GP.BOARD)

pins = [37,35,33,31]

for pin in pins:
	GP.setup(pin,GP.OUT)
	GP.output(pin,0)

halfStepSequence = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

for i in range(512):
	for halfStep in range(8):
		for pin in range(4):
			GP.output(pins[pin],halfStepSequence[halfStep][pin])
			sleep(0.001)

	if i == 127 :
		print('take picture1')
		sleep(1)
	if i == 255 :
		print('take picture2')
		sleep(1)
	if i == 383 :
		print('take picture3')
		sleep(1)
	if i == 511 :
		print('take picture4')
		sleep(1)


GP.cleanup()

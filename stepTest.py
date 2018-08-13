import RPi.GPIO as GP
from time import sleep
from picamera import PiCamera

Camera = PiCamera()
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

j = 0

for i in range(512):
	for halfStep in range(8):
		for pin in range(4):
			GP.output(pins[pin],halfStepSequence[halfStep][pin])
			sleep(0.001)

	if (i% 31 == 0) :
		sleep(1)
		Camera.capture('/home/pi/projects/stepperMotor/img/img%s.jpg'%j)
		print('take picture %d' %(j))
		j=j+1

GP.cleanup()

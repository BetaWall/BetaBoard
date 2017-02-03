from array import array
import random
from time import sleep
import wiringpi

INTENSITY = 0xFF

wiringpi.wiringPiSetup()
wiringpi.pinMode(8, 1)

DEBUG = True

#
# Image Processing
#

def set_row(row):
	if row in [0, 1]:
		wiringpi.digitalWrite(8, row)
	else:
		raise ValueError("row %i  not in range." % row)

def send(input, row, location):
	# Compile pixel data in to a data field
	data = [0x00] * 4
	set_row(row)
	for pixel in input:
		r, g, b = pixel
		data.extend([INTENSITY, b, g, r])
	data.extend([0xFF]*4)
	if DEBUG:
		print format(row, '02x'),
		for i in data:
			print format(i, '02x'),
		print ""
	array('B', data).tofile(location)
	location.flush()

def randomframe():
	pixels = []
	for i in range(3):
		pixels.append((
			random.randrange(0, 255),
			random.randrange(0, 255),
			random.randrange(0, 255)
		))
	return pixels

with open("/dev/spidev0.0", "wb") as spi:
	while True:
		send(randomframe(), 0x00, spi)
		send(randomframe(), 0x01, spi)
		sleep(0.1)

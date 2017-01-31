from array import array
import random
from time import sleep

import sys

INTENSITY = 0xFF

def send_row(row, location):
	# Compile pixel data in to a data field
	data = [0x00] * 4
	for pixel in row:
		r, g, b = pixel
		data.extend([INTENSITY, b, g, r])
	data.extend([0xFF]*4)
	for i in data:
		print format(i, '02x'),
	print "\r",
	array('B', data).tofile(location)
	location.flush()

with open("/dev/spidev0.0", "wb") as spi:
	while True:
		for r in range(0, 255):
			for g in range(0, 255):
				for b in range(0, 255):
					pixel = (r, g, b)
					row = [pixel]*3
					send_row(row, spi)
					sleep(0.01)

from array import array
import random
from time import sleep

import sys

INTENSITY = 0xFF

#
# Image Processing
#

def data_field(row):
	# Compile pixel data in to a data field
	data = [0x00] * 4
	for pixel in row:
		r, g, b = pixel
		data.extend([INTENSITY, b, g, r])
	data.extend([0xFF]*4)
	for i in data:
		print format(i, '02x'),
	print ""
	return array('B', data)

def send_data(data_array, location):
	# Alias for array.tofile()
	data_array.tofile(location)
	location.flush()

image = []
image.append([
	(0x00, 0x00, 0x00),
	(0x00, 0x00, 0x00),
	(0x00, 0x00, 0x00)
])
image.append([
	(0xFF, 0xFF, 0xFF),
	(0xFF, 0xFF, 0xFF),
	(0xFF, 0xFF, 0xFF)
])
with open("/dev/spidev0.0", "wb") as spi:
	while True:
		#for pixels in image:
		#	send_data(data_field(rgb), spi)
		#	sleep(0.25)
		send_data(data_field(image[0]), spi)
		sleep(1)
		send_data(data_field(image[1]), spi)
		sleep(1)

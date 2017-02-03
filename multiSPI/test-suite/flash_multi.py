from array import array
import random
from time import sleep
import wiringpi

INTENSITY = 0xFF

wiringpi.wiringPiSetup()
wiringpi.pinMode(8, 1)


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
		for f in [0, 1]:
			for i in [0, 1]:
				wiringpi.digitalWrite(8, i)
				send_data(data_field(image[(f+i)%2]), spi)
			sleep(0.25)

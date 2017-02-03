from array import array
import random
from time import sleep, time
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


display = []
display.append([
	[0xff, 0x00, 0x00],
	[0x00, 0xff, 0x00],
	[0x00, 0x00, 0xff]
])
display.append([
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff]
])

dir = 30
max_change = 30
max_frame_rate = 10
base_color = 0x55

with open("/dev/spidev0.0", "wb") as spi:
	while True:
		for line in range(len(display)):
			for pixel in range(len(display[line])):
				for color in range(len(display[line][pixel])):
					if not display[line][pixel][color] == 0x00:
						if display[line][pixel][color] > 0xff-max_change:
							dir = -1 * max_change
						if display[line][pixel][color] < base_color+max_change:
							dir = max_change
						display[line][pixel][color] += dir
		try:
			while (time() < (frame_start_time + (1.0/max_frame_rate))):
				pass
		except:
			pass
		frame_start_time = time()
		for i in range(len(display)):
			send(display[i], i, spi)

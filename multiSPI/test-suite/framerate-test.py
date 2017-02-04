from array import array
import random
from time import sleep, time
import wiringpi

INTENSITY = 0xcc

wiringpi.wiringPiSetup()
wiringpi.pinMode(8, 1)
wiringpi.digitalWrite(8, 1)

DEBUG = True

#
# Image Processing
#

def set_row(row):
	if row in [0, 1]:
		wiringpi.digitalWrite(8, row)
	else:
		pass
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
	array('B', data).tofile(location)
	location.flush()


display = []
display.append([
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff],
	[0xff, 0xff, 0x00],
	[0x00, 0xff, 0xff],
	[0xff, 0x00, 0xff]
])
display = display*18
print display

dir = 1
max_change = 1
base_color = 0x11

print "Target", "Actual"
with open("/dev/spidev0.0", "wb") as spi:
	for max_frame_rate in range(10, 1000, 5):
		start_time = time()
		frames = 0
		frame_start_time = time()
		while (time() - start_time < 0.25):
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
			frames += 1
			for i in range(len(display)):
				send(display[i], i, spi)

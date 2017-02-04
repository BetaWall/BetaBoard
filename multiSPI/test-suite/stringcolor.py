from array import array
from time import sleep
import wiringpi

#
# Constants
#

INTENSITY = 0xFF
DEBUG = True

#
# Setup Pi Outputs
#

wiringpi.wiringPiSetup()
wiringpi.pinMode(8, 1)

#
# Output Funtions
#

def set_row(row):
	if row in [0, 1]:
		wiringpi.digitalWrite(8, row)
	else:
		raise ValueError("row %i  not in range." % row)

def send_line(inputdata, row, location):
	# Compile pixel data in to a data field
	data = [0x00] * 4
	set_row(row)
	for pixel in inputdata:
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

def send_lines(inputdata, location):
	i = 0
	for line in inputdata:
		sendline(line, i, location)
		i += 1

#
# Frame Genorator Functions
#

BLACK   = (0x00, 0x00, 0x00)
WHITE   = (0xff, 0xff, 0xff)
RED     = (0xff, 0x00, 0x00)
GREEN   = (0x00, 0xff, 0x00)
BLUE    = (0x00, 0x00, 0xff)
CYAN    = (0x00, 0xff, 0xff)
MAGENTA = (0xff, 0x00, 0xff)
YELLOW  = (0xff, 0xff, 0x00)

colorhash = {
	'k' : BLACK,
	'w' : WHITE,
	'r' : RED,
	'g' : GREEN,
	'b' : BLUE,
	'c' : CYAN,
	'm' : MAGENTA,
	'y' : YELLOW
}

def stringframe(string):
	frame = []
	for char in string:
		frame.append(colorhash[char])
	return frame

#
# Run
#

if DEBUG:
	spi = open("/dev/spidev0.0", 'wb')

#
# Game Start
#

lines = [0, 1]

with open("/dev/spidev0.0", "wb") as spi:
	while True:
		for line in lines:
			send_line(stringframe(input("%i: " % line)), line, spi)

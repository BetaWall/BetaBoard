#include <avr/io.h>
#include <avr/interupt.h>

#define BUFFER_SIZE 32 // Make this as big as you can afford
#define STRIP_OUTPUT PORTB
#define BOARD_ID_INPUT PORTA
#define INTENSITY 0xCC

// 256 Byte Input Buffer
char* buffer[BUFFER_SIZE];
int buffer_in, buffer_out;

void init_buffer(void) 
{
	buffer_in = 0;
	buffer_out = 0;
}

int buffer_add(char c)
{
	buffer[buffer_in] = c;
	buffer_in++;
	if (buffer_in == BUFFER_SIZE - 1) {
		// Return buffer_in to start
		buffer_in = 0;
	}
}

char buffer_pop(void)
{
	while (buffer_out == buffer_in) {
		// Wait for a byte rx
		continue;
	}
	char r = buffer[buffer_out];
	buffer_out++;
	if (buffer_out == BUFFER_SIZE - 1) {
		// Return buffer_out to start
		buffer_out = 0;
	}
	return r;
}

// UART Interupt
ISR(USART_RXC_vect) {
	buffer_add(UDR0)
}

void begin_line(void)
{
	// Send start sequence
	// 0x00000000
	for (int i = 0; i < 3; i++) {
		output_spi(0x00);
	}
}

void end_line(void)
{
	// Send end sequence
	// 0xFFFFFFFF
	for (int i = 0; i < 3; i++) {
		output_spi(0xFF);
	}
}

void output_spi(char c) {
	// Make sure nothing is being sent
	// TODO
	// Send char c
	// TODO
	// Wait untill it's sent
	// TODO
	continue;
}

int main(void)
{
	// Initalise
	init_buffer();
	uint8_t board_id = PORTA;
	uint8_t data_length;
	while (1) {
		board_id = buffer_pop();
		STRIP_OUTPUT = buffer_pop();
		data_length = buffer_pop();
		if (board_id == BOARD_ID_INPUT) {
			// Send start, data , end to selected strip.
			begin_line()
			for (int i = 0; i < data_length/3; i+=3) {
				output_spi(INTENSITY);
				output_spi(buffer_pop()); // B
				output_spi(buffer_pop()); // G
				output_spi(buffer_pop()); // R
			}
			end_line();
		} else {
			// Ignore message content, it's not for this board.
			for (int i = 0; i < data_length; i += 3) {
				buffer_pop();
			}
		}
	}
}
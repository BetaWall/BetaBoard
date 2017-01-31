# multiSPI

Scripts that talk SPI to APA102 LEDs using the multiplexing technology on the BetaBoard hardware. 

These are currently written in Python, however the final project will have the SPI multiplexing handled by hardware and this software will only be used for image proccessing and serial output to the BetaBoard.

These are tested and working on a Raspberry Pi 2 running Ubuntu Server.

## Dependancies

Uses WiringPi for the multiplexing, needs to be run on a linux machine with SPI hardware at `/dev/spidev0.0`. This is hardcoded and can be changed by editing the source.

Otherwise the software just uses your device as a file so no SPI libraries are required.


# LightshowOnTheGo
A DIY Car LED project designed to be responsive to music (and other potential inputs). This project will involve a series of versions that will focus on space optimization, interface methods (eg. Bluetooth, WiFi, JTAG, etc.) and I/O handling (eg. microphone, button/switch controls, etc.)

# Lightshow Version 1.0

Below is a general outline of the project architecture. All files relating to V1.0 can be found in the Lightshow1.0 directory.

## Hardware

### Parts listing
* 1 LED Strip
* AVNET MicroZed FPGA (considering a Teensy 3.6 microcontroller as well
* A protoboard with the following components:
  * Transistors used for PWM of LEDs (p2n2222a transitor)
  * 4x1 male Molex pin headers for LED Strip
  * 3.5mm DC Power connector (see TODO)
  * 3x1 male or female socket pin header (FPGA/Microcontroller connector to transistors)
* 3 Resistors (100 Ohm) to limit current draw
* 12V Car power adapter with a 3.5 mm connector
* Wire (22 gauge)

### Transistor/LED Circuit
* 12v power supply in series with a 100 Ohm resistor, p2n2222a transistor (input at collector) and ground connected to emitter.
* Zedboard interfaces with a common ground at the collector
* Gate is driven by a 3.3V signal from the Minized
* The above circuit yields a 50mA current draw. If we can get it to 1A we can get really bright LEDs which would be ideal.

### Microphone

* Documentation: MiniZed-HW-UG...pdf
* Output
 * Audio Clk
 * Dout
* The Dout signal alternates between the right and left channel every other clock cycle. Output is in pulse-density modulation (PDM)
 * Clk Low = Left Channel
* The microphone is connected to some codec inside the FPGA
* Demodulate the signal by using a low pass filter... and try to figure out why this works.


### TODO
* ~~Estimate current draw on the LEDs given a 12V DC power source.~~ 1A current draw
* ~~Determine the max level of brightness desired from LED strip~~ Max brightness at 1A
* Consider power draw of LED strips in parallel for future versions
* Create circuit diagram
* Create small PCB to interface 12V power cable to LED strip
 * Add a switch to enable/disable pwm capabilities
* ~~Select a transistor capable of meeting the following constraints:~~
  * ~~Max current drawn by the LEDs~~
  * ~~Can be driven by a 3.3V/2.7V/1.3V signal at the gate (voltage constrained by microcontroller/FPGA)~~
  * ~~Does not overheat to unsafe levels~~
* Find suitable protoboard
* Verify wires are capable of current levels selected


## Software 

### TODO
* Determine the sample rate of your microphone
 * Figure out interrupt timing in relation to the sample rate
* Design lowpass filter to receive microphone input
* Design a filter to detect the base in a song

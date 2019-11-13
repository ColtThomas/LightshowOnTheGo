# LightshowOnTheGo
A DIY Car LED project designed to be responsive to music (and other potential inputs). This project will involve a series of versions that will focus on space optimization, interface methods (eg. Bluetooth, WiFi, JTAG, etc.) and I/O handling (eg. microphone, button/switch controls, etc.)

# Lightshow Version 1.0

Below is a general outline of the project architecture. All files relating to V1.0 can be found in the Lightshow1.0 directory.

## Hardware

### Parts listing
* 1 LED Strip
* AVNET MicroZed FPGA (considering a Teensy 3.6 microcontroller as well
* A protoboard with the following components:
  * Transistors used for PWM of LEDs (see TODO)
  * 4x1 male Molex pin headers for LED Strip
  * 3.5mm DC Power connector (see TODO)
  * 3x1 male or female socket pin header (FPGA/Microcontroller connector to transistors)
* 3 Resistors to limit current draw
* 12V Car power adapter with a 3.5 mm connector
* Wire (22 gauge)

### TODO
* Estimate current draw on the LEDs given a 12V DC power source.
* Determine the max level of brightness desired from LED strip
* Consider power draw of LED strips in parallel for future versions
* Select a transistor capable of meeting the following constraints:
  * Max current drawn by the LEDs
  * Can be driven by a 3.3V/2.7V/1.3V signal at the gate (voltage constrained by microcontroller/FPGA)
  * Does not overheat to unsafe levels
* Find suitable protoboard
* Verify wires are capable of current levels selected


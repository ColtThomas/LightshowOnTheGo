# -*- coding: utf-8 -*-
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#######################
# Generate a Sine wave
#######################

analogSamples = 2000
amplitude = 1
t = np.linspace(0,1.0,analogSamples+1)

sig = amplitude * np.sin(2*np.pi*5*t)

## Plot
style.use('ggplot')
style.use('dark_background')
f,plt_arr = plt.subplots(3,sharex = True)
f.suptitle('Multiplot')

plt_arr[0].plot(sig, color='magenta')
plt_arr[0].set_title('Initial Signal',color='magenta')

######################################
# Create a Pulse Density Modulation
######################################

bitResolution = 8
convert = 0

# represent highest signal value as all 1's, lowest value as all 0's
# E.G. 5V max -> 0b11111111 and 0V -> 0b0000000
normFact = (2**bitResolution - 1) / (amplitude*2)  

ADC = np.zeros(int(analogSamples/bitResolution)) # new array
for i in range(0,int(analogSamples/bitResolution)):
    convert = int((sig[(bitResolution * (i)) - 1] + amplitude) * (normFact))
    ADC[i] = convert


PDM = np.zeros(analogSamples+1,dtype=int)
for i in range(0,analogSamples):
    derp = int(i / bitResolution)
    idx = i % bitResolution 
    
    try:
        #bit = f'{int(ADC[derp]):016b}'# int to 8 bit binary... not dynamic
        bit = bin(int(ADC[derp]))[2:].zfill(bitResolution) # int to <bitResolution> bit binary
        # bin() returns a 0b010101010 format. The [2:] cuts off the prefix 0b
    except IndexError:
        print("End of data")
        break

    
    # DEBUG #
    #print(bit)
    #print(i," Index: ",derp, " String Index: ",idx, " -> ",bit[idx] )

    PDM[i] = bit[idx]

## Plot
plt_arr[1].plot(PDM, color='yellow')
plt_arr[1].set_title('PDM Signal',color='magenta')

###################################
# Low Pass Filter to convert back
###################################


## Plot
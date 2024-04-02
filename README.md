# CV Extractor

This is an envelope detector eurorack module.
It is intended to take in eurorack signals or audio input and output the envelope.


## Description of schematic
An input waveform passes through an adjustable gain noninverting amplifier, then an active rectifier, then finally a 2-pole sallen-key LPF with adjustable gain and cutoff.

## Features

    * Buffered input/output
    * Adjustable input/output gain
    * Adjustable timescale of envelope detection

## Rack info

    * +12V: ?? mA
    * -12V: ?? mA
    *  +5V: unused
    * Width: 8HP   

## Issues

The module works, but its not that great.

    * Gain Pots are oriented reverse, unintuitive
    * Turning the cutoff knob can cause it to oscillate
    * The gain range is too large

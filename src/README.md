# Badger2040, Apple Macintosh 1984
 
## Overview

This is a custom UI for Badger 2040 that I built for the Census
engineering offsite in 2022. I aimed to recreate the iconic 1984
Macintosh UI in a compact design.

## Known bugs

I had to cut some corners, so that I could finish the assembly of a small batch
before the event. Here is a list of known bugs:
- If you open the same application twice (e.g. open QR app, open Badge
  app, and open QR app again), the device will restart and show a
  welcome screen. I shouldn't have tried to build a multi app
  experience in the first place. IMO, it is too much to do to
  implement this right in Python. I think if it was Lisp environment,
  it would have been easier.
- I forgot to adjust the battery voltage to calculate the battery
  level. The device may show that a battery is empty or it is not
  plugged in.

## Upload steps

- Upload pimonori-badger2040-micropython bootloader
- Upload Python scripts

## User Guide

- A button opens Badge app
- B button opens QR app
- C button opens Special app. Up/Down buttons randomly load a new
  quote
- A + C buttons open Welcome screen

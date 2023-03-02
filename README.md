# Badger2040 System II

Tired of boring badges that just blend in with the crowd? You want to show off your quirky personality and love of retro technology? You are looking for a fun project to bond with your engineering team? Look no further than the programmable e-ink badge!

https://kruzenshtern.org/the-e-ink-badge-the-coolest-badge-you-didnt-know-you-needed/

![image](https://user-images.githubusercontent.com/198995/219474204-890703d2-fb32-4299-a39b-2d434ac3f215.png)

## Source code

Don't expect much, but it works (tm). See in /src.

## Components

1. Badger 2040: https://shop.pimoroni.com/products/badger-2040
2. Coin Cell Battery Holder: https://www.adafruit.com/product/783
3. 2x CR2032: https://www.amazon.com/gp/product/B078GC5K81/
4. 4x M2 8mm bolts: https://www.amazon.com/gp/product/B01BNIHG0E/
5. 3D-printed case: see /case folder. I was using Prusament PLA: https://www.prusa3d.com/product/prusament-pla-ms-pink-blend-970g/

## A quick glance at assembly steps

1. 3D print top and bottom panels. 
2. Disassemble & attach a 2xCR2032 battery holder
3. Assemble the badge, use hot glue whenever applicable
4. Upload pimonori-badger2040-micropython bootloader
5. Upload Python scripts

## License & acknowledgements

Inspiration sources for the case:

- https://kaenner.de/badger2040 (CC4)
- https://www.thingiverse.com/thing:5320100/files (CC4)

I ended up using an OpenSCAD blueprint by usedbytes to get measurements of the device. Reconstructed/synthesized a new case in Fusion360. Noticeable changes:
- A different battery holder / back pannel to simplify the assembly to some extend
- Two coin cells vs three
- Added hidden buttons inspired by Känner's design
- Back panel is inspired by Känner's design too, I like that connectors are accessible
- Battery toggle button
- Any mistakes are exclusively mine

Source code:
- To a large extend based on pimoroni Badger2040 OS example: https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/badger2040 (MIT)
- Font & rendering: custom code, but it is not worth extracting it to a standalone app/library. Let's stick with MIT for simplicity too.

Assets:
- Font: 16bfZX https://www.pentacom.jp/pentacom/bitfontmaker2/gallery/?id=246 (Public domain)
- Clippy: hand-drawn, I think the character is trademarked by Microsoft though.
- Other assets: hand-drawn

What does it mean in terms of license? I guess, it is good for a hobby project. Hire a lawyer to check if it is good for commercial use.

## From

:wave: The folks at [Census](http://getcensus.com) originally put this together. Have data? We'll sync your data warehouse with your CRM and the customer success apps critical to your team.

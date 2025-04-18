#!/bin/bash

cvt 1920 1013 55
xrandr --newmode 1920x1013_55.00 146.50 1920 2032 2232 2544 1013 1016 1026 1048 -hsync +vsync
xrandr --addmode Virtual1 1920x1013_55.00
xrandr --output Virtual1 --mode 1920x1013_55.00

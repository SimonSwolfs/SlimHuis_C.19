#!/usr/bin/env python
__author__ = "Simon Swolfs en Robbe de Budt"
__email__ = "simon.swolfs@student.kdg.be"
__version__ = "1.0"

# LIBRARIES
import time
import gpiozero
from gpiozero import Button
from gpiozero import LED

# VARIABLES
systemwork = True
howworks = {
    Button(26): LED(6),
    Button(16): LED(5),
    Button(25): LED(23),
    Button(17): LED(24)
}


while systemwork:
    for key, value in howworks.items():
        if key.value == 1:
            print('The button was pressed!')
            if value.value == 1:
                value.off()
            else:
                value.on()

        time.sleep(0.50)
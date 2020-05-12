#!/usr/bin/env python

__author__ = "Simon Swolfs"
__email__ = "simon.swolfs@student.kdg.be"
__version__ = "2.0"

# LIBRARIES
import time
from gpiozero import Button
from gpiozero import LED
import time
import timeit

# import multiprocessing

# CONFIG

TRESHHOLD_PUSHLONG = 1
TRESHHOLD_TIME_PRESS = 1.5
BOUNCE_TIME = 0.01

# SETUP
# Buttons
BTN_AMOUNT = 4
BTN_PIN = [26, 16, 25, 17]  # BUTTON PINS

# Leds
LEDS_AMOUNT = 4
LED_PIN = [6, 5, 23, 24]  # LED PINS

# VARIABLES
led_list = []
button_list = []


# FUNCTIONS
def main():
    set_up_led()
    set_up_button()
    check.button()

def set_up_led():
    for led_nr in LED_PIN:  # het led nummer in de lijst met pins
        print(led_nr)
        led_list.append(LED(led_nr))  # voeg de lijst met pins toe aan led_list


def set_up_button():
    for button_nr in BTN_PIN:
        button_list.append(Button(button_nr))


def button_toggle(nr_list, times_pressed):
    if times_pressed == 1:
        if led_list[nr_list].value == 0:
            led_list[nr_list].on()
            check_button()

def leds_on():
    for l in range(LEDS_AMOUNT):
        led_list[l].on()

def leds_off():
    for l in range(LEDS_AMOUNT):
        led_list[l].off()

# def button_pushlong(nr_list):

# def button_pressed(nr_list):

def check_button():
    while True:
        for b in range(BTN_AMOUNT):
            button_pressed(b)



# START
if __name__ == "__main__":
    main()


# functies zijn in kleine letters
# .append betekend toevoegen aan
# altijd checken voor : 
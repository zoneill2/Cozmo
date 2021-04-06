import asyncio
import io
import json
import math
import sys
import flask_helpers
import cozmo
from pynput.keyboard import Key, Listener
from cozmo.util import degrees, distance_mm, speed_mmps
import keyboard  # using module keyboard

from pynput import keyboard


class ControlCozmo:

    def __init__(self, coz):
        self.cozmo = coz
        while True:
            
    

    def on_press(key):
        if key == keyboard.KeyCode(char='w'):
            try:
                print('- Started recording -'.format(key))
            except IOError:
                print("Error")
        else:
            print('incorrect character {0}, press cmd_l'.format(key))


    def on_release(key):
        print('{0} released'.format(key))
        if key == keyboard.KeyCode(char='w'):
            print('{0} stop'.format(key))


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

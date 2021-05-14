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



def run(sdk_conn):
    robot = sdk_conn.wait_for_robot()
    robot.enable_device_imu(True,True,True)
    
    global remote_control_cozmo
    
    robot.camera.image_stream_enabled = True
    
    while True:
        theCamera = cozmo.camera.Camera()
    
cozmo.connect(run)
    
    




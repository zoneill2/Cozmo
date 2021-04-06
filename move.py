import cozmo    
import asyncio
import time

from cozmo.util import degrees, distance_mm, speed_mmps

def squaredrive(robot: cozmo.robot.Robot):
    
    for _ in range(4):

        notes = [cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter)]
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.say_text("Fuck").wait_for_completed()
        robot.play_song(notes, loop_count=1).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()


        
cozmo.run_program(squaredrive, use_viewer=True)
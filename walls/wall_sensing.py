# Project 3: GEARS Robot
# File: wall_sensing.py
# Date: 3/14/21
# By: Alex Wiseman
# ajwisema
# Ben Chappell
# chappeb
# Trevor Moorman
# tmoorma
# Cole Kingery
# ckinger
# Section: 5
# Team: 70
#
# ELECTRONIC SIGNATURE
# Ben Chappell
# Cole Kingery
# Trevor Moorman
# Alex Wiseman
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# Interfacing between ultrasonic data and various processing. Determines whether or not a corridor is passable or not and sends that to processing to turn into usable data.
# Inputs: Ultrasonic Data, Hazard Existence
# Outputs: Wall/Corridor Data

import math
import time
from ..interfacing import grove_ultrasonic
from ..interfacing import lego_ultrasonic
from .. import constants as r

def senseWalls(robot):

    value = 20
    list = [0,0,0]
    rightSense = grove_ultrasonic.readGroveUltrasonic(robot.r_ultra)
    leftSense = grove_ultrasonic.readGroveUltrasonic(robot.l_ultra)
    #frontSense = lego_ultrasonic.legoUltrasonic(robot.bp, robot.f_ultra)
    frontSense = 30

    if (rightSense < value):
        print("Sensing right wall")
        list[0] += 1
    if (frontSense < value):
        print("Sensing left wall")
        list[1] += 1
    if  (leftSense < value):
        list[2] += 1

    return list

#!/usr/bin/env python3

import sys

from rqt_gui.main import Main

def main():
    rqt_main = Main()
    sys.exit(rqt_main.main(sys.argv, standalone='rqt_joint_trajectory_controller.joint_trajectory_controller.JointTrajectoryController'))

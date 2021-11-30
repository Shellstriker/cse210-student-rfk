import os

MAX_X = 10
MAX_Y = 14
FRAME_LENGTH = 0.1
PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 1
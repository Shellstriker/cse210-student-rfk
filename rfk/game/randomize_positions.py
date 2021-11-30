import random
from game.action import Action
from game import constants
from game.point import Point

class RandomizePositionsAction(Action):
    def execute(self, cast):
        if random.randint(0, 100) != 92:
            return
        
        else:
            for I in cast["artifact"]:
                x = random.randint(0, constants.MAX_X - 1)
                y = random.randint(1, constants.MAX_Y - 1)
                position = Point(x, y)
                I.set_position(position)
import random
from game.action import Action
from game import constants
from game.point import Point

class RandomizePositionsAction(Action):
    def execute(self, cast):
        number_1 = 0
        arftifacts = cast["artifact"]
        if random.randint(0, 100) != 92:
            return
        
        else:
            for I in arftifacts:
                arftifacts.pop(number_1)
                number_1 += 1
                '''x = random.randint(0, constants.MAX_X - 1)
                y = random.randint(1, constants.MAX_Y - 1)
                position = Point(x, y)
                I.set_position(position)'''
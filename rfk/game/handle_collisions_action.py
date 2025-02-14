import random
import sys
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        marquee = cast["marquee"][0] # there's only one
        robot = cast["robot"][0] # there's only one
        artifacts = cast["artifact"]
        level_2 = cast["level_2"]
        cracks = cast["cracks"]
        marquee.set_text("")
        finish = artifacts[0]
        if robot.get_position().equals(finish.get_position()):

            for object in artifacts:
                object.hide()
            
            cracks.clear()

            for object in level_2:
                object.unhide()
        
        for crack in cracks:
            if len(cracks) != 0:
                 if robot.get_position().equals(crack.get_position()):
                    sys.exit()
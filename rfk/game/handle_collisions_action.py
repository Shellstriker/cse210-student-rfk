import random
import sys
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

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
        robot = cast["robot"][0] # there's only one
        level_1 = cast["level_1"]
        level_2 = cast["level_2"]
        level_3 = cast["level_3"]
        level_4 = cast["level_4"]
        level_5 = cast["level_5"]
        level_6 = cast["level_6"]
        level_7 = cast["level_7"]
        level_8 = cast["level_8"]
        level_9 = cast["level_9"]
        level_10 = cast["level_10"]
        cracks = cast["cracks"]
        congratulations = cast["congratulations"][0]

        if not level_1[0].ishidden(): 
            finish = level_1[0]
            position = Point(2,5)

        elif not level_2[0].ishidden(): 
            finish = level_2[0]
            position = Point(2,2)

        elif not level_3[0].ishidden(): 
            finish = level_3[0]
            position = Point(3,5)

        elif not level_4[0].ishidden():
            finish = level_4[0]
            position = Point(3,7)

        elif not level_5[0].ishidden():
            finish = level_5[0]
            position = Point(14,2)

        elif not level_6[0].ishidden():
            finish = level_6[0]
            position = Point(4,6)

        elif not level_7[0].ishidden():
            finish = level_7[0]
            position = Point(4,8)

        elif not level_8[0].ishidden():
            finish = level_8[0]
            position = Point(5,4)

        elif not level_9[0].ishidden():
            finish = level_9[0]
            position = Point(2,5)

        elif not level_10[0].ishidden():
            finish = level_10[0]
            position = Point(7,5)

        elif not congratulations.ishidden():
            finish = level_1[0]
        

        for crack in cracks:
            if len(cracks) != 0:
                 if robot.get_position().equals(crack.get_position()):
                    cracks.clear()
                    robot.set_position(position) 

        if robot.get_position().equals(finish.get_position()) and not level_1[1].ishidden() and len(cracks) == 20:

            for object in level_1:
                object.hide()
            
            cracks.clear()
            robot.set_position(Point(2,2))

            for object in level_2:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_2[1].ishidden() and len(cracks) == 26:

            for object in level_2:
                object.hide()
            
            cracks.clear()
            robot.set_position(Point(3,5))

            for object in level_3:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_3[1].ishidden() and len(cracks) == 7:

            for object in level_3:
                object.hide()
            
            cracks.clear()
            robot.set_position(Point(3,7))

            for object in level_4:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_4[1].ishidden() and len(cracks) == 44:

            for object in level_4:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(14,2))

            for object in level_5:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_5[1].ishidden() and len(cracks) == 42:

            for object in level_5:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(4,6))

            for object in level_6:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_6[1].ishidden() and len(cracks) == 25:

            for object in level_6:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(4,8))

            for object in level_7:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_7[1].ishidden() and len(cracks) == 40:

            for object in level_7:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(5,4))

            for object in level_8:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_8[1].ishidden() and len(cracks) == 19:

            for object in level_8:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(2,5))

            for object in level_9:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_9[1].ishidden() and len(cracks) == 42:

            for object in level_9:
                object.hide()
                
            cracks.clear()
            robot.set_position(Point(7,5))

            for object in level_10:
                object.unhide()

        if robot.get_position().equals(finish.get_position()) and not level_10[1].ishidden() and len(cracks) == 40:

            for object in level_10:
                object.hide()
                
            cracks.clear()
            robot.hide()
            congratulations.unhide()
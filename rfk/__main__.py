import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen
from game.level_1 import level_1
from game.level_2 import level_2
from game.level_3 import level_3
from game.level_4 import level_4
from game.level_5 import level_5
from game.level_6 import level_6
from game.level_7 import level_7
from game.level_8 import level_8
from game.level_9 import level_9
from game.level_10 import level_10
 
def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    position = Point(2, 5)
    robot = Actor()
    robot.set_text("#")
    robot.set_position(position)
    cast["robot"] = [robot]

    cast["level_1"] = level_1

    for obstacle in level_2:
        obstacle.hide()
    cast["level_2"] = level_2

    for obstacle in level_3:
        obstacle.hide()
    cast["level_3"] = level_3

    for obstacle in level_4:
        obstacle.hide()
    cast["level_4"] = level_4

    for obstacle in level_5:
        obstacle.hide()
    cast["level_5"] = level_5

    for obstacle in level_6:
        obstacle.hide()
    cast["level_6"] = level_6

    for obstacle in level_7:
        obstacle.hide()
    cast["level_7"] = level_7

    for obstacle in level_8:
        obstacle.hide()
    cast["level_8"] = level_8

    for obstacle in level_9:
        obstacle.hide()
    cast["level_9"] = level_9

    for obstacle in level_10:
        obstacle.hide()
    cast["level_10"] = level_10


    cracks = []
    cast["cracks"] = cracks

    congratulations = Actor()
    congratulations.set_text("!!CONGRATULATIONS ON BEATING THE GAME!!")
    congratulations.set_position(Point(2,8))
    congratulations.hide()
    cast["congratulations"] = [congratulations]

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
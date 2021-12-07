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
from game.randomize_positions import RandomizePositionsAction

 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    marquee = Actor()
    marquee.set_text("")
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(2, 5)
    robot = Actor()
    robot.set_text("#")
    robot.set_position(position)
    cast["robot"] = [robot]

    level_1 = []
    position = Point(1, 1)
    finish = Actor()
    finish.set_text("*")
    finish.set_position(position)
    level_1.append(finish)
    
    text = "@"
    position = Point(1, 3)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_1.append(rock)

    
    position = Point(1, 5)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_1.append(rock)

    position = Point(1, 6)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_1.append(rock)
    
    
    
    cast["artifact"] = level_1

    level_2 = []
    position = Point(1, 2)
    finish = Actor()
    finish.set_text("*")
    finish.set_position(position)
    level_2.append(finish)

    text = "N"
    position = Point(4, 5)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_2.append(rock)
   
    position = Point(5, 5)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_2.append(rock)

    position = Point(6, 5)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(position)
    level_2.append(rock)
    
    
    
    
    for obstacle in level_2:
        obstacle.hide()
    cast["level_2"] = level_2

    cracks = []
    cast["cracks"] = cracks

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    randomize_positions = RandomizePositionsAction()

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
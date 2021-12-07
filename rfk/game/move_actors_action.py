from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor, cast)

    def _move_actor(self, actor, cast):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        cracks = cast["cracks"]
        level_1 = cast["artifact"]
        level_2 = cast["level_2"]
        position = actor.get_position()
        velocity = actor.get_velocity()
        past_position = position
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        
        move = "yes"
        finish_1 = level_1[0]
        finish_2 = level_2[0]
        for obstactle in level_1:
            if obstactle == finish_1 and not level_1[1].ishidden():
                pass
            elif position.equals(obstactle.get_position()) and not level_1[1].ishidden():
                move = "no"
        for obstactle in level_2:
            if obstactle == finish_2 and not level_2[1].ishidden():
                pass
            elif position.equals(obstactle.get_position()) and not level_2[1].ishidden():
                move = "no"
                
        if move == "yes":
            actor.set_position(position)
            crack = Actor()
            crack.set_text("/")
            crack.set_position(past_position)
            cracks.append(crack)
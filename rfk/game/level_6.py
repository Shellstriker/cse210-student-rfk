from game.actor import Actor
from game.point import Point

level_6 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(4,1))
level_6.append(finish)

for x in range (1, 4):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_6.append(rock)

for x in range (5, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_6.append(rock)

for x in range (1, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,7))
    level_6.append(rock)

for y in range(1,8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_6.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(7,y))
    level_6.append(rock)
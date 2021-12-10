from game.actor import Actor
from game.point import Point

level_7 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(5,1))
level_7.append(finish)

for x in range(1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_7.append(rock)

for x in range(1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_7.append(rock)

for x in range(6, 10):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_7.append(rock)

for y in range(4,7):
    for x in range(4, 7):
        rock = Actor()
        rock.set_text("@")
        rock.set_position(Point(x,y))
        level_7.append(rock)

for x in range(1, 10):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,9))
    level_7.append(rock)

for y in range(1,10):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_7.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(9,y))
    level_7.append(rock)
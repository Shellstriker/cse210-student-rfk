from game.actor import Actor
from game.point import Point

level_8 = []
finish = Actor()
finish.set_text("*")
finish.set_position(Point(5,1))
level_8.append(finish)

for x in range (1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_8.append(rock)

for x in range (6, 9):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_8.append(rock)

for x in range (1, 9):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,5))
    level_8.append(rock)

for y in range (1, 6):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_8.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(9,y))
    level_8.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(6,4))
level_8.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(3,3))
level_8.append(rock)




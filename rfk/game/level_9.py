from game.actor import Actor
from game.point import Point

level_9 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(14,1))
level_9.append(finish)

for x in range (1, 4):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_9.append(rock)

for x in range (3, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_9.append(rock)

for x in range (6, 11):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,2))
    level_9.append(rock)

for x in range (10, 14):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_9.append(rock)

for x in range (15, 18):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_9.append(rock)

for x in range (1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_9.append(rock)

for x in range (4, 18):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,7))
    level_9.append(rock)

for y in range(1,6):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(13,y))
    level_9.append(rock)

for y in range(3,8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(17,y))
    level_9.append(rock)

for y in range(1,4):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(15,y))
    level_9.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(8,6))
level_9.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(1,5))
level_9.append(rock)
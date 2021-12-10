from game.actor import Actor
from game.point import Point

level_4 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(14,8))
level_4.append(finish)

for x in range (1, 6):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_4.append(rock)

for x in range (5, 13):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,2))
    level_4.append(rock)

for x in range (5, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_4.append(rock)

for x in range (11, 13):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_4.append(rock)

for x in range (12, 17):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_4.append(rock)

for x in range (1, 3):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_4.append(rock)

for x in range (2, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,8))
    level_4.append(rock)

for x in range (4, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,5))
    level_4.append(rock)

for x in range (6, 12):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,8))
    level_4.append(rock)

for x in range (10, 14):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,5))
    level_4.append(rock)

for y in range(1,5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_4.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(16,y))
    level_4.append(rock)

for y in range(5,9):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(4,y))
    level_4.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(6,y))
    level_4.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(11,y))
    level_4.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(13,y))
    level_4.append(rock)

for y in range(4,9):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(15,y))
    level_4.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(2,y))
    level_4.append(rock)
from game.actor import Actor
from game.point import Point

level_1 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(14,1))
level_1.append(finish)

for x in range (1, 6):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_1.append(rock)
    
for x in range (5, 12):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,2))
    level_1.append(rock)

for x in range (11, 14):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_1.append(rock)


for x in range (1, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_1.append(rock)

for x in range (7, 10):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_1.append(rock)

for x in range (9, 16):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_1.append(rock)

for y in range (4, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_1.append(rock)

for y in range (2, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(5,y))
    level_1.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(11,y))
    level_1.append(rock)

for y in range (1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(13,y))
    level_1.append(rock)

for y in range (1, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(15,y))
    level_1.append(rock)

for y in range (4, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(7,y))
    level_1.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(9,y))
    level_1.append(rock)
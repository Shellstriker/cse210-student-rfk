from game.actor import Actor
from game.point import Point

level_2 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(13,1))
level_2.append(finish)

for x in range (1, 4):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_2.append(rock)

for x in range (4, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,3))
    level_2.append(rock)

for x in range (7, 13):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_2.append(rock)

for x in range (1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,7))
    level_2.append(rock)

for x in range (4, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_2.append(rock)

for x in range (7, 15):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,7))
    level_2.append(rock)
    
for x in range (10, 12):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_2.append(rock)

for x in range (3, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,4))
    level_2.append(rock)

for y in range (1, 8):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_2.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(14,y))
    level_2.append(rock)

for y in range (1, 5):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(3,y))
    level_2.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(12,y))
    level_2.append(rock)
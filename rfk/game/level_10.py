from game.actor import Actor
from game.point import Point

level_10 = []

finish = Actor()
finish.set_text("*")
finish.set_position(Point(7,1))
level_10.append(finish)

for x in range (1, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_10.append(rock)
    
for x in range(1,13):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,6))
    level_10.append(rock)

for x in range (8, 13):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(x,1))
    level_10.append(rock)

for y in range (1, 7):
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(1,y))
    level_10.append(rock)
    rock = Actor()
    rock.set_text("@")
    rock.set_position(Point(13,y))
    level_10.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(10,5))
level_10.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(2,5))
level_10.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(7,3))
level_10.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(11,3))
level_10.append(rock)

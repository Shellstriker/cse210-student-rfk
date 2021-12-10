from game.actor import Actor
from game.point import Point

level_3 = []

position = Point(3, 2)
finish = Actor()
finish.set_text("*")
finish.set_position(position)
level_3.append(finish)
    
text = "@"
for x in range (1, 5):
    rock = Actor()
    rock.set_text(text)
    rock.set_position(Point(x,1))
    level_3.append(rock)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(Point(x,6))
    level_3.append(rock)

for y in range (1, 7):
    rock = Actor()
    rock.set_text(text)
    rock.set_position(Point(1,y))
    level_3.append(rock)
    rock = Actor()
    rock.set_text(text)
    rock.set_position(Point(5,y))
    level_3.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(2,5))
level_3.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(2,2))
level_3.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(4,2))
level_3.append(rock)

rock = Actor()
rock.set_text("@")
rock.set_position(Point(4,3))
level_3.append(rock)
print("Rectangle")
from graphics.rectangle import rectanglearea,rectangleperimeter
rectanglearea(2,4)
rectangleperimeter(3,6)

print("Circle")
from graphics.circle import circlearea as a,circleperimeter as p
a(2)
p(4)

import graphics.threedgraphics.cuboid as c
print("Cuboid")
c.cuboidarea(2,3,4)
c.cuboidperimeter(5,6,7)

import graphics.threedgraphics.sphere as s
print("Sphere")
s.spherearea(6)
s.sphereperimeter(4)
print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")

import math

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def _init_(self, corner: Point, width: float, height: float):
        self.corner = corner  
        self.width = width
        self.height = height

class Circle:
    def _init_(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

def point_in_circle(circle: Circle, point: Point) -> bool:
    dx = circle.center.x - point.x
    dy = circle.center.y - point.y
    distance = math.hypot(dx, dy)
    return distance <= circle.radius

def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
    ]
    return all(point_in_circle(circle, corner) for corner in corners)

def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
    ]
    return any(point_in_circle(circle, corner) for corner in corners)


if _name_ == "_main_":
    my_circle = Circle(Point(150, 100), 75)

    test_point = Point(160, 120)

    my_rect = Rectangle(Point(120, 80), 40, 30)

    print("Point in circle:", point_in_circle(my_circle, test_point))
    print("Rectangle fully in circle:", rect_in_circle(my_circle, my_rect))
    print("Rectangle overlaps circle:", rect_circle_overlap(my_circle, my_rect))

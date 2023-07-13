#!/usr/bin/python3
"""Base model"""
import json
import os.path
import turtle


class Base:
    """class for base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to Json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""
        list = []
        if list_objs is not None:
            list = [items.to_dictionary() for items in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """Json string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to instance"""
        if cls.__name__ == "Rectangle":
            holder = cls(1, 1)
        if cls.__name__ == "Square":
            holder = cls(1)
        holder.update(**dictionary)
        return holder

    @classmethod
    def load_from_file(cls):
        """file to instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws our shapes"""
        turtle.getscreen()
        turtle.shape("turtle")
        for rect in list_rectangles:
            turtle.pencolor(red)
            turtle.setpos(rect.x, rect.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.forward(rect.width)
                turtle.left(90)
            turtle.penup()
        for sq in list_squares:
            turtle.pencolor(blue)
            turtle.setpos(sq.x, sq.y)
            turtle.pendown()
            for i in range(4):
                turtle.foward(sq.height)
                turtle.left(90)
            turtle.penup()
        turtle.exitonclick()

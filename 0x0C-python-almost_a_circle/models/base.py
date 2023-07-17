#!/usr/bin/python3
'''
    Importing modules
'''
import json
import csv
import turtle

'''
    Base - Class
'''


class Base:
    '''
        Initialisation of the class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
            Initialisation of the constructor of the class Base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            to_json_string - Static method to return the json format of dicts
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            save_to_file - Class method to save the json format in a file
        '''
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''
            from_json_string - Method to extract the list of dicts from json.
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            create - Class method to create an instance of the class
        '''
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == "Square":
                obj = cls(11)
            else:
                obj = cls(22, 11)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        '''
            load_from_file - Class method to instances from json file
        '''
        inst_list = []
        filename = cls.__name__ + ".json"
        content = ""
        try:
            with open(filename, "r") as f:
                content = f.read()
        except Exception:
            return inst_list
        list_dict = Base.from_json_string(content)
        for dictionary in list_dict:
            inst_list.append(cls.create(**dictionary))
        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
            save_to_file_csv - Class method to store instance in CSV file.
        '''
        filename = cls.__name__ + ".csv"
        list_data = []
        for obj in list_objs:
            dictionary = obj.to_dictionary()
            data = []
            data.append(int(dictionary["id"]))
            if cls.__name__ == "Rectangle":
                data.append(int(dictionary["width"]))
                data.append(int(dictionary["height"]))
            elif cls.__name__ == "Square":
                data.append(int(dictionary["size"]))
            data.append(int(dictionary["x"]))
            data.append(int(dictionary["y"]))
            list_data.append(data)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for row in list_data:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        '''
            load_from_file_csv - Class method to load the instances from csv
        '''
        filename = cls.__name__ + ".csv"
        inst_list = []
        list_dict = []
        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                list_dict = list(csv.DictReader(f, fieldnames=fields))
        except Exception:
            return inst_list
        for dictionary in list_dict:
            for elem in dictionary:
                dictionary[elem] = int(dictionary[elem])
            obj = cls.create(**dictionary)
            inst_list.append(obj)
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
            draw - Static method to draw the shapes passed by the lists
        '''
        screen = turtle.Turtle()
        screen.screen.bgcolor("white")
        screen.pensize(3)
        screen.shape("turtle")

        screen.color("#bbaaff")
        for rect in list_rectangles:
            screen.showturtle()
            screen.up()
            screen.goto(rect.x, rect.y)
            screen.down()
            for i in range(2):
                screen.forward(rect.width)
                screen.left(90)
                screen.forward(rect.height)
                screen.left(90)
            screen.hideturtle()

        screen.color("#bbbb00")
        for sq in list_squares:
            screen.showturtle()
            screen.up()
            screen.goto(sq.x, sq.y)
            screen.down()
            for i in range(4):
                screen.forward(sq.size)
                screen.left(90)
            screen.hideturtle()
        turtle.exitonclick()

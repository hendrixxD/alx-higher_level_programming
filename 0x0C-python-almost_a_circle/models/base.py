#!/usr/bin/python3
""""base class" of all classes in this project.
the goal is to manage 'id' attribute in all future classes
and avoid duplicating the the same code"""


class Base:
    """base class with private class attribute
    and class contructor
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """if 'id' is not None
            public instance attribute 'id' is assign to it current value
            i assume id is and type(int)[no need to test for that]

            otherwise:
                __nb_object is increamented, and the value is asssigned
                to 'id' attribute
        """

        if id is not None:
            self.id = id
        else:
           Base. __nb_object += 1
           self.id =Base. __nb_object

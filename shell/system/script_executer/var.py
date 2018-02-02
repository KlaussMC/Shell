from string import *

class Var:
    name = ""
    val = 0
    namingChars = "abcdefghijklmnopqrstuvwxyz_-*ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, name, val):
        if (name[0] in self.namingChars):
            self.name = name
        self.val = val

    def set(self, val):
        self.val = val

    def get(self):
        if (isinstance(self.val, string)):
            return self.val.get()
        else:
            return self.val
        #
        # return self.val

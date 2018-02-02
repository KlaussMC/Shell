from system import *
import os

class Path(System):
    val = "/"

    def __init__(startDir):
        val = startDir

    def getPath():
        return val

    def changeDir(self, newDir):
        if (newDir[0] != "/" and newDir[:2:] != ".."):
            if (os.path.isdir(self.val + newDir)):
                self.val += newDir + "/"
            else:
                err.rnf()
        elif (newDir[:2:] == ".."):
            self.val = self.val[:self.val.rfind("/"):]
            self.val = self.val[:self.val.rfind("/"):]
            self.val += "/"
        else:
            if (os.path.isdir(newDir)):
                self.val = newDir
            else:
                err.rnf()

    def listDir(self):
        items = []
        for item in os.listdir(self.val):
            if (os.path.isfile(self.val + item)):
                items.append("file: " + item)
            else:
                items.append("dir:  " + item)

        return items

# [".", ".", "l", "l", "o"]

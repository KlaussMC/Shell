class statement:
    val = 0

    def __init__(self, val):
        self.val = val[1:]
        self.cmd = val[0]

    def get(self):
        return self.val
    def getCMD(self):
        return self.cmd
    def getAll(self):
        return [self.cmd, self.val]

    def set(self, val):
        self.val = val
        return self.val

    def getType(self):
        return "stm"

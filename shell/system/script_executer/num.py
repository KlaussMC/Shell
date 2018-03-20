class num:
    val = 0

    def __init__(self, val):
        self.val = float(val)

    def get(self):
        return self.val

    def set(self, val):
        self.val = nnt(val)
        return self.val

    def getType(self):
        return "int"

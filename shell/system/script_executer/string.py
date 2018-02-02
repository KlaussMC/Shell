class string:
    val = ""

    def __init__(self, val):
        self.val = val
        # print "val: " + self.val

    def get(self):
        return self.val

    def set(self, val):
        self.val = val
        return self.val

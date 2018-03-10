class string:
    val = ""

    def __init__(self, val):
        self.val = val
        

    def get(self):
        return self.val

    def set(self, val):
        self.val = val
        return self.val

class Label:
    name = ""
    code = ""

    _vars = []
    _args = []

    def __init__(self, name, code, args=[]):
        self.name = name
        for i in range(len(code)):
            # if (i > 1):
            self.code += code[i] + "\n"
        self.args = args
            # else:
                # self.code += code[i]

    def get(self):
        return self.code

    def getVar(self, varName):
        for i in self._vars:
            if (i.name == varName):
                return i.get()

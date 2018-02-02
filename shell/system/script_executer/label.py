class Label:
    name = ""
    code = ""

    _vars = []

    def __init__(self, name, code):
        self.name = name
        for i in range(len(code)):
            # if (i > 1):
            self.code += code[i] + "\n"
            # else:
                # self.code += code[i]

    def get(self):
        return self.code

    def getVar(self, varName):
        for i in self._vars:
            if (i.name == varName):
                return i.get()

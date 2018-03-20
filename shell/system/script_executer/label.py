class Label:
    name = ""
    code = ""

    _vars = []
    _args = []

    def __init__(self, name, code, args=[]):
        self.name = name
        for i in range(len(code)):
            newStr = code[i]+"\n"
            self.code += newStr.lstrip()
        self.args = args

    def get(self):
        return self.code

    def getVar(self, varName):
        for i in self._vars:
            if (i.name == varName):
                return i.get()


    def getType(self):
        return "label"

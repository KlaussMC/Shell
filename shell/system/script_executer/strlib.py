class stng:
    def flipString(self, str):
        newStr = str[::-1]

        return newStr

    def trim(self, val):
        newStr = ''
        for i in range(len(val)):
            if (val[i] != " " and val[i] != "\t" and val[i] != "\n"):
                newStr = val[i::]
                break

        newStr = self.flipString(newStr)
        for i in range(len(val)):
            if (val[i] != " " and val[i] != "\t" and val[i] != "\n"):
                newStr = val[i::]
                break

        return newStr

    def popChar(self, str, char):
        newStr = str[:str.rfind(char):]
        return newStr

    def clearChar(self, _str, char):
        newStr = ""
        newStr = _str.replace(char, "")

        return newStr

STR = stng()

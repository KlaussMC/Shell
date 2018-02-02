from string import *

var = []

def run(val):
    code = val

    global var

    val = STR.popChar(val, ";")
    val = STR.trim(val)

    statements = code.split(";")

    try:
        if (len(statements) > 0):
            for s in statements:

                words = s.split()
                if (words[0] == 'var'):
                    if (words[2] == "="):
                        var.append({words[1]: words[3]})
                    else:
                        err = code_error("SyntaxError", "invalid syntax")

                else:
                    if (varExists(var, words[0])):
                        if (len(words) == 1):
                            return getVar(var, words[0])
                        elif (words[1] == "="):
                            var = setVar(var, words[0], words[2])
                        elif (words[1] == "+="):
                            if (getVarType(var, words[0] != 0)):
                                setVar(var, words[0], getVar(var, words[0]) + words[3])
                            else:
                                err = code_error("TypeError", "cannot perform \'append\' action on boolean variable")
                        elif (words[1] == "-="):
                            if (getVarType(var, words[0] == 1)):
                                etVar(var, words[0], getVar(var, words[0]) - words[3])
                            else:
                                err = code_error("TypeError", "cannot perform \'subtract\' action on non-numeric variable")
                    else:
                        err = code_error("VarError", "The Specified variable does not exist")
    except:
        val = STR.popChar(val, ";")
        return run (val)

    return var

def varExists(var, varName):
    matches = 0
    try:
        for i in var:
            if (i[varName]):
                return True
            else:
                matches += 1
    except:
        return False

    if (matches == 0):
        return False

def getVar(var, varName):
    matches = 0
    for i in var:
        if (i[varName]):
            return i[varName]
        else:
            matches += 1

    if (matches == 0):
        err = code_error("VarError", "The Specified variable does not exist")

def setVar(var, varName, val):
    matches = 0
    for i in var:
        if (i[varName]):
            index = var.index(i)

            i = {varName: val}
            var[index] = i
            return var
        else:
            matches += 1

    if (matches == 0):
        err = code_error("VarError", "The Specified variable does not exist")

def getVarType(var, varName):
    varVal = getVar(var, varName)

    if (varVal == True or varVal == False):
        return 0
        #boolean
    elif (varVal / 1 == varVal):
        return 1
        #number, this can be a floating point or an integer, in most cases, the difference is non-critical
    else:
        return 2
        #string

class code_error:
    types = ["TypeError", "SyntaxError", "MathError", "VarError"]
    errType = "none"
    msg = ""
    def __init__(self, typ, msg):
        self.errType = self.types[self.types.index(typ)]

        if (not msg):
            print self.errType
        else:
            print self.errType+ ": " + msg

print run (str(open("testScript.src").read()))

from var import *
from function import *
from label import *
from string import *
from num import *
from strlib import *

from zerofy import *
import evaluate
from filter import *    

import re

_coms = []
_vars = []
_lbls = []

output = ""

done = False
interruptLoc = 0
loop = 0

def Code(_str, rptnum, scope=0, resume=0): #rptnum is repeatNumber, resume is where to resume
    global loop
    global _vars
    global _coms
    global _cmds

    if not isinstance(scope, Label):
        scope = 0

    _coms = re.split("; |\n|;", _str)
    _coms = filterTypes(_coms)

    if _coms:
        _int(scope, resume)

    if (output != None):
        out = output.split("\n")
        print("")
        for op in out:
            if (op != ""):
                print(STR.trim(op))

def _int(s, resume=0):
    global output
    global _coms

    scope = None
    if (s == None):
        scope = 0
    else:
        scope = s

    for i in _coms:
        if i.getCMD() == "out":
            output += evaluate(i.get()) + "\n"
        elif i.getCMD() == "var":
            newVar(i.get()[0], i.get()[1], i.get()[2:])
        else:
            if (not isinstance(i.getCMD(), string)) and (not isinstance(i.getCMD(), num)):
                output += "Error: The command " + i.getCMD() + "is unrecognised\n"
                print i.getCMD()

class code_error:
    types = ["TypeError", "SyntaxError", "MathError", "VarError"]
    errType = "none"
    msg = ""
    def __init__(self, typ, msg):
        self.errType = self.types[self.types.index(typ)]

        if (not msg):
            print(self.errType)
        else:
            print(self.errType+ ": " + msg)

def setVar(varName, value):
    global _vars

    matches = 0
    for i in _vars:
        if (i.name == varName):
            matches += 1
            i.set(value)

    if (varName != ""):
        if (matches == 0):
            print("The variable \"" + varName + "\" does not exist")

def isVar(varName):
    global _vars

    matches = 0
    for i in _vars:
        if (i.name == varName):
            matches += 1
            return True

    if (varName != ""):
        if (matches == 0):
            return False

def getVar(varName):
    global _vars

    matches = 0
    for i in _vars:
        if (i.name == varName):
            matches += 1
            return i.get()

    if (varName != ""):
        if (matches == 0):
            print("The variable \"" + varName + "\" does not exist")

def isLabel(name):
    global _lbls
    matches = 0
    for i in _lbls:
        if (name == i.name):
            matches += 1
            return True

    if (matches == 0):
        return False

def getLabel(name):
    global _lbls
    matches = 0
    for i in _lbls:
        if (name == i.name):
            matches += 1
            return i

    if (matches == 0):
        return False

def callLabel(name):
    global _lbls, done, interruptLoc

    Code(getLabel(name).get(), 0, getLabel(name), interruptLoc + 1)

def getVarObj(varName):
    global _vars

    matches = 0
    for i in _vars:
        if (i.name == varName):
            matches += 1
            return i

    if (matches == 0):
        try:
            err = code_error("VarError", "The Variable " + varName + " Does not exist (obj does not exist)")
        except:
            err = code_error("TypeError", "The input " + varName.get() + " is not a variables")

def newVar(name, action, val):
    print val[0].get()
    global output

    if action == "=":
        _vars.append(Var(name, val[1:]))
    else:
        output += "unexpected token" + tokens[0]

# Code calls main Loop. 0 defines Scope and the open request instructs what really needs to executed. this can (should be able to be) replaced by a string of code stored in a label class.
#Now scope is defined last.
Code(open("testScript.arcs").read(), 0)

from var import *
from function import *
from label import *
from string import *
from strlib import *

from zerofy import *

import re

_vars = []
_lbls = []
_coms = []
_cmds = []

output = ""

verbose = False
done = False
interruptLoc = 0
loop = 0

def Code(_str, rptnum, scope=0, resume=0): #rptnum is repeatNumber, resume is where to resume
    global loop
    global _vars
    global _coms
    global _lbls
    global _cmds
    global verbose

    if not isinstance(scope, Label):
        scope = 0

    if (loop <= rptnum):
        if (len(_str) > 7):
            if ("verbose" in _str[:7]):
                verbose = True
            else:
                verbose = False

        _coms = re.split("; |\n|;", _str)
        # _coms = _str.split(";")

        # print len(_coms)
        _coms = filter(None, _coms)
        # print len(_coms)

        startPos = None
        endPos = None

        for i in range(len(_coms)):

            if (_coms[i][0] == ">"):
                startPos = i

            elif(_coms[i][0] == "<"):
                if (startPos != 0):
                    endPos = i

            if (startPos != None and endPos != None):
                name = _coms[startPos][2:_coms[startPos].index("(")]
                _lbls.append(Label(name, _coms[startPos + 1:endPos]))

                # _cmds[i] = Label(name, _coms[startPos + 1:endPos])
                # _cmds = _coms[:startPos] + _coms[endPos:]

                startPos = None
                endPos = None

            elif (startPos == None and endPos == None):
                _cmds.append(_coms[i])

        _int(scope, resume)

    else:
        loop = 0
        return

    if (output != None):
        out = output.split("\n")
        # out = out[1:]
        print("")
        for op in out:
            if (op != ""):
                if (verbose):
                    print(" > " + STR.trim(op))
                else:
                    print(STR.trim(op))
        print("")

def _int(s, resume=0):
    global output

    global _cmds
    global _vars
    global verbose
    global interruptLoc

    global done

    scope = None
    if (s == None):
        scope = 0
    else:
        scope = s

    if (verbose):
        print(_cmds)

    a = 0

    for a in range(resume, len(_cmds)):
        i = _cmds[a]
        if (i != "\n"):
            if (isinstance(i, Label)):
                if (verbose):
                    print(i)
                else:
                    continue
            else:
                words = i.split(" ")
                formatted = []

                #Merge Strings into one index of words array
                firstQuote = 0.0
                secondQuote = 0.0

                __str = ""
                for j in range(len(words)):
                    for x in range(len(words[j])):
                        if (words[j][x] == "\""):
                            if (firstQuote == 0.0):
                                firstQuote = j
                                firstQuote += zerofy(x)
                            else:
                                secondQuote = j
                                secondQuote += zerofy(x)

                    if (firstQuote != 0.0 and secondQuote != 0.0):
                        i1 = int(firstQuote)
                        i2 = int(secondQuote) + 1

                        words.append("")
                        __str = words[i1:i2:]

                        _str_ = ""

                        if (len(__str) != 0): #there is indeed a string that needs to replace the words
                            for x in __str:
                                _str_ += x + " "

                            tmp = words[:i1:]
                            strobj = string(_str_)
                            tmp.append(strobj)
                            # tmp.append(_str_)

                            for x in words[i2:]:
                                tmp.append(x)

                            formatted = tmp

                # strings have been filtered and has not replaced the original words, in addition,
                # a new instance of the string class takes the place of the string that was once the formatted string.
                #however, the son of a bitch is being stubborn and won't work when I request a variable, the var returns Null and I get an error.
                #life suxxx

                fmt = []

                if (len(formatted) > 0):
                    _cmnd = ""
                    _cmnd = formatted[0]

                    fmt = formatted[1:]

                elif (len(words) > 0):

                    _cmnd = ""
                    _cmnd = words[0]

                    fmt = words[1:]

                if (_cmnd == "out"):
                    str_ = ""
                    for w in range(len(fmt)):
                        if (isinstance(fmt[w], string)):
                            str_ += fmt[w].get()[1:len(fmt[w].get()) - 2:]
                        else:
                            try:
                                if (scope == 0):
                                    str_ += getVar(fmt[w]).replace("\"", "")
                                else:
                                    str_ += scope.getVar(fmt[w]).replace("\"", "")
                            except:
                                continue
                    output += "\n" + str_

                elif (isLabel(_cmnd)):
                    l = getLabel(_cmnd)

                    # break
                    interruptLoc = a
                    callLabel(_cmnd)
                    break

                elif (_cmnd == "var"):
                    if (scope == 0 or scope == None):
                        _vars.append(Var(fmt[0], fmt[2]))
                    else:
                        scope._vars.append(Var(fmt[0], fmt[2]))


                    if (verbose):
                        if (scope == 0):
                            print("var created: " + _vars[len(_vars) - 1].name + ": " + getVar(_vars[len(_vars) - 1].name))
                        else:
                            print("var created: " + scope._vars[len(scope._vars) - 1].name + ": " + scope.getVar(scope._vars[len(scope._vars) - 1].name))

                elif ("::" in _cmnd):
                    continue

                else:
                    if (verbose):
                        print("The command " + _cmnd + " is not a variable name, label call or a command")
                    else:
                        print("unknown command " + _cmnd)

        # print a
    # a += 1
    return

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

def getVar(varName):
    global _vars

    # matches = 0
    for i in _vars:
        if (i.name == varName):
            # matches += 1
            return i.get()

    # if (matches == 0):
    #     try:
    #         err = code_error("VarError", "The Variable " + varName + " Does not exist")
    #     except:
    #         err = code_error("TypeError", "The input " + varName.get() + " is not a variable")

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

# Code calls main Loop. 0 defines Scope and the open request instructs what really needs to executed. this can (should be able to be) replaced by a string of code stored in a label class.
#Now scope is defined last.
Code(open("testScript.src").read(), 0)

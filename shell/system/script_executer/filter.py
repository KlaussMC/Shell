from zerofy import *
from string import *
from num import *
from statement import *
from label import *
from statement import *

def filterTypes(input):
    coms = [''] + input
    filtered = []

    startPos = 0
    endPos = 0

    # print coms

    def isNum(str):
        numericChars = "012346789."
        for i in str:
            if i not in numericChars:
                return False;
        else:
            return True

    def getCharsBetween(start, end):
        val = ""
        for i in range(len(coms)):
            if i >= int(start//1) and i <= int(end//1):
                for j in range(len(coms[i])):
                    if j >= int((start - int(start//1))*10) and j <= int((end - int(end//1))*10):
                        val += coms[i][j]
        return val[1:-1:]

    def filterStatement(statement):
        b = 0
        newStatementVal = []
        for i in statement.split(" "):
            if i[0] == "\"" and i[-1] == "\"":
                newStatementVal.append(string(i[1:-1]))
            elif isNum(i):
                newStatementVal.append(num(i))
            else:
                newStatementVal.append(i)

        print newStatementVal
        if newStatementVal:
            return newStatementVal
        else:
            return None

    for i in range(len(coms)):
        if not isinstance(coms[i], string):
            if coms[i]:
                val = filterStatement(coms[i])
                if val:
                    if not val[0] == "::":
                        s = statement(val)
                        filtered.append(s)
                else:
                    continue

            for j in range(len(coms[i])):
                if coms[i][j] == ">":
                    startPos = i + zerofy(j)
                elif coms[i][j] == "<":
                    endPos = i + zerofy(j)
                    lbl = Label(coms[1], getCharsBetween(startPos, endPos), coms[2:])
                    filtered.append(lbl)

    filtered = removeWhiteSpace(filtered)
    return filtered

def removeWhiteSpace(arr):
    newArr = []
    for i in arr:
        if i:
            newArr.append(i)
        else:
            continue
    return newArr

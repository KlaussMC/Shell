from var import *
import index

def evaluate(input):
    tokens = insertVarVals(input)
    retType = identifyReturnType(tokens)
    newValue = None

    actions = "+ - * / = += -= *= /=".split(" ")
    strActions = "+ +=".split(" ")

    action = "+"

    if retType == "int":
        newValue = 0
        for i in tokens:
            # print i
            if i in actions:
                action = i
            else:
                if action == "+":
                    newValue += i.get()
                elif action == "-":
                    newValue -= i.get()
                elif action == "*":
                    newValue *= i.get()
                elif action == "/":
                    newValue /= i.get()

    elif retType == "str":
        newValue = ""
        for i in tokens:
            if i in strActions:
                action = i
            elif i.getType() == "var":
                i = i.get()
            else:
                if action == "+":
                    newValue += i.get()

    return newValue

def identifyReturnType(tokens):
    type = "int"
    for i in tokens:
        try:
            if i.getType() == "str":
                type="str"
            elif i.getType() == "var":
                if i.getValType() == "str":
                    type="str"
        except:
            continue

    return type

def insertVarVals(input):
    newArr = []
    for i in input:
        if index.isVar(i):
            newArr.append(index.getVar(i))
        else:
            newArr.append(i)
    return newArr

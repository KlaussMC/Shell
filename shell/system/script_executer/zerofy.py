def zerofy(num):
    strlen = len(str(num))

    numstr = "0."
    for i in range(len(str(num)) - 1):
        numstr += "0"

    numstr += "1"

    return num * float(numstr)

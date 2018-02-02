def formatCode(val):
    code = val
    var = []

    statements = code.split(";")

    for s in statements:
        words = s.split()
        if (words[0] == 'var'):
            if (words[2] == "="):
                var.append({words[1]: words[3]})

            

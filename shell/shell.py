from system.system import *
from system.path import Path
# import system.system

import os

input_str = ""
command = ""

clear = lambda: os.system('cls')

sys = System()
path = Path()

def loop(i_s):
    global path, input_str

    # input_str = raw_input(path.val + " > ")
    input_str = i_s

    format_str(input_str)

def format_str(input_str):
    global command
    command = ""
    vals = ""

    for i in range(len(input_str)):
        if (input_str[i] == " "):
            vals = input_str[i + 1::]
            break
        else:
            command += input_str[i]

    command = command.lower()

    if (command == "exit"):
        exit()
    else:
        interpret(vals)

def interpret(val):
    global err
    global command
    try:
        if (command == "cd"):
            path.changeDir(val)
        elif (command == "ls"):
            items = path.listDir()
            for i in items:
                return i
        elif (command == "echo"):
            return val
        elif (command == "clear"):
            clear()
        else:
            err.uc()
    except("NameError"):
        err.uc()

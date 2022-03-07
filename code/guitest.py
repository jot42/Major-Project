from multiprocessing.connection import wait
import tkinter
import time
from pynput.keyboard import Key, Controller
from vcos_commands import *

root = tkinter.Tk()
root.title("VCOS - Voice Controlled OpenSCAD")
root.geometry('800x600')
w = tkinter.Label(root, text="Hello, world!")
w.pack()

def load_commands():
    return {
        #Core System Commands
        'load' : load_projects,

        #Mathmatical Operations
        'addition' : run_addition,
        'subtraction' : run_subtraction,
        'multiplication' : run_multiplication
    }

command = load_commands()

keyboard = Controller()

#Open Dictation
keyboard.press(Key.cmd_l)
keyboard.tap('h')
keyboard.release(Key.cmd_l)

time.sleep(1)

keyboard.press(Key.cmd_l)
keyboard.tap('h')
keyboard.release(Key.cmd_l)

button_calibrate = tkinter.Button(
    text="Calibrate microphone",
    width="25",
    height="5",
)

button_calibrate.pack()
#root.mainloop()

#app = gui()
#app.setTitle("VCOS - Voice Controlled OpenSCAD")
#app.addButton("calibrate", calibrate)
#app.setLocation("CENTER")
#app.setSize(800,600)
#app.go()
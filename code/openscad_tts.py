import sys
from vcos_commands import *
import speech_recognition as sr
import argparse

#Variables
user_speech = ""
recognizer = sr.Recognizer()
microphone_calibration = 0
current_file = None

run_main = True #Will dictate whether the main function is run (some arguments require immediate exit)

#Command Line Argument Vars
arg_config = False # -c 'Opens the program in config mode'
arg_filename = False # -f 'Specifies a an OpenSCAD file'
arg_list_projects = False # -p 'Generates a list of SCAD files in the "user_files dir"'

def load_commands():
    return {
        #Core System Commands
        'load' : load_projects,

        #Mathmatical Operations
        'addition' : run_addition,
        'subtraction' : run_subtraction,
        'multiplication' : run_multiplication
    }



def config_mode():
    
    #Menu Loop
    run_menu = True

    print("System Information")
    if os.name == "nt":
        print("OS: Windows")
    elif os.name == "posix":
        print("OS: UNIX")

    while(run_menu):
        print("")
        print("Voice Controlled OpenSCAD Configuration Menu")
        print("1. Set microphone calibration level")
        print("2. Run Voice Controlled OpenSCAD")
        print("3. Quit")
        user_option = input()

        if user_option == '1':
            print("Calibration Menu")

        elif user_option == '2':
            print("Running VCOS")

        elif user_option == '3':
            print("Quitting")
            quit()


def parse_args():
    for item in sys.argv:
        loading_file = False

        if loading_file:
            current_file = os.listdir(os.getcwd() + "/projects/" + item)
            print(current_file)
            loading_file = False

        if item == '-c':
            print("Opening configuration window")
            config_mode()
        elif item == '-f':
            loading_file = True
        elif item == '-p':
            commands.show_projects()
            run_main = False
            
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config', help='Opens VCOS configuration menu', required=False, action='store_true')
    parser.add_argument('-f', '--file'  , help='Specifies a file to be opened', required=False, nargs=1) 
    args = parser.parse_args()

    if args.c:
        config_mode()

    #parse_args() #Parses the command line arguments
    #startup() #Starts the program
from click import command
import os

if __name__ == "__main__":
    pass

#Core System Commands

def show_projects():
    file_amount = 0

    print("Here are your available projects:")
    for file in os.listdir(os.getcwd() + "/projects"):
        
        if file.endswith(".scad"):
            file_amount += 1
            print(file_amount, " ", file)

    #Returns the named OpenSCAD file (if found)
def load_projects():
    print("Here are your available projects:")
    for file in os.listdir(os.getcwd() + "/user_files"):
        file_amount = 0

        if file.endswith(".scad"):
            file_amount += 1
            print(file_amount, " ", file)

    #Mathmatical Operations
def run_addition():
        print("ADDITION NOT IMPLETMENTED YET")
def run_subtraction():
        print("SUBTRACTION NOT IMPLEMENTED YET")
def run_multiplication():
        print("MULTIPLICATION NOT IMPLEMENTED YET")
def run_division():
        print("DIVISION NOT IMPLEMENTED YET")
def run_modulo():
        print("MODULO NOT IMPLEMENTED YET")
def run_exponentiation():
        print("EXPONENTIATION NOT IMPLEMENTED YET")
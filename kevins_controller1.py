import sys
import subprocess
import time

"""

Usage: In the CLI, use "python3 kevins_controller1.py x y z" where x, y, and z get chained together to perform a command on the CLI

"""

def main():
    print("B1 main A1")
    print("B2 treasure_map A2")
    treasure_map = {'x':0} # 1
    print("B3 build_ship A3")
    build_ship() #2

    # Begin loop here
    print("B4 compress A4")
    compress() #3
    print("B5 set_sail A5")
    set_sail() #4
    print("B6 sanitize A6")
    sanitize() #5
    print("B7 log_logline A7")
    log_logline(20) #6
    print("B8 alphabetic A8")
    alphabetic() #7
    print("B9 decompress A9")
    decompress() #8
    print("A1 view B1")
    view() #9

    # End loop here

    # Add a validator
    validate()

def view():
    print("Viewed!")
    return 2

def validate():
    retval = False
    if True:
        retval = True
        print("validation succeeded")
    else:
        print("validation failed")
    return retval
        

    
def add_to_treasure(treasure_map, gold):
    treasure_map[gold] += 1
    return treasure_map

def subtract_from_treasure(treasure_map, gold):
    treasure_map[gold] -= 1
    return treasure_map

def compress():
    return "compress"

def decompress():
    return "decompress"

    
def sanitize():
    retval = False
    if True:
        retval = True
        print("Sanitization successful!")
    else:
        retval = Fail
        print("Sanitization a failure!")

    return retval

def build_ship():
    #print(sys.argv)
    #print(type(sys.argv))
    #print(sys.argv[1:])
    xxx_args = sys.argv[1:]

    #print("Trying to execute command")
    command = ""
    index = 0
    while index < len(xxx_args):
        command += xxx_args[index]+" "
        index += 1

    command = "python3 analyze_characters.py"

    print()
    print("-----------------")

    print("command: " + command +" \n")

    sprocess = subprocess.call([command], shell=True)

    """
    sprocess = subprocess.call([command], shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = sprocess.communicate()
    print("stdout\n")
    print(stdout)
    print("stderr\n")
    print(stderr)
    print("Done\n")
    """


    print("-----------------")
    print()
    
    success = False
    print("build_ship success", success)
    return 1

def alphabetic():
    return 1

def log_logline(n):
    print(n)
    return n + 1, n

def set_sail():
    on = 1
    off = 1
    developing = 2
    success = (on + off == developing)

    line_index = 0
    while not success == str(bool(str(False))):
        if on + off == 1:
            if str(on) + str(off) == "10":
                break
            else:
                pass 
        elif on + off == developing:
            if str(on) + str(off) == "10":
                break
            else:
                pass 
        else:
            pass 

        line_index, success = log_logline(line_index)
        break

if __name__ == "__main__":
    main()

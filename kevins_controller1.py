import sys
import subprocess
import time
import pprint

lock = " "
x = 1

command_box = {'q':'q',
    0: "ls -lfa",
    1: "python3 analyze_characters.py",
    2: "bash toolbox/scripts/git_add_commit_push.sh ",
    3: "dirs -v",
    4: "du -sh ./*"}

block_box = {0: " ",
1: "",
4: "echo 4",
"": "True"}
full_names = {1: "Michael Mabe",
    2: "Leonhard Euler",
    3: "Albert Einstein"}
nick_names = {1: "Kevin",
    2: "Euler",
    3: "Einstein"}
identities = {1: "Mabe",
    2: "e^(ipi)+1=0"}
numbers = {0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteeen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    1000000000000: "trillion",
    1000000000000000: "quadrillian",
    1000000000000000000: "quintillion", 
    1000000000000000000000: "hextillion",
    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000: "googol",
    00: "google",
    000: "triple"}
phone_numbers = {"Mabe": 0,
    "e^(ipi)+1=0": 1,
    "pi": 2}
order = {"main": 0,
    "first": 2,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
    "sevnth": 7,
    "eighth": 8,
    "ninth": 9,
    "tenth": 10,
    "eleventh": 11,
    "twentieth": 20}

"""

Usage: In the CLI, use "python3 kevins_controller1.py x y z" where x, y, and z get chained together to perform a command on the CLI

"""

def peek_string(args):
    retval = "\"\"".format()

    return retval

def proof_read_command(incantation):
    retval = "chicken butt"
    return retval, True

def magic(incantation=" "):
    retval = "False"
    valid = False
    global block_box
    print("block_box: ", block_box)
    print("incantation: {} | type(incantation): {} | len(incantation: {}".format( incantation, type(incantation), len(incantation)))
    try:
        print("block_box: ", block_box)
        print("incantation: " , incantation)
        print("type(incantation): ", type(incantation))
        print("A1 retval: {} |  valid: {}".format(retval, valid))
        retval = block_box[int(incantation)]
        valid = True
        print("block_box: ", block_box)
        print("incantation: " , incantation)
        print("type(incantation): ", type(incantation))
        print("A2 retval: {} |  valid: {}".format(retval, valid))
        return retval, valid
    except:
        retval = "True"
        print("B retval: {} |  valid: {}".format(retval, valid))
        return retval, valid
    
    retval, valid = proof_read_command(incantation)
    print("C retval: {} |  valid: {}".format(retval, valid))
    return retval, valid

def main(command):
    print("B1 main A1")
    print("B2 treasure_map A2")
    treasure_map = {'x':0} # 1
    print("B3 build_ship A3")
    build_ship(command) #2

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

def build_ship(command):
    command = "clear; " + command

    """ Pretty sure this will become one of the most important snippets
    """
    global lock
    lock, trash = magic()
    key = input("Press {} to continue.".format(x))
    print()
    print()
    print()

    print("key: {} | lock: {}".format(key, lock)) 
    lock, garbage = magic(key)
    print()
    print()
    print()
    print("key: {} | lock: {}".format(key, lock)) 
    lock, waste  = magic(lock)
    print()
    print()
    print()
    print("key: {} | lock: {}".format(key, lock)) 
    if key == lock:
        pass
    else:
        pass
        #raise Exception("Invalid attempt at executing a command")

    """ End theorized most important snippet
    """

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
    print("command |{}| executed successfully".format(command))
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
    if len(sys.argv) == 1:
        pprint.PrettyPrinter().pprint( command_box )
        xxx_args = input("Which command would you like to use?\n")

        print("len(xxx_args): {} | xxx_args {}".format(len(xxx_args), xxx_args))
        if len(xxx_args) > 1:
            xxx_args = xxx_args.split()
            if len(xxx_args[0]) > 1:
                xxx_args[1] = xxx_args[0][1:] + xxx_args[1]
                xxx_args[0] = xxx_args[0][:1]
        else:
            if xxx_args[0] == 'q':
                raise NotImplementedError("Thank you for browsing the command options. Good bye!")
            else:
                print("nothing")
        print("len(xxx_args): {} | xxx_args {}".format(len(xxx_args), xxx_args))
    else:
        xxx_args = sys.argv[1:]
    sanitized = False
    index = 0

    while sanitized == False:
        try: 
            command = command_box[int(xxx_args[index])]
            index += 1
            sanitized = True
        except:
            fail_safe, valid = magic(xxx_args[index])
            print("fail_safe: " , fail_safe)
            print("type(fail_safe): ", type(fail_safe))
            if valid == False:
                raise Exception("Invalid command. What is it that you would like to do?")
            else:
                command = str(fail_safe)
                print("command is: " + command)
                sanitized = True

    print("AHHHHHHHHHHHHHHHHH: ", command)

    while index < len(xxx_args):
        command += xxx_args[index]+" "
        index += 1

    print()
    print("-----------------")

    print("command: " + command +" \n")

    main(command)

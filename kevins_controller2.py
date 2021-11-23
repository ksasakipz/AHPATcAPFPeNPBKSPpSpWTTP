# Kevin's Configs Begin
# Double-spaced: Off
# Status: In Progress
import sys
import subprocess
import time
import pprint

import check_format

lock = " "
x = 1

command_box = {'q':'q',
    "0": "ls -lfa",
    "1": "python3 check_format.py",
    "2": "bash toolbox/scripts/git_add_commit_push.sh ",
    "3": "dirs -v",
    "4": "du -sh ./*",
    "t": "python3 toolbox/code/habit_tracker/controller_habit_tracker.py"}

block_box = {0: " ",
1: "",
4: "echo 4",
"": "True"}

"""

Usage: In the CLI, use "python3 kevins_controller1.py x y z" where x, y, and z
get chained together to perform a command on the CLI

"""

def main(command):
    clean = sanitize() #5
    if not clean:
        raise Exception("Code not clean")


    build_ship(command) #2

def sanitize():
    """ I think this was going to filter for valid inputs
    """
    retval = check_format.main()
    if retval:
        print("Sanitization successful!")
    else:
        print("Sanitization a failure!")

    return retval

def build_ship(command):
    """ This gathers the pieces and executes our commands
    """
    if command == command_box["t"]:
        bypass = True
    else:
        bypass = False
    command = "clear; " + command
    print(command)

    global lock
    if bypass:
        key = "1"
    else:
        key = input("Press {} to continue.".format(x))
    print()
    print()
    print()

    if key == "1":
        pass
    else:
        raise Exception("Exited without execution")

    """ End theorized most important snippet
    """

    sprocess = subprocess.call([command], shell=True)

    print("-----------------")
    print()
    print("command |{}| executed successfully".format(command))
    return 1

if __name__ == "__main__":
    if len(sys.argv) == 1:
        pprint.PrettyPrinter().pprint( command_box )
        xxx_args = input("Which command would you like to use?\n")

        print("len(xxx_args): {} | xxx_args {}".format(len(xxx_args),
            xxx_args))
        if len(xxx_args) > 1:
            xxx_args = xxx_args.split()
            if len(xxx_args[0]) > 1:
                xxx_args[1] = xxx_args[0][1:] + xxx_args[1]
                xxx_args[0] = xxx_args[0][:1]
        else:
            if xxx_args[0] == 'q':
                raise NotImplementedError("Thank you for browsing the\n" +
                    "command options. Good bye!")
            else:
                print("nothing")
        print("len(xxx_args): {} | xxx_args {}".format(len(xxx_args),
            xxx_args))
    else:
        xxx_args = sys.argv[1:]
    sanitized = False
    index = 0

    while sanitized == False:
        try: 
            command = command_box[xxx_args[index]]
            index += 1
            sanitized = True
        except:
            fail_safe, valid = magic(xxx_args[index])
            print("fail_safe: " , fail_safe)
            print("type(fail_safe): ", type(fail_safe))
            if valid == False:
                raise Exception("Invalid command. What is it that you\n" +
                    "would like to do?")
            else:
                command = str(fail_safe)
                print("command is: " + command)
                sanitized = True

    print("command: {}".format(command))

    while index < len(xxx_args):
        command += xxx_args[index]+" "
        index += 1

    print()
    print("-----------------")

    print("command: " + command +" \n")

    main(command)

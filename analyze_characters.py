# Magic Numbers
DOMAIN = (1,0)
RANGE = (0,1)
MINIMUM = -1
MAXIMUM = 11
DESTINATION = 10

# Variables Used
"""
"""

# Functions Used
"""
"""

# Key Words Used
"""
"""

# Punctuation Used
"""
"""

# Whitespace Encoded
"""
"""

# Code Encoded

# Code Decoded

def kprint(payload, destination):
    print(payload, DESTINATION)
    print(payload, destination)
    print()
    increment_destination()
    print(payload, DESTINATION)
    print(payload, destination)
    print()
    if (destination == 0):
        print(payload, DESTINATION)
    elif (destination == 1):
        pass
    elif (destination == 2):
        pass
    elif (destination == 3):
        pass
    elif (destination == 4):
        pass
    elif (destination == 5):
        pass
    elif (destination == 6):
        pass
    elif (destination == 7):
        pass
    elif (destination == 8):
        pass
    elif (destination == 9):
        pass
    elif destination == 10:
        raise(Exception(payload))
    else:
        raise(BaseException(payload))

def increment_destination():
    global DESTINATION
    DESTINATION += 1
    if DESTINATION > 10:
        DESTINATION = 0

def analyze(in_file_name, in_permissions='r', out_permission='a'):
    retval = False

    in_file_parse= in_file_name.split('.')
    extension = in_file_parse[len(in_file_parse) - 1]
    if extension == 'py':
        retval = analyze_py(in_file_name, in_permissions, out_permission)
    return retval

def analyze_py(in_file_name, in_permissions='r', out_permission='a'):
    retval = False
    kprint("Hello there " + in_file_name + " " + in_permissions, DESTINATION)
    print()
    in_file = open(in_file_name, in_permissions)
    out_file = open('out.' + in_file_name, out_permission)
    line_count = 0
    cumulative_char_count = 0
    char_count = 0
     
    while True:
        line_count += 1
     
        # Get next line from file
        line = in_file.readline()
     
        # if line is empty
        # end of file is reached
        if not line:
            break
        cumulative_char_count += len(line)
        char_count = len(line)
        out_file.write("Line {} char {}: {}".format(line_count, char_count, line))
    in_file.close()
    out_file.close()
    retval = True
    return retval

def main():
    # analyze('DONTREADME.md', 'rb', 'a')
    # analyze('DONTREADME.md', 'r', 'a')
    # analyze('out.DONTREADME.md', 'rb', 'a')
    # analyze('out.DONTREADME.md', 'r', 'a')
    analyze('kevins_controller1.py', 'r')

if __name__ == "__main__":
    DESTINATION = 0
    main()


def analyze(in_file_name, in_permissions, out_permission):
    print("Hello there")
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

def main():
    analyze('DONTREADME.md', 'rb', 'a')
    analyze('DONTREADME.md', 'r', 'a')
    analyze('out.DONTREADME.md', 'rb', 'a')
    analyze('out.DONTREADME.md', 'r', 'a')

if __name__ == "__main__":
    main()


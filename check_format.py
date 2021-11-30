import sys

def check_format(in_filename, peek_line, line_length_check, insert_comments,
    remove_comments, out_filename):
    retval = True
    in_file = open(in_filename, "r")
    out_file = open(out_filename, "w")
    count = 0
    while True:
        line = in_file.readline()
        count += 1

        if peek_line and count < 4:
            print("line: {} | ".format(line))

        if line_length_check and count >= 4:
            if len(line) > 80:
                print("count: {}".format(count))
                print("line: {}".format(line[70:90]))
                print("line: {}".format(line[70:79]))
                retval = False
        if insert_comments:
            if count == 2:
                if line[18] == "n":
                    raise Exception("Redundant attempt to add spacing")
                else:
                    line = line[:18] + "n\n"
            chunk = ""
            if count >= 4:
                chunk += "#\n"
            chunk += line
            if count >= 4:
                chunk += "\n"
            out_file.write(chunk)
        if remove_comments:
            if count == 2:
                if line[18] == "f":
                    raise Exception("Redundant attempt to remove spacing")
                else:
                    line = line[:18] + "ff\n"
            chunk = ""
            if count >= 4:
                line = in_file.readline()
            chunk += line
            out_file.write(chunk)
            if count >= 4:
                line = in_file.readline()
                


        if not line:
            break

    in_file.close()
    out_file.close()
    return retval

def main():
    in_filename = "out_kevins_controller1.py"
    in_filename = "check_format.py"
    in_filename = "kevins_controller1.py"
    peek_line = False
    line_length_check = True
    insert_comments = False
    remove_comments = False
    if len(sys.argv) > 1:
        # "Comments on"
        if sys.argv[1] == ["co"]:
            insert_comments = True

    print("checking the format for: {}".format(in_filename))
    print()
    print("paramters are:")
    print("    peek_line: {}".format(peek_line))
    print("    line_length_check: {}".format(line_length_check))
    print("    insert_comments: {}".format(insert_comments))
    print("    remove_comments: {}".format(remove_comments))

    retval = check_format(in_filename, peek_line, line_length_check,
        insert_comments, remove_comments, "out_"+in_filename)

    print()
    print("format has been checked.")
    
    return retval
    
    

if __name__ == "__main__":
    main()

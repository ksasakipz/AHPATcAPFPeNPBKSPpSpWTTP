import sys

def check_format(in_filename, peek_line, line_length_check, insert_comments,
    remove_comments, out_filename):
    print("checking line lengths...")
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
    print("line length checking finished.")

if __name__ == "__main__":
    in_filename = "out_kevins_controller1.py"
    peek_line = False
    line_length_check = True
    insert_comments = False
    remove_comments = False
    if len(sys.argv) > 1:
        # "Comments on"
        if sys.argv[1] == ["co"]:
            insert_comments = True

    check_format(in_filename, peek_line, line_length_check, insert_comments, remove_comments, "out_"+in_filename)

def main():
    print("Hello there")
    file1 = open('DONTREADEME.md', 'r')
    line_count = 0
    char_count = 0
     
    while True:
        line_count += 1
     
        # Get next line from file
        line = file1.readline()
     
        # if line is empty
        # end of file is reached
        if not line:
            break
        char_count += len(line)
        print("Line {} char {}: {}".format(line_count, len(line), line.strip()))
     
    file1.close()



if __name__ == "__main__":
    main()


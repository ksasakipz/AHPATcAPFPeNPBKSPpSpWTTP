import subprocess
import sys
import os

prefix = "/Users/kevinsasaki1/"

if __name__ == "__main__":
    print("Hello to Kevin's Macbook pro")
    x = os.listdir(prefix)
    print('os.listdir(~/): ' + str(x))

    target = prefix + "twenty-something_link_spotify"
    command = "touch " + target

    os.system(command)

    
    

import subprocess
import sys
import os
import random


if __name__ == "__main__":
    seed = 0   
    while True:
        ten = "1234567890"
        
        retval = "Hello to your Macbook"
        
        ten = ten * 7

        ten = ten + "12345"

        eleven = random.randint(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        
        # print(f'{retval}{ten}')
        print(f'{eleven}')

        out_file = open("garbage", "wb")
        out_file.write(eleven.to_bytes(len(str(eleven)), 'big'))

        seed += 1
        



    
    

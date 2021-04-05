import math
import time
from os import system, name
def magic_square(num,white_to_file = False):
    out = ""
    print("Number is {}".format(num))
    root = int(round(math.sqrt(num),0))
    row = 0
    count = 0
    if(num > (root * root)):
        row +=1
    for i in range(0,root):
        if(i <= root - 1):
            numb = root + row
        else:
            numb = root
        for j in range(0,numb):
            if(count < num):
                if(not white_to_file):
                    print(".".format(count),end = "")
                else:
                    out = out + "."
                count+=1
        if(not white_to_file):
            print("")
        else:
            out = out + "\n"
    with open("outfile.txt", "w") as file:
        file.write(out)

        
nums = 3000000000

magic_square(nums,True)
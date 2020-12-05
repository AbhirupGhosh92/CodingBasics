'''

Given a string find the first recurring character of the string and return it

e.g 

1) Input - "ABABC" Output - A
2) Input - "ABCBA" Output - B
3) Input - "ABC" Output - No Characters
'''

input = "VUVTYCVBHUCRTXCUIVBOV"

hash_table = {}

def find_first_occuring_char(input : str):
    for item in input:
        if(item in hash_table):
            return item
        else:
            hash_table[item] = True
    return "No Characters"

print(find_first_occuring_char(input))
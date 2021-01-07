#Question given an array find the first recurring character O(1) using hash tables

arr = [1,2,3,4,5,6,7,8,9,5,6]

def find_first_recurring_char(arr : list) -> int:
    temp = {}
    for item in arr:
        if(item in temp):
            return item
        else:
            temp[item] = True
    return None

print(find_first_recurring_char(arr))
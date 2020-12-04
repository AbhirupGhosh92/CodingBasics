#Random operations on lists

x = [1,2,3,4,5]
print("append")
x.append(6)
print(x)
print("Pop")
x.pop()
print(x)
print("Inset in start")
x.insert(0,0)
print(x)
print("Remove in start")
x.pop(0)
print(x)

#Implementing an array using dictionary

class my_array:
    def __init__(self):
        self.dit = {}
        self.length = 0
    def get_length(self):
        return self.length
    def append(self,item):
        self.dit[self.length] = item
        self.length+=1
    def get(self,index):
        return self.dit[index]
    def pop(self):
        del self.dit[self.length-1]
        self.length-=1
    def insert(self,index,item):
        for i in range(self.length+1,index):
            self.dit[i] = self.dit[i-1]
        self.dit[index] = item
        self.length+=1

arr = my_array()
# print("Length of arr is " + str(arr.get_length()))
arr.append(0)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)
# print("Length of arr is " + str(arr.get_length()))
# print(arr.get(2))
# arr.pop()
# for i in range(0,arr.get_length()):
#     print(arr.get(i))

arr.insert(1,"p")
for i in range(0,arr.get_length()):
    print(arr.get(i))
    
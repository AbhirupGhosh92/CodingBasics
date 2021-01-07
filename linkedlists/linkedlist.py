#Pointers exaple concepts

# point1 = {'a' : 0}
# point2 = point1

# print("1",point1)
# print("2",point2)

# point1['a'] = 1

# print("Modified")

# print("1",point1)
# print("2",point2)

# del point1

# print("Delete")
# print("2",point2)



#Implemeting linked list. 10 -> 5 -> 16

class LinkedList:

    class __Node__:
        def __init__(self,value):
            self.__value__ = value
            self.__next__ = None
        def value(self):
            return self.__value__
        def set_next(self,node):
            self.__next__ = node
        def get_next(self):
            return self.__next__


    def __init__(self,value):
        self.__head__ = self.__Node__(value)
        self.__size__ = 1
        self.__tail__ = self.__head__
    def len(self):
        return self.__size__
    def head(self):
        return self.__head__
    def tail(self):
        return self.__tail__

    def append(self,value):
        node = self.__Node__(value)
        self.__size__ = self.__size__ + 1
        self.__tail__.set_next(node)
        self.__tail__ = node

linkedList = LinkedList(10)
linkedList.append(5)
linkedList.append(16)
linkedList.append(26)
linkedList.append(243)
linkedList.append(427)

print(linkedList.len())

# traverse a linked list

def traverse(linkedList):
    if(linkedList.head() == linkedList.tail()):
        print(linkedList.head().value())
    else:
        temp = linkedList.head()
        while(True):
            if(temp.get_next() == None):
                print(temp.value())
                break
            else:
                print(temp.value())
                temp = temp.get_next()

print("$$$$$$$Traverse$$$$$$$$")
traverse(linkedList)

print(linkedList)

#### Here is an implemetation using dictionaries for better visualisations


   








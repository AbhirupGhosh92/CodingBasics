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

    def prepend(self,value):
        node = self.__Node__(value)
        self.__size__ = self.__size__ + 1
        node.set_next(self.__head__)
        self.__head__ = node

    def get(self,index):
        if(index >= self.__size__):
            raise Exception("Index out of bound")

        temp : self.__Node__ = None
        prev : self.__Node__ = None
        if(index == 0 ):
            return self.__head__
        elif(index == self.__size__ -  1):
            return self.__tail__
        else:
            for i in range(0,index + 1):
                if(i==0):
                        prev = None
                        temp = self.__head__
                else:
                    prev = temp
                    temp = temp.get_next()
            return temp

    def insert(self,index,value):
        temp : self.__Node__ = None
        prev : self.__Node__ = None
        if(index < self.__size__):
            if(index==0):
                    self.prepend(value)
                    return
            elif(index == self.__size__ - 1):
                    self.append(value)
                    return
            for i in range(0,index+1):
                    if(i==0):
                        prev = None
                        temp = self.__head__
                    else:
                        prev = temp
                        temp = temp.get_next()
                        node = self.__Node__(value)
            node.set_next(temp)
            prev.set_next(node)
            self.__size__ = self.__size__ + 1

        else:
            raise Exception("Index out of bound")

    def delete(self,index):
        if(index < self.__size__):
            if(index == 0):
                self.__head__ = self.__head__.get_next()
                self.__size__ = self.__size__ -  1
            elif(index == self.__size__ - 1):
                self.get(index-1).set_next(None)
                self.__tail__ = self.get(index-1)
                self.__size__ = self.__size__ - 1
            else:
                prev = self.get(index - 1)
                next = prev.get_next().get_next()
                prev.set_next(next)
                self.__size__ = self.__size__ - 1
                
                
        else:
            raise Exception("Index out of bound")

    def reverse(self):
        first = self.__head__
        sec = first.get_next()
        self.__tail__ = self.__head__
        while(sec!=None):
            temp = sec.get_next()
            sec.set_next(first)
            first  = sec
            sec = temp
        self.__head__.set_next(None)
        self.__head__ = first
        return self


# linkedList = LinkedList(0)
# linkedList.append(1)
# linkedList.append(2)
# linkedList.append(3)
# linkedList.append(4)
# linkedList.append(5)
# linkedList.prepend(-1)
# linkedList.prepend(-2)
# linkedList.append(6)

# linkedList.insert(1,-1.5)
# linkedList.insert(0,-2.5)
# linkedList.insert(linkedList.len()-1,7)
# linkedList.insert(5,0.5)
# linkedList.delete(linkedList.len()-1)

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

# print("$$$$$$$Traverse$$$$$$$$")
# traverse(linkedList)
# print("$$$$$$$Traverse$$$$$$$$")
# linkedList.delete(1)
# linkedList.delete(4)

# traverse(linkedList)

# print(linkedList)
# print("$$$$$$$Traverse$$$$$$$$")

# #linkedList.delete(0)
# traverse(linkedList)

#### Here is an implemetation using dictionaries for better visualisations


   








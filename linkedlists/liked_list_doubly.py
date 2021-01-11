class DoublyLinkedList:

    class __Node__:
        def __init__(self,value):
            self.__value__ = value
            self.__next__ = None
            self.__prev__ = None
        def value(self):
            return self.__value__
        def set_next(self,node):
            self.__next__ = node
        def set_prev(self,node):
            self.__prev__ = node
        def get_next(self):
            return self.__next__
        def get_prev(self):
            return self.__prev__


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
        node.set_prev(self.__tail__)
        self.__tail__ = node

    def prepend(self,value):
        node = self.__Node__(value)
        self.__size__ = self.__size__ + 1
        node.set_next(self.__head__)
        self.__head__.set_prev(node)
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
            temp.set_prev(node)
            prev.set_next(node)
            node.set_prev(prev)
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
                next.set_prev(prev)
                self.__size__ = self.__size__ - 1
                
                
        else:
            raise Exception("Index out of bound")


dlist = DoublyLinkedList(0)
dlist.append(1)
dlist.append(2)

dlist.insert(1,10)
dlist.insert(1,11)
dlist.delete(1)

print(dlist.get(1).value())

def traverse_reverse(linkedList):
    if(linkedList.head() == linkedList.tail()):
        print(linkedList.head().value())
    else:
        temp = linkedList.tail()
        while(True):
            if(temp.get_prev() == None):
                print(temp.value())
                break
            else:
                print(temp.value())
                temp = temp.get_prev()

traverse_reverse(dlist) 
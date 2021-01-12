
#Implemment queue using list

import sys
sys.path.insert(1,'/'.join(sys.path[0].split('/')[0:-1]))

from linkedlists.linkedlist_single import LinkedList

class Queue:
    def __init__(self):
        self.__first__ = None
        self.__last__ = None
        self.__size__ = 0
        self.__dats__ = []

    def peek(self):
        return self.__first__

    def enque(self,value):
        if(self.__size__ == 0):
            self.__first__ = value
            self.__last__ = value
            self.__dats__.append(value)
        else:
            self.__first__ = value
            self.__last__ = self.__dats__[0]

    def deque(self):
        temp = self.__dats__[0]
        self.__dats__ = self.__dats__[1:]
        return temp

    def size(self):
        return len(self.__dats__)

q = Queue()

q.enque(0)
q.enque(1)
q.enque(2)

print(q.deque())
print(q.deque())
print(q.deque())


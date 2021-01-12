# Implemennting stacks using list

import sys
sys.path.insert(1,'/'.join(sys.path[0].split('/')[0:-1]))

class Stack:
    __stack_arr__ = []
    def __init__(self,value):
        self.__stack_arr__.append(value)

    def push(self,value):
        self.__stack_arr__.append(value)

    def pop(self):
        if(len(self.__stack_arr__) > 0):
            temp = self.__stack_arr__[-1]
            self.__stack_arr__ = self.__stack_arr__[0:-1]
        else:
            raise Exception("Index out of bound")
        return temp

    def peek(self):
        if(len(self.__stack_arr__) > 0):
            return self.__stack_arr__[-1]
        else:
            return self.__stack_arr__
    
    def size(self):
        return len(self.__stack_arr__)

    def print(self):
        print(self.__stack_arr__)

# stk = Stack(0)

# stk.push(1)
# stk.push(2)
# stk.push(3)
# stk.pop()
# stk.pop()
# stk.pop()
# stk.pop()


# print(stk.peek())

# Implemennting stacks using doubly linked list

from linkedlists.liked_list_doubly import DoublyLinkedList

ll = DoublyLinkedList(0)

class Stack2:
    
    def __init__(self,value):
        self.__ll__ = DoublyLinkedList(value)
    
    def push(self,value):
        self.__ll__.append(value)

    def pop(self):
        if(self.__ll__.__size__ > 0):
            temp = self.__ll__.tail()
            self.__ll__.__tail__ = self.__ll__.__tail__.get_prev()
        else:
            raise Exception("Index out of bound")
        return temp

    def peek(self):
            return self.__ll__.tail()
    
    def size(self):
        return self.__ll__.__size__

    def print(self):
        print(self.__ll__)


stk = Stack2(0)

stk.push(1)
print(stk.peek().value())
stk.push(2)
print(stk.peek().value())
stk.push(3)
print(stk.peek().value())
stk.pop()
stk.pop()
stk.pop()
stk.pop()
print(stk.peek())


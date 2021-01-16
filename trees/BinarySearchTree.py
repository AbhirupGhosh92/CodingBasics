#Implementinng a binary seqarch tree. For sake of visualisation we use a. dictionary to visualize

class BinarySearchTree:
    
    class __Node__:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.__root__ : self.__Node__ = None

    def __compare__(self,node,value):
        pass
    
    def insert(self,value):
        if(self.__root__ == None):
            self.__root__ = self.__Node__(value)
        else:
           current = self.__root__
           while(True):
                if(value < current.value):
                    if(current.left == None):
                       current.left = self.__Node__(value)
                       break
                    else:
                        current = current.left
                else:
                    if(current.right == None):
                       current.right = self.__Node__(value)
                       break
                    else:
                        current = current.right

    def lookup(self,value):
        if(self.__root__ == None):
            return False
        else:
            current = self.__root__
            while(current != None):
                if(value < current.value):
                    current = current.left
                elif(value > current.value):
                    current = current.right
                elif(value == current.value):
                    return current
            return False




tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(70)

print(tree.lookup(70))
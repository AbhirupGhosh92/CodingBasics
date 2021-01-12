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
            if(value < self.__root__.value):
                
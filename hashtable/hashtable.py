#Implemetaton of hash table using arrays

class HashTable:
    
    __dats__ = []

    def __init__(self):
        pass
    
    def set(self,key : str,value ):
        found = False
        for i in range(0,len(self.__dats__)):
            if(self.__dats__[i][0] == key):
                self.__dats__[i] = [key,value]
                found = True
                break
        if(not found):
            self.__dats__.append([key,value])

    def get(self,key : str):
        for item in self.__dats__:
            if(item[0] == key):
                return item[1]
        return None

    def len(self) -> int:
        return len(self.__dats__)

    def keys(self) -> str:
        temp = []
        for item in self.__dats__:
            temp.append(item[0])
        return temp


tab = HashTable()

tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)
tab.set("hello",10)



print(tab.get("hello"))
print(tab.len())
print(tab.keys())

tab.set("hello",11)
tab.set("helloa",10)
tab.set("helloas",10)
tab.set("helloasas",10)

print(tab.get("hello"))
print(tab.len())
print(tab.keys())

tab_key = HashTable()
tab.set(tab_key,60)


print("Got ----",tab.get(tab_key))
print(tab.len())
print(tab.keys())

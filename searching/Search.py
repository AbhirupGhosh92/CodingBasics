import sys
sys.path.insert(1,'/'.join(sys.path[0].split('/')[0:-1]))

from trees.BinarySearchTree import BinarySearchTree
from queue.Queue import Queue

tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

dfs_out = [9,4,20,1,6,15,170]




def breadth_first_search(tree : BinarySearchTree.__Node__):
    temp = []
    queue = Queue()
    temp.append(tree.value)
    queue.enque(tree)
    while(queue.size() > 0):
        current :  BinarySearchTree.__Node__= queue.deque() 
        if(current.left != None):
            queue.enque(current.left)
            temp.append(current.left.value)
        if(current.right != None):
            queue.enque(current.right)
            temp.append(current.right.value)
    print(temp)


print(dfs_out)
breadth_first_search(tree.__root__)

queue = Queue()
queue.enque(tree.__root__)
temp = [tree.__root__.value]

def breadth_first_search_recursion(temp,queue):
    
    if(queue.size()==0):
        return temp
    tree = queue.deque()
    if(tree.left != None):
        temp.append(tree.left.value)
        queue.enque(tree.left)

    if(tree.right != None):
        temp.append(tree.right.value)
        queue.enque(tree.right)
    return breadth_first_search_recursion(temp,queue)

print(breadth_first_search_recursion(temp,queue))
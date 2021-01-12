from linkedlist_single import LinkedList,traverse
arr = [4,2,5,7,8,3]

linkedList = LinkedList(1)

for item in arr:
    linkedList.append(item)

traverse(linkedList)


rev_list = (linkedList.reverse())

print("*************************")

traverse(rev_list)




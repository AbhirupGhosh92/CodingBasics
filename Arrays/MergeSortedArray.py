'''
Given two arrays A => [1,2,3,5,6] and B => [1,5,6,7,8,9]
Write a function which merges both these arrays in such a way that it is still sorted
'''

A = [1,2,3,5,6,9,34]
B = [1,2,5,6,7,8,9,12,15,26]

def merge(A,B):
    return list(sorted(A+B))

#This is a naive solution The time complexity will be O(log(N)), lets try a O(N)
print(merge(A,B))

def merge_2(A,B):
    merged_arr = []
    iter_lenA,iter_lenB = len(A),len(B)
    i,j = 0,0
    while(i <= iter_lenA-1 or j <= iter_lenB -1):
        if(i <= iter_lenA):
            if(A[i] <= B[j]):
                merged_arr.append(A[i])
            else:
                merged_arr.append(B[j])
            i+=1
        if(j <= iter_lenB):
             if(B[i] <= A[j]):
                merged_arr.append(B[i])
             else:
                merged_arr.append(A[j])
    print(merged_arr)
        
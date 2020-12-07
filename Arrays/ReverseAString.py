# Write a function to reverse a string

input = "Abhirup Ghosh"

def reverse(inp : str):
    out = ""
    for i in range(len(inp)-1,-1,-1):
        out = out + inp[i]
    return out

#print(reverse(input))

print(input[0:-len(input)])
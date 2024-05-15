
# find unique element in the array  by XOR operator 

'''
XOR Operator 

a   b   output
0   0   0
0   1   1
1   0   1
1   1   0
'''

def findUnique(arr):
    ans = 0
    for i in range(len(arr)):
        ans = ans^arr[i]
    return ans 

# by using dictionary 
# def findUnique(arr):
#     map = {}
#     for i in map:
#         if arr[i] in map:
#             map[arr[i]]+=1
#         else:
#             map[arr[i]]=1
#     print(map)
#     for i in map:
#         if map[i]%2!=0:
#             return i
#     return -1



arr = [1,2,3,4,1,2,3]
output = findUnique(arr)

print("Unique elementr is: ",output)

# sort 0 and 1  of an array       brute force solution  apparoach

'''
1. count zero and one 
2. palced zero and one in array 
'''
arr = [1,1,1,1,0,1,0,0,0,0,1,0,1]
zeroCount = 0
oneCount = 0
for i in range(len(arr)):
    if(arr[i]==0):
        zeroCount+=1
    if(arr[i]==1):
        oneCount+=1
# print(zeroCount)
# print(oneCount)

k= 0
for i in range(0,zeroCount):
    arr[i]= 0
    k+=1

for j in range(k,len(arr)):
    arr[j] = 1




print(*arr)
    

# print al possible pair in tha array     brute force solution 

def printAllPair(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i],arr[j])

arr = [1,2,3,4,5]
printAllPair(arr)

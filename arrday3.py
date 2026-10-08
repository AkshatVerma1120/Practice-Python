# import array as a

# val = a.array("i", [1, 2, 3, 4, 5, 6, 7, 8])

# for i in range(0,len(val)):
#     print(val[i] , end=" ")

# print("\n")

# for x in val:
#     print(x , end=" , ")

# print("\n")

# print(val.typecode)


# val.insert(4,1111222333)

# for i in range(0,len(val)):
#     print(val[i],end=' ')

from array import *

arr = array('i', [])

n = int(input("Enter a number: "))


for i in range(0,n):
    arr.append(int(input("Enter next number : ")))

for x in arr:
    print(x, end = " ")

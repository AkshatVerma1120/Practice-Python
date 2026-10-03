import array as a

val = a.array("i", [1, 2, 3, 3,6,7,5,8])

for i in range(0,8):
    print(val[i] , end=" ")
print("\n")
for x in val:
    print(x , end=" , ")

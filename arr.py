import array as a

val = a.array("u", ["a", "t", "c"])

for i in range(0,len(val)):
    print(val[i] , end=" ")
print("\n")
for x in val:
    print(x , end=" , ")

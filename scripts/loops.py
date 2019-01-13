#comment CTRL/

# for i in range(10):
#     print(i)

# while (True):
#     str = input("Please say something, quit to exit from loop:")
#     if str == "quit":
#         break
#     print(str)

while ( True ):
    str = input("Please say something, quit to exit from loop:")
    if str == "quit":
        break
    print(str)

print("reached end of program")

l = ["one", "two", "three"]
m = ["four", "file", "siz"]

#loop through each item in list
for i in l:
	print(i)

#print list
print(l)
#extend list l with list m
l.extend(m)
print(l)

# chr(Asciicode)

print(chr(98))

# ord(character)

print(ord('b'))


for i in range(65,91):
    print(chr(i),end=" ")
    
for i in range(65,91):
    print(chr(ord(chr(i+32))),end=" ")    


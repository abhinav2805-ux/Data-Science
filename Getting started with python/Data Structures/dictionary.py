dict = {1:'ankur',2:'abhinav',3:'rahul',4:'sajna'}
print(dict[2]) # on the bases of key 
print(dict.get(1))
print('-'*48)

# adding , changeing , delete 
dict[5]='daksh'
print(dict)
del dict[5]
print(dict)
dict[4]='kl rahul'
print(dict)
dict.clear()
print(dict)
print('-'*48)


dict = {1:'ankur',2:'abhinav',3:'rahul',4:'sajna'}

# to know the keys and valuse 
print(dict.keys())
print(dict.values())

# iteration 
for i in dict.keys():
    print(i , dict[i])
    
print(dict.items())
for i in dict.items():
    print(i)
    
print('-'*48)    
    # to check the existence of key
print(1 in dict)
print(10 in dict)    
print('-'*48)

# merging a dictionary 

dict2 = {5:'daksh',6:'rahul'}
dict.update(dict2)
print(dict)
print('-'*48)

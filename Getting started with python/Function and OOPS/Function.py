def greet():
    print("Hello ji")
    
greet()
greet()
greet()    
    

def sum(a,b):
    return a + b
a=9
b=6
print(a,"+",b,"=",sum(a,b))

def greetbyname(name):
    print("Hello", name,"sir")
    
greetbyname("ABHINAV") 


def greetname(name="abc"):
    print("Hello", name,"sir")
    
greetname()   


def arthimatic(a,b):
    return a+b, a-b, a*b, a/b, a//b, a**b

print(arthimatic(7,3))       


# Calling Different Functions
lst = [1, 2, 3, 4, 5]

def sq(lst):
    return [i**2 for i in lst]

def cu(lst):
    return [i**3 for i in lst]

def final(lst):
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]

print(sq(lst))
print(cu(lst))
print(final(lst))
    
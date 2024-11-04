import math

x=10.8
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

y =8

print(math.sqrt(y))
print(math.pow(y,2))
print(math.exp(y))
print(math.log10(y))

print(math.pi)
print(math.e)

print("factorial of 8" , math.factorial(8) )




print('-'*50)


import random

print(random.random())
print(random.randint(0,100))
print(random.choice([1,2,3,4,5,6,7,8]))
print(random.sample([1,2,3,4,5,6,7,8],3))
print(random.uniform(4.0,7.0))

print('-'*50)

import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))

print('-'*50)



from collections import Counter,defaultdict

my_list = [1,2,3,4,5,5,5,6,7,8,9,9,9]
print(Counter(my_list))


my_dict = {'a':1, 'b':2, 'c':3}
print(defaultdict(lambda: 0, my_dict))


print('-'*50)


import string 

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

print('-'*50)

print(string.punctuation)





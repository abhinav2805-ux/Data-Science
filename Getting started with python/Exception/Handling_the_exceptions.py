try:
    x = 10
    print(x/0)
except ZeroDivisionError:
    print("An error occurred while trying to divide by zero.")
except :
    print("An unexpected error occurred.")    
    
    
    
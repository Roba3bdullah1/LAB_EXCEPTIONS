

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b) # b is not defined 
         

try:       
    additoin(10,20)
    print("The operation was successful.")

except NameError as e:
    print("Exception type:" ,e.__class__)
    print("variable used is not defined.")

except ValueError as e:
    print("Value is wrong")
    print(e)

except Exception as e:
    print(e)


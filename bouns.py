# Function convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit: ",round(fahrenheit,2),"F")
    
# Function convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius: ",round(celsius,2),"C")

# loop to repeat ask user
while True:
    try:  
        temperature = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'):")

        # Remove spaces and split into num,unit
        num,unit=temperature.strip().split()
        unit_upper=unit.upper()
        tump_num=float(num)

        # cheak unit
        if unit_upper == "C":
            celsius_to_fahrenheit(tump_num)

        elif unit_upper == "F":
            fahrenheit_to_celsius(tump_num)
    
        else:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

       
        break
       
        
     # Handle exeption
    except TypeError as e:
        print("Invalid unit.")

    except ValueError as e:
        print("Invalid temperature valu. try again")

    except Exception as e:
        print(e)
   
    break



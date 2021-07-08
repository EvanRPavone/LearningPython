def sum(num1, num2):
    try: # what the function is suppose to do goes here
        print(num1+num2)
    except:
        print("There was an error!")
    
number1 = input("Enter a number: ")

sum(number1, 12)

def sumAgain(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1+num2)
    else:
        print("data type was not a number for the parameters")
        
number1Again = input("Enter a number: ")
sumAgain(number1Again, 12)
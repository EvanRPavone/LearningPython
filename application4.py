# SECTION 4

# 1. Control Flow: If & Else Statements

elephant = 800
hippo = 900

if elephant < hippo:
    print("Elephant weighs less than the hippo")
else:
    print("hippo weighs less than the elephant") # <-----
    
if True:
    print("This will always be printed")
else:
    print("this will never be printed")
    
if (elephant < hippo and (3 > 2)):
    print("the if statement evaluated to true")
    if 5 < 7:
        print("5 < 7")
else:
    print("if statement evaluated to false")
    
# MESSING AROUND

my_list = ["Evan", "Robert", "Pavone"]

if "Evan" in my_list or "Robert" in my_list or "Pavone" in my_list or "Bobby" in my_list:
    print("Evan, Robert and Pavone are on the List")
    if "Bobby" in my_list:
        print("Bobby is also on the list")
    else:
        print("Bobby is not on the list")
else:
    print("These people are not on the list")
    
# 2. Control Flow: Elif statements

# if something takes place do this, if something else takes place do that, if something else takes place do that etc..

animal = "ape"

if animal == "cow":
    print("eats grass")
elif animal == "bird":
    print("eats seeds")
elif animal == "monkey" or animal == "ape":
    print("eats bananas")
else:
    print("We don't know what the animal eats")


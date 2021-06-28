# SECTION 5

# 1. Revisiting the Differences between Methods and Functions

mylist = [1,2,3,4]

mylist.pop() # <- Method

print(mylist)

# -> [1,2,3]

mylist = [1,2,3]

max_number = max([1,2,3,4,100,900]) # <- Function

# mylist.max() -> this isn't a thing because max is a function
# error -> unresolved attribute reference 'max' for class 'list

print(max_number) # -> 900

def myname(name):
	print("Hello " + name)

myname("Evan")


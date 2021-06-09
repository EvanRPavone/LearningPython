# SECTION 2

# 1. Lists in Python

# You can change the contents of a list. Mutable object
# A List can contain another list and any item

my_list = [1,2,3,4,5]
my_list.pop() # takes out the last value of the list by default, Specify the index of an item in the list to take out in the ()
my_list[0] = 'S' # The first item is now an S
my_list[2] = ['A', 'list', 'within', 'a', 'list']
my_list.append("this is a sentence appended")
sentence = my_list.pop() # will take out the new appended sentence and sets it to a variable, can be printed and will show sentence
print(my_list)
print(type(my_list)) # -> <class 'list'>
print(sentence)

my_list = [4,5,3,1,2]
my_list.sort() # modifies the object, puts the list in the correct order
print(my_list)
my_list.reverse() # reverses
print(my_list)

string_list = ['4', '5', '3', '1', '2'] # will be sorted and reversed still.
string_list.sort()
print(string_list)
string_list.reverse()
print(string_list)
print(string_list[2:])
list_length = len(string_list) # can be done on normal string too. Counts the number of elements of a string, list, etc.
print(list_length)

another_list = [1,2,3,4,5]
new_list = my_list + another_list
print(new_list) # will print one big list
my_list.append(another_list)
print(my_list)

# List assignment
assign_list_1 = ['b', 'd', 'a', 'z', 'x']
assign_list_2 = [1,2,3,4,5]
assign_list_1.sort()
assign_list_1.reverse()
assign_list_2.reverse()
final_list = assign_list_1[2:] + assign_list_2[2:]
print(final_list) # ['d', 'b', 'a', 3, 2, 1]

# 2. Accessing Elements in Nested Lists

my_list = ['a', 'b', 'c', 1,2,3, ['apple', 'orange', 'banana'], 'd']
extracted_list = my_list[6] #grabs the list inside the list
print(extracted_list)
extracted_fruit = my_list[6][2] # grabs the list inside the list and then grabs the banana
print(extracted_fruit)
my_list = ['a', 'b', 'c', 1,2,3, ['apple', 'orange',['John', 'Robert'], 'banana'], 'd']
extracted_name = my_list[6][2][1]
print(extracted_name)
my_list[2] = "computer"
print(my_list)
# change roberts name to joe
my_list[6][2][1] = "Joe"
print(my_list)
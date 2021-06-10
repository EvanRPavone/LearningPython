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

# 3. Finding index positions in Lists and Counting Duplicates

my_list = ['a', 'b', 'c', 'd']
idx_pos = my_list.index('c') # return the index position of c
print(idx_pos)
my_list = ['a', 'b', 'c', 'd', 'c', 'c']
c_count = my_list.count('c') # How many times c is in the list
print(c_count)

# 4. Tuples

# Very similar to list but they cannot be modified

my_tuple = (1,2,3, "Some Data", "Some Data", "Some Data", [1,2,3]) # Tuple with a list inside
# my_tuple[3] = "other data"  TypeError: 'tuple' object does not support item assignment
count = my_tuple.count("Some Data")
extracted = my_tuple[6] # extracts the list [1,2,3]
my_tuple[6][2] = "New Value" # You can still modify lists inside tuples
some_data = my_tuple[3:6] # will return all Some Data and returns it as a tuple
print(my_tuple)
print(count)
print(some_data)
print(type(some_data)) # <class 'tuple'>
print(type(extracted)) # <class 'list'>

# 5. Dictionaries

# Key (Word) and Value (Definition)
# Not position oriented - Dictionaries are key oriented
# Format: dict = {'key': 'value'}
# Cannot Sort

dict = {'k1': 'some data', 'k2': 'Evan Pavone'}
value = dict['k1']
value_2 = dict['k2']
print(value)
print(value_2)
dict['k2'] = "New Value"
print(dict) # {'k1': 'some data', 'k2': 'New Value'}

people_weight_dict = {'john': 134, 
                      'Evan': 120, 
                      'Robert': 165, 
                      'items': ['orange', {'k1': 'some value'}],
                      'tuple': (1,2,3,4,5)
                      }
print(people_weight_dict)
people_weight_dict['john'] = 170
weight_of_evan = people_weight_dict.pop('Evan') # will remove Evan - Must give the key you want to pop out.
items_dict = people_weight_dict['items'][1]['k1'] # will return some value
my_tuple = people_weight_dict['tuple']
print(my_tuple)
tuple_removed = people_weight_dict.pop('tuple')
print(people_weight_dict)
print(tuple_removed)
print(items_dict)
print(weight_of_evan)
print(people_weight_dict)
print(people_weight_dict['items'])
print(people_weight_dict['items'][1])
people_weight_dict.clear() # can do this to lists too. Will clear the dictionary
print(people_weight_dict)
people_weight_dict['99'] = "some data" # adding new data to the dictionary
print(people_weight_dict)

# 6. Comparison Operators

# == , < >, >= <=, !=

10 == 10 # not assigning. is 10 equal to 10. Can use strings as well. Case Sensitive. Same as other languages I know. Boolean expressions
print(10 == 10)
print ((5 < 10) or (5 != 5) and ('8' == '8')) # True
print ((5 < 4) or (5 != 5) and ('8' == '8')) # False

condition = not (5 == 5)
print(type(condition)) # <class 'bool'>
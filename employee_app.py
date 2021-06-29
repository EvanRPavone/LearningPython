from employees.employee import Employee

tom = Employee("Tom Lanister", 47)
print(tom) # -> <__main__.Employee object at 0x10c875df0>
# with __str__ now in play it will print "Tom Lanister age is 47"
print(len(tom)) # -> Error: object of type 'Employee' has no len()
# -> with __len__ in play it will print 47
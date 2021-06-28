from machines.vehicle_stuff import Vehicle, Truck, Motorcycle

truck1 = Truck("Big Rig", "Mercedes")
car1 = Vehicle("SUV", "Subaru")
moto1 = Motorcycle("Sport", "Yamaha")

print(truck1.get_vehicle_count())

truck1.drive()

for v in [truck1, car1, moto1]:
    v.drive() # polymorphism
    
def perform_tasks(vehicle_object):
    vehicle_object.drive()
    
perform_tasks(car1)
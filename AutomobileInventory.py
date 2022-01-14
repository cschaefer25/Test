class automobile:

    def __init__(self):
        self.make = ''
        self.model = ''
        self.color = ''
        self.year = ''
        self.mileage = ''
    def addvehicle(self):
        try:
            self.make = input('Enter make: ')
            self.model = input('Enter model: ')
            self.color = input('Enter color: ')
            self.year = int(input('Enter year: '))
            self.mileage = int(input('Enter mileage: '))
            return True
        except ValueError:
            print('Please use numbers for mileage and year')
            return False
    def __str__(self):
        return '\t' .join(str(x) for x in [self.make, self.model, self.color, self.model, self.mileage])


class inventory:
    def __init__(self):
        self.vehicles = []
    def addvehicle(self):
        vehicle = automobile()
        if vehicle.addvehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('Vehicled added')
    def viewinventory(self):
        print('\t' .join(['', 'Make', 'Model', 'Color', 'Year', 'Mileage']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

inventory = inventory()
while True:

    print('''
    1.Add a vehicle
    2.Delete a Vehicle
    3.View Inventory
    4.Update Inventory
    5.Export Inventory
    6.Quit
    ''')
    userinput = input('Please choose one of the options: ')
    if userinput =="1":
        inventory.addvehicle()
    elif userinput =="2":
        if len(inventory.vehicles) < 1:
            print('Sorry, there are no vehicles in inventory')
            continue
        inventory.viewinventory()
        item = int(input('Enter number associated with the vehicle to remove: '))
        if item -1 > len(inventory.vehicles):
            print('Invalid number')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print()
            print('Vehicle has been removed')
    elif userinput =="3":
        if len(inventory.vehicles) < 1:
            print('Sorry, there are no vehicles in inventory')
            continue
        inventory.viewinventory()
    elif userinput =="4":
        if len(inventory.vehicles) < 1:
            print('Sorry,there are no vehicles in inventory')
            continue
        inventory.viewinventory()
        item = int(input('Enter the number associated with the vehicle to update: '))
        if item - 1 > len(inventory.vehicles):
            print('Invalid number')
        else:
            automobile = automobile()
            if automobile.addvehicle() == True:
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print()
                print('Vehicle has been updated')
    elif userinput =="5":
        if len(inventory.vehicles) < 1:
            print('Sorry, there are no vehicles in inventory')
            continue
        f = open('vehicle_inventory.txt', 'w')
        f.write('\t' .join(['Make', 'Model', 'Color', 'Year', 'Mileage']))
        f.write('\n')
        for vehicle in inventory.vehicles:
            f.write('%s\n' %vehicle)
        f.close()
        print('Vehicle inventory has been exported to text file')
    elif userinput =="6":
        print('Closing Program')
        break
    else:
        print('Invalid input, please try again')

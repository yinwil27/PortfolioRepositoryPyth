# Ayinde Williams Student ID #001418743
import datetime

import HashMap
import csv
import delivery_truck

# These imports
# Setup Hashmap
PackageID = []
Address = []
h = HashMap.HashMap()
with open('WGUPS Package File.csv', 'r', encoding='utf8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        PackageID = []
        Address = []
        package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
        h.add(row[0], package)
        PackageID.append(row[0])
        Address.append(package)

# Holistic Loading, Packages

Ride1 = ['1, 34, 30, 31, 37, 40, 29, 17, 4, 33, 7']
Ride2 = ['13, 16, 14, 15, 20, 19, 5, 9, 36, 3, 38, 18, 2, 35, 39']
Ride3 = ['6, 32, 8, 10, 11, 21, 22, 23, 24, 27, 28, 12, 25, 26']

Ride1Optimized = [1, 34, 30, 31, 37, 40, 29, 17, 4, 33, 7]

Ride2Optimized = [13, 16, 14, 15, 20, 19, 5, 9, 36, 3, 38, 18, 2, 35, 39]

Ride3Optimized = [6, 32, 8, 10, 11, 21, 22, 23, 24, 27, 28, 12, 25, 26]

FullLoad = []
f = 1
while len(FullLoad) < 40:  # O(n) , create a loop of 40 for timecheck
    FullLoad.append(f)
    f += 1

# When do the Trucks leave the hub, in hours

FirstLeave = 8  # 8:00
SecondLeave = 8  # 8:00
ThirdLeave = 9.1  # 9:10

# Activate the nearest neighbor algorithm to get started


AmazonTruck = delivery_truck.Truck()
UPSTruck = delivery_truck.Truck()

AmazonTruck.neighbor(FirstLeave, Ride1Optimized, h)  # First Truck
UPSTruck.neighbor(SecondLeave, Ride2Optimized, h)  # Second Truck
AmazonTruck.neighbor(ThirdLeave, Ride3Optimized, h)  # Third Truck
delivery_truck.TimeCheck(h, FullLoad, datetime.timedelta(hours=9.417))

delivery_truck.TimeCheck(h, FullLoad, datetime.timedelta(hours=10.417))

delivery_truck.TimeCheck(h, FullLoad, datetime.timedelta(hours=13.2))  # You can change the 'hours' input to the time
# of your choice. For example, 10:30 = 10.5
print('The total mileage is: ' + str(AmazonTruck.totalMiles + UPSTruck.totalMiles))

# Lookup Function at O(1)
txt = input("Hi, welcome to the WGUPS, How may I help you? Press '0' to get all packages displayed, "
            "or type the key to get a specific package ")

if txt == '0':
    h.print()

    search = input("type the number of the package to get that one specifically ")
    print(h.get(search))
if txt != '0':
    print(h.get(txt))

from time import time, ctime
import time
import datetime
import csv
from datetime import datetime, timedelta
from _datetime import datetime
import datetime


GPSMatrix = []
# Read in csv file that is the mapping of distances between locations
with open('WGUPS Distance Numbers.csv') as csvfile:
    readCSV2 = csv.reader(csvfile, delimiter=',')
    readCSV2 = list(readCSV2)
    for row in readCSV2:
        GPS = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
               row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
               row[23], row[24], row[25], row[26]]
        GPSMatrix.append(row)
print("GPS Numbers")
print(GPSMatrix)

# Read in csv file that is the names of all possible delivery locations
Rolodex = []
RolodexAddressOnly = []
with open('WGUPS Distance Names.csv') as csv_name_file:
    readCSV3 = csv.reader(csv_name_file, delimiter=',')
    readCSV3 = list(readCSV3)
    for row in readCSV3:
        Book = [row[0], row[1], row[2]]

        Rolodex.append(row)
        RolodexAddressOnly.append(row[2])
print("GPS NAMES")
print(Rolodex)
print(RolodexAddressOnly)

# Print GPS Matrix
for row in GPSMatrix:
    print(row)
for i in range(27):
    for j in range(27):
        print(GPSMatrix[i][j])


# Get distance function for finding distance between two addresses.
def getDistance(fromAddress, toAddress):  # Runs at O(1) , Space at O(1)
    try:
        return float(GPSMatrix[RolodexAddressOnly.index(toAddress)][RolodexAddressOnly.index(fromAddress)])
    except ValueError:
        return float(0.0)


# Test the getDistance function
print("Get Distance Results")
print(getDistance('4001 South 700 East', '1060 Dalton Ave S'))


class Truck:
    CurrentTime = 0 # Current time, in hours
    LeaveTime = 0  # Time you left, in hours,
    TravelTime = 0  # Time it takes for you to travel with this package
    newdistance = 0
    listOfDeliveredItems = []
    # CurrentMilesTraveled = []
    newMiles = 0  # Miles traveled so far, miles traveled on CURRENT truck
    odomoter = 0

    def __init__(self):
        self.package_list = []
        self.size = 6
        self.Location = '4001 South 700 East'
        self.LeaveTime = 0  # in hours,
        self.CurrentTime = datetime.time(hour=0, minute=0, second=0) # in hours
        self.totalMiles = 0

    # Package ID

    # The 'wait' function is for package 9. The address is lait, but that doesn't mean it can't
    # leave immediately and wait for the real address while on the ride
    def wait(self):
        self.CurrentTime = datetime.timedelta(hours=10.333) # Running at O(1)
    def neighbor(self, timetostart, Ride, h): # Running at O(N^3), space complexity of O(1)

        self.CurrentTime = datetime.timedelta(hours=timetostart)

        if 25 in Ride:
            while 25 in Ride:   # Runs O(n), space O(1)

                PossiblePackage = '25'
                self.deliver(PossiblePackage,h, 4.8)
                PossiblePackage = '26'
                self.deliver(PossiblePackage,h, 0.0)
                Ride.remove(25)
                Ride.remove(26)
            while len(Ride) > 0:   # runs O(n^2), Space at O(1)
                        minDistance = 1000  # highest number not in list
                        minPID = 200  # minPID = Minimum package number

                        for n in Ride:
                            # Is Hub
                            nuPIN = str(n)
                            h.get(nuPIN)

                            PossiblePackage = h.get(nuPIN)

                            status = "In Transit"  # Change the status to 2 'in transit'

                            PossiblePackage[8] = status
                            g = getDistance(self.Location, PossiblePackage[1])

                            if g < minDistance:
                                minDistance = g

                                minPID = str(n)

                        # b = RolodexAddressOnly[int(minPID)]
                        dist = g
                        self.deliver(minPID, h, dist)  # Delliver the package, process inside line 108's function

                        Ride.remove(int(minPID))
        # Return back to the hub with getDistance and Location
        # loop through until that list is empty.
            self.totalMiles = self.totalMiles + getDistance(self.Location, '4001 South 700 East')
        elif 15 in Ride:
            while 15 in Ride:   # runs at O(n^3), space at O(1)
                PossiblePackage = '14'
                self.deliver(PossiblePackage, h, getDistance(RolodexAddressOnly[0], RolodexAddressOnly[14]))

                PossiblePackage = '15'
                self.deliver(PossiblePackage, h, 2.0)
                PossiblePackage = '16'
                self.deliver(PossiblePackage, h, 0.0)
                Ride.remove(14)
                Ride.remove(16)
                Ride.remove(15)
                while len(Ride) > 0:
                    minDistance = 1000  # highest number not in list
                    minPID = 200  # minPID = Minimum package number

                    for n in Ride:
                        # Is Hub

                        PossiblePackage = h.get(str(n))

                        status = "In Transit"  # Change the status to 2 'in transit'

                        PossiblePackage[8] = status
                        g = getDistance(self.Location, PossiblePackage[1])

                        if g < minDistance:
                            minDistance = g

                            minPID = str(n)

                    # b = RolodexAddressOnly[int(minPID)]
                    dist = g
                    self.deliver(minPID, h, dist)  # Delliver the package, process inside line 108's function

                    Ride.remove(int(minPID))
                # Return back to the hub with getDistance and Location
                # loop through until that list is empty.
                self.totalMiles = self.totalMiles + getDistance(self.Location, '4001 South 700 East')

        elif 9 in Ride:
            self.wait()
            while 9 in Ride:     # running at O(n^3), space O(1)
                PossiblePackage = '9'
                self.deliver(PossiblePackage, h, (2* (getDistance(RolodexAddressOnly[0], RolodexAddressOnly[9]))))
                Ride.remove(9)
                while len(Ride) > 0:
                    minDistance = 1000  # highest number not in list
                    minPID = 200  # minPID = Minimum package number

                    for n in Ride:
                        # Is Hub

                        PossiblePackage = h.get(str(n))

                        status = "In Transit"  # Change the status to 2 'in transit'

                        PossiblePackage[8] = status
                        g = getDistance(self.Location, PossiblePackage[1])

                        if g < minDistance:
                            minDistance = g

                            minPID = str(n)

                    # b = RolodexAddressOnly[int(minPID)]
                    dist = g
                    self.deliver(minPID, h, dist)  # Delliver the package, process inside line 108's function

                    Ride.remove(int(minPID))
                # Return back to the hub with getDistance and Location
                # loop through until that list is empty.
                self.totalMiles = self.totalMiles + getDistance(self.Location, '4001 South 700 East')
        else:
            while len(Ride) > 0:  # Running at O(n^2), space O(1)
                minDistance = 1000  # highest number not in list
                minPID = 200  # minPID = Minimum package number

                for n in Ride:
                    # Is Hub

                    PossiblePackage = h.get(str(n))

                    status = "In Transit"  # Change the status to 2 'in transit'

                    PossiblePackage[8] = status
                    g = getDistance(self.Location, PossiblePackage[1])

                    if g < minDistance:
                        minDistance = g

                        minPID = str(n)

                # b = RolodexAddressOnly[int(minPID)]
                dist = g
                self.deliver(minPID, h, dist)  # Deliver the package, process inside line 108's function

                Ride.remove(int(minPID))
            # Return back to the hub with getDistance and Location
            # loop through until that list is empty.
            self.totalMiles = self.totalMiles + getDistance(self.Location, '4001 South 700 East')

    def deliver(self, packageID, h, dist): # Running at O(1), Space O(1)
        package_list = h.get(packageID)
        addy = package_list[1]
        self.Location = addy
        Truck.listOfDeliveredItems.append(addy)
        newdistance = dist
        stopwatch = newdistance / 18
        self.totalMiles = newdistance + self.totalMiles

        package_list[8] = "delivered"   # marks the item as delivered
        self.CurrentTime = self.CurrentTime + timedelta(hours=stopwatch) # Get the final time
        s = self.CurrentTime.seconds
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)

        s = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
        package_list[9] = s # Mark the time the package is delivered
        #Result here
        return print("Truck Delivery: package: " + package_list[0] + "  is now delivered. It was delivered at: " +
                     addy + ", with a total distance of " +
                     str(self.totalMiles) + ' miles.' )
def TimeCheck(h,checkFullLoad, timeDelta): # Runs at O(n), Space O(1)
            for n in checkFullLoad:
                t = h.get(str(n))
                stamp = t[9]
                stamp = datetime.datetime.strptime(stamp, '%H:%M:%S')
                stamp = datetime.timedelta(hours=stamp.hour,minutes=stamp.minute,seconds=stamp.second)





                if stamp < timeDelta:
                    t[10] = str('Package will be delivered at: ' + str(timeDelta))
                    print(t)

                else:
                    t[10] = str('Package will not be delivered at: ' + str(timeDelta))
                    print(t)
            print(str('this is the status at time: ' + str(timeDelta)))
            n+=1


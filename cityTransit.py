class User:
    def __init__(self, location, destination):
        self.location = location
        self.destination = destination

    def bestRoute(self, vehicles):
        x = 3
        route = []  # route is a list of trains and buses that take the user to their destination
        smallest_distance = 1000
        fastest_vehicle = vehicles[0]

        current_vehicle = self.nearestVehicle(vehicles)
        intersecting_vehicles = current_vehicle.intersectingRoutes(vehicles)
        while (x>0):
            for vehicle in intersecting_vehicles:
                for j in vehicle.stops:
                    if ((j[0] - self.destination[0]) ** 2 + (j[1] - self.destination[1]) ** 2) < smallest_distance:
                        smallest_distance = (j[0] - self.destination[0]) ** 2 + (j[1] - self.destination[1]) ** 2
                        fastest_vehicle = vehicle
            route.append(fastest_vehicle)
            current_vehicle = fastest_vehicle
            intersecting_vehicles = current_vehicle.intersectingRoutes(vehicles)
            x -= 1

        for i in range(len(route)):
            print(route[i])

    def nearestVehicle(self, vehicles):
        current_vehicle = vehicles[0]
        current_stop = current_vehicle.stops[0]
        for vehicle in vehicles:
            for stop in vehicle.stops:
                if ((self.location[0] - stop[0]) ** 2 + (self.location[1] - stop[1]) ** 2) < (
                        (self.location[0] - stop[0]) ** 2 + (self.location[1] - current_stop[1] ** 2)):
                    current_vehicle = vehicle
                    current_stop = stop
        return current_vehicle


class Vehicle:
    def __init__(self, name, stops):
        self.stops = stops
        self.name = name

    def intersectingRoutes(self, all_vehicles):
        # returns the route that is intersecting with the passed route.
        lst = []
        t1_stops = self.stops
        for i in range(len(t1_stops)):
            for j in range(len(all_vehicles)):
                for k in range(len(all_vehicles[j].stops)):
                    if t1_stops[i] == all_vehicles[j].stops[k]:
                        lst.append(all_vehicles[j])
        return lst

    def __str__(self):
        return self.name

class Simulation:
    train1 = Vehicle('Blue Line',
                            [[10, 14], [9, 15], [8, 16], [7, 17], [6, 18], [5, 19], [4, 20], [3, 21], [11, 13],
                             [11, 12], [11, 11], [11, 10],
                             [11, 9], [12, 9], [13, 9], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [13, 13],
                             [12, 13], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11],
                             [10, 11]])
    train2 = Vehicle('Red Line',
                            [[14, 0], [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 14],
                             [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [11, 13], [11, 12], [11, 11], [11, 10],
                             [11, 9], [12, 9], [13, 9], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [13, 13],
                             [12, 13]])
    train3 = Vehicle('Orange Line',
                            [[4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 13], [11, 12], [11, 11],
                             [11, 10],
                             [11, 9], [12, 9], [13, 9], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [13, 13],
                             [12, 13]])
    bus1 = Vehicle('Bus1', [[11, 20], [11, 19], [11, 18], [10, 18], [9, 18], [9, 17], [9, 16], [8, 16]])
    bus2 = Vehicle('Bus2', [[1, 18], [1, 17], [1, 16], [1, 15], [2, 15], [3, 15], [4, 15], [4, 14], [4, 13],
                                   [5, 13], [6, 13], [7, 13], [7, 12], [7, 11]])
    bus3 = Vehicle('Bus3',
                          [[2, 9], [2, 8], [2, 7], [3, 7], [4, 7], [4, 8], [5, 8], [6, 8], [7, 8], [7, 9], [8, 9],
                           [9, 9], [10, 9], [11, 9]])
    bus4 = Vehicle('Bus4',
                          [[2, 5], [3, 5], [4, 5], [5, 5], [5, 4], [5, 3], [6, 3], [7, 3], [8, 3], [8, 4], [9, 4],
                           [10, 4], [10, 5], [11, 5],
                           [12, 5], [12, 4], [12, 3], [12, 2], [13, 2], [14, 2]])

    start = (input('Enter your start location.\nE.g. Enter "2,5" for x-coordinate 2 and y-coordinate 5.'))
    start_list = start.split(',')
    while len(start_list) != 2:
        start = input('Try again.')
        start_list = start.split(',')
    for i in range(len(start_list)):
        start_list[i] = int(start_list[i])
    end = input('Enter your destination.\nE.g. Enter "2,5" for x-coordinate 2 and y-coordinate 5.')
    end_list = end.split(',')
    while len(end_list) != 2:
        end = input('Try again.')
        end_list = end.split(',')
    for j in range(len(end_list)):
        start_list[i] = int(end_list[i])
    User1 = User(start_list, end_list)
    User1.bestRoute([train1, train2, train3, bus1, bus2, bus3, bus4])
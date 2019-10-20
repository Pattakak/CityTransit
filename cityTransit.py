class User:
    def __init__(self, iLocation, fLocation, preference='fast'):
        self.iLocation = iLocation
        self.fLocation = fLocation
        self.preference = preference

    def distance(self):
        iX = self.iLocation[0]
        iY = self.iLocation[1]
        fX = self.fLocation[0]
        fY = self.fLocation[1]
        dist = ((fX-iX)**2 + (fY-iY)**2)**0.5
        return dist

    def nearest_stop(self, trans):
        pass

class Transportation:
    def __init__(self, cost, speed, stops):
        self.cost = cost
        self.speed = speed
        self.stops = stops

    def travelTime(self, user):
        # each transportation object has a list of stops, so the distance of the route is
        # equal to the length of the list of stops, since each stop is one unit long
        dist = user.distance()
        time = self.speed/dist
        return time

    def atIntersection(self, grid, x, y): #bool
        #returns true if the location [x, y] on the grid has value '5'.
        return grid[x, y] == 5

    def bestRoute(self, user, *trans):
        route = [] #route is a list of trains and buses that take the user to their destination
        list_of_transportations = [] #all trains and buses on the map
        for tran in trans:
            list_of_transportations.append(tran)
        if user.preference == 'cheap':
            cheapest = list_of_transportations[0]
            nearest = user.nearest_stop(list_of_transportations)
            for i in range(len(list_of_transportations)):
                if user.nearest_stop() == list_of_transportations[i] and list_of_transportations[i].cost < cheapest.cost:
                    cheapest = list_of_transportations[i]

        else: #user.preference == 'fast'
            #do something else
            pass

        return route

class Simulation:
    grid = []
    for i in range(295):
        grid.append([0])
    for x in grid:
        for y in grid[x]:
            grid[x][y] = 0
    print(grid)
    train1 = Transportation(4, 10, )
    train2 = Transportation(6, 15, [])
    train3 = Transportation(5, 12, [])
    bus1 = Transportation(2, 6, [])
    bus2 = Transportation(3, 7, [])
    bus1 = Transportation(2, 6, [])
    bus1 = Transportation(2, 6, [])

    start = input('Enter you start location as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    end = input('Enter you destination as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    preference = input('Do you want the cheapest or fastest way to get to your destination? Enter "cheap" or "fast".')
    User1 = User(start, end, preference)

class User:
    def __init__(self, iLocation, fLocation):
        self.iLocation = iLocation
        self.fLocation = fLocation

    def bestRoute(self, *trans):
        route = [] #route is a list of trains and buses that take the user to their destination
        list_of_transportations = [] #all trains and buses on the map
        smallestDistance = 1000
        for tran in trans:
            list_of_transportations.append(tran)
        nearest = self.nearest_trans(list_of_transportations)
        fastestTran = list_of_transportations[0]
        list_of_routes = nearest.intersectingRoute(list_of_transportations)
        for tran in list_of_transportations:
            for j in tran.stops:
                if (j[0] - self.fLocation[0])**2 +  (j[1] - self.fLocation[1])**2 < smallestDistance:
                    smallestDistance = (j[0] - self.fLocation[0])**2 +  (j[1] - self.fLocation[1])**2
                    fastestTran = tran
        route.append(fastestTran)
        return route

    def nearest_trans(self, transportations):
        currenttrans = transportations[0]
        currentstop = currenttrans[0]
        for tran in transportations:
            for stop in tran.stops:
                if ((self.iLocation[0] - stop[0]) ** 2 + (self.iLocation[1] - stop[1]) ** 2) < (
                        (self.iLocation[0] - stop[0]) ** 2 + (self.iLocation[1] - currentstop[1] ** 2)):
                    currenttrans = tran
                    currentstop = stop
        return currenttrans


class Transportation:
    def __init__(self, stops):
        self.stops = stops

    def intersectingRoute(self, all_transportations):
        #returns the route that is intersecting with the passed route.
        list = []
        t1_stops = self.stops
        for i in range(len(t1_stops)):
            for j in range(len(all_transportations)):
                for k in all_transportations:
                    if t1_stops[i] == all_transportations[j].stops[k]:
                        list.append(all_transportations[j])
        return list

class Simulation:
    train1 = Transportation([[10, 14],[9,15],[8,16],[7,17],[6,18],[5,19],[4,20],[3,21],[11,13],[11,12],[11,11],[11,10],
                             [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],
                             [12,13],[1,11],[2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11]])
    train2 = Transportation([[14,0],[14,1],[14,2],[14,3],[14,4],[14,5],[14,6],[14,7],[14,8],[14,14],
                             [14,15],[14,16],[14,17],[14,18],[14,19],[11,13],[11,12],[11,11],[11,10],
                             [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],[12,13]])
    train3 = Transportation([[4,2],[5,3],[6,4],[7,5],[8,6],[9,7],[10,8],[11,13],[11,12],[11,11],[11,10],
                            [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],[12,13]])
    bus1 = Transportation([[11,20],[11,19],[11,18],[10,18],[9,18],[9,17],[9,16],[8,16]])
    bus2 = Transportation([[1,18],[1,17],[1,16],[1,15],[2,15],[3,15],[4,15],[4,14],[4,13],
                           [5,13],[6,13],[7,13],[7,12],[7,11]])
    bus3 = Transportation([[2,9],[2,8],[2,7],[3,7],[4,7],[4,8],[5,8],[6,8],[7,8],[7,9],[8,9],[9,9],[10,9],[11,9]])
    bus4 = Transportation([[2,5],[3,5],[4,5],[5,5],[5,4],[5,3],[6,3],[7,3],[8,3],[8,4],[9,4],[10,4],[10,5],[11,5],
                           [12,5],[12,4],[12,3],[12,2],[13,2],[14,2]])

    start = input('Enter you start location as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    end = input('Enter you destination as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    User1 = User(start, end)
    User1.bestRoute()


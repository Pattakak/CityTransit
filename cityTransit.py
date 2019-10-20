class User:
    def __init__(self, iLocation, fLocation):
        self.iLocation = iLocation
        self.fLocation = fLocation

    def distance(self):
        iX = self.iLocation[0]
        iY = self.iLocation[1]
        fX = self.fLocation[0]
        fY = self.fLocation[1]
        dist = ((fX-iX)**2 + (fY-iY)**2)**0.5
        return dist

    def nearest_stop(self, transportations):
        pass

class Transportation:
    def __init__(self, stops):
        self.stops = stops

    def intersectingRoute(self, transportation, all_transportations):
        #returns the route that is intersecting with the passed route.
        list = []
        t1_stops = transportation.stops
        for i in range(len(t1_stops)):
            for j in range(len(all_transportations)):
                for k in all_transportations:
                    if t1_stops[i] == all_transportations[j].stops[k]:
                        list.append(all_transportations[j])
        return list
    
    def nearestStopToPoint(self, point):
        nearestPoint = self.stops[0] #Init in case of emergency
        nearestDistanceSq = (nearestPoint[0] - point[0])**2 + (nearestPoint[1] - point[1])**2
        for stop in self.stops:
            if (stop[0] - point[0])**2 + (stop[1] - point[1])**2 < nearestPoint:
                nearestPoint = stop
                nearestDistanceSq = (nearestPoint[0] - point[0])**2 + (nearestPoint[1] - point[1])**2

    
    def isIntersecting(self, point, tran):
        for stop in tran.stops:
            if (point == stop):
                return True
        return False

    def transferRoute(self, user, point, prevTrans, *trans):
        
        nearestStop = point #Initialize the stops and transportations if we dont find anything in the for loop
        currentTrans = prevTrans


        for tran in trans:

            
    def bestRoute(self, user, *trans):
        route = [] #route is a list of trains and buses that take the user to their destination
        list_of_transportations = [] #all trains and buses on the map
        for tran in trans:
            list_of_transportations.append(tran)
        nearest = user.nearest_stop(list_of_transportations)
        return route

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

    # start = input('Enter you start location as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    # end = input('Enter you destination as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    # preference = input('Do you want the cheapest or fastest way to get to your destination? Enter "cheap" or "fast".')
    #User1 = User(start, end)

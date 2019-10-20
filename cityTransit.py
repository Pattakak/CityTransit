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
        currenttrans = transportations[0]
        currentstop = currenttrans[0]
        for tran in transportations:
            for stop in tran.stops:
                if ((self.iLocation[0] - stop[0])**2 + (self.iLocation[1] - stop[1])**2) < ((self.iLocation[0] -stop[0])**2 + (self.iLocation[1] - currentstop[1]**2)):
                    currenttrans = transportations
                    currentstop = stop
        return [currenttrans, currentstop]

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
        list_of_transportations = [] #all trains and buses on the map
        for tran in trans:
            list_of_transportations.append(tran)
        nearestlist = user.nearest_stop(list_of_transportations)
        currentTransit = nearestlist[0]
        currentStop = nearestlist[1]
        for stop in currentTransit.stops:
            transferRoute(self, user, user.iLocation, currentTransit)

class Simulation:
    train1 = Transportation([[10, 14],[9,15],[8,16],[7,17],[6,18],[11,13],[11,12],[11,11],[11,10],
                             [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],
                             [12,13],[1,11],[2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11]])
    train2 = Transportation([[14,0],[14,1],[14,2],[14,3],[14,4],[14,5],[14,6],[14,7],[14,8],[14,14],
                             [14,15],[14,16],[14,17],[14,18],[14,19],[11,13],[11,12],[11,11],[11,10],
                             [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],[12,13]])
    train3 = Transportation([[11,13],[11,12],[11,11],[11,10],
                                    [11,9],[12,9],[13,9],[14,9],[14,10],[14,11],[14,12],[14,13],[13,13],[12,13]])
    # bus1 = Transportation([])
    # bus2 = Transportation([])
    # bus3 = Transportation([])
    # bus4 = Transportation([])

    # start = input('Enter you start location as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    # end = input('Enter you destination as a list with x, y coordinates. \n  E.g. Enter "[2,5]" for x-coordinate 2 and y-coordinate 5.')
    # preference = input('Do you want the cheapest or fastest way to get to your destination? Enter "cheap" or "fast".')
    #User1 = User(start, end)

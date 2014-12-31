'''
William Baskin
created 12-30-14
edited  12-30-14
'''
from automatic_driver.auto_driver import Driver
from data_manipulation.data_loader import Trip, Loader_Manager
from data_manipulation.data_loader import Driver as trips
import math

class Accel_Driver(Driver):
    
    def __init__(self, driver_id):
        Driver.__init__(self, driver_id)
        self.pattern_list = []
        
    def _analyze_trip(self, trip):
        stop_points = []
        for index, vel in enumerate(trip.v_()):
            if vel < .5 and index >= 5 and index < len(trip.v_())-5: # speed less than ~ 1mph
                stop_points.append(index)
                
        index = 0
        while index < len(stop_points)-1:
            if stop_points[index] - stop_points[index+1] == 1:
                # combined points
                del stop_points[index+1]
            else:
                index = index + 1
                
        if not stop_points:
            # if its empty
            return -1
        # it has at least one distinct stop
        patterns = []
        for index, v_ind in enumerate(stop_points):
            patterns.append(Pattern(trip.v_()[v_ind-5:v_ind+6])) 
        if not patterns:
            # if its empty
            return -1
        # it has at least one pattern
        self.pattern_list = self.pattern_list + patterns
        
        return 1
        
        return 0
    
    def train_trip(self, trip):
        output = self._analyze_trip(trip)
        if output <= 0:
            print 'training error'
        else:
            print 'successful train'
    
    def develop_data(self):
        if not self.pattern_list:
            print 'no valid patterns'
        else:
            # collect normal distribution info (mean, stdev)
            data = [ [ 0.0 ] * len(self.pattern_list) ] * 11
            for i in xrange(0,10):
                for j in xrange(0,len(self.pattern_list)):
                    data[i][j] = self.pattern_list[j].v_(i)
            avg = [ 0.0 ] * 11
            sdv = [ 0.0 ] * 11
            for i in xrange(0,10):
                avg = average(data[i])
                sdv = stdev(data[i])
            # now I have the fingerprint
                
                
    
    def test_trip(self, trip):
        return False
    
    def _rate_trip(self, trip):
        return 0.0

class Pattern(object):
    
    def __init__(self, list_subsection):
        self.list = [0.0]*11
        for i in xrange(0,10):
            #normalize to the first data point
            self.list[i] = list_subsection[i]/list_subsection[0]
        # the middle point is 0
        self.list[5] = 0.0
    
    def v_(self, index):
        return self.list[index]

class Fingerprint(object):
    
    def __init__(self, average, stdev):    
        self.average = average
        self.stdev = stdev
        
    def test_run(self, velocity_list):
        # return average confidence of fit
        '''# TODO START HERE'''
        pass
    
def average(lst):
    return sum(lst)*1.0/len(lst)

def stdev(lst):
    avg = average(lst)
    var = map(lambda x: (x-avg)**2, lst)
    stdev = math.sqrt(average(var))
    return stdev

def main():
    pass

if __name__ == '__main__':
    main()
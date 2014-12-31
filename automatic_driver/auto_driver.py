'''
William Baskin
created 12-30-14
edited  12-30-14
'''

class Driver(object):
    '''
    A class that implements the driving analysis
    The objects of the class also store identifying kinematics information 
        about the specific driver
        
    '''
    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.trip_list = []
        self.fingerprint = None
    
    def analyze_trip(self, trip):
        '''
        helper method:
        given a trip, it runs through and tries to identify the kinds of 
            roads the driver was driving
        data is then accumulated by road type for further analysis
        This is where different parts of driving can be quantified for 
            "fingerprinting"
        '''
        pass
    
    def train_trip(self, trip):
        '''
        Given a trip, train the Driver to recognize the trip as part of 
            the collection of trips that are the driver 
        '''
        self.trip_list.append(self.analyze_trip(trip))
        pass
    
    def develop_data(self):
        '''
        Collect all trained trips to date and develop a fingerprint to compare 
            to test data
        '''
        pass
    
    def test_trip(self, trip):
        '''
        Given a trip, check against the Driver training to assign either
            a boolean yes or no to whether or not the trip is by the same
            driver
        '''
        return False
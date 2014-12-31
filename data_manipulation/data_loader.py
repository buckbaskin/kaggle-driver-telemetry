'''
William Baskin
created 12-22-14
edited  12-22-14
'''
import csv
import math
import random

class Loader_Manager(object):
    
    def __init__(self, data_folders_location):
        self.file_loc = data_folders_location
    
    def load(self, instruction):
        '''
        returns list of drivers
        '''
        if(instruction[0] == 'r'):  # random selection of drivers
            return self.load_drivers_random(instruction[1:len(instruction)])
        elif(instruction[0] == 'a'):
            return self.load_drivers_range('1:3216-1:200')
        else:
            return self.load_drivers_range(instruction)
            
            
    def load_drivers_random(self, sub_instruction='2-r2'):
        split_index = sub_instruction.find('-')
        print("preinstruction = " + sub_instruction[0:split_index] + 
              " | postinstruction = " + sub_instruction[split_index + 1:len(sub_instruction)])
        if split_index <= 0: return -1
        else:
            driver_list = []
            sub_inst = sub_instruction[split_index + 1:len(sub_instruction)]
            # ran = Random
            for i in xrange(1, int(sub_instruction[0:split_index])):
                driver_list.append(self.load_trips(random.randint(1, 3612), sub_inst))
            return driver_list
    
    def load_drivers_range(self, sub_instruction='1:2-1:2'):
        split_index = sub_instruction.find('-')
        print("preinstruction = " + sub_instruction[0:split_index] + 
              " | postinstruction = " + sub_instruction[split_index + 1:len(sub_instruction)])
        if split_index <= 0: return -1
        else:
            driver_list = []
            sub_inst = sub_instruction[split_index + 1:len(sub_instruction)]
            # set x range
            split_2 = 0
            split_2 = sub_instruction.find(':', 0, split_index)
            print('xrange(' + str(int(sub_instruction[0:split_2])) + ', '
                  + str(int(sub_instruction[split_2 + 1:split_index])) + ')')
            for i in xrange(int(sub_instruction[0:split_2]), 1 + int(sub_instruction[split_2 + 1:split_index])):
                print i
                driver_list.append(self.load_trips(i, sub_inst))
            return driver_list
    
    def load_trips(self, driver_num=1, sub_instruction='1:2'):
        '''
        returns a driver with the requested trips
        '''
        if(sub_instruction[0] == 'r'):  # random selection of drivers
            return self.load_trips_random(sub_instruction[1:len(sub_instruction)])
        else:
            return self.load_trips_range(sub_instruction)
    
    def load_trips_random(self, driver_num=1, sub_instruction='2'):
        d = Driver(driver_num)
        for i in range(1, int(sub_instruction) + 1):
            d.add_trip(self.load_trip(driver_num, random.randint(1, 200)))
        return d
    
    def load_trips_range(self, driver_num=1, sub_instruction='1:2'):
        d = Driver(driver_num)
        split_2 = sub_instruction.find(':')
        for i in range(int(sub_instruction[0:split_2]),
                       int(sub_instruction[split_2 + 1, len(sub_instruction)])):
            d.add_trip(self.load_trip(driver_num, i))
        return d
    
    def load_trip(self, driver_num=1, trip_num=1):
        specific_file = self.file_loc + "/" + str(driver_num) + "/" + str(trip_num) + ".csv"
        t = Trip(trip_num)
        with open(specific_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                # print row
                if(row[0] is not 'x'):
                    t.add_point(float(row[0]), float(row[1]))
            csvfile.close()
        return t

class Driver(object):
    
    def __init__(self, id_=-1):
        pass
        self.id_num = str(id_)
        self.trip_list = []
        
    def add_trip(self, trip):
        if isinstance(trip, Trip):
            self.trip_list.append(trip)
    

class Trip(object):
    
    def __init__(self, id_num=-1):
        self.id_num = str(id_num)
        self.x_list = []
        self.y_list = []
        self.v_list = []
        self.a_list = []
        
    def add_point(self, x, y):
        if (len(self.x_list) <= 0):
            self.y_list = []
            self.v_list = []
            self.a_list = []
            self.x_list.append(x)
            self.y_list.append(y)
            # just add point, no other info
        
        elif (len(self.x_list) == 1):
            self.x_list.append(x)
            self.y_list.append(y)
            
            # fill in the first two spots in velocity with the same value
            self.v_list.append(dist(x - self.x_list[0], y - self.y_list[0]) / 1.0)
            self.v_list.append(dist(x - self.x_list[0], y - self.y_list[0]) / 1.0)
            # fill in the first two accel spots with 0 (b/c of velocity fill)
            self.a_list.append(0)
            self.a_list.append(0)
        
        else:
            # else append x,y, speed acel as normal
            self.x_list.append(x)
            self.y_list.append(y)
            self.v_list.append(dist(x - self.x_list[-2], y - self.y_list[-2]) / 1.0)
            self.a_list.append((self.v_list[-1] - self.v_list[-2]) / 1.0)
            
    def x_(self, index =  -1):
        if index == -1:
            return self.x_list
        else:
            return self.x_list[index]
    
    def y_(self, index):
        if index == -1:
            return self.y_list
        else:
            return self.y_list[index]
    
    def v_(self, index):
        if index == -1:
            return self.v_list
        else:
            return self.v_list[index]
    
    def a_(self, index):
        if index == -1:
            return self.a_list
        else:
            return self.a_list[index]

def dist(a, b):
    return math.sqrt(a * a + b * b)

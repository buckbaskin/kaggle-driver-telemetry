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
        global file_loc
        file_loc = data_folders_location
    
    def load(self, instruction):
        '''
        returns list of drivers
        '''
        if(instruction[0] == 'r'): #random selection of drivers
            return self.load_drivers_random(instruction[1:len(instruction)])
        elif(instruction[0] == 'a'):
            return self.load_drivers_range('1:3216-1:200')
        else:
            return self.load_drivers_range(instruction)
            
            
    def load_drivers_random(self, sub_instruction='2-r2'):
        split_index = sub_instruction.find('-')
        print("preinstruction = "+sub_instruction[0:split_index]+
              " | postinstruction = "+sub_instruction[split_index+1:len(sub_instruction)])
        if split_index <= 0: return -1
        else:
            driver_list = []
            sub_inst = sub_instruction[split_index+1:len(sub_instruction)]
            #ran = Random
            for i in xrange(1, int(sub_instruction[0:split_index])):
                driver_list.append( self.load_trips(random.randint(1, 3612), sub_inst) )
            return driver_list
    
    def load_drivers_range(self, sub_instruction='1:2-1:2'):
        split_index = sub_instruction.find('-')
        print("preinstruction = "+sub_instruction[0:split_index]+
              " | postinstruction = "+sub_instruction[split_index+1:len(sub_instruction)])
        if split_index <= 0: return -1
        else:
            driver_list = []
            sub_inst = sub_instruction[split_index+1:len(sub_instruction)]
            #set x range
            split_2 = 0
            split_2 = sub_instruction.find(':',0,split_index)
            print('xrange('+str(int(sub_instruction[0:split_2]))+', '
                  +str(int(sub_instruction[split_2+1:split_index]))+')')
            for i in xrange(int(sub_instruction[0:split_2]), 1+int(sub_instruction[split_2+1:split_index])):
                print i
                driver_list.append( self.load_trips(i, sub_inst) )
            return driver_list
    
    def load_trips(self, driver_num=1, sub_instruction='1:2'):
        '''
        returns a driver with the requested trips
        '''
        if(sub_instruction[0] == 'r'): #random selection of drivers
            return self.load_trips_random(sub_instruction[1:len(sub_instruction)])
        else:
            return self.load_trips_range(sub_instruction)
    
    def load_trips_random(self, driver_num=1, sub_instruction='2'):
        d = Driver(driver_num)
        for i in range(1,int(sub_instruction)+1):
            d.add_trip(self.load_trip(driver_num,random.randint(1,200)))
        return d
    
    def load_trips_range(self, driver_num=1, sub_instruction='1:2'):
        d = Driver(driver_num)
        split_2 = sub_instruction.find(':')
        for i in range(int(sub_instruction[0:split_2]), 
                       int(sub_instruction[split_2+1,len(sub_instruction)])):
            d.add_trip(self.load_trip(driver_num,i))
        return d
    
    def load_trip(self, driver_num=1, trip_num=1):
        specific_file = file_loc+"/"+str(driver_num)+"/"+str(trip_num)+".csv"
        t = Trip(trip_num)
        with open(specific_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                #print row
                if(row[0] is not 'x'):
                    t.add_point(float(row[0]), float(row[1]))
            csvfile.close()
        return t

class Driver(object):
    
    def __init__(self, id_ = -1):
        pass
        global id_num
        id_num = str(id_)
        global trip_list
        trip_list = []
        
    def add_trip(self, trip):
        if isinstance(trip, Trip):
            trip_list.append(trip)
    

class Trip(object):
    
    def __init__(self, id_ = -1):
        global id_num
        id_num = str(id_)
        global x_list
        x_list = []
        global y_list
        y_list = []
        global v_list
        v_list = []
        global a_list
        a_list = []
        
    def add_point(self,x,y):
        global x_list
        global y_list
        global v_list
        global a_list

        if (len(x_list) <= 0):
            y_list = []
            v_list = []
            a_list = []
            x_list.append(x)
            y_list.append(y)
            # just add point, no other info
        
        elif (len(x_list) == 1):
            x_list.append(x)
            y_list.append(y)
            
            #fill in the first two spots in velocity with the same value
            v_list.append(dist(x-x_list[0],y-y_list[0])/1.0)
            v_list.append(dist(x-x_list[0],y-y_list[0])/1.0)
            #fill in the first two accel spots with 0 (b/c of velocity fill)
            a_list.append(0)
            a_list.append(0)
        
        else:
            #else append x,y, speed acel as normal
            x_list.append(x)
            y_list.append(y)
            v_list.append(dist(x-x_list[-2],y-y_list[-2])/1.0)
            a_list.append((v_list[-1]-v_list[-2])/1.0)
            
    def x_(self,index):
        return x_list[index]
    
    def y_(self,index):
        return y_list[index]
    
    def v_(self,index):
        return v_list[index]
    
    def a_(self,index):
        return a_list[index]

def dist(a,b):
    return math.sqrt(a*a+b*b)
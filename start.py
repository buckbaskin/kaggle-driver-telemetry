'''
William Baskin
created 12-22-14
edited  12-22-14
'''
from data_manipulation.data_loader import Loader_Manager
from data_manipulation.data_writer import Output_Manager
from os import sys

def main():
    file_loc = "/home/buck/Documents/driver_telemetry/drivers"
    l = Loader_Manager(file_loc)
    # load drivers 1-10, load trips 1-10 for each 
    #    l.load('1:10-1:10',file_loc)
    # load 10 random drivers, load 10 random trips for each
    #     l.load('r10-r10',file_loc)
    trips = l.load_drivers_range('1:2-r2')
    
    w = Output_Manager(file_loc)
   # w.collect_index()
    w.write_out_1()
    sys.exit(1)

if __name__ == '__main__':
    main()
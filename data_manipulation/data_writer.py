'''
William Baskin
created 12-22-14
edited  12-22-14
'''

import csv
import os

class Output_Manager(object):
    
    def __init__(self, data_folders_location):
        '''
        global file_loc
        file_loc = data_folders_location
        '''
        global file_loc
        file_loc = "/home/buck/Documents/driver_telemetry/submissions"
    def write_out_2(self, list_of_drivers):
        # TODO
        '''
        Fills out a csv file based on drivers, where the first index is the 
            driver id and the second is the trip id.
        '''
        return -1
    
    def write_out(self, solution_array):
        with open(file_loc+'/output.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['driver_trip'] + ['prob'])
            count = 0
            index_list = self.collect_index()
            print index_list
            for i in xrange(0,len(index_list)):
                for j in xrange(0,200):
                    writer.writerow([str(index_list[i])+'_'+str(j+1)]+[str(solution_array[i][j])])
                    count = count + 1
                    print count
            csvfile.close()
            print "count "+str(count)+ " is valid ? "+str(count == 547200)
            print "data write out complete"
    
    def write_out_1(self):
        with open(file_loc+'/output.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['driver_trip'] + ['prob'])
            count = 0
            index_list = self.collect_index()
            print index_list
            for i in xrange(0,len(index_list)):
                for j in xrange(0,200):
                    writer.writerow([str(index_list[i])+'_'+str(j+1)]+[str('1')])
                    count = count + 1
                    print count
            csvfile.close()
            
            print "count "+str(count)+ " is valid ? "+str(count == 547200)
            print "all 1s generated"
    
    def collect_index(self):
        file_loc = "/home/buck/Documents/driver_telemetry/drivers"
        directory_list = os.walk(file_loc).next()[1]
        directory_list = sorted(directory_list, key = self.getKey)
        return directory_list
    
    def getKey(self,item):
        return int(item)
        
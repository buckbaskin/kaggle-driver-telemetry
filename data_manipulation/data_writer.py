'''
William Baskin
created 12-22-14
edited  12-22-14
'''

import csv

class Output_Manager(object):
    
    def __init__(self, data_folders_location):
        '''
        global file_loc
        file_loc = data_folders_location
        '''
        global file_loc
        file_loc = "/home/buck/Documents/driver_telemetry/submissions"
    
    def write_out(self, solution_array):
        with open(file_loc+'/output.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['driver_trip'] + ['prob'])
            for i in xrange(1,3216):
                for j in xrange(1,200):
                    writer.writerow([str(i)+'_'+str(j)]+[str(solution_array[i][j])])
            csvfile.close()
    
    def write_out_1(self):
        with open(file_loc+'/output.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['driver_trip'] + ['prob'])
            for i in xrange(1,3216):
                for j in xrange(1,200):
                    writer.writerow([str(i)+'_'+str(j)]+[str('1')])
            csvfile.close()
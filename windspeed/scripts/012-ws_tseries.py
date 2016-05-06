#The aim of this script is to produce a timeseries of windspeed for each 
#station, with lines for winds at 0000, 0600, 1200 and 1800

import glob,os
import pandas as pd

#change the directory in here first
os.chdir("/home/sophie/projects/windspeed/data/")
fname_list = glob.glob('*allwinds.txt')

def read_file(fname):
    '''take a file and read it into a dataframe'''
    
    print """ %s please select the index of the following files to make a plot \
          of: """ % list(enumerate(fname))
    location = int(raw_input("> "))
            
    date_spec = {'date_time': [0,1,2]}
    column_names=["year","month","day","hour","ws"]
    dtype={"year":int,"month":int,"day":int,"hour":int,"ws":float}
    
    print fname[location]
    wind = pd.read_csv(fname[location], sep=" ",parse_dates=date_spec, 
    keep_date_col=True, names=column_names, index_col=False)
    #Dealing with hour - going from 600, 1200 etc to 6,12, 18
    wind["hour"]=(wind["hour"]/100).astype(int)
    
    #adding a date_time column with timestamp data
    wind['date_time'] = pd.to_datetime(wind.date_time) + \
    wind.hour.astype('timedelta64[h]')
  
    print "here the data from %s will be split up" % fname_list[location]
    print "location index= %d" %location
    print "wind dataframe= %r" %wind[0:5]
    #data_subs(wind,location)
    return data_subs(wind,location)
    
    
def data_subs(wind,location):
    '''Takes a dataframe and splits it into four new dataframes ready for 
    plotting'''
    print wind[0:5]
    print location
    #print "here the data from %s will be split up" % fname_list[location]
    pass

if __name__ == "__main__":
   
    data = read_file(fname_list)
    #data_subs(wind, location)
#The aim of this script is to produce a timeseries of windspeed for each 
#station, with lines for winds at 0000, 0600, 1200 and 1800

import glob,os
import pandas as pd
import matplotlib.pyplot as plt


class Analysis(object):
    '''take a file and read it into a dataframe
    then ask user if they want to show statistics 
    or make plots'''
   
    
    def __init__(self):
      
        #df with all values
        self.wind=wind
       
        #why can't I do this here?
        #wind_00['hour'] = wind[wind['hour'].isin([0000])]
 
        
    def split_df(self,wind):
        '''Split the original dataframe up into hours'''
        
        #self.wind_00= wind[wind['hour'].isin([0000])]
        #print self.wind_00['hour'][0:5]
        wind_00=wind[wind['hour'].isin([0])]
        wind_06=wind[wind['hour'].isin([6])]
        wind_12=wind[wind['hour'].isin([12])]
        wind_18=wind[wind['hour'].isin([18])]
        #do I need to have return here?
        
        #do you want to look at some stats for these?
        stats = raw_input("Do you want to see some data stats for the " 
	                  "hours 00,06,12,18, y/n ? \n> ")
	if stats == 'y' or 'Y' or 'Yes': 
	    self.investigate(wind, wind_00, wind_06, wind_12, wind_18)
	
	else: pass
	
	#Ask user if they want a timeseries plot
	plots = raw_input("Do you want to look at a timeseries plot y/n ?"
			  "\n>")
	
	if plots == 'y' or 'Y' or 'Yes':
	    self.plot_tseries(wind, wind_00, wind_06, wind_12, wind_18)
	    
	else: pass
        
    def plot_tseries(self, wind, wind_00, wind_06, wind_12, wind_18):
        
        plt.plot(wind['date_time'],wind['ws'])
        
        #labels
        plt.xlabel("Time")
        plt.ylabel("wind-speed", size=10)


        #change size of x ticks
        plt.rc("font", size=7)
        
               
        #chopping the file extension off to put in the name of the image file
        fname = fname_list[location][:-4]
        
        #print the plot to the screen
        plt.show()
        
        #Ask user if they want to save the plot in a file
        qu = raw_input("Do you want save the timeseries in a png y/n ?"
			  "\n>")

        if qu == 'y' or 'Y' or 'Yes':
            path = '/home/sophie/projects/windspeed/output/'
            plt.savefig(path+'%stseries.png' % fname, format='png')
                
        else: pass
    
    def plot_hist(self, wind, wind_00, wind_06, wind_12, wind_18):
        pass
        
    
    def investigate(self, wind, wind_00, wind_06, wind_12, wind_18):
        
        print "-" * 10
        print "00 subset:"
        print wind_00.describe(percentiles=[.05,0.5,0.95])
        print "-" * 10
        print "06 subset:"
        print wind_06.describe(percentiles=[.05,0.5,0.95])
        print "-" * 10
        print "12 subset:"
        print wind_12.describe(percentiles=[.05,0.5,0.95])
        print "-" * 10
        print "18 subset: "
        print wind_18.describe(percentiles=[.05,0.5,0.95])
        print "-" * 10

        

if __name__ == "__main__":
   
    #change the directory in here first
    os.chdir("/home/sophie/projects/windspeed/data/")
    fname_list = glob.glob('*allwinds.txt')

    #Choose a station from the list.
    print """ %s please select the index of the following files to make a plot\ 
          of: """ % list(enumerate(fname_list))

    location = int(raw_input("> "))

    ##Group first 3 columns into a datetime object
    date_spec = {'date_time': [0,1,2]}
    column_names=["year","month","day","hour","ws"]

    #specify the data type of each column
    dtype={"year":int,"month":int,"day":int,"hour":int,"ws":float}

    #read in the data into a dataframe called wind
    wind = pd.read_csv(fname_list[location], sep=" ",parse_dates=date_spec, 
    keep_date_col=True, names=column_names, index_col=False)
    
    #using keep_date_col=True puts forgets the dtypes specified for the columns
    #so we need to change them again here.
    wind[['year','month','day']]=wind[['year','month','day']].astype(int)

    #Dealing with hour - going from 600, 1200 etc to 6,12, 18
    wind["hour"]=(wind["hour"]/100).astype(int)

    #adding a date_time column with timestamp data
    wind['date_time'] = pd.to_datetime(wind.date_time) + \
    wind.hour.astype('timedelta64[h]')
    
    b = Analysis()
    b.split_df(wind)
    
import pandas as pd
import numpy as np
import datetime as datetime
import matplotlib.pyplot as plt

# Creating a panel of timeseries for each group of stations.

# Panel will have a timeseries of 00,06,12,18 ws if that hour has at least 14 
# obs per month. 

# An average over the group will be an extra plot in the panel.

NAl=['60525Biskra','60549Mecheria','60550Elbayadh',
'60555Touggourt','60559ElOued','60566Ghardaia','60580Ouargla',
'60581HassiMessaoud']

CSar=['60607Timimoun','60611InAmenas','60620Adrar','60630InSalah',
'62103Ghadames','62124Sebha']

WSa=['61223Tombouctou','61226Gao','61230NioroDuSahel','61498Kiffa',
'61499AiounElAtrouss','61492Kaedi','61497Nema','61450Tidjika']

CSal=['61024Agadez','61045Goure','61052Niamey','64753Faya',
'61017Bilma'] 

Egy=['62387Minya','62393Asyut','62405Luxor','62414Asswan',
'62420Baharia','62423Farafra','62435Kharga'] 

Sud=['62600WadiHalfa','62640AbuHamed','62650Dongola','62660Karima',
'62680Atbara']


stations=[NAl,CSar,WSa,CSal,Egy,Sud]

group_names={'NAlgeria':NAl,'CSahara':CSar,'WSahel':WSa,'CSahel':CSal, 
'Egypt':Egy,'Sudan':Sud}


def read_file(fname):
    '''put the station name into read_file and read_file will return a 
    dataFrame called wind which has the following columns a dataframe with a 
    datetime index'''
    
     
    column_names=["year","month","day","hour","ws"]
    dtype={"year":int,"month":int,"day":int,"hour":int,"ws":float}
    
    datafile='/home/sophie/projects/windspeed/data/%s_allwinds.txt' %fname

    # specify the columns you want to group together. Can't include hour at 
    # this point as it is not in the right format. 
    date_spec = {'date_time': [0,1,2]}

    # when you use keep_dat_col it keeps them as objects, not as the dtype you 
    # read them in as.
    wind = pd.read_csv(datafile, sep=" ", names=column_names, 
    parse_dates=date_spec,   keep_date_col=True, index_col=False ) 

    # Dealing with hour - going from 600, 1200 etc to 6,12, 18
    wind["hour"]=(wind["hour"]/100).astype(int)

    # combining year, month, day that were parsed together into date_time with 
    # hour, which is now in the correct format.
    wind['date_time'] = pd.to_datetime(wind.date_time) + \
    wind.hour.astype('timedelta64[h]')
  
    # make datetime the index before making subsections.
    wind.index = wind['date_time']  
    
    # Adds extra rows where value is kept if it meets isin() criteria. Nan if 
    # it doesn't.
    wind['ws_0']= wind['ws'][wind['hour'].isin([0])]
    wind['ws_06']= wind['ws'][wind['hour'].isin([6])]
    wind['ws_12']= wind['ws'][wind['hour'].isin([12])]
    wind['ws_18']= wind['ws'][wind['hour'].isin([18])]
    
    return wind

def group_mean(group):
    '''loop over items in group list, using read_file on each one
    return'''
    pass
    
def plot_tseries():
    '''set up n+1 subplots where n is number of stations in the group. Fill in 
    each plot with timeseries from each station and then a mean of all the 
    stations. Output to file eps.'''
    pass


    









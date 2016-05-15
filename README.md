# Data Science Daily Discoveries

This is a daily diary to keep me focussed and moving. 
For ~74 days (over 3 months) I will upload something related to learning 
Python, git and other tools useful for data science. 

I'm using the [IPython Notebook](http://ipython.org) with the Anaconda (2.4.1) 
Python (2.7.11) distribution.



--------------------

####Day 21

#####MySQL

`mysql -u root -p --local-infile` if you want to load local files into a database.
  
Today covered:
- Making a new database (CREATE DATABASE)
- Select database to work on (USE ..). Don't need semi colon ';'
- Making a table in a database (CREATE TABLE)
- Inserting values into the table (INSERT INTO table VALUES (list of values))
- Loading data from a locally stored text file into the table (LOAD DATA)
- Changing a record in the table (UPDATE table SET .. WHERE ..)
- Selecting unique values form a column (SELECT DISTINCT column FROM table;)   
Finished with [datetime selections](http://dev.mysql.com/doc/refman/5.5/en/date-calculations.html)


--------------------

####Day 20

#####MySQL

- Installed version and client 5.5, using [this 
tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)

- To remove current version, to make way for new version (5.6 - 5.7 is available too) follow 
[this](http://askubuntu.com/questions/489815/cannot-install-mysql-server-5-5-the-following-packages-have-unmet-dependicies)  

- To log in `mysql -u root -p` and it will ask for a password.

#####windspeed plotting 

- Make index a datetime object - easier to slice when plotting i.e.     
`wind.index=wind['date_time']`        
`year_sub = wind['1997':'2001']`          
`plt.plot(year_sub.date_time,year_sub.ws)`      

- I want to create a box and whisker plot, with the number of observations on top for each box and whisker. The issue is sharing the x-axis 
between the two sets of data. Its nice to use pandas for making the boxplot (very easy to create groups), but very hard to then plot a line 
of counts which correspond to each boxplot (labelled with a MultiIndex!).

- Violin plots might be an interesting alternative. 

Workings [here](windspeed/notebooks/019-windspeed.ipynb)

--------------------
####Day 19

#####MySQL   

Learned some basics:
- Noticed lots of similarities to ideas from python oop. 
- SQL has classes with attributes, these are similar to python class attributes.
Python class methods are called associations in SQL and the associated class is a child of the parent (which the child inherits attributes 
from)    
- Each row is a tuple.   
- Super Key (SK), Primary Key(PK), Foreign Key(FK), Candidate Key(CK), surrogate PK and substitute PK.    


#####windspeed plotting

- Opened an issue on creating the datetime index from a grouped dataframe and `reset_index()`
- Could still achieve the above using a loop.
- Some overplotting of different frequency data and shaded error region

Notebook found [here](windspeed/notebooks/019-windspeed.ipynb).

*To do* - make a script to group stations, make panels of plots, and output them to a file per group. 

--------------------
####Day 18

#####windspeed plotting

- Used `reset_index()` to add a datetime index to a dataframe created from a groupby() object with monthly averages.
- First tried to do the above with a loop and MultiIndex- it worked fine.
- Subsections can be selected by specifying datetimes as strings e.g.    
`w['mean']['1998-05':'1998-10'].plot(yerr=w['std'])`. 
- Plotted some error bars and a shaded error "band"

Have added an [updated version](windspeed/notebooks/018_2-windspeed.ipynb) of this because the datetime index was wrong and I have no idea 
how it worked [here](windspeed/notebooks/018-windspeed.ipynb).

--------------------
####Day 17

#####windspeed plotting

- Select rows based on two different conditions in two different columns. 
I was nearly there before - just needed brackets around each condition!  
`onemonth = wind[(wind['year']== 1984) & (wind['month'] == 3)]`
This selects rows from march in 1984.   

- Grouping and averaging data using `df.groupby` and `.aggregate([np.mean,np.std])`.  

- Using lambda to define a function to pass to transform():   
  `f = lambda x: x.mean()     
   transformed = grouped.transform(f)` 

- Some very simple code for plotting a comparison between an averaged dataset and it's original:
`compare = pd.DataFrame({'Original':wind['ws'], 'Transformed':wind['mean_ws']})`   
`compare.plot()`

- Experimented a little with plotting std error bars. 

[Notebook](windspeed/notebooks/017-windspeed.ipynb) with the working


--------------------
####Day 16

#####windspeed plotting

- Used pandas plotting. `df.plot` is a wrapper for `plt.plot(df)`.    
- Plotted density functions (kind='kde') of ws at different times of day.  
- Overplotted several lines in one plot.    
- Added a legend.     
- Specified the colour of each line.    

Averaging timeseries data:

- resampling using resample() is handy with datetime information, but you have to turn it into an index. There are two steps here, first you 
have to make object with resample, then apply `.agg()` do do the statistics (mean, std).     
- couldn't upsample the mean and std for each month to the same irregular original array, though it is very easy to make it 
into a regularly spaced array. Could do that, then match it to the original array. 
- Or, use groupby `grouped = wind.groupby(['year','month'])` though I haven't worked out if this is actually doing what I want, and if it 
is possible to upsample it to the original array.

[See the notebook](windspeed/notebooks/016-windspeed.ipynb) for the working.

--------------------

####Day 15 
#####Markdown

I configured Kate to extend the line length limit to 140, up from 80. This should reduce the problems from long web links.

#####Monkey Learn visualisation

Enriching the [raw data](monkeylearn/indeed_edin.csv) with Monkeylearns API, 
with the help of pandas and requests in python, found 
[here](monkeylearn/015-selectdata.py) led to this plot in plot.ly: [Industries which hire data scientists in 
England](https://plot.ly/~SophMC/6/industries-employing-data-scientists-in-england-indeedcouk/).  


#####Plot.ly

I can produce a graph in ipython notebook and it will appear on the plot.ly 
account online, along with a table with the data.    
This is publicly available, privacy is paid for.




--------------------------
####Day 14
#####Import.io

I'm trying to work through a short 
article which uses import.io (to scrape 
lists from the web) and Monkeylearn (to get data from text using machine 
learning) to ["Create an Employment Analytics Visualization in Less Than 10 
Minutes"]
(https://blog.monkeylearn.com/how-to-create-an-empl&#160
oyment-analytics-visualization-in-less-than-10-minutes/). It's definitely taken 
me more than 10 mins due to lots of teething 
problems with import.io.

- Can use [magic import.io](https://magic.import.io/examples) to very quickly 
get up to 20 consecutive pages.

- Better to input the values manually in the [extractor 
page](https://dash.import.io/) if you have more than 20 pages. Use excel to 
change the last digit i.e.

```http://www.indeed.co.uk/jobs?q=data+scientist&l=England&start=10
http://www.indeed.co.uk/jobs?q=data+scientist&l=England&start=20
http://www.indeed.co.uk/jobs?q=data+scientist&l=England&start=30
```

It took 7mins to scrape the data from 203 pages. 




--------------------------
####Day 13 

#####Windspeed Plotting
`list(df)` - really nice way to show dataframe column names

[New script](windspeed/scripts/013-ws_tseries.py) where I am trying to practise 
using OOP methods with classes. Whether it is suitable or not for the problem I 
am not sure. So far, the script does the following (you can download [3 data 
files](windspeed/data) to try it with):

* Shows you a list of N African stations from which you can pick the index.
* Gives you options to; 
    - Give descriptive statistics
    - Make a time series plot to view 
    - Save a copy of the plot

The few final things I want to get into this script before I will move on:

* Plot the timeseries in monthly bins (error bars)
* Make a nice plot with 4 timeseries on the same plot from obs at 00,06,12 and 
18
* Design a test script (really need to practise this!)

I will test the ideas out in a notebook first before trying to organise them in 
a script with classes and methods. 

---------------------------

####Day 12

#####Web App Building

A [very primative game](gothonweb) which can take an input and move to another 
page, based on the user input. It only works for the first two rooms. I think 
you will pretty much die whatever input you put after that. 

Instructions:  
* Download /notechain/gothonweb recursively.
* Inside /gothonweb entering: `python
bin/app.py` should return `http://0.0.0.0:8080/` to the terminal.
* Copy `http://localhost:8080/game` into your address bar.
* Follow the game!

The [tutorial](http://learnpythonthehardway.org/book/ex52.html) suggests a lot 
more refining but spent as much time on this as I want to.

#####Windspeed plotting
I want to make a script using and classes and functions which can: 
- Allow a file to be selected by the user from a list of files in the directory 
- This will then be plotted as a timeseries of windspeed, split 4 lines of 
winds at 00,06,12 and 18.
- The graph will be output into a image file.

So far I have made [this mess](windspeed/notebooks/012-ws_tseries.py). Maybe functions 
and classes are just not needed for this task, or maybe I don't really have a 
clue on how to apply them. 

---------------------

####Day 11
#####Plotting windspeed


Opened an [issue](https://github.com/SophMC/notechain/issues). Not able to use 
`df.query()` as apparently `numexpr` is not supported. 

The following working is in 
[011-windspeed.ipynb](windspeed/notebooks/011-windspeed.ipynb).   
`%matplotlib inline` ensures plots display in the notebook

`plt.plot(xaxis,yaxis)` `plt.xlable()` `plt.show()`   
Change size of x ticks `plt.rc("font", size=7)`

Three different ways to use `pd.astype()`

To make a sub-set of data (a more limited method):  
1) create a mask `row_mask = wind['year'].isin([1985,1986])`  
2) apply mask to the df or column `wind['year'].loc[row_mask][0:5]`

Better to apply one criteria at a time and make a new data fram each time:  
`years_sub = wind[wind['year'].isin([1998,1999,2000,2001,2002])]`   
`highwind_sub = years_sub[years_sub['ws'] > 8]`   
This way you can apply conditions to select a subset. Can't do that using 
isin().


----------------

####Day 10
#####Plotting Windspeed

Solved my [issue](https://github.com/SophMC/notechain/issues/1) on the 
timestamp problem.
Here is [some working](windspeed/notebooks/010_1-windspeed.ipynb) on the way to finding 
it out. 
Tips to remember:   

Double brackets to ref several columns at once:
`print wind[['year','month','day']][0:5]`

`index_col=False` stops pandas using the first column as the index:    
`wind = pd.read_csv(datafile, sep=" ", names=column_names, index_col=False )` 

Having a quick squint at discrete values
`for x in range(0,4): print wind[column_names[x]].unique()`

This didn't work. Anything above 12 in the hour column only recognised the 
second digit, i.e. 2 in 12, 8 in 18.   
`p = pd.to_datetime(year + month + day + hour, yearfirst=True, utc=True, 
format='%Y%m%d%H') ; print p` 

`0   1984-03-10 06:00:00`  
`1   1984-03-11 02:00:00`  
`2   1984-03-11 08:00:00`  
`3   1984-03-20 06:00:00`  
`4   1984-03-21 02:00:00`  
`dtype: datetime64[ns]`  


-----------------

####Day 9

Opened an [issue](https://github.com/SophMC/notechain/issues/1) on the 
timestamp problem.

----------------


####Day 8
#####Web App Building

Exercise 52 from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex52.html). I think I will be 
working on this a few days more before uploading something that you can test 
out. 

#####Plotting windspeed 

My [first attempt](windspeed/notebooks/008-windspeed.ipynb) to read in [windspeed 
data](windspeed/61401BirMoghrein_allwinds.txt) with the format:   
`year, month, day, time, ws`         
I wanted to combine the first four columns into a new timestamp column but this 
has proved difficult. I tried to use read_csv but as the time data were in the 
format 600, 1200, 1800 it wasn't recognised when reading in.   
Next, I created the timestamp after reading in the data but there were problems 
with the input requiring a string and I can't seem to change the dataFrame 
objects to strings to allow it to do this. 

-----------------


####Day 7
#####Web App Building
Exercise 52 from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex52.html)

Nothing to show yet as only have the first room working. Need to work out how 
to take the input from the form to lead onto the next room.

$ is used to specify python expressions in html, using web.py
$elif cannot be used. Replace with $else and $if.
You must place a `__init__.py` inside a directory if you wish to use 
`from bin.app import app` to run app_tests.py nosetests on app.py which is 
inside /bin

-----------------

####Day 6
#####Web App Building
[Exercise 51](firstform) from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex51.html)

Instructions:  
* Download /notechain/firstform recursively.
* Inside /firstform entering: `python
bin/app.py` should return `http://0.0.0.0:8080/` to the terminal.
* Copy `http://localhost:8080/hello` into your address bar.

-----------------

####Day 5 
#####Pandas Data Analysis
The following actions are found 
[here](pandas-notebooks-csv/004-LendingClub.ipynb):  

* Removed % signs and "months" and converted the rest into a number.  
* Removed null values with `df.dropna()`. Investigate null values by saving 
them in a new df.  
* Removed data above the 95th percentile by using conditional statements for 
  each column. There must be a cleaner way to do it than this:

`no_outliers = nonan[(nonan[columns[0]] < p[0]) & (nonan[columns[1]] < p[1]) &
(nonan[columns[2]] < p[2]) & (nonan[columns[3]] < p[3]) & (nonan[columns[4]] < 
p[4]) & (nonan[columns[5]] < p[5])]` 
  
* Saved the new dataframe with `to_csv()`. 
* Eyeballed the difference before/after cleaning with a subset of columns in 
`scatter_matrix`

IMPORTANT: `df.count()` only returns non-nans.

---------------

####Day 4 

#####Git:  
If you remove from local directory you must do this before the changes will be 
made on the remote repository:   
`git rm filename`
`git commit -m "message"`
`git push`

#####Building Web Apps: 
I made [this](http://learnpythonthehardway.org/book/ex50.html) work, only after 
working out (google useless!) where to put a line continuation in 
index.html  
`$if greeting:
    I just wanted to say <em style="color: green; font-size: 
2em;">$greeting</em>.`

Did not fit in one line in my editor. When I shortened it to one line it 
worked. An \ was needed between the message and the html emphasized text.

```$if greeting:
    I just wanted to say \    
<em style="color: green; font-size: 2em;">$greeting</em>.```

#####More Data Analysis in Pandas: 
Started [plotting the data](pandas-notebooks-csv/004-LendingClub.ipynb) with  
`df.plot(kind = 'box'), df.hist() and scatter_matrix(df)`

To suppress the printing of the object before a panel of plots
`_ = df.hist()` etc.


--------------

####Day 3  
%timeit : time how long a command takes to run.  
More pandas practise [here](pandas-notebooks-csv/003-LendingClub.ipynb).   
`df.dropna(), df.isnull(), df.any(), df.sum()`

--------------


####Day 2                                                                       
More pandas practise [here](pandas-notebooks-csv/002-LendingClub.ipynb). 
Re-discovered the 
usefulness of cheatsheats. Now have a number of functions for exploring the 
data.    
```df.head(), df.unique(), df.describe(), df.iloc(), df.count(), 
df.isin(), np.where()```

--------------

####Day 1                                                                
I learned some [git commands](001-git-basics.md) and [played around 
with some data](pandas-notebooks-csv/001-LendingClub.ipynb) in ipython using 
DataFrames (df) in pandas library. 
`df.columns(), df.index(), df.dtypes()`

-------------


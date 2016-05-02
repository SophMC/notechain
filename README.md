# Data Science Daily Discoveries

This is a daily diary to keep me focussed and moving. 
For ~74 days (over 3 months) I will upload something related to learning 
Python, git and other tools useful for data science. 

I'm using the [IPython Notebook](http://ipython.org) with the Anaconda (2.4.1) 
Python (2.7.11) distribution.

-------------

####Day 1                                                                
I learned some [git commands](001-git-basics.md) and [played around 
with some data](pandas-notebooks-csv/001-LendingClub.ipynb) in ipython using 
DataFrames (df) in pandas library. 
`df.columns(), df.index(), df.dtypes()`

-------------

####Day 2                                                                       
More pandas practise [here](pandas-notebooks-csv/002-LendingClub.ipynb). 
Re-discovered the 
usefulness of cheatsheats. Now have a number of functions for exploring the 
data.    
```df.head(), df.unique(), df.describe(), df.iloc(), df.count(), 
df.isin(), np.where()```

---------------

####Day 3  
%timeit : time how long a command takes to run.  
More pandas practise [here](pandas-notebooks-csv/003-LendingClub.ipynb).   
`df.dropna(), df.isnull(), df.any(), df.sum()`

----------------

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

----------------

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


----------------

####Day 6
#####Web App Building
[Exercise 51](firstform) from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex51.html)

Instructions:  
* Download /notechain/firstform recursively.
* Inside /firstform entering: `python
bin/app.py` should return `http://0.0.0.0:8080/` to the terminal.
* Copy `http://localhost:8080/hello` into your address bar.

----------------

####Day 7
#####Web App Building
Exercise 52 from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex52.html)

Nothing to show yet as only have the first room working. Need to work out how 
to take the input from the form to lead onto the next room.

$ is used to specify python expressions in html, using web.py
$elif cannot be used. Replace with $else and $if.
You must place a __init__.py inside a directory if you wish to use 
`from bin.app import app` to run app_tests.py nosetests on app.py which is 
inside /bin


-----------------

####Day 8
#####Web App Building

Exercise 52 from [Learning Python the Hard 
Way](http://learnpythonthehardway.org/book/ex52.html). I think I will be 
working on this a few days more before uploading something that you can test 
out. 

#####Plotting windspeed 

My [first attempt](windspeed/008-windspeed.ipynd) to read in [windspeed 
data](windspeed/61401BirMoghrein_allwinds.txt) with the format:   
`year, month, day, time, ws`         
I wanted to combine the first four columns into a new timestamp column but this 
has proved difficult. I tried to use read_csv but as the time data were in the 
format 600, 1200, 1800 and it wasn't recognised when reading in.   
Next, I created the timestamp after reading in the data but there were problems 
with the input requiring a string and I can't seem to change the dataFrame 
objects to strings to allow it to do this. 

-----------------

####Day 9

Opening an [issue](https://github.com/SophMC/notechain/issues/1) on the 
timestamp problem.

----------------

# Data Science Daily Discoveries

This is a daily diary to keep me focussed and moving. 
For ~74 days (over 3 months) I will upload something related to learning 
Python, git and other tools useful for data science. 

I'm using the [Jupyter Notebook](http://jupyter.org/) with the Anaconda (2.4.1) 
Python (2.7.11) up to ~ day 35, and Python 3.5 thereafter.

------------------
####Day 51

##### SQL

- Completed (and understood) Qu 13 on the Joins [Movie tutorial](http://sqlzoo.net/wiki/More_JOIN_operations). Now stuck on 16.

##### Think Bayes

- Baysian methods are most useful when you carry the posterior distribution into the next step of the analysis to perform some kind of 
decision analysis, or some kind of prediction.

------------------
####Day 50

##### SQL

- More Joins using [this](http://sqlzoo.net/wiki/More_JOIN_operations) tutorial. Stuck on Qu. 13.

##### Think Bayes - Euro problem

- Beta distribution: Allows an update with two additions.
- Conjugate priors and distributions: If the prior and posterior distributions are in the same family.
- Swamping the priors: Given enough data, people with different priors will tend to converge on the same posterior.
- Cromwell's rule: Don't give a hypothesis a prior probability of 0, if there is ANY chance of it occurring. If p(H) = 0, p(H|D) will 
always be 0, no matter the data.
- [Notebook](tutorials/ThinkBayes/050-Euro.ipynb) with the Euro Estimation problem.

##### Titanic

- [Played around](Titanic/notebooks/050-pandas_vis.ipynb) trying to visualise the data with histograms to work out which features 
are important. 
- Overplotted subsections of histograms on each other, i.e. Age for survived/died.
- seaborn statistical package has some nice functions for plotting features. 
- resubmitted, changing column "FareBin" to "Fare" so that it matched the training set. It didn't make any difference. 

------------------
####Day 49

##### Think Bayes

**Estimation**

- An example equation in Markdown:      
`\begin{equation} PMF(x) \:\alpha \left(\frac{1}{x}\right)^\alpha \end{equation}`
- [Locomotive example notebook](tutorials/ThinkBayes/049-Locomotive.ipynb). How many trains are there operating in a particular area? We 
investigate the possible ways to answer this. First using a set prior (i.e 1000 or 500) which gives a very uncertain number. This is 
improved by:      
a) adding more data (seeing more trains) 
or b) improving the prior (can we start out with a more realistic prior).                 
To use b, we introduce the power law into the hypothesis prior which provides a better first guess. 

**Credible Intervals and Cumulative Distribution Function (cdf)**

- A credible interval is the values between which there is a 90% chance that the unknown value falls between them.
- Use a cdf, rather than a pmf if computing several interval values at the same time. These two methods are 
shown [here](tutorials/ThinkBayes/049-Credible_intervals_cdfs)

#### Titanic Random Forest

- Have to remove any null values and turn the whole dataframe into floats. Remove or convert string columns.
- Repeated the data clean-up exercise for the training set, and in a [stand-alone 
script](Titanic/bin/clean_test.py) for the test-set, before calculating the [survival predictions using 
RandomForest](Titanic/notebooks/049-Titanic_RandomForest.ipynb).
 
------------------
####Day 48

##### SQL

- Some good tutorials at [SQLZOO](http://sqlzoo.net/). Have made a new repository especially for 
SQL [here](https://github.com/SophMC/SQLtutorials).
- HAVING is used on GROUP BY objects, as WHERE can't be.


------------------
####Day 47

##### Think Bayes

**Estimation**

- Investigating the probability you roll a 4,6,8,12 or 20 sided die, given the number (or list of numbers) that is rolled.
- Using numbers for hypotheses, create concrete class type (Dice) and write a new Likelihood method. Full explanation and working 
[here](tutorials/ThinkBayes/047-Dice.ipynb).


##### Titanic: Machine Learning

- Rewrote the [first tutorial](Titanic/notebooks/045-Titanic.ipynb) in pandas, and I much prefer it. Notebook [here](Titanic/notebooks
/047-pandas_prediction.ipynb).
- Some particularly useful snippets
  - `df.isnull().sum()` : null value count for each column
  - `df['Farebin'] = df['Fare'].map(binfare)` : using map to apply a function to each value in a column
  - `len(df[(df['Pclass'] == 2) & (df['Farebin'] == 1)])` : count how many rows match these criteria.

##### SQL  

- To read in a textfile delimited by spaces:      
`LOAD DATA LOCAL INFILE '../winds.txt' INTO TABLE Biskra FIELDS TERMINATED BY ' ';`
- To create a windspeed table:      
`CREATE TABLE Biskra (year integer(4), month integer(2), day integer(2), hour integer(4), ws float(10));`


------------------
####Day 46

##### Think Bayes

- Making a framework for the Monty Hall problem. Notes on how this is done are in 
[this notebook.](tutorials/ThinkBayes/046-MontyHall_framework.ipynb)
- [Instructions](tutorials/ThinkBayes/046-ImplimentingSuite.ipynb) on how to impliment a Suite of hypotheses to create class Monty from 
[thinkbayes.py](tutorials/ThinkBayes/thinkbayes.py). Very useful!
- Using Suite from thinkbayes.py to calculate probability that an m&m came from a particular bag. I can't quite follow the code but have 
written notes in [this workbook.](tutorials/ThinkBayes/046-Suite_m&m.ipynb)
- **Suite** is an *abstract* type
- [**Monty**](tutorials/ThinkBayes/046-ImplimentingSuite.ipynb) is a *concrete* type: A class which extends an *abstract* parent class and 
provides an implementation of the missing methods. For example, Monty extends Suite, so that it inherits Update and provides Likelihood.

##### Titanic Machine Learning

- A good few more tips on using Pandas for data cleaning in [this Titanic tutorial workbook](Titanic/notebooks/046-Titanic_pandas.ipynb) 
(annotated by me):
  - Filling in columns with nans with "probable" values. The success of your ML could depend on the techniques you use to do this.
  - Keeping track of values which were filled in with "probable" values. 
- To do: rewrite the [first tutorial](Titanic/notebooks/045-Titanic.ipynb) in pandas.
- `df.isnull().sum()` : count number of null values in each column.


------------------
####Day 45

##### Think Bayes

- [This workbook](tutorials/ThinkBayes/045-Cookie_framework.ipynb), using the "Cookie" problem, contains the code necessary to compute 
POSTERIOR probabilities for a suite of hypotheses, as well as being able to update these POSTERIOR probabilities with new data. 

##### Titanic Machine Learning

- I understand [this](https://www.kaggle.com/c/titanic/details/getting-started-with-python) Titanic python tutorial better now. We use the 
training set (with Survived) column to develop a model. Then apply the model to the test set with the final goal to produce an indexed list 
of prediction for each passenger. 
- Working [here](Titanic/notebooks/045-Titanic.ipynb), for a model which is based on gender, class (1st,2nd,3rd) and price (4 bins of $10) 
and produces the following prediction in [genderclassmodel.csv](Titanic/genderclassmodel.csv)
- Can't quite get the final model to print out. 

##### SQL

- Working through [24 SQL Interview Questions](https://www.toptal.com/sql/interview-questions) and 
[KhanAcademy](https://www.khanacademy.org/computing/computer-programming/sql) - great interface for learning SQL. 
- When comparing a value to Null, you must us `is`, not `=`. e.g. `null is null`, not `null = null`.


------------------

####Day 44

##### Exercism Ex 6 - Word Count

- 'Write a program that given a phrase can count the occurrences of each word in that phrase'
- My solution [here](tutorials/exercism_py3/word_count/wordcount2.py). I couldn't get it to pass the [last 
test](tutorials/exercism_py3/word_count/word_count_test.py). It has trouble detecting the space in the 
russian characters. 
There is no `str.decode()` in python 3 as everything is decoded from UTF-8 already. I need to look through more of other peoples 
submissions. [For example](tutorials/exercism_py3/word_count/wordcount3.py) this works but I'm not sure why 
yet. 

------------------
####Day 43 

##### Bayes's Theorem

- Cookie problem and Monty Hall Problem from [Think Bayes](http://www.greenteapress.com/thinkbayes/thinkbayes.pdf)
- Have started using the module [ThinkBayes.py](tutorials/ThinkBayes/thinkbayes.py) written by the author, to follow the Computation 
Statistics: Distributions chapter. Have converted bits of it from python 2 to python 3. i.e. `itervalues()` to `values()`.
- [Cookie problem notebook](tutorials/ThinkBayes/043-Distributions.ipynb), using pmf module. 

##### Machine Learning - Titanic Kaggle comp

- Going through [the tutorial](https://www.kaggle.com/c/titanic/details/getting-started-with-python) using python 3, to become acquainted 
with open(), read_csv(), next() standard python modules, rather than pandas.  
- [Notebook](Titanic/notebooks/Titanic_explore.ipynb) with the first step: creating a gender-based model. Consistst of Passengerid and 
Survived, though I am confused, as it should perhaps be Sex because it is binary 1 or 0 for female/male.


------------------
####Day 42

##### Bayes's Theorem

- Learned the following terms from [Think Bayes](http://www.greenteapress.com/thinkbayes/thinkbayes.pdf).
  - Conditional and Conjoint probability
  - How to derive Bayes Theorem
  - Diachronic Interpretation
    - Specify a 'suite' of hypotheses that are *Mutually Exclusive* and *Collectively Exhaustive*
    - Then you can use the *law of total probability*

##### Windspeed

- Resolved and closed github [issue](https://github.com/SophMC/notechain/issues/3) with DateTimeIndex.


------------------
####Day 41

Make a website for your project with [Github pages](https://pages.github.com/). An example 
[here](http://cs109.github.io/2015/pages/projects.html).

[Building a data science portfolio](https://www.dataquest.io/blog/data-science-portfolio-project/).

##### K-means

- I don't fully understand each step in [this example](tutorials/K-means/MNIST.ipynb) of using PCA and Kmeans with sklearns [digits 
dataset](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) but I've tried to unpick most of it and 
annotated it a bit further. 
- `np.linspace(start,stop,num)` where num = num of equally spaced samples
- `np.tolist` Return the array as a (possibly nested) list.

##### Windspeed

- Finally managed to convert a MultiIndex into a dateTime index for date data. Full working 
[here](windspeed/notebooks/041-Tidjika_faya.ipynb).      
  `df['date_time'] = df[['year', 'month']].apply(lambda x: pd.to_datetime('/'.join(x)), axis=1)`
- The plot format is looking much better, though I still don't have the xaxis in the format I want.
At the moment it is like [this](windspeed/plots/WSahel.png) and I want the month and year to be displayed on top of each other. 

##### Exercism Ex 5

- Counting the differences between two dna strands
- Got to [my solution](tutorials/exercism_py3/Ex5_hamming/hamming.py) fairly quickly. 
[Here](tutorials/exercism_py3/Ex5_hamming/hamming2.py) is a two-liner using `zip()`.

------------------
####Day 40

##### Windspeed

- If there is an observation at 1200 and 1224, these both get converted into the time index:
`1987-04-04 12:00:00`. This leads to duplicate values in the Index (bad!).
These are found with the code `wind.index.value_counts()`.   
- dropped duplicated rows based on the 'date_time' column. 
- This fixed the mysterious `ValueError: cannot reindex from a duplicate axis` which occurred at Niamey.
- All groups are printing plots now, but still need to fix an error with the xaxis at Tidjika and Faya.
- [Working script](windspeed/scripts/040-group_tseries.py) and the above problem [investigation](windspeed/notebooks/040-Niamey_issue.ipynb)

##### Kmeans

- Once the optimal number of clusters is found from the elbow curve plot, you can split the data into the number of clusters. If 
you you have 3 clusters, your data is split into 3 classes. Like, walking, standing, sitting etc. in the Samsung example. 
- [kmeans.py](tutorials/K-means/kmeans.py) is a good example of making your own function so that you can easily change variables 
in a plot. What I have been trying to do for windspeed. 
- The process is similar to Linear, Logistic and Random Forests:
  - Set up the model (Linear `sm.OLS()`- , Logistic - `sm.Logit()`, Random Forests - `sk.RandomForestClassifier()`, Kmeans - `KMeans()`)
  - Fit the model to some data (model.fit())
  - Make predictions using (model.predict())


##### Exercism Ex 4

- Mapping dna sequence to rna sequence.
- Used a dictionary to map letters `d={'G':'C','C':'G','T':'A','A':'U'}`
- used `''.join([d[m] for m in p])` to loop over input such as 'GCTTA' and return it as 'CGAAU'
- [My submitted solution](tutorials/exercism_py3/dna/dna.py)
- [Another solution](tutorials/exercism_py3/dna/dna2.py) using `str.maketrans(intab, outtab)` - A very easy way to substitute characters.

------------------
####Day 39

##### K-means - [notebook](tutorials/K-means/039-kmeans_exploredata.ipynb)

- Create a list of code books and distortions(tuples in KM).        
- Extract code books to a list of their own(centroids).    
- Each code book has [n_cluster, n_features], where n_features is the number of columns.     

Here it gets  a little tricky

- For each cluster set (ie. using 1,2,...10 clusters) we make a distance matrix (D_k). Shape=[n_rows,n_clusters]. I'm not sure where 
different features (columns) disappear to in this step.     
- For each cluster set we have an accompanying indices-of-mins(cIdx) and values-of-mins(dist) matrix.
- We find the average min for each cluster set `avgWithinSS = [sum(d)/X.shape[0] for d in dist]`. This will be used to find the k "elbow" 
(where the improvement from increasing the number of clusters starts to drop off.)

##### Windspeed

- Script was getting stuck at Ouargla as there was no data in my sub-set period.
- Have put an assertion in to warn that a station will be skipped if no data. 
- [Script](windspeed/scripts/039-group_tseries.py) after today.

------------------
####Day 38

##### Python 3

**Ex 3 Pangrams**
- [set()](https://docs.python.org/3/library/stdtypes.html#set) creates class object which you can use to query the unique values in a list. 
   
e.g. `set(list) >= set(other)` or `list.issuperset(other)` : is every element of other found in list? 
     ``
- `s.lower()` is the key to dealing with non-english letters in the line:   
`return len(list(set(letters.lower())))== 26` in my submission [here](tutorials/exercism_py3/pangram/pangram.py).      
Also need `# -*- coding: UTF-8 -*-` at the beginning of the script.    
- use \u to insert a unicode character       
- `re.sub(pattern,repl,string)`       
  `letters = re.sub('[^a-zA-Z]','',s)` to get rid of anything not a letter.   
- My submission was heavily influenced by this [amazingly short 
one](tutorials/exercism_py3/pangram/pangram2.py) which helped me work my solution out.
I started out lots of [unnecessary code](tutorials/exercism_py3/pangram/pangram_detailed.py).

##### SQL

- DELETE FROM tablename : deletes all the records in a table, but the table name and column constraints remain.  
- DROP TABLE tablename : if you want to completely remove the table.
- Now on to [SQL Course 2!](http://www.sqlcourse2.com/) which focuses entirely on the SELECT command.

##### Windspeed

- In the read_file functions of [p3group_tseries](windspeed/scripts/038-group_tseries.py) I've made two small functions to calculate the 
mean over each group, while returning nan if the group has less than 10 obs. Should these small functions (meanf,sdf) be inside or outside 
read_file?
I read in only read_file into the [following notebook](windspeed/notebooks/038-group_tseries.ipynb) and somehow it still accessed meanf and 
sdf.

- One way to drop month from the tuple creating the messy xaxis (see [here](windspeed/plots/038-62124Sebha.png)) is to drop the month level 
from the MultiIndex created when using groupby. droplevel() is one of a [few 
methods](http://pandas.pydata.org/pandas-docs/stable/api.html#multiindex) that can be applied to MultiIndex objects
`wind_group.index = wind_group.index.droplevel(['month'])`   
Now gives an xaxis with just year, [here](windspeed/plots/038-62124Sebha_2.png), though 1995 is missing.

##### Linux

- `eog image.png` in the terminal to quickly view an image. 

##### K-means clustering

- Started K-means analysis [here](tutorials/K-means/038-kmeans_exploredata.ipynb)
- numpy array [attributes](http://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.ndarray.html#array-attributes) 
and [methods](http://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.ndarray.html#array-methods).


------------------
####Day 37

##### SQL

- Practised INSERT INTO and UPDATE into table.

##### Windspeed

- More working in [this notebook](windspeed/notebooks/037-group_stations.ipynb) to plot:      
  - Different time slices from a groupby object.      
  - Several subplots within one figure.         
- Implimented the above in [my script](windspeed/scripts/037-group_tseries.py), trying to use oop. Can't get it to run.

------------------
####Day 36

##### SQL

- `LIKE` is powerful, similar to grep.    
  `SELECT first, city`   
  `FROM empinfo`            
  `WHERE first LIKE 'Er%';`  select from rows first and city in tabel empinfo where the first two letters are Er.
  
- CREATE TABLE: don't forget to fill in the right data type for each column:               
`CREATE TABLE myemps_smc (first varchar(15),last varchar(20),title char(10),age number(2),salary number(8));`

##### Windspeed

- Solved my problem of aggregating grouped columns based on the number of observations going into each group. See working 
[here](windspeed/notebooks/036-group_stations.ipynb) in the last cell.

##### Python 3

- exercism.io: 
  - Ex 2 - Determing if a year is a leap year. [My (revised) answer](tutorials/exercism_py3/leap/year4.py). A [crazy short 
one](tutorials/exercism_py3/leap/year5.py) which passes the test. So many fascinating and different ways to do this. 

##### K-means clustering

- Overview. Used to discover natural groupings in data. An example of "unsupervised" learning where we don't have any original 
classification to "train" the data. [Experimented](tutorials/K-means/Iris_explore.ipynb) with the known groupings of Iris data. 
- K-means can be used to:
  - determine ambiguous terms in a document. Is a Jaguar a car or an animal? What words cluster nearby? What is the whole document about?
  - Initial exploration when training samples are not available.

------------------
####Day 35

##### Git

- To find a particular commit, just add commit/commitnum to the end of your URL i.e.:    
`https://github.com/SophMC/notechain/commit/d61ca5f`

##### Conda python 3 environment

To create a python 3 environment to work on:           
`conda create -n py3 python=3.5 anaconda` : creates an environment named py3, using version 3.5       
`source activate py3` : activates the py3 env            
`source deactivate` : back to old env         
`conda remove -n py3 --all` : remove py3 environment          

##### Python 3

- exercism.io, exercise 1 "Hello World". Not as simple as I initially thought.     
[My answer](tutorials/exercism_py3/hello-world/hello_world.py) was much longer than the two lines that most of the others ([an 
example](tutorials/exercism_py3/hello-world/hello_world2.py)) which made the tests pass but didn't do exactly what [the 
instructions](tutorials/exercism_py3/hello-world/README.md) asked. 

- no longer a dedicated `xrange()` in python 3. `range(start, stop[, step])` does the business.


##### Random Forest - black box method

- `rfc.feature_importances_` gives the relative importance of each feature in the forest. Sum=1.     
- plotting two confusion matrices next to each other using:         
`fig = pl.figure()`    
`fig.add_subplot(121)` : (122) for the second plot. 1x2 grid, 2nd plot.        
`pl.matshow(test_cm,fignum=0)` : fignum=0 was the key point to prevent a new fig being created.

- In the end the black-box model is easier because you don't have to read the documentation or spend any time wrangling the column names.
- It gives greater accuracy/precision but adding domain knowledge allows you to focus in on the relative importance of the features which 
are important to you, depending on you are trying to find out. 
- [Black Box notebook workings](tutorials/Samsung/notebooks/035-Samsung_analysis_blackbox.ipynb).

------------------
####Day 34

##### Random Forests

- Create an instance of the class RandomForestClassifier (rfc). We then have a large number of methods that can be applied.
- RandomForestClassifier fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to 
improve the predictive accuracy and control over-fitting.
- Methods `predict()`, then `score()` - in that order are applied to our object, rfc.
  - `rfc.predict(X)` - takes input samples, X, and returns the predicted class
  - `rfc.score(X,y)` - returns the mean accuracy of predict(X) with respect to y (true labels for X)
- Attributes such as 
  - `oob_score_` - model accuracy estimate
- Two different ways to drop the mystery "unnamed column"
  - `samtrain = samtrain.drop(samtrain.columns[0], axis=1)`
  - `samtrain.drop(samtrain.columns[0], axis=1, inplace=True)`            

All this working is in [this notebook](tutorials/Samsung/notebooks/034-Samsung_analysis.ipynb).
 
##### Windspeed plotting

- Select a column by integer `wind.iloc[:,3]` --> select all rows in 4th column. How can iloc be combined with multiIndex?

##### Python

- To learn Test Driven Development(TDD) I set up the exericsm.io [command line interface](http://exercism.io/cli) so I can [practise python 
problems](http://exercism.io/languages/python) and get feedback on them.  Installing 
[linuxbrew](http://linuxbrew.sh/) seemed the easiest way to get it all set up right. 

-------------------
####Day 33

[Data Tau](http://www.datatau.com/) - Hacker news for data science.

[Good list](https://github.com/ujjwalkarn/DataSciencePython) of Python resources for data science

##### Windspeed plotting

- Can't work out how to apply `map()`, `filter()` or `apply()` to my messy groupby object.    
Instead of `mean` and `std` passed to agg() in the following line:     
`wind_group = group['ws','ws_0','ws_06','ws_12','ws_18'].agg(['mean','std','count'])`    
I want to pass functions in their place which would only assign the mean for the group, if count > 10, otherwise assign nan. 
- The difficulty is navigating the different levels of indices (year and month) and columns (for each of 'ws', 'ws_06'..etc. there is 
another level with mean, std and count. See all this unintelligible working [here](windspeed/notebooks/033-group_stations.ipynb).


##### Random Forests (Samsung data)

- Worked out that the remap_col() function was made by the author - I made accessible copy of the randomforests.py module to 
get the function.     
- Started working with sklearn.ensemble.RandomForestClassifier to build a random forest model. Will upload the workbook when it is finished 
tomorrow.


##### SQL 

-CREATE INDEX speeds up finding values in a table.     
Syntax: `CREATE INDEX index_name ON table_name (column_name)(or col1,col2,col3)`    
  `CREATE UNIQUE INDEX` to create a unique index on the table

- Go through [this tutorial](http://www.sqlcourse.com/) and do the exercises. There is also an [more advanced 
one](http://www.sqlcourse2.com/), which I have covered some material from. 


-------------------
####Day 32

[DataKind](http://www.datakind.org/) looks like a good place to find an interesting project to work on. 


##### SQL - Qu 19

- `CREATE TRIGGER name when event ON tablename action`. Another way of enforcing integrity (similar to constraints).
- In theory my Qu 19 solution should work, but it doesn't. I checked with the author and he says there may be a bug. Investigate 
tomorrow.

##### Random Forests

*data cleaning*

- I *can* access samtrain.csv etc...from github. Not sure it is possible to get it into the correct format with the 
information in the tutorial.
- Tomorrow email author and continue with the analysis now I have correctly formatted data.

##### Windspeed plotting

- getting my head around `map()` and `filter()` and using lambda to make functions in them. Still can't get these things to work with 
grouped dataframes though. 

-------------------
####Day 31

[CrowdFlower](https://www.crowdflower.com/)
Sentiment analysis which encorporates human intelligence to identify nuances in the sentiment of text.    
Used as a benchmark by MonkeyLearn to [evaluate their 
performance](https://blog.monkeylearn.com/sentiment-analysis-apis-benchmark/?utm_source=Email&utm_medium=Intercom&utm_content=FP&
utm_campaign=22-sentiment-analysis-benchmark) against other platforms such as MetaMind, AlchemyAPI, Aylien, Idol and Datumbox

##### SQL - Qu 18

- UNION: Combines queries, discards duplicates.   
- UNION ALL: Same as UNION, keeps duplicates.     
- INTERSECT: Only returns rows which match.   
- EXCEPT: performs set subtraction (those which don't match the SELECT statement).

#### Random Forests

*Data cleaning*

- [Final go](tutorials/Samsung/notebooks/031-Samsung_cleanup.ipynb) at reducing variables to the list in the tutorial. 

#### Windspeed plotting

- [My failed attempts](windspeed/notebooks/031-group_stations.ipynb) to create a grouped dataFrame where counts less than 10 are turned 
into Nans, without a loop. Will just do it will a loop tomorrow. 

-------------------

####Day 30

##### Random Forests

*Data cleaning*

- Stick to `df.replace` and `df.contains` for dataFrames, as opposed to python `re` module, which would need loops.
- Worked out how to search for two different words within one string:
  
    `df[df.name.str.contains('Body.*Mag')]`

- Almost there with [this workbook](tutorials/Samsung/notebooks/030-Samsung_cleanup.ipynb) - have changed strings and dropped rows with 
certain expressions. There is still work to do as my list of remaining names is not the same as that 
[here]
(http://nbviewer.jupyter.org/github/nborwankar/LearnDataScience/blob/master/notebooks/C2.%20Random%20Forests%20-%20Data%20Exploration.ipynb) 
in the tutorial.

##### SQL

- I got Qu 17 to work with [my own solution](SQL/galaXQL_17.sql)!
- Practised using GROUP BY, INNER and LEFT OUTER JOIN and understand them much better. 

##### Windspeed plotting

- Got the first function of [my .py script](windspeed/scripts/030-group_tseries.py) working (read_file) so that I can access it in [jupyter 
notebook](windspeed/notebooks/030-group_stations.ipynb).

##### General Python

- To add a path to a directory with modules that you want to call on:

`import sys`     
`sys.path.append("path/to/Modules")`        
`print sys.path`
   
It's better to have fewer of these though, and store most of your modules in the same place. 

- STUCK - if I restart the Jupyter kernel (which I think I have to do everytime I update the module group_tseries) then it no longer 
finds the module

-------------------

####Day 29 

##### Random Forests 

*Theory*

- Out of Bag (oob) error: Using the subset that is left out of the bootstrapping sampling to test the decision trees (models). As accurate 
as using a test set the same size as the training set.

*[Data cleaning](tutorials/Samsung/notebooks/029-Samsung_cleanup.ipynb)*

- Did some initial search and replace in Kate of [this list](tutorials/Samsung/data/features_copy.txt) of 
variable names
- Removed duplicate columns using df.drop_duplicates().
- Removed "()", "-" and numbers from the list of names.

##### SQL

- ALTER TABLE tablename alteration(RENAME TO, ADD COLUMN, RENAME COLUMN TO, MODIFY COLUMN, DROP COLUMN)
- Show the columns in a table:
  - SQLlite - PRAGMA table_info(tablename)
  - MySQL - SELECT * tablename.INFORMATION_SCHEMA.COLUMNS (There is a long list of other things that can be queried other than COLUMNS)
- GROUP BY and HAVING (an equivalent to WHERE, applied to the grouped data) (Ex 17)
- Couldn't do Qu 17 myself - must learn and understand the solution (copied!)
 

--------------------
####Day 28

##### SQL 

- CREATE TABLE tablename(columnname datatype constraints). (Qu 14)
- constraints: PRIMARY KEY, NOT NULL, UNIQUE, FOREIGN KEY, CHECK
- To fill the table: INSERT INTO tablename(column1,column2) VALUES(column1value, column2value). (Qu 15)

##### Random Forests 

*Theory*

- **Classification**: Task of assigning objects to one of several pre-defined categories.   
- **Bootstrapping**: Random sampling WITH replacements. Repeatedly sampling from the same sample.    
- **Bootstrap Aggregation (Bagging)**: Each model in an ensemble has an equal weight. Each model is built in parallel. Example: Random 
Forest.   
- **Boosting**: Can be better than Bagging. Models are built sequentially and learn where previous models were strong/weak and weight them 
accordingly. Example: AdaBoost

--------------------
####Day 27

##### Markdown

- use \$a_2$\ to create maths symbols $a_2$
- [Guide](https://en.wikibooks.org/wiki/LaTeX/Mathematics) for writing equations in Tex.

##### Lending Club Linear Regression

- Finished [the workbook](tutorials/026-Linear_Regression_Analysis.ipynb). Didn't show how to make predictions using the model.

##### Lending Club Logistical Regression

- Using the Log Function to predict the probability that score x will lead to a win.
- Log Function = Logit function combined with Linear Model.    
  1) Work out the coefficients for multivariate linear regression    
  2) Plug the variables(we want to query) and coefficients(worked out in step 1) into Z(equation of a straight line)     
  3) Calculate the probability of Z using p(Z) = 1 \ 1+ e^(Z)       
- Plotted how probability varies with Loan amount and FICO score (changing the colour/symbols). See 
[here](tutorials/027-Logistical_regression.ipynb)


--------------------

####Day 26

##### SQL [tutorial](http://sol.gfxile.net/g3/)

- INNER JOIN, OUTER JOIN (Qu12)
- CREATE VIEW (Qu13)

##### Lending Club Linear Regression 

- Modelling Interest rate as a function of Loan Amount and FICO Score. Steps:
  - Put the pandas columns into seperate variables. Turn these into 2D arrays and into columns eg `x1=np.matrix(fico).T`
  - Put the two idependent vars into a stacked 2D array `x = np.column_stack([x1,x2])`
  - Add a constant (a column on 1s) to x:  `X = sm.add_constant(x)`. X is now x.
  - Create an ordinary least squarts model with `model = sm.OLS(y,X)`, y=response, X=independents+constant
  - Apply a fitting method to the model. `f = model.fit()`
    - There is now a list of attributes to f, such as `f.params`(coefficients), `f.pvalues`
    
Full notes and working [here](tutorials/026-Linear_Regression_Analysis.ipynb).



--------------------
####Day 25

##### SQL [tutorial](http://sol.gfxile.net/g3/)

- Best to use transations (BEGIN; ROLLBACK) when using UPDATE or DELETE
- COALESCE(value1,value2,value3) returns the first non-NULL value in a list
- Using UPDATE with WHERE to only update columns if they meet a criteria
- Can't get my head around the query:     
  `SELECT COUNT() FROM stars, (SELECT AVG(intensity) AS ai2 FROM stars, (SELECT AVG(intensity) AS ai FROM stars) WHERE intensity > ai) WHERE 
intensity > ai2` --> count the stars that have higher than average intensity of only those stars that have higher than average intensity.

##### Indexing tutorial

- Using `isin()` together with `all()` to select particular values from particular columns in a DataFrame.
- Using `where()` to select values, change them inplace and change them with values from other columns.

##### Windspeed groups

- `type(obj)`  to find the object type.
- Improved the code by adding the 06,12 etc values to the wind dataframe, then grouping them all at the same time. 
`wind['ws_06']= wind['ws'][wind['hour'].isin([6])]`     
`group = wind.groupby(['year','month'])`        
`wind_group = group['ws','ws_0','ws_06','ws_12','ws_18'].aggregate([np.mean,np.std])`        
Now these will be much easier to plot against each other. Can even use a loop to do it. 

#### Todo list

- [These are](TOdo.md) the learning resources I am in the process of working through. This is the very minimum I would 
like to get through in the next couple of months!

--------------------
####Day 24

##### SQL [tutorial](http://sol.gfxile.net/g3/)

- Must use brackets around a query using OR.      
  `SELECT * FROM stars WHERE starid>1000 AND starid <2000 AND (class=0 OR class=1)`
- `<>` for NOT.    
- `ORDER BY ..` for ascending `ORDER BY .. DESC for descending`
- BEGIN;..queries...ROLLBACK to "undo"
- INSERT INTO .. with SELECT..

##### Indexing tutorial

- `list('abcdef')` splits up the string into a,b,c,d,e,f. Good to remember! 
- selecting from df using lambda function 
  - `criterion = df2['a'].map(lambda x: x.startswith('t'))`   
    `df2[criterion]`
    
##### Windspeed group plots

- nearly broken the back of this, hope to complete tomorrow.

--------------------
####Day 23

##### SQL

- Using REGEXP(RLIKE) to find patterns. Using ^ and $ to specify beginning and end.
- '[abd]' finds any values which have a, b or d in them. '[0-9]' to find a number.
- Going to do [this](http://sol.gfxile.net/g3/) tutorial from now on.

##### Index tutorial

- Working through the Pandas [basics of indexing](http://pandas.pydata.org/pandas-docs/stable/indexing.html). Need to get a good grounding 
in this. Notebook found [here](tutorials/023-indexing.ipynb).

##### Windspeed group plots

- Working on a script which produces a panel of plots for a group of stations in one output file. 


--------------------
####Day 22

#####boxplot with width = counts

My annotated working through a tutorial [here](tutorials/022-boxplot_counts.ipynb).

Applied to a subsection of windspeed data [here](windspeed/notebooks/022-windspeed.ipynb).
  - used `ax.set_xticklabels()` to add a counts label to each tick.     
  - splitting up tuples to get counts `counts = [len(v) for k,v in windg]` where windg = grouped object 

#####datetime

- pd.to_datetime and datetime both need year, month and day. I don't think it is possible to just do with year and month.

#####SQL
- You can extract parts of a date from a column (type=date) using functions YEAR(), MONTH() and DAYOFMONTH()
- An empty string in a cell IS NOT NULL. so " " IS NOT NULL = 1 (true)
- Use LIKE instead of = and NOT LIKE instead of !=
- Find names with a w in table pet: `SELECT * FROM pet WHERE name LIKE '%w%';`
  - % is like * or `wildcard`
- Find something with 5 characters; '_____' (5 _ underscores)

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

Workings [here](windspeed/notebooks/020-windspeed.ipynb)

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
[here](LendingClub/004-LendingClub.ipynb):  

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
Started [plotting the data](LendingClub/004-LendingClub.ipynb) with  
`df.plot(kind = 'box'), df.hist() and scatter_matrix(df)`

To suppress the printing of the object before a panel of plots
`_ = df.hist()` etc.


--------------

####Day 3  
%timeit : time how long a command takes to run.  
More pandas practise [here](LendingClub/003-LendingClub.ipynb).   
`df.dropna(), df.isnull(), df.any(), df.sum()`

--------------


####Day 2                                                                       
More pandas practise [here](LendingClub/002-LendingClub.ipynb). 
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


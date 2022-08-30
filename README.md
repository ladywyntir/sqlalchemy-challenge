# sqlalchemy-challenge
Module 10 Challenge - SURFS UP

Please note the folders are categorized as they seem.  
* **Images** holds all images for this readme.
* **Resources** holds the source files
* **SurfsUp** holds the Jupyter Notebook and the Python file for Flask to run.
___
## Instructions
![Image](https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/surfs-up.png) 

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

### Part 1: climate_analysis.ipynb

#### Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

1. Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.
2. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
3. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

___

#### Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame, and set the index to the "date" column.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/precipitation.png" width="600"/>
                                                                                                           
                                                                                                           
7. Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
    * List the stations and observation counts in descending order.
    * Answer the following question: which station id has the greatest number of observations?
    * Using the most-active station id, calculate the lowest, highest, and average temperatures.
3. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
    * Filter by the station that has the greatest number of observations.
    * Query the previous 12 months of TOBS data for that station.
    * Plot the results as a histogram with bins=12, as the following image shows:

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/station-histogram.png" width="600"/>

4. Close your session.

___

### Part 2: Design Your Climate App  (climate_app.py)
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. `/`
    * Start at the homepage.
    * List all the available routes.

2. `/api/v1.0/precipitation`
    * Convert the query results to a dictionary by using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.

3. `/api/v1.0/stations`
    * Return a JSON list of stations from the dataset.

4. `/api/v1.0/tobs`
    * Query the dates and temperature observations of the most-active station for the previous year of data.
    * Return a JSON list of temperature observations for the previous year.

5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

___

## Code Theory

**climate_analysis.ipynb**
1. Checked the csv files to get all the header names. 
2. Declared and imported needed dependencies.
3. Pointed to the sqlite file to later pull the information from there into Jupyter Notebook.
4. Created a new database model to save the info pulled.
5. Found the classes that were automapped and added their references: measurement & station.
6. Created a session to link to from Python to the database.
7. Worked on the Precipitation Analysis:
    1. Separated the date up into year/month/day
    2. Using the datetime class I took the delta between the recent date and 1 year ago (had to use 366 days to go from date to date).
    3. Plotted the data on a chart.
   
    <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climate_analysis_precip_bar.png" width="600"/>
    
8. Worked on the Exploratory Analysis:
    1. Used the tride and true count() function for the # of stations.
    2. Found lowest, highest and average temps.
    3. Using a dataframe, I was able to plot a histogram
    <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climate_analysis_tobs_bar.png" width="600"/>
    
9. Closed the session.



**app.py**
1. Took a lot of code from the original Jupyter Notebook :)
2. First I set up the engine, the classes, and opened a session. (the session could have also been opened by each definition clause, but I was doing a bit of experimenting.)
3. Next had to define the Flask app.
4. Then I had to remember how to initiate Flask:
    1. Git Bash to the folder where the Flask file has been saved. (For me it was in the SurfsUp folder)
    2. Type in "flask run"
    3. Note the IP address that's given with the port number and copy it.
    4. Paste that into an Internet browser and that's your homepage.
    5. I realized that I was not able to make changes to my code and see those changes if I already had a Flask session running.  So I tried to make as efficient changes as I could then restarted the sessions.  Lots of ctrl+c and then flask run.
5. Once I was connected successfully, I began working on the routes menu: home (/), precipitation, stations, tobs, temp start and temp start-end.
6. Then came the definitions for each route. 
    * Precipitation was pretty straight forward as we already had an end date from the previous exercise. 
    * Stations gave me some trouble as I had to use a list instead of a dictionary.  Imagine my facepalm moment when I realized I didn't have my numpy statement at the beginning of the code correct. Once i fixed `import numpy as numpy` to `import numpy as np` you can imagine my joy it was finally working.
    * TOBS was similar to Stations with the numpy statement. And I believe I had to correct the capitalization of `ourStation` to ensure it matched the rest of the code.
    * the Start and End gave me the largest headache.
        1. I wasn't sure of the start and end values at first.  It took me some time, and some research, to understand those placeholders were for the user of the app to actually insert dates into the URL. 
        2. I didn't know that a null value when the URL just had Start or End was a correct value, again until I did some research.
        3. I am also worried that I didn't fully understand the use of the `TMIN`, `TAVG` and `TMAX` functions that were given in the directions. I know they're a part of scipy.stats but when I attempted to add them, I just got error messages that the `TMIN`, etc. weren't defined.
___
### Results

I was able to run the Flask app, check the provided routes and have saved a copy of my results here:
* Home Page:

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-home.png" />

___
* Precipitation :

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-precip.png" />
___
* Stations:

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-stations.png" />
     
 ___
* TOBS

   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-temps.png" />
___
* Start:

   With empty date: <br/>
   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-start-null.png" /> 

   With a specific date: <br/>
   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-start-date.png" />
___
* Start-End

   With empty dates: <br/>
   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-startend-null.png" /> 

   With specific dates:<br/>
   <img src="https://github.com/ladywyntir/sqlalchemy-challenge/blob/main/Images/climateapp-startend-dates.png" />

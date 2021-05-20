# SQLAlchemy: Precipitation and Climate Analysis

## SQLAlchemy Database Exploration
For this project I was required to do a climate analysis on a popular vacation destination. I had to analyze a .sqlite database of recorded temperature observations and plan a vacation time accordingly. Using Pythons object oriented database library SQLAlchemy, I performed the analysis and explored the data in the suplied climate database. Along with SQLAlchemy, all analysis was completed using ORM queries, Pandas, and Matplotlib.

### Task 1: Connect to Database
To begin this project I first needed to create a Jupyter Notebook and establish a connection to the database. This notebook would be the same notebook that Precipitation Analysis and Stations Analysis would be completed in. The steps that I followed to connect to the database are as follows. 
* Create a Jupyter Notebook, load module libraries and define database location
* Use SQLAlchemy create_engine to connect to the sqlite database
* Use SQLAlchemy automap_base() variable to reflect tables and identify classes called Station and Measurement
* Identify database column names
* Identify database format
* Link Python to the database by creating an SQLAlchemy session

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task1Capture.JPG?raw=true">
</p>

### Task 2: Conduct Precipitation Analysis
Now that I was connected to the database via SQLAlchemy, I could begin to conduct my precipitation analysis. In order to do this I had to perform multiple specific queries within the Measurement class. In order to achieve this I used the datetime, pandas, matplotlib and alchemy libraries. The steps that I took to conduct the precipitation analysis are as follows.
* Find the most recent date in the data set
* Use most recent date and retrieve previous 12 months of precipitation data through query
* Select only the date and prcp values
* Load results into a Pandas DataFrame and set index to date column
* Sort DataFrame by date
* Print the summary statistics for the precipitation data

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task2aCapture.JPG?raw=true">
</p>

* Plot the results using the DataFrame plot method

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task2bCapture.JPG?raw=true">
</p>

### Task 3: Conduct Stations Analysis
Similar

* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations (i.e. which stations have the most rows?).
* List the stations and observation counts in descending order.
* Which station id has the highest number of observations?
* Using the most active station id, calculate the lowest, highest, and average temperature.

Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filter by the station with the highest number of observations.
* Query the last 12 months of temperature observation data for this station.
* Plot the results as a histogram with bins=12.
* Close out your session.

<p align="center">
    <img width="700" alt="level1" src="https://github.com/mathewqpmiller/Tableau-CitBikeAnalysis/blob/main/Resources/Images/AggregateData2.JPG?raw=true">
</p>

### Task 4 - Create Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

Routes
/
Home page.

List all routes that are available.

/api/v1.0/precipitation

Convert the query results to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations

Return a JSON list of stations from the dataset.

/api/v1.0/tobs

Query the dates and temperature observations of the most active station for the last year of data.

Return a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

Hints

You will need to join the station and measurement tables for some of the queries.

Use Flask jsonify to convert your API data into a valid JSON response object.

#
#
<p align="center">
UNIVERSITY OF OREGON: Data Analytics Boot Camp - Repository for project 8(SQLAlchemy Challenge)
</p>
<p align="center">
Mathew Miller © 2021. All Rights Reserved.
</p>

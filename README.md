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
Similar to the precipitation analysis, I now had to answer multiple specific queries about the Stations class within the database. For this section of the project I utilized the pandas, matplotlib and sqlalchemy libraries. The steps that I took to complete this section are as follows.
* Design a query to calculate the total number of stations in the dataset
* Design a query to find the most active stations (i.e. which stations have the most rows?)
* List the stations and observation counts in descending order
* Identify which station id has the highest number of observations
* Use func.min, .max, .avg and .count to calculate the lowest, highest, and average temperature of the most active station

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task3aCapture.JPG?raw=true">
</p>

* Query the last 12 months of temperature observation data
* Filter the list by the station with the most observations
* Query the last 12 months of temperature observation data for this station
* Plot the results as a histogram with twelve bins

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task3bCapture.JPG?raw=true">
</p>

### Task 4 - Create Climate App
With the initial Measurements and Stations analysis completed, I now had to design a Flask API app that would return jsonified datasets of the results. I had to create a seperate python file to achieve this task. Within the python file I used the same libraries as before but I also added the flask app library to convert the data in to .JSON format. The steps that I took to complete this section are as follows.
* Load Modules
* Define routes
* Convert Jupyter Notebook queries using date as key and precipitation as value
* Return a JSON representation of the precipitation dictionary
* Return a JSON list of the stations in the dataset
* Query the last years dates and temperature observations of the most active station
* Return a JSON list of temperature observations
* Return a JSON list of the minimum, average and maximum temperature of a specified start and end date 
* Create a for loop that calculates the TMIN, TAVG, and TMAX for dates between the start and end date inclusive

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task4aCapture.JPG?raw=true">
</p>

* Precipitation jsonified returned results

<p align="center">
    <img width="600" alt="level1" src="https://github.com/mathewqpmiller/SQLAlchemy-ClimateAnalysis/blob/main/Resources/Images/Task4bCapture.JPG?raw=true">
</p>

#
#
<p align="center">
UNIVERSITY OF OREGON: Data Analytics Boot Camp - Repository for project 8(SQLAlchemy Challenge)
</p>
<p align="center">
Mathew Miller © 2021. All Rights Reserved.
</p>

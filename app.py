# Engineer Climate App

# Now that I have finished my precipitation and weather stations analysis, I must now use FLASK to engineer an API based on 
# the queries that I have just executed.

# Load Modules

# Customizable style sheets and parameters for matplotlib
from matplotlib import style
style.use('fivethirtyeight')
# Plot generator for bar, pie, line, scatter, box and other plots
import matplotlib.pyplot as plt
# High-level math and basic algebra computing tool
import numpy as np
# Dataframe generator that prints out various types of datasets
import pandas as pd
# Date and time attributes such as year, month, day, hour, minute, second 
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
# Load flask function that serializes data to Java Open Script Notation format 
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Define file path and create engine
sqlite_file_path = "Resources/hawaii.sqlite"
sqlite_engine = create_engine(f"sqlite:///{sqlite_file_path}")

# Reflect tables, detect and define classes
base = automap_base()
base.prepare(sqlite_engine, reflect=True)
Measurement = base.classes.measurement
Station = base.classes.station

#################################################
# Flask Setup
#################################################

# Start session and initiate Flask
session = Session(sqlite_engine)
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Identify All Possible Flask App Routes
@app.route("/")
def main():

        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    

@app.route("/api/v1.0/precipitation")
def precipitation():

    print("Received precipitation api request.")

    # Find the most recent date in the data set.
    latest_dataset_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_dataset_date_print = dt.date(2017,8,23)
    
    # Define variable that finds the date one year ago to the day from the most recent date in the dataset
    last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Define variable that represents the query of the last 12 months of Percipitation data
    last_years_precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= last_year).\
    order_by(Measurement.date).all()
    
    # prepare the dictionary with the date as the key and the prcp value as the value
    results_dict = {}
    for result in last_years_precipitation_data:
        results_dict[result[0]] = result[1]

    return jsonify(results_dict)

@app.route("/api/v1.0/stations")
def stations():

    print("Received station api request.")

    # Define variable that calculates the total number weather stations in the dataset
    total_weather_stations = session.query(Measurement.station).distinct().count()

    # Create the stations list of dictionaries
    stations_list = []
    for station in total_weather_stations:
        station_dict = {}
        station_dict["id"] = station.id
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        station_dict["latitude"] = station.latitude
        station_dict["longitude"] = station.longitude
        station_dict["elevation"] = station.elevation
        stations_list.append(station_dict)

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
 
    print("Received tobs api request.")

    # Find the most recent date in the data set.
    latest_dataset_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_dataset_date_print = dt.date(2017,8,23)
    
    # Define variable that finds the date one year ago to the day from the most recent date in the dataset
    last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    # With the most live station id, query the last 12 months of temperature observations (tobs) 
    temperature_observations = session.query(Measurement.tobs).\
                filter(Measurement.date >= last_year).\
                filter(Measurement.station == "USC00519281").\
                order_by(Measurement.date).all()

    # Create the tobs list of dictionaries
    tobs_list = []
    for result in temperature_observations:
        tobs_dict = {}
        tobs_dict["date"] = result.date
        tobs_dict["station"] = result.station
        tobs_dict["tobs"] = result.tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):
    
    print("Received start date api request.")

    # Find the most recent date in the data set.
    latest_dataset_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_dataset_date_print = dt.date(2017,8,23)

    # Define variable that calculates the minimum, maximum and average temperature from the Measurements class.
    temp_stats = [func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)]

    # Create temperature stats list
    return_list = []
    date_dict = {'start_date': start, 'end_date': latest_dataset_date}
    return_list.append(date_dict)
    return_list.append({'Observation': 'TMIN', 'Temperature': temps[0][0]})
    return_list.append({'Observation': 'TAVG', 'Temperature': temps[0][1]})
    return_list.append({'Observation': 'TMAX', 'Temperature': temps[0][2]})

    return jsonify(return_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
  
    print("Received start date and end date api request.")

    # Find the most recent date in the data set.
    latest_dataset_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_dataset_date_print = dt.date(2017,8,23)
    
    # Define variable that finds the date one year ago to the day from the most recent date in the dataset
    last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Define variable that calculates the minimum, maximum and average temperature from the Measurements class.
    temp_stats = [func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)]
    
    #create a list
    return_list = []
    date_dict = {'start_date': last_year, 'end_date': latest_dataset_date}
    return_list.append(date_dict)
    return_list.append({'Observation': 'TMIN', 'Temperature': temps[0][0]})
    return_list.append({'Observation': 'TAVG', 'Temperature': temps[0][1]})
    return_list.append({'Observation': 'TMAX', 'Temperature': temps[0][2]})

    return jsonify(return_list)

#code to actually run
if __name__ == "__main__":
    app.run(debug = True)
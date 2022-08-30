# import dependencies

import datetime as dt
import numpy as np
import pandas as pd 
from scipy import stats


# import app

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


# access the SQLite database
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# set up the classes
Base = automap_base()
Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station 

# open session for Python to the database
ourSession = Session(engine)

# define the Flask app
app = Flask(__name__)

# welcome route aka home page
@app.route("/")

# display of routes available 
def welcome():
    return(
        '''
        Welcome to my API for Climate Analysis! <br/><br/>
        Here are the available routes. Please copy and paste after the URL above: <br/><br/>
        /api/v1.0/precipitation <br/>
        /api/v1.0/stations <br/>
        /api/v1.0/tobs <br/>
        /api/v1.0/temp/start <br/>
        /api/v1.0/temp/start/end

        ''')


# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = ourSession.query(Measurement.date, Measurement.prcp) .\
        filter(Measurement.date >= previous_year).all()
    precip_dict = {date: prcp for date, prcp in precipitation}
    ourSession.close()
    return jsonify(precipitation=precip_dict)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = ourSession.query(Station.station).all()
    stations_list = list(np.ravel(results))
    ourSession.close()
    return jsonify(stations=stations_list)


# Temp Observations Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = ourSession.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previous_year).all()
    temperatures = list(np.ravel(results))
    ourSession.close()
    return jsonify(temperatures=temperatures)

# Statistics Route
# get the start and end date routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def date_stats(start=None,end=None):

    # query for MIN, MAX and AVG
    math_stats = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    # if there is no end date, calculate the following:
    if not end:
        agg_data = ourSession.query(*math_stats).\
            filter(Measurement.date >= start).all()
        date_stats = list(np.ravel(agg_data))
        ourSession.close()
        return jsonify(Min_Max_Avg_Temp=date_stats)

    # else calculate with a start and end date
    agg_data = ourSession.query(*math_stats).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    date_stats = list(np.ravel(agg_data))
    ourSession.close()
    return jsonify(Min_Max_Avg_Temp=date_stats)

    # note: the start and end keywords will behave like variables. A null value will return as a
    # result. A date will have to be submitted in the YYYY-MM-DD format in the URL to get a 
    # calculation.  Examples have been provided in the readme.md

    

    if __name__ == '__main__':
        app.run(debug=True)

    


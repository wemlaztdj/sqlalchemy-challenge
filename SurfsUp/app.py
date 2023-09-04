# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Start at the homepage.

# List all the available routes.
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    # all_names = list(np.ravel(results))

    return 


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    mostActive= session.query(Measurement.station).\
    group_by(Measurement.station).\
    all()
    # mostActive

    session.close()

    return jsonify(list(np.ravel(mostActive)))


@app.route("/api/v1.0/tobs")
def tobs():
    mostActive= session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by((func.count(Measurement.station)).desc()).\
    all()

    activestationid=mostActive[0][0]
    last_date = session.query(Measurement.date).\
    filter(Measurement.station == activestationid).\
    order_by(Measurement.date.desc()).\
    first()
    # last_date[0]

    datelast_date=dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    year_agoMA = dt.date(year=datelast_date.year - 1, month=datelast_date.month, day=datelast_date.day)
    # year_agoMA

    temperature = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == activestationid).\
    filter(Measurement.date >= year_agoMA).\
    all()
    # temperature

    session.close()
    # need to change something
    return jsonify(dict(np.ravel(temperature)))



@app.route("/api/v1.0/<start>")
def start():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    # """Return a list of all passenger names"""
    # # Query all passengers
    # results = session.query(Passenger.name).all()

    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    return 
@app.route("/api/v1.0/<start>/<end>")
def startend():
    # # Create our session (link) from Python to the DB
    # session = Session(engine)

    # """Return a list of all passenger names"""
    # # Query all passengers
    # results = session.query(Passenger.name).all()

    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    return




if __name__ == '__main__':
    app.run(debug=True)

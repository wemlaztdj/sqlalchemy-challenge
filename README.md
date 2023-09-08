# sqlalchemy-challenge
a climate analysis of Hawaii

## Analyze and Explore the Climate Data
Precipitation Over the Last Year

![1](https://github.com/wemlaztdj/sqlalchemy-challenge/assets/19890554/fafc32dc-6fee-4455-ac15-ad290cb57f81)



last 12 months of temperature

![2](https://github.com/wemlaztdj/sqlalchemy-challenge/assets/19890554/17e04143-4ef5-47f3-8acb-b80dbd5c3acd)


## Design Climate App

/: List all routes.

/api/v1.0/precipitation: Return last year's precipitation data as JSON.

/api/v1.0/stations: Return a list of stations as JSON.

/api/v1.0/tobs: Return the temperature observations of the most active station for the last year as JSON.

/api/v1.0/<start> and /api/v1.0/<start>/<end>: Return a JSON list of minimum, average, and maximum temperatures for a given start or start-end range.

For example, "/api/v1.0/2016-6-15/2016-6-20". The date has to be in "%Y-%m-%d" format.

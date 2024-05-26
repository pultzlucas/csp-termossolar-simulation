# Libraries 
import pandas as pd
from pvlib.location import Location

import pvlib
import pytz

# for t in pytz.all_timezones:
#     print(t)

# Definition of Location oject. Coordinates and elevation of Madrid Ciemat Headquarters (Spain)
site = Location(-22.170811, -47.393904, 'Brazil/East', 619, 'MyHouse') # latitude, longitude, time_zone, altitude, name

# Definition of a time range of simulation
times = pd.date_range('2023-12-30 12:00:00', '2023-12-30 19:00:00', freq='H', tz=site.tz)

# Estimate Solar Position with the 'Location' object
solpos = site.get_solarposition(times)

print(solpos)
# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2014, 1, 1)
end = datetime(2021, 12, 31)

# Create Point for Wandersleben
wandersleben = Point(50.897598, 10.853470, 70)

# Get daily data from 2014 until 2021
data = Daily(wandersleben, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tsun'])
plt.show()



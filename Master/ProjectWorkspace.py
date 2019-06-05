cities = {'CA': ['San Diego', 'San Francisco', 'Los Angeles'], 'WA': ['Seattle'], 'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['New York'], 'IL': ['Chicago'], 'MI': ['Detroit'],
          'GA': ['Atlanta'], 'FL': ['Miami', 'Orlando'], 'AZ': ['Phoenix'], 'PA': ['Philadelphia', 'Pittsburgh'], 'WI': ['Milwaukee', 'Madison'], 'CO': ['Denver'], 'NV': ['Las Vegas'], 'UT': ['Salt Lake City'], 'MA': ['Boston'], 'DC': ['Washington, DC'], 'HI': ['Honolulu'], 'MN': ['Minneapolis']}
bokeh_counties = {'CA': ['San Diego County, California', 'San Francisco County, California', 'Los Angeles County, California'], 'WA': ['King County, Washington'], 'TX': ['Austin County, Texas', 'Houston County, Texas', 'Dallas County, Texas'], 'NY': ['New York County, New York'], 'IL': ['Cook County, Illinois'], 'MI': ['Wayne County, Michigan'],
                  'GA': ['Fulton County, Georgia'], 'FL': ['Miami-Dade County, Florida', 'Orange County, Florida'], 'AZ': ['Maricopa County, Arizona'], 'PA': ['Philadelphia County, Pennsylvania', 'Allegheny County, Pennsylvania'], 'WI': ['Milwaukee County, Wisconsin', 'Dane County, Wisconsin'], 'CO': ['Denver County, Colorado'], 'NV': ['Clark County, Nevada'], 'UT': ['Salt Lake County, Utah'], 'MA': ['Suffolk County, Massachusetts'], 'DC': ['District of Columbia, District of Columbia'], 'HI': ['Honolulu County, Hawaii'], 'MN': ['Hennepin County, Minnesota']}
bokeh_counties_xs = {'CA': [-117.1625, -122.42905, -118.24532], 'WA': [-122.32945], 'TX': [-97.74299, -95.36978, -96.7954], 'NY': [-75.6107], 'IL': [-87.623177], 'MI': [-83.045753], 'GA': [-84.386330], 'FL': [-80.191788, -81.379234],
                     'AZ': [-112.074036], 'PA': [-75.165222, -79.995888], 'WI': [-87.906471, -89.401230], 'CO': [-104.991531], 'NV': [-115.172813], 'UT': [-111.876183], 'MA': [-71.057083], 'DC': [-77.03196], 'HI': [-157.858093], 'MN': [-93.258133]}
bokeh_counties_ys = {'CA': [32.715, 37.77986, 34.05349], 'WA': [47.60357], 'TX': [30.26759, 29.76045, 32.77815], 'NY': [42.937084], 'IL': [41.881832], 'MI': [42.331429],
                     'GA': [33.753746], 'FL': [25.761681, 28.538336], 'AZ': [33.448376], 'PA': [39.952583, 40.440624], 'WI': [43.038902, 43.073051], 'CO': [39.742043], 'NV': [36.114647], 'UT': [40.758701], 'MA': [42.361145], 'DC': [38.89037], 'HI': [21.315603], 'MN': [44.986656]}
col_index = [1, 2, 4, 6, 8, 10, 12]
# Column indices for US county data
col_index2 = [1, 3, 5, 7, 9, 11, 13]
# Column indices for old US county data
col_index_names = ['Urban Population', 'Vehicles in Service', 'Vehicles Available',
                   'Vehicle Revenue Miles', 'Vehicle Revenue Hours', 'Unlinked Passenger Trips', 'Passenger Miles']
col_index_names1000 = ['Urban Population', 'Vehicles in Service (per 1000 persons)', 'Vehicles Available (per 1000 persons)',
                       'Vehicle Revenue Miles (per 1000 persons)', 'Vehicle Revenue Hours (per 1000 persons)', 'Unlinked Passenger Trips (per 1000 persons)', 'Passenger Miles (per 1000 persons)']
col_index_names_p = ['Urban Population', 'Vehicles in Service (per person)', 'Vehicles Available (per person)',
                     'Vehicle Revenue Miles (per person)', 'Vehicle Revenue Hours (per person)', 'Unlinked Passenger Trips (per person)', 'Passenger Miles (per person)']
states_fips = {'California': 6, 'Washington': 53, 'Texas': 48, 'New York': 36, 'Illinois': 17, 'Michigan': 26,
               'Georgia': 13, 'Florida': 12, 'Arizona': 4, 'Pennsylvania': 42, 'Wisconsin': 55, 'Colorado': 8, 'Nevada': 32, 'Utah': 49, 'Massachusetts': 25, 'Washington, DC': 11001, 'Hawaii': 15, 'Minnesota': 27}
cities_fips = {'California': ['06073', '06075', '06037'], 'Washington': ['53033'], 'Texas': ['48015', '48225', '48113'], 'New York': ['36061'], 'Illinois': ['17031'], 'Michigan': ['26163'],
               'Georgia': ['13121'], 'Florida': ['18103', '12095'], 'Arizona': ['04013'], 'Pennsylvania': ['42101', '42003'], 'Wisconsin': ['55079', '55087'], 'Colorado': ['08031'], 'Nevada': ['32033'], 'Utah': ['49035'], 'Massachusetts': ['25025'], 'Washington, DC': ['11001'], 'Hawaii': ['15003'], 'Minnesota': ['27053']}

cities = {'CA': ['San Diego', 'San Francisco', 'Los Angeles'], 'WA': ['Seattle'], 'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['New York'], 'IL': ['Chicago'], 'MI': ['Detroit'],
          'GA': ['Atlanta'], 'FL': ['Miami', 'Orlando'], 'AZ': ['Phoenix'], 'PA': ['Philadelphia', 'Pittsburgh'], 'WI': ['Milwaukee', 'Madison'], 'CO': ['Denver'], 'NV': ['Las Vegas'], 'UT': ['Salt Lake City'], 'MA': ['Boston'], 'DC': ['Washington, DC'], 'HW': ['Honolulu'], 'MN': ['Minneapolis']}
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
states_fips = {'CA': 6, 'WA': 53, 'TX': 48, 'NY': 36, 'IL': 17, 'MI': 26,
               'GA': 13, 'FL': 12, 'AZ': 4, 'PA': 42, 'WI': 55, 'CO': 8, 'NV': 32, 'UT': 49, 'MA': 25, 'DC': 11001, 'HW': 15, 'MN': 27}
cities_fips = {'CA': ['06073', '06075', '06037'], 'WA': ['53033'], 'TX': ['48015', '01069', '01047'], 'NY': ['36061'], 'IL': ['17031'], 'MI': ['26163'],
               'GA': ['13121'], 'FL': ['18103', '12095'], 'AZ': ['04013'], 'PA': ['42101', '42003'], 'WI': ['55079', '55087'], 'CO': ['08031'], 'NV': ['32033'], 'UT': ['49035'], 'MA': ['25025'], 'DC': ['11001'], 'HW': ['15003'], 'MN': ['27053']}
states = ['California', 'Washington', 'Texas', 'New York', 'illinois', 'Michigan', 'Georgia',
          'Florida', 'Arizona', 'Pennsylvania', 'Wisconsin', 'Colorado', 'Nevada', 'Utah', 'Massachusetts', 'Hawaii', 'Minnesota']

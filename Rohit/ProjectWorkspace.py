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
cities_fips = {'CA': ['073', '075', '037'], 'WA': ['269'], 'TX': ['015', '225', '047'], 'NY': ['061'], 'IL': ['031'], 'MI': ['153'],
               'GA': ['049'], 'FL': ['121', '361'], 'AZ': ['013'], 'PA': ['101', '003'], 'WI': ['079', '087'], 'CO': ['031'], 'NV': ['033'], 'UT': ['035'], 'MA': ['025'], 'DC': ['11001'], 'HW': ['003'], 'MN': ['053']}

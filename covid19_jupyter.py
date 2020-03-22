#!/usr/bin/python
# Python module to help with parsing COVID-19 data
#
import pandas
import os 

def load_combined_data(path='./covid19-data/data/csv'):
    contents = os.listdir(path)
    dates = pandas.date_range('2020-03-14', periods=len(contents)-2)

    date_strs = [str(date.date()) for date in dates]

    paths = [os.path.join(path, date+'.csv') for date in date_strs]

    data_frames = [pandas.read_csv(path) for path in paths]

    for date, frame in zip(dates, data_frames):
        frame['Date'] = date

    
    combined_data = pandas.concat(data_frames, ignore_index=True)

    return combined_data

def get_state_data(data_frame, state):
    state_data = data_frame[data_frame['State_Name']==state].copy()

    return state_data

def get_county_data(data_frame, county):
    county_data = data_frame[data_frame['County_Name']==county].copy()
    county_data.set_index('Date', inplace=True)
    return county_data

def get_county_names(data_frame):
    """returns all the county names in the data frame"""
    return data_frame['County_Name'].tolist()

def tranform_state_to_time_series(data_frame):
    county_names = get_county_names(data_frame)
    # Create the data frame
    new_frame = get_county_data(data_frame, county_names[0])[['Confirmed']]
    new_frame.rename(columns={'Confirmed': county_names[0]}, inplace=True)

    for county in county_names[1:]:
        county_frame = get_county_data(data_frame, county)
        new_frame[county] = county_frame['Confirmed']

    return new_frame

if __name__ == "__main__":
    combined_data = load_combined_data()

    state_data = get_state_data(combined_data, 'California')

    time_series_data = tranform_state_to_time_series(state_data)

    print(time_series_data.head(10))
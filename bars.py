import json


def load_data(filepath):
    date = []
    with open(filepath, 'r', ) as file_dat:
        date = json.load(file_dat)
    return date


def get_biggest_bar(data):
    seats = data[0]['Cells']['SeatsCount']
    the_biggest_bar = data[0]['Cells']['Name']
    for all_bars in data:
        if all_bars['Cells']['SeatsCount'] > seats:
            seats = all_bars['Cells']['SeatsCount']
            the_biggest_bar = all_bars['Cells']['Name']
    return the_biggest_bar


def get_smallest_bar(data):
    seats = data[0]['Cells']['SeatsCount']
    the_smallest_bar = data[0]['Cells']['Name']
    for all_bars in data:
        if all_bars['Cells']['SeatsCount'] < seats:
            seats = all_bars['Cells']['SeatsCount']
            the_smallest_bar = all_bars['Cells']['Name']
    return the_smallest_bar


def get_closest_bar(data, longitude, latitude):
    distance_longitude = abs(longitude - data[0]['Cells']['geoData']['coordinates'][0])
    distance_latitude = abs(latitude - data[0]['Cells']['geoData']['coordinates'][1])
    the_closest_bar = data[0]['Cells']['Name']
    for distance in data:
        if (abs(longitude - distance['Cells']['geoData']['coordinates'][0]) + abs(
                    latitude - distance['Cells']['geoData']['coordinates'][
                    1])) < distance_longitude + distance_latitude:
            distance_longitude = abs(longitude - distance['Cells']['geoData']['coordinates'][0])
            distance_latitude = abs(latitude - distance['Cells']['geoData']['coordinates'][1])
            the_closest_bar = distance['Cells']['Name']
    return the_closest_bar


if __name__ == '__main__':
    bars_inf = load_data('data.json')
    print('bigest bar is %s' % get_biggest_bar(bars_inf))
    print('smallest bar is %s' % get_smallest_bar(bars_inf))
    longitude = float(input('Input longitude(GPS) = '))
    latitude = float(input('Input latitude(GPS) = '))
    print('Closest bar is %s' % get_closest_bar(bars_inf, longitude, latitude))

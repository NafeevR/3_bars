import json


def load_data(filepath):
    date = []
    date = json.load(open(filepath, 'r', ))
    return date


def get_biggest_bar(data):
    the_biggest_bar = max(data,key=lambda i:i['Cells']['SeatsCount'])['Cells']['Name']
    return the_biggest_bar


def get_smallest_bar(data):
    the_smallest_bar = min(data, key=lambda i: i['Cells']['SeatsCount'])['Cells']['Name']
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
    path_to_the_file = input('Input path to the file = ')
    bars_inf = load_data(path_to_the_file)
    print('bigest bar is %s' % get_biggest_bar(bars_inf))
    print('smallest bar is %s' % get_smallest_bar(bars_inf))
    longitude = float(input('Input longitude(GPS) = '))
    latitude = float(input('Input latitude(GPS) = '))
    print('Closest bar is %s' % get_closest_bar(bars_inf, longitude, latitude))

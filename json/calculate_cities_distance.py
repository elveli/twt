
import json,os,sys,certifi
import requests
import pprint
from opencage.geocoder import OpenCageGeocode
#from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from pprint import PrettyPrinter

printer = PrettyPrinter()

def enter_city(number):
    city = input(f"Enter name of city {number}: ")
    return city

def get_latitude(results, city):
    if results and len(city):
        latitude = results[0]['geometry']['lat']
        return latitude
    else:
        sys.stderr.write("not found: %s\n" % city)

key = os.getenv('OPENCAGE_KEY')
#print(key)

if not key:
    print("API key is missing. Please set the OPENCAGE_KEY environment variable.")
    exit(1)

#url = "http://api.opencagedata.com/geocode/v1/json?key=key&q=52.3877830%2C+9.7334394&pretty=1&no_annotations=1"

url = f"http://api.opencagedata.com/geocode/v1/json?key={key}&q=52.3877830%2C+9.7334394&pretty=1&no_annotations=1"

city1 = enter_city(1)
city2 = enter_city(2)
#print(city1, city2)

geocoder = OpenCageGeocode(key)
#results = geocoder.geocode(city1, no_annotations='1',verify=False)
results_city1 = geocoder.geocode(city1, 
                           no_annotations='1',
                           verify=certifi.where()
                        )

results_city2 = geocoder.geocode(city2, 
                           no_annotations='1',
                           verify=certifi.where()
                        )
# printer.pprint(results_city1)
# printer.pprint(results_city2)

lat_city1 = get_latitude(results_city1, city1)
lat_city2 = get_latitude(results_city2, city2)
print(lat_city1)
print(lat_city2)

lat_difference = abs(lat_city1 - lat_city2)

print(f"Latitude difference in km between {city1} and {city2} is {lat_difference}")

# if results_city1 and len(results_city1):
#         #longitude = results[0]['geometry']['lng']
#         city1_latitude  = results_city1[0]['geometry']['lat']
#        # print(u'%f;%s' % (latitude, city1))
# else:
#         sys.stderr.write("not found: %s\n" % city1)

response = requests.get(url)
data = json.loads(response.text)


# Extract the location bounds from the results
# if 'results' in data and len(data['results']) > 0:
#     first_result = data['results'][0]  # Access the first element of the results list
#     geometry = first_result.get('geometry')  # Get 'geometry' from the first result
#     if geometry:
#         lat = geometry.get('lat')
#         printer.pprint(lat)
#     else:
#         print("Lat data is not available in the first result.")
# else:
#     print("No results found in the response.")

''' {'northeast': {'lat': 52.387833, 'lng': 9.7334894},
 'southwest': {'lat': 52.387733, 'lng': 9.7333894}}
'''

#print(f"{name} premiered on {premiered} on {network}. It summary is {summary}")
#printer.pprint(data)
#printer.pprint(data.keys())

# dict_keys(['documentation', 'licenses', 'rate', 'results', 'status', 'stay_informed', 'thanks', 'timestamp', 'total_results'])

'''
$ python3 geo_loc_test.py
http://api.opencagedata.com/geocode/v1/json?key=7c250aac0e194cc98584ca2e492cc25e&q=52.3877830%2C+9.7334394&pretty=1&no_annotations=1
{'documentation': 'https://opencagedata.com/api',
 'licenses': [{'name': 'see attribution guide',
               'url': 'https://opencagedata.com/credits'}],
 'rate': {'limit': 2500, 'remaining': 2497, 'reset': 1727395200},
 'results': [{'bounds': {'northeast': {'lat': 52.387833, 'lng': 9.7334894},
                         'southwest': {'lat': 52.387733, 'lng': 9.7333894}},
              'components': {'ISO_3166-1_alpha-2': 'DE',
                             'ISO_3166-1_alpha-3': 'DEU',
                             'ISO_3166-2': ['DE-NI'],
                             '_category': 'building',
                             '_normalized_city': 'Hanover',
                             '_type': 'building',
                             'city': 'Hanover',
                             'city_district': 'Vahrenwald-List',
                             'continent': 'Europe',
                             'country': 'Germany',
                             'country_code': 'de',
                             'county': 'Region Hannover',
                             'house_number': '2',
                             'office': 'Design Offices',
                             'political_union': 'European Union',
                             'postcode': '30165',
                             'road': 'Philipsbornstraße',
                             'state': 'Lower Saxony',
                             'state_code': 'NI',
                             'suburb': 'Vahrenwald'},
              'confidence': 10,
              'distance_from_q': {'meters': 0},
              'formatted': 'Design Offices, Philipsbornstraße 2, 30165 '
                           'Hanover, Germany',
              'geometry': {'lat': 52.387783, 'lng': 9.7334394}}],
 'status': {'code': 200, 'message': 'OK'},
 'stay_informed': {'blog': 'https://blog.opencagedata.com',
                   'mastodon': 'https://en.osm.town/@opencage'},
 'thanks': 'For using an OpenCage API',
 'timestamp': {'created_http': 'Thu, 26 Sep 2024 01:07:13 GMT',
               'created_unix': 1727312833},
 'total_results': 1}
~/github/twt/json
'''
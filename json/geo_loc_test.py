
import json,os
import requests
import pprint
from pprint import PrettyPrinter

printer = PrettyPrinter()

key = os.getenv('OPENCAGE_KEY')
#print(key)
#url = "http://api.opencagedata.com/geocode/v1/json?key=key&q=52.3877830%2C+9.7334394&pretty=1&no_annotations=1"

url1="http://api.opencagedata.com/geocode/v1/json?key="
url2=key
url3="&q=52.3877830%2C+9.7334394&pretty=1&no_annotations=1"

url = url1 + url2 + url3
print(url)


response = requests.get(url)
data = json.loads(response.text)

# name = data['name']
# premiered = data['premiered']
# summary = data['summary']
# network = data['network']['name']



#print(f"{name} premiered on {premiered} on {network}. It summary is {summary}")
printer.pprint(data)

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
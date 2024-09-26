# https://opencagedata.com/tutorials/geocode-in-python#batch
# https://opencagedata.com/tutorials/geocode-in-python#background

import os,sys
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

value = os.getenv('PATH')
print(value)

key = 'YOUR-API-KEY'
geocoder = OpenCageGeocode(key)
addressfile = 'addresses.txt'

try:
  with open(addressfile,'r') as f:
    for line in f:
      address = line.strip()

      # no need to URI encode query, module does that for you
      results = geocoder.geocode(address, no_annotations='1')

      if results and len(results):
        longitude = results[0]['geometry']['lng']
        latitude  = results[0]['geometry']['lat']
        print(u'%f;%f;%s' % (latitude, longitude, address))
        # 40.416705;-3.703582;Madrid, Spain
        # 45.466797;9.190498;Milan, Italy
        # 52.517037;13.388860;Berlin, Germany
        # 48.1371079;11.5753822;München, Deutschland
        # 52.3878553;9.7332249;Philipsbornstr 2, 30165 Hannover, Germany
      else:
        sys.stderr.write("not found: %s\n" % address)
except IOError:
  print('Error: File %s does not appear to exist.' % addressfile)
except RateLimitExceededError as ex:
  print(ex)
  # You have used the requests available on your plan.

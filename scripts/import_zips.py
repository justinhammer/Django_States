#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import State, StateCapital, City

print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
zip_file_name = "zip_codes_states.csv"

# print "%s/%s" % (dir_name, file_name)
# print "{0}/{1}".format(dir_name, file_name)

zip_file_name_csv = os.path.join(dir_name, zip_file_name)

zip_file_name_csv = open(zip_file_name_csv, 'r')

reader = csv.DictReader(zip_file_name_csv)

for row in reader:

    new_city, created = City.objects.get_or_create(city=row['city'])
    new_city.lat = row['latitude']
    new_city.lon = row['longitude']
    new_city.city = row['city']
    new_city.county = row['county']
    new_city.zip_code = row['zip_code']

    try:
        new_city.state = State.objects.get(abbrev=row['state'])
    except Exception, e:
        print "City missing! %s" % e
        
    try:
        new_city.save()
    except Exception, e:
        print new_city.city

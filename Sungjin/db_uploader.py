import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sungjin.settings")
django.setup()

from starbucks.models import Drinks

CSV_PATH_PRODUCTS = './starbucks_drink.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    for row in data_reader:
        print(row)

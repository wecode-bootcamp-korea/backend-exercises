import os
import django
import csv
import sys

os.environment.setdefault("DJANGO_SETTINGS_MODULE","starbucks_sqlite.settings")
django.setup()

from product.models import Menu, Category, Drink

CSV_PATH_PRODUCTS = './starbucks_crawling.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    date_reader =csv.reacer(in_file)
    for row in data_reader:
        print(row)

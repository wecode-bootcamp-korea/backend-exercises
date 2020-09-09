import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","donghyun.settings")
django.setup()

from starbucks.models import Users

CSV_PATH='./starbucks_crawling.csv'

with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    for row in data_reader:
        Users.objects.create(name = row[0], img_link =row[1])

## OS CONFIG
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')

import django
django.setup()

## FAKER CODE
import random
from apptwo.models import AccessRecord, Topic, Webpage

from faker import Faker

generatefake = Faker()

topics = ['Search', 'News', 'Social', 'Marketplace', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save
    return t

def populate(N=5):
    for entry in range(N):
    ## topic

        topname = add_topic()
        fakeurl = generatefake.url()
        fakedate = generatefake.date()
        fakename = generatefake.company()

    ## webpage
        webpname = Webpage.objects.get_or_create(topic=topname, url=fakeurl, name=fakename)[0]

    ##fake access record
        acc_rec= AccessRecord.objects.get_or_create(name=webpname, date=fakedate)

    print("generating...")

if __name__ == '__main__':
    print("seeding the database")
    populate(20)
    print("I'm done, now you have something on your db")
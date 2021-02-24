import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projectDjango.settings')

import django
django.setup()

import random
from firstApp.models import Topic,WebPage,AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Social','Search','Market Place','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        # GET THE TOPIC FOR THE ENTRY
        topic = add_topic()

        #Create the fake data for the entry
        fake_date = fakegen.date()
        fake_url = fakegen.url()
        fake_name = fakegen.company()

        web_page = WebPage.objects.get_or_create(topic=topic,name=fake_name,url=fake_url)[0]

        access_record = AccessRecord.objects.get_or_create(name=web_page,date=fake_date)[0]

if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Populating complete!")

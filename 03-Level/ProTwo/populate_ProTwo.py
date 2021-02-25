import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import Users
from faker import Faker
faker = Faker()


def populate(N=5):
    for i in range(N):
        fakename = faker.name().split()
        fname = faker.first_name()
        lname = faker.last_name()
        femail = faker.email();
        user = Users.objects.get_or_create(first_name=fname,last_name=lname,email=femail)[0]


if __name__ == "__main__":
    print("Starting population scirpt")
    populate(10)
    print("Population executed scuccessfully")
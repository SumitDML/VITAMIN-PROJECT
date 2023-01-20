from .models import *


def switch(name):
    return switcher.get(name, default)()


def zones():
    return Zones


def Sunshine_availibilty():
    return SunshineAvailability


def Common_Food_Allergy():
    return FoodAllergy


def Spice():
    return Spices


def default():
    return "Invalid Model"


switcher = {
    "Zones": zones,
    "Sunshine_Availability": Sunshine_availibilty,
    "Common_Food_Allergy": Common_Food_Allergy,
    "Spices": Spice
}

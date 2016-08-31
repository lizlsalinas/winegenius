#!/usr/bin/env python
def winegenius():
    print "intro statement welcome"

    is_eating=raw_input("Are you eating [y/n]")
    if is_eating == "y":
        what_are_you_eating()
    else:
        what_do_you_prefer()
def what_are_you_eating():
    food_type=raw_input("Is your meal... heavy, light, unsure?")
    if food_type== "heavy":
        type_of_heavy_food()

    elif food_type== "light":
        type_of_light_food()
    else:
        print "you should have a glass of Pinot Noir!"

def type_of_heavy_food():
    heavy_food=raw_input("are you eating pizza, steak, quiche?")
    if heavy_food=="pizza":
        print "have a glass of Chianti!"
    elif heavy_food== "steak":
        print "have a glass of Cab!"
    elif heavy_food== "quiche":
        print "have a glass of Malbec"
def type_of_light_food():
    light_food=raw_input("are you eating exotic, poultry, or veggies?")
    if light_food=="exotic":
        print "have a glass of Grenache!"
    elif light_food=="veggies":
        print "have some beaujolais"
    elif light_food=="poultry":
        print "have a glass of Zinfandel!"
def what_do_you_prefer():
    preference=raw_input("do you prefer dry or sweet? ")
    if preference== "dry":
            type_of_dry()
    elif preference=="sweet":
            type_of_sweet()
    else:
        print "didn't understand %s, please use dry/sweet" % preference
        what_do_you_prefer()
def type_of_sweet():
    sweet_pref=raw_input("what sweet are you in the mood for? Jam, Cinnamon, or Cherry?").lower()
    if sweet_pref=="jam":
        print "zinfandel"
    elif sweet_pref=="cherry":
        print "pinot noir"
    elif sweet_pref=="cinnamon":
        print "grenache"

def type_of_dry():
    dry_pref=raw_input("what type of dry are you in the mood for? smoky, earthy, peppery?")
    if dry_pref=="smoky":
        print "Rioja"
    elif dry_pref=="peppery":
        print "cotes du rhone"
    elif dry_pref=="earthy":
        print "beaujolais"



if __name__ == "__main__":
    winegenius()

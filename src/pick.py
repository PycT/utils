#!python

# An utility to pick a random number from a range with no repeating
# The range is defined with the variables range_start and range_end
# (lines 14 and 15)
#
# The numbers used are stored in "picks.json"
# usage: ./pick.py


import random
import json

range_start = 1
range_end = 62

pick = 0

if __name__ == "__main__":
    try:
        with open("picks.json", "r") as past_records:
            past = json.load(past_records)
    except Exception as e:
        print(e)
        past = {"past": [0]}
        print("'picks.json' file created.")
    
    if len(past) > range_end:
        print("Range exceeded")
        print("clear the 'picks.json' file")
        exit()

    while pick in past["past"]:
        pick = random.randrange(range_start, range_end)

    print("Your pick is {}".format(pick))
    past["past"].append(pick)

    with open("picks.json", "w") as past_records:
        json.dump(past, past_records, indent = 4)

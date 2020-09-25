import csv
import os

# prompt user for video lookup
video = input("What show or movie are you looking for?")

# set path for file
csvpath = os.path.join("Resources", "netflix_ratings.csv")

found = False

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + "with a rating of " + row[5])
            found = True

    if found is False:
        print("Sorry")
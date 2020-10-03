# Election Analysis
Module 3 election analysis with python

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of cotes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.49.1

## Election-Audit Results

The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes.
- The winner of the election was candidate Diana DeGette who received 272,892 votes, or 73.8% of the total votes.
- The vote by county breakdown was:
  - Jefferson county received 38,855 votes, or 10.5% of the votes.
  - Denver county received 306,055 votes, or 82.8% of the votes.
  - Arapahoe county received 24,801 votes, or 6.7% of the votes.
- Denver County had the largest number of votes, with 306,055 votes. 

## Election-Audit Summary: 
By changing a few things about this script, you could use it for other elections in the future as well. One thing you would have to change is the file to import that has your data from the election in it. You would do this by changing the file_to_load variable to equal the new file with election data in it. This code is shown below:
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```
Another thing you may have to change is the code on lines 48 and 51 that retrieve the candidate and country names, shown below. If the csv for your new election results data does not have the candidate and country names in the same rows as our csv, your code would have to reflect that by having the correct index. 
```
  # Get the candidate name from each row.
    candidate_name = row[2]

  # 3: Extract the county name from each row.
    county_name = row[1]
```
## Challenge Overview
This analysis of a local congressional election in Colorado allowed us to look at every candidate who received votes, how many votes each candidate received, what percentage of the vote each candidate received, and the winner of the election. The analysis also showed us votes by county, and the percentage of votes each county received.

## Challenge Summary
Diana Degette was the clear winner of the election with more than 73% of the vote and over 272,000 votes. Charles Stockham was the runner up, and Raymon Doane came in third. The county with the most votes was Denver, with 306,055 votes or 82.8% of the votes. 
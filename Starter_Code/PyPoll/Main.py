# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
# Dictionary to store candidate names and their vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row if there is one
    next(reader, None)

    # Loop through each row in the CSV file
    for row in reader:
        total_votes += 1  # Increment the total vote count
        candidate_name = row[2]  # Assume candidate name is in the third column (index 2)

        # Increment the vote count for the candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

f = open("output.txt", "a")
# Print the results
print(f"Total Votes: {total_votes}", file=f)
#print("\nCandidate Results:")
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"\nCandidate Results:","{candidate}: {vote_percentage:.2f}% ({votes} votes)", file=f)

    # Find the candidate with the highest votes
winner = max(candidate_votes, key=candidate_votes.get)
print(f"\nWinner: {winner} with {candidate_votes[winner]} votes", file=f)

f.close()

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
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        # Add a vote to the candidate's count
summary = []
summary.append("Election Results:\n")
summary.append(f"\nTotal Votes: {total_votes}\n")

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    summary.append(f"{candidate}: {vote_percentage:.2f}% ({votes} votes)\n")

# Find the candidate with the highest votes
winner = max(candidate_votes, key=candidate_votes.get)
summary.append(f"\nWinner: {winner}")

# Print the summary
for line in summary:
    print(line, end='')

# Save the results to a text file
output_file = 'voting_results.txt'  # Replace with your desired output file path
with open(output_file, 'w') as file:
    file.writelines(summary)


# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferons\n                        \nTotal # of votes\n-------------------\n369,711\n                     \nCandidates\n------------------------\nCharles Casper: 23.0% (85,213)\nDiana DeGette: 73.8% (272,892)\nRaymon Anthony Doane: 3.1% (11,606)"
    )

# Open the election results & read the file object with the reader function   
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data, delimiter=",")
    
# Read and print the header row
    header = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count 
        total_votes += 1
        
        #3. Print the candidates name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:

            # Add the candidates name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidates's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # Determine the percentage of votes for each candidate by looping through the counts
        #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
            #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
            #3 Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)* 100

        # To do: print out each candidate's name, vote count, and percentage of # votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # To do: print out the winning candidate, Final %_Votes for each candi AFinal %_Votes for each candi Avote count and percentage to # terminal
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    

  



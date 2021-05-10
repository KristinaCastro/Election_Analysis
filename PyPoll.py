# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #for row in election_data:
        #print(row)

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferons")

# Open the election results & read the file object with the reader function   
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data, delimiter=",")
    for row in file_reader:
        print(row)

# Read and print the header row
    #header = next(file_reader)
    #print(header)



    
    
    
'''
     practice_writing = (
        f"\nCounties in the Election\n"
        f"___________________________\n"
        f"\nArapahoe\nDenver\nJefferson\n")
print(practice_writing, end="")
'''


#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


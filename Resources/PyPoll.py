# The data we need to retrieve 
# 1. the total # of votes cast
# 2. a complete list of candidates who receied votes
# 3. The % of votes each candidate won 
# 4. The total # of votes each candidate won
# 5. the winner of the election based on popular votes

import csv
import os
# Assigning variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigning variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initializing total number of votes
total_votes = 0 
# initializing candidate options variables
candidate_options = []
# Declare empty dictionary to count the total votes for each candidate
candidate_votes = {}
# Initializing variables to determine winning candidate
winning_candidate = ""
winning_count = 0 
winning_percentage = 0
# Open the file to just read
with open(file_to_load) as election_data:
    # read and analyze the data using reader function
    file_reader = csv.reader(election_data)
    # print header and each row in the csv file
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            ## adding candidate name to the list and make sure to list the name once
            candidate_options.append(candidate_name)
            ## begin tracking votes for each candidate by setting to 0
            candidate_votes[candidate_name] = 0
        # add a vote towards the candidate count // make sure this is in 'for' loop & out of 'if' statement
        candidate_votes[candidate_name] += 1
    # Determine percentage of votes for each candidate
    for candidate_name in candidate_votes: ### make sure this for loop is outside the above for loop
        # setting variable to get vote count for each candidate
        votes = candidate_votes[candidate_name]
        # calculation of votes; changingthe numbers to floating in order to calculate
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate name: vote % and (total number fo votes)
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate by running an if statement
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true
            winning_count = votes
            winning_percentage = vote_percentage
            # set winning candidate to candidates name
            winning_candidate = candidate_name
    # Print out the winner's: name, vote count, percentage 
    winning_candidate_summary = (
        f"---------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")
    print(winning_candidate_summary)




# Left as comments (these were used to output the first couple steps)
## print(total_votes) 
## total_votes = 369711
## print(candidate_votes)

#writing to files

#opening the file with the 'w' mode to write data to the file
# open(file_to_save, "w") //// This code to open a working document in vs code
# using the with statment, open the file as text file
#with open(file_to_save, "w") as txt_file:
    # write data to test
    # txt_file.write("Arapahoe, Denver, Jefferson") --- outputs all on the same line
    # to write on separate lines, between each county type '\n' essentially saying return
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

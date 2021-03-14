# Election_Analysis
Module 3: Election Analysis - Python
## Overview
The election commission has requested the following additional data and information to complete the audit:
-	The voter turnout for each county 
-	The percentage of votes from each county out of the total count
-	The county with the highest turnout
First will be to look and analyze the results. Then a quick summary of how the election commission can use this script of code can be used and some modifications that can be used for future elections.  

## Election-Audit Results
Here is the complete output of the election-audit results and each section of the results is looked at below.

<img width="335" alt="election_results output" src="https://user-images.githubusercontent.com/79118630/111083102-21d4c680-84e2-11eb-9806-598a2d724150.png">

### Votes casted in this congressional election
- As we can see, there was a total 369,711 votes casted during this election from the three observed counties. 
### Breakdown of the number of votes and the percentage of total votes for each county
#### And Largest County Turnout

<img width="240" alt="election_results_county_votes" src="https://user-images.githubusercontent.com/79118630/111083346-82183800-84e3-11eb-9bb8-d7bfc8f3bf4f.png">

- There were three counties observed: Jefferson, Denver, and Arapahoe. Denver had the most votes with 82.8% of the total votes, Jefferson in second with 10.5% and Arapahoe last with 6.7% of votes. One may think there might have been an error when python was reading the csv file, but if we go into the *election_results.csv* excel file and run a simple countif statement, `=COUNTIF(B2:B3697712, “Denver”)` the result is 306055, which as we can see is the total of amount of votes casted from Denver. We can confirm, 82.8% of the total votes were from Denver. This is also not shocking since Denver is the capitol of Colorado, Denver County could potentially be a very populated region, causing for a higher voter turnout, as compared to other counties.
- Future candidates will want to keep note of this as to focus a majority of their attention in Denver. Over four-fifths of the casted votes were from one county, meaning 2-out-of-3 counties had less than one-fifth (<20%) of the votes casted. Every vote does count, but when you see you have such a lop-sided voter concentration, it is important to keep note of that. 
- Another way to look at it, half of the Denver votes would be 153,027.5 votes, that would be 41.4% of the total votes. To win an election, you need to have over 50% of the votes, the majority. If you lockdown half of Denver, you would only need less than 10% of the total votes.
### Breakdown of the number of votes and the percentage of total votes for each candidate

<img width="288" alt="election_results_candidate_votes" src="https://user-images.githubusercontent.com/79118630/111083409-d3282c00-84e3-11eb-82d5-8778ac5f8bc4.png">

- There were three candidates running: Charles Casper Stockham (CCS), Diana DeGette (DD), Raymon Anthony Doane (RAD).  We can clearly see here that this election was won in a landslide fashion from DD with 73.8% of the total votes. CCS came in second with 23% and RAD is last with only 3.1% of the votes. 
- Again, we have another lop-sided results with DD receiving over 70% of the votes. This time the election results aren’t crazy favored, but still, only one of the candidates received less than 4% of votes, so we can do the same thing using another countif function to double check the code: `=COUNTIF(C2:C369712, "Diana DeGette")`. Sure enough, we get 272892, which as we can see right above, is the total amount of votes DD receives. 
### Winning candidate, Vote Count, and Percentage of Total Votes
We already know Diana DeGette won this election, here are the winning numbers.

<img width="214" alt="election_results_winner" src="https://user-images.githubusercontent.com/79118630/111083216-c1925480-84e2-11eb-8ace-413526a8cced.png">

## Election-Audit Summary
- This script of code is good to save and have for future elections because it can be used with any election data. We can see that we get all the results we needed and was outputted at a decent pace. The great thing about code is that since we know it works, we can make modifications for future use. One major modification that will be needed to be made is when looking at other election results (or other csv files), to change certain lines. Another modification that can be added will be for the code to read through the ballot ids to make sure there are no duplicates. 
### Modifications of script 
#### Changing the csv and output files 
- This _exact_ code will need modifications for future use because it is just looking at this election’s results. In the *PyPoll_Challenge.py* file, line 9 shows `file_to_load = os.path.join(“Resources”, “election_results.csv”)`, this opens the csv file and assigns it to a variable to reference the csv file for later use. Line 11 is `file_to_save = os.path.join(“analysis”, “election_results.txt”)`, this will create a ‘txt’ file and assign it the variable “file_to_save” to be referenced later to output the results. Line 34 calls the csv file with the command line `with open(file_to_load) as election_data`, this tells the code to cycle (or read) through the csv file and will be referred to as `election_data` within the script. Lines 34 – 76 is the block of code under the `with open()` statement assigns different variables to be stored for later outputs. Line 80 is another `with open` statement `with open(file_to_save, “w”) as txt_file:`. The `“w”` within the statement tells python that we want to write in the “election_results.txt” and will be referred to as `txt_file` within the block of code. Lines 80 – 158 (till the end of the script), is where we begin to run for loops to output the stored data to the terminal and to the txt_file.
- The modifications needed to be made here for future use would be inside of the `os.path.join`. These are the paths taken to get to the csv file and txt files. So for future election use, it is important to edit these lines and make sure the files and path are spelled exactly how they show on your device, or else the code will not run. The two `with open ()` statements don’t need to be changed unless you change the "file_to_load" or "file_to_save" variable names. 
#### Preventing voter fraud
- We know this code works because we even double checked it with the excel *countif* function in the csv file. But when looking at the csv file, the candidate is the third column, the county is in the second and the ballot id (voter id) is in the first column. Each ballot receives a unique ID number to ensure that each person’s vote is recorded and counted, but we did not make this csv file, therefor we don’t know the extent of cleaning it went through. 
Depending on the state, a duplicate vote will either be thrown out or any vote with that ID might be thrown out because it has been tampered/manipulated with. This sometimes happens when creating datasets, especially if these ballots were mainly entered. 

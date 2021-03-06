# Election Analysis
## Overview of Election Audit:
The Colorado Board of Election Commission has requested an election audit of the election results for the US Congressional precinct in Colorado. The election commission has requested the following additional data to complete the audit:
  1) The voter turnout for each county
  2) The percentage of votes from each county out of the total count
  3) The county with the highest turnout

Our goal: 
  - To generate a vote count report to certify the US congressional election
  - To automate the election audit process using Python, if done successfully the code we write will be used to audit other congressional districts, senatorial districts and local elections. 

## Election-Audit Results:
   - How many votes were cast in this congressional election?
      - 369,711 total votes were cast
        - [Total Votes Cast](https://github.com/KristinaCastro/Election_Analysis/blob/main/total_votes.png)
    
          -  <img width="250" alt="Screen Shot 2021-06-08 at 2 59 54 AM" src="https://user-images.githubusercontent.com/81998045/121138376-9da28e80-c805-11eb-9739-4fefaeaa351a.png">

  - Number of votes and the percentage of total votes for each county in the precinct. 
    - I used a for loop to retrieve the county, county vote count and then calculated the percentage of county votes for each county.
      - [County Votes & %](https://github.com/KristinaCastro/Election_Analysis/blob/main/county-votes_py.png) 
     
        -  <img width="249" alt="Screen Shot 2021-06-08 at 3 02 22 AM" src="https://user-images.githubusercontent.com/81998045/121138695-f40fcd00-c805-11eb-8082-3d7268c7fe4b.png">
   
  -  Which county had the largest number of votes?     
     - Denver had the largest county turnout
        - [Largest County Turnout](https://github.com/KristinaCastro/Election_Analysis/blob/main/lg_county_turnout.png)
        
           -  <img width="246" alt="Screen Shot 2021-06-08 at 3 13 38 AM" src="https://user-images.githubusercontent.com/81998045/121140155-8795cd80-c807-11eb-93f3-a0da8828534f.png">
  - Number of votes and the percentage of the total votes each candidate received 
    - Again, a for loop was used to determine each candidate, then retrieve the vote count and percentage of votes for each candidate.
      - [Candidate Votes & %](https://github.com/KristinaCastro/Election_Analysis/blob/main/candidate_votes%20info_py.png) 
         - <img width="297" alt="Screen Shot 2021-06-08 at 3 25 25 AM" src="https://user-images.githubusercontent.com/81998045/121141609-2bcc4400-c809-11eb-8953-ee4362b32640.png">
  - Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Diana DeGette won the election
      - [Election Winner](https://github.com/KristinaCastro/Election_Analysis/blob/main/candidate_winner_py.png)
        - <img width="259" alt="Screen Shot 2021-06-08 at 3 33 35 AM" src="https://user-images.githubusercontent.com/81998045/121142754-5074eb80-c80a-11eb-9a57-c7b2a72ef6ea.png">

## Election-Audit Summary:

This automated script can be used for any election, by modifying the script with the appropriate csv file, updating the variables and creating the appropriate lists and dictionaries, this automation will serve to be extremely useful while saving time. Furthermore, the Board of Elections can use this code for other elections such as a county sheriff's election, by modifying the code with the corresponding csv file and updating the code to reflect the specific districts within a county. 

With just a few modifications, this code can provide all the needed information, certify the winning results and as a result successfully audit any election. 
<p align="center">
  <img width="324" alt="Screen Shot 2021-06-08 at 4 09 14 AM" src="https://user-images.githubusercontent.com/81998045/121147898-4acdd480-c80f-11eb-9bba-247ccb3e080f.png">
</p>

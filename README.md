# IML-FALL2025---Voter-Bias

09/10/2025 - Goals after meeting: (double check with log on box)
- can we look to streamline some parts of the code? 
- let's also make sure to sort everything into separate folders to get everything organized 
- look to start calculate biases by monday 09/15?
    - spearman distance stuff -> we would expect "bias" to go down as the season goes on... 
    - ^^let's make a master bias file for each week, each season, and each voter pair^^ <- can serve as basis for additional analysis 
- work on conference affiliations 

# _______________________________________________________________________________________________________________
09/09/2025 - Current TODO list:
Create various auxiliary files:

Consensus/Average/Median rankings:  Using the main poll data files (in Box, under Data), create a file listing, for each team and each week/season, their (1) official AP Poll rank, (2) average rank, (3) median rank.  Notes:

For the AP Poll ranks, rather than taking those from published rankings, compute the ranks directly from the data by adding up the points earned by each team (25 for 1st, 24 for 2nd, etc).  Then do some spot checks to compare the computed ranks with the “official” ranks.

Handling non-ranked teams:   One approach would be to just assign a non-ranked team rank 26, and 0 points.   Another approach might be to assign ranks based  on the accumulated points (i.e., extend the points-based ranking beyond the top 25).

Conference affiliations:  A file showing,  for each week/season and each team earning points in this week/season, the conference affiliation (SEC, BIG10, ACC, BIG12, PAC10. Note):

Since teams occasionally change conferences, just having a list of teams along with their affiliation won’t do.

# _________________________________________________________________________________________________________________
Project Goals
• Develop measures to quantify voter biases in AP Top 25 polls in a statistically rigorous manner.
• Using these measures, analyze the ballot data from AP Top 25 College Football and Men’s Basket-
ball Polls for biases by voters towards (or against) specific teams.
• Determine if there are correlations between such biases and a voter’s geographic location, alma
mater team, or alma mater conference.

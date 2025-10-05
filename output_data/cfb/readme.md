# College Football Datasets README
## This folder contains the following CSV files:

- cfb_teams
- cfb_teams_summary
- cfb_voters
- cfb_voters_summary
- cfb_master_bias_file
- cfb_conf_aff
- cfb_average_biases

### cfb_teams
<b>Columns:</b>

- year: year of corresponding season
- week: AP poll week number in the season
- teams: list of school/teams that appeared in the AP poll for said week (team names are standardized to be lowercased and hyphenated)

This dataset records the list of teams that have appeared in the top 25 College Football AP polls over time, keyed by year and week. 

### cfb_teams_summary
<b>Columns:</b>

- Team: list of school/teams that appeared in the AP poll (team names are standardized to be lowercased and hyphenated)
- appearances_AP25: # of that teams apperances in the Top 25 AP polls
- avg_rank: average rank of the team in the Top 25 AP polls

This dataset records the list of teams that have appeared in the top 25 College Football AP polls over time, recording number of appearances and average rank in the polls. 

### cfb_voters
<b>Columns:</b>

- year: year of corresponding season
- week: AP poll week number in the season
- voters: list of pollsters that participated in the AP poll for said week

This dataset records the list of pollsters that participated in the top 25 College Football AP polls over time, keyed by year and week. 

### cfb_voters_summary
<b>Columns:</b>

- Voter: list of pollsters that participated in the AP poll for said week
- appearances: number of times pollster has participated in the top 25 College Football AP polls

This dataset records the list of pollsters that participated in the top 25 College Football AP polls over time, and how many times they've appeared. 

### cfb_master_bias_file
<b>Columns:</b>

- Pollster (v): voter name correspoding to row recording their vote 
- Season: season year
- Week: AP poll week number in the season
- Rank: the position assigned by the voter
- Team(t): the team being ranked (team names are standardized to be lowercased and hyphenated)
- ap_rank: calculated AP rank for said team. Unranked teams are ranked by default value of 26
- average: average rank of calculated AP rank for said team for that given week
- median: median rank of calculated AP rank for said team for that given week
 
#### Biases were calculated using the spearman distance formula:  
$$\frac{r(v, t) - r#(t)}{min(r(v, t) - r#(t))}$$
- bias1(v, t): ... (mention equation used)
- bias2(v, t): ... (mention equation used)
- bias3(v, t): ... (mention equation used)



### cfb_conf_aff
<b>Columns:</b>

### cfb_average_biases
<b>Columns:</b>
# College Football Datasets README
## This folder contains the following CSV files:

- `cfb_teams`
- `cfb_teams_summary`
- `cfb_voters`
- `cfb_voters_summary`
- `cfb_master_bias_file`
- `cfb_conf_aff`
- `cfb_relative_biases.csv`
- `cfb_cam_output.csv`

### `cfb_teams.csv`
<b>Columns:</b>

- year: year of corresponding season
- week: AP poll week number in the season
- teams: list of school/teams that appeared in the AP poll for said week (team names are standardized to be lowercased and hyphenated)

This dataset records the list of teams that have appeared in the top 25 College Football AP polls over time, keyed by year and week. 

### `cfb_teams_summary.csv`
<b>Columns:</b>

- Team: list of school/teams that appeared in the AP poll (team names are standardized to be lowercased and hyphenated)
- appearances_AP25: # of that teams apperances in the Top 25 AP polls
- avg_rank: average rank of the team in the Top 25 AP polls

This dataset records the list of teams that have appeared in the top 25 College Football AP polls over time, recording number of appearances and average rank in the polls. 

### `cfb_voters.csv`
<b>Columns:</b>

- year: year of corresponding season
- week: AP poll week number in the season
- voters: list of pollsters that participated in the AP poll for said week

This dataset records the list of pollsters that participated in the top 25 College Football AP polls over time, keyed by year and week. 

### `cfb_voters_summary.csv`
<b>Columns:</b>

- Voter: list of pollsters that participated in the AP poll for said week
- appearances: number of times pollster has participated in the top 25 College Football AP polls

This dataset records the list of pollsters that participated in the top 25 College Football AP polls over time, and how many times they've appeared. 

### `cfb_master_bias_file.csv`
<b>Columns:</b>

- Pollster (v): voter name correspoding to row recording their vote 
- Season: season year
- Week: AP poll week number in the season
- Rank: the position assigned by the voter
- Team(t): the team being ranked (team names are standardized to be lowercased and hyphenated)
- ap_rank: calculated AP rank for said team. Unranked teams are ranked by default value of 26
- average: average rank of calculated AP rank for said team for that given week
- median: median rank of calculated AP rank for said team for that given week
 
<b>The bias columns were calculated using the weighted Spearman distance formula:</b>

$$
\text{bias}_{\text{number}}(v, t) = \frac{r(v, t) - r_{\text{number}}(t)}{\min\big(r(v, t), r_{\text{number}}(t)\big)}, \quad 
\text{where r(v,t) is the rank given by voter v for team t}
$$
 

- bias1(v, t): 

$$
\text{bias}_1(v, t) = \frac{r(v, t) - r_1(t)}{\min\big(r(v, t) , r_1(t)\big)}, \quad r_1(t) = \text{AP rank}
$$

- bias2(v, t): 

$$
\text{bias}_2(v, t) = \frac{r(v, t) - r_2(t)}{\min\big(r(v, t) , r_2(t)\big)}, \quad r_2(t) = \text{Mean rank}
$$
- bias3(v, t):

$$
\text{bias}_3(v, t) = \frac{r(v, t) - r_3(t)}{\min\big(r(v, t) , r_3(t)\big)}, \quad r_3(t) = \text{Median rank}
$$

- bias0(v, t)_ap:

$$
\text{bias}_0(v, t)_{ap} = r(v, t) - r_1(t) = \text{unweighted AP rank}
$$

- bias0(v, t)_mean:

$$
\text{bias}_0(v, t)_{mean} = r(v, t) - r_2(t) = \text{unweighted mean rank}
$$

This dataset serves as a lookup file for the calcualted biases for a given voter 

### `cfb_conf_aff.csv`
<b>Columns:</b>

- Season: season year
- week: AP poll week number in the season
- Team: The team being ranked
- Conference: Given team's conference in that week/season
- Total_points: Total points earned that week

This dataset records the teams that appear across the original poll data mapped to their respective conferences in a given season. 

### `cfb_relative_biases.csv`
<b>Columns:</b>

- Percentile: records the percentage of biases in the given row of the dataset that are at or below a particular value
- bias1(p): weighted AP bias measure corresponding to the percentile
- bias2(p): weighted mean bias measure corresponding to the percentile
- bias3(p): weighted median bias measure corresponding to the percentile
- bias0ap(p): unweighted AP bias measure corresponding to the percentile
- bias0mean(p): unweighted mean bias measure corresponding to the percentile

This dataset records the relative biases to a percentile

### `cfb_cam_output.csv`
<b>Columns:</b>

- team: list of school/teams that appeared in the AP poll (team names are standardized to be lowercased and hyphenated)
- year: year of corresponding season
- week: AP poll week number in the season
- ap_rank: calculated AP rank for said team. Unranked teams are ranked by default value of 26
- average: average AP ranking
- median: median AP ranking

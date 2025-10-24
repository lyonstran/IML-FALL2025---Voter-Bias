# College Football Datasets README
## This folder contains the following CSV files:

- `cfb_teams.csv`
- `cfb_teams_summary.csv`
- `cfb_voters.csv`
- `cfb_voters_summary.csv`
- `cfb_master_bias.csv`
- `cfb_conf_aff.csv`
- `cfb_percentile_biases.csv`
- `cfb_cam_output.csv`
- `cfb_master_relative_percentage_bias.csv`

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
\text{bias}_{i \in (1, 2, 3)}(v, t) = \frac{r(v, t) - r_{i}(t)}{\min\big(r(v, t), r_{i}(t)\big)}, \quad 
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

Both bias0 columns represent a measure of bias using the raw difference between the rank given by the voter v for team t and either the AP rank or mean rank: 

- bias0(v, t)_ap:

$$
\text{bias}_0(v, t)_{ap} = r(v, t) - r_1(t) = \text{unweighted AP rank}
$$

- bias0(v, t)_mean:

$$
\text{bias}_0(v, t)_{mean} = r(v, t) - r_2(t) = \text{unweighted mean rank}
$$

This dataset serves as a lookup file for the calculated biases, using both the relative and raw differences for a given voter. “Relative difference” shows how strongly a voter deviates from the reference ranking, scaled by how important that rank is.

### `cfb_conf_aff.csv`
<b>Columns:</b>

- Season: season year
- week: AP poll week number in the season
- Team: The team being ranked
- Conference: Given team's conference in that week/season
- Total_points: Total points earned that week

This dataset records the teams that appear across the original poll data mapped to their respective conferences in a given season. 

### `cfb_percentile_biases.csv`
<b>Columns:</b>

- Percentile: The percentile rank (1–99). Each value represents the proportion of all bias values that are at or below the corresponding bias measure.

- bias1(p): Weighted bias relative to the AP Rank at the given percentile, measuring how much a voter’s ranking deviates from the AP ranking as a percentage of the smaller rank.

- bias2(p): weighted mean bias measure corresponding to the percentile

- bias3(p): weighted median bias measure corresponding to the percentile

- bias0ap(p): unweighted AP bias measure corresponding to the percentile

- bias0mean(p): unweighted mean bias measure corresponding to the percentile

This dataset records the relative biases to a percentile. For any given percentile p, each bias column records the bias value below which p% of all observations fall.

### `cfb_cam_output.csv`
<b>Columns:</b>

- team: list of school/teams that appeared in the AP poll (team names are standardized to be lowercased and hyphenated)
- year: year of corresponding season
- week: AP poll week number in the season
- ap_rank: calculated AP rank for said team. Unranked teams are ranked by default value of 26
- average: average AP ranking
- median: median AP ranking

### `cfb_master_relative_percentage_bias.csv`
<b>Columns:</b>

- Pollster (v): voter name correspoding to row recording their vote 
- Season: season year
- Week: AP poll week number in the season
- Rank: the position assigned by the voter
- Team(t): the team being ranked (team names are standardized to be lowercased and hyphenated)
- ap_rank: calculated AP rank for said team. Unranked teams are ranked by default value of 26
- average: average rank of calculated AP rank for said team for that given week
- median: median rank of calculated AP rank for said team for that given week

<b>The bias columns were calculated using the weighted Spearman distance formula, and these relative differences were converted to appropriate percentages:</b>

$$
\text{bias}_{i \in (1, 2, 3)}(v, t) = (\frac{r(v, t) - r_{i}(t)}{\min\big(r(v, t), r_{i}(t)\big)}) * 100, \quad 
\text{where r(v,t) is the rank given by voter v for team t}
$$
 

- bias1(v, t): 

$$
\text{bias}_1(v, t) = (\frac{r(v, t) - r_1(t)}{\min\big(r(v, t) , r_1(t)\big)}) * 100, \quad r_1(t) = \text{AP rank}
$$

- bias2(v, t): 

$$
\text{bias}_2(v, t) = (\frac{r(v, t) - r_2(t)}{\min\big(r(v, t) , r_2(t)\big)}) * 100, \quad r_2(t) = \text{Mean rank}
$$
- bias3(v, t):

$$
\text{bias}_3(v, t) = (\frac{r(v, t) - r_3(t)}{\min\big(r(v, t) , r_3(t)\big)}) * 100, \quad r_3(t) = \text{Median rank}
$$


Both bias0 columns represent a measure of bias using the raw difference between the rank given by the voter v for team t and either the AP rank or mean rank: 

- bias0(v, t)_ap:

$$
\text{bias}_0(v, t)_{ap} = r(v, t) - r_1(t) = \text{unweighted AP rank}
$$

- bias0(v, t)_mean:

$$
\text{bias}_0(v, t)_{mean} = r(v, t) - r_2(t) = \text{unweighted mean rank}
$$

This dataset serves as a lookup file for the calculated biases, using both the relative and raw differences for a given voter, except the bias1, bias2, and bias3 are converted by multiplying the values by 100 to represent the percent difference(i.e. say Voter A has calculated bias1 of 120, that would mean they voted 120% more in favor of team t over the general AP consensus).
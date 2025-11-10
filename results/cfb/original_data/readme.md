# College Football Datasets README
## This folder contains the following CSV files:

- `master_bias.csv`
- `master_bias_relative.csv`
- `conference_affiliation.csv`
- `ranked_teams.csv`
- `team_apperances.csv`
- `team_ranks.csv`
- `voter_apperances.csv`
- `voters_by_week.csv`

---

### `master_bias.csv`
<b>Columns:</b>

- Pollster (v): voter name corresponding to row recording their vote  
- Season: season year  
- Week: AP poll week number in the season  
- Rank: the position assigned by the voter  
- Team (t): the team being ranked (team names are standardized to be lowercased and hyphenated)  
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
\text{bias}_1(v, t) = \frac{r(v, t) - r_1(t)}{\min\big(r(v, t), r_1(t)\big)}, \quad r_1(t) = \text{AP rank}
$$

- bias2(v, t):  

$$
\text{bias}_2(v, t) = \frac{r(v, t) - r_2(t)}{\min\big(r(v, t), r_2(t)\big)}, \quad r_2(t) = \text{Mean rank}
$$

- bias3(v, t):  

$$
\text{bias}_3(v, t) = \frac{r(v, t) - r_3(t)}{\min\big(r(v, t), r_3(t)\big)}, \quad r_3(t) = \text{Median rank}
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

This dataset serves as a lookup file for the calculated biases, using both the weighted and raw differences for a given voter. “Weighted difference” shows how strongly a voter deviates from the reference ranking, scaled by how important that rank is.

---

### `master_bias_relative.csv`
<b>Columns:</b>

- Pollster (v): voter name corresponding to row recording their vote  
- Season: season year  
- Week: AP poll week number in the season  
- Rank: the position assigned by the voter  
- Team (t): the team being ranked (team names are standardized to be lowercased and hyphenated)  
- ap_rank: calculated percentile AP rank for said team. 
- average: percentile average rank of calculated AP rank for said team for that given week  
- median: percentile median rank of calculated AP rank for said team for that given week  

This dataset serves as a lookup file for the calculated percentile biases, using both the weighted and raw differences for a given voter.

---

### `conference_affiliation.csv`
<b>Columns:</b>

- Season: season year  
- Week: AP poll week number in the season  
- Team: The team being ranked (standardized format)  
- Conference: Given team's conference in that week/season  
- Total_points: Total points earned that week  

This dataset maps each team appearing in the AP poll to its respective conference for that week and season.

---

### `ranked_teams.csv`
<b>Columns:</b>

- year: season year  
- Week: AP poll week number in the season  
- Team: list of school/teams that appeared in the AP poll 

This dataset provides the complete weekly rankings of teams across seasons

---

### `team_apperances.csv`
<b>Columns:</b>

- Team: list of school/teams that appeared in the AP poll 
- appearances_AP25: number of that team's appearances in the Top 25 AP polls  
- avg_rank: average rank of the team in the Top 25 AP polls  

This dataset summarizes how often each team appears in the AP Top 25 over all seasons and computes their average rank performance.

---

### `team_ranks.csv`
<b>Columns:</b>

- Team: list of school/teams that appeared in the AP poll (standardized format)  
- year: season year
- week: AP poll week number in the season
- average: average AP ranking over all appearances  
- median_rank: median AP ranking across appearances  
- ap_rank: Official AP rank given for corresponding week

This dataset compiles team-level aggregate ranking statistics, allowing for comparison of team consistency and peak performance across seasons.

---

### `voter_apperances.csv`
<b>Columns:</b>

- Voter: name of pollster participating in the AP poll  
- appearances: number of times that pollster has participated in the Top 25 AP polls  

This dataset provides summary-level statistics for each voter, showing their total number of appearances in the AP polls.

---

### `voters_by_week.csv`
<b>Columns:</b>

- Year: season year  
- Week: AP poll week number in the season  
- Voter: pollster names  

This dataset tracks which pollsters participated each week by year.


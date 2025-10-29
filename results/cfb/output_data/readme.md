# README for summary_stats

## Files in this folder:

- `team.csv`

- `voter.csv`

- `week.csv`

- `week_apbias_std.png`

- `week_bias_mean.png`

- `week_mean_nc.png`

- `week_std_nc.png`

- `week_visual_std.png`

### `week.csv`
<b>Columns:</b>

- season: year of season respectively. 
- week: week in corresponding season. 
- bias1_mean: average weighted difference between voter rank and AP rank for the respective week in the season.
- bias1_std: standard deviation of weighted difference between voter rank and AP rank for the respective week in the season.
- bias2_mean: average weighted difference between voter rank and mean ranks for the respective week in the season.
- bias2_std: standard deviation of weighted difference between voter rank and mean ranks for the respective week in the season.
- bias3_mean: average weighted difference between voter rank and median rank for the respective week in the season.
- bias3_std: standard deviation of weighted difference between voter rank and median rank for the respective week in the season.
- bias0_ap_mean: average unweighted difference between voter rank and mean ranks for the respective week in the season.
- bias0_ap_std:  standard deviation of unweighted difference between voter rank and AP rank for the respective week in the season.
- bias0_mean_mean: average unweighted difference between voter rank and mean ranks for the respective week in the season.
- bias0_mean_std: standard deviation of unweighted difference between voter rank and mean ranks for the respective week in the season.

Dataset containing calculations of mean/std of the various bias measures for a given week of each season

### `team.csv`(WIP)
 - output - season,team,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std
 - calculates mean/std of bias for a given team of each season

### `voter.csv` (WIP)
 - output - season,voter,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std
 - calculates mean/std of bias for a given voter of each season

# README for output_data

## Files in this folder:

- `conference_bias_nc.png`
    - bar chart that shows the bias by conference, no correction

- `conference_bias.csv`
    - CSV that shows bias1, bias2, bias3, and bias0 by voter and conference
    - columns: voter,Conference,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean

- `conference_bias.png`
    - bar chart that shows the bias by conference, no correction

- `season_team_alt_relative.csv`
    - relative biases by season and team
    - columns: season,team,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean,n

- `season_team_alt.csv`
    - biases by season and team, alternate
    - columns: season,team,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean,n

- `season_team_nc.png`
    - bar chart of top 5 / bottom 5 season team pairs, no correction

- `season_team.csv`
    - biases by season and team
    - columns: season,team,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std,bias0_ap_mean,bias0_ap_std,bias0_mean_mean,bias0_mean_std

- `season_team.png`
    - bar chart of top 5 / bottom 5 season team pairs

- `season_voter_conference_biases.csv`
    - biases by season, voter, and conference
    - columns: voter,season,Conference,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean

- `season_voter_team.csv`
    - biases by season, voter, and team
    - columns: season,voter,team,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean

- `season_voter.csv`
    - biases by season and voter 
    - columns: season,voter,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std,bias0_ap_mean,bias0_ap_std,bias0_mean_mean,bias0_mean_std

- `season_week.csv`
    - biases by season and week
    - columns: season,week,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std,bias0_ap_mean,bias0_ap_std,bias0_mean_mean,bias0_mean_std

- `voter_team_nc.png`
    - bar chart of top 5 / bottom 5 voter team pairs, no correction

- `voter_team.csv`
    - biases by voter and team
    - columns: voter,team,bias1-a,bias1-b,bias1-c,bias2-a,bias2-b,bias2-c,bias3-a,bias3-b,bias3-c,bias0-ap,bias0-mean,n

- `voter_team.png`
    - bar chart of top 5 / bottom 5 voter team pairs

- `week_apbias_std.png`
    - line chart of the SD of AP, Mean, and Median bias, week-by-week

- `week_mean.png`
    - line chart of the mean of AP, Mean, and Median bias, week-by-week

- `week_mean_nc.png`
    - line chart of the mean of Spearman AP, Spearman Mean, uncorrected AP, and uncorrected mean, week-by-week

- `week_std_nc.png`
    - line chart of the SD of Spearman AP, Spearman Mean, uncorrected AP, and uncorrected mean, week-by-week

- `week_std.png`
    - line chart of the SD of AP, Mean, and Median bias, week-by-week



### 
<b>Column Meanings:</b>

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





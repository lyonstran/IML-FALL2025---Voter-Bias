# README for voter_team_biases

## Files in this folder: 

- `voter_team_biases.csv`

- `voter_team_biases.png`
  
- `voter_team_biases_nc.png`

### `voter_team_biases.csv`
<b>Columns:</b>

- Voter: name of voter corresponding to poll submitted by them.
- Team: name of team corresponding to poll.
- bias1-(a, b, c): ...
- bias2-(a, b, c): ...
- bias3-(a, b, c): ...
- bias0-ap: naive bias measure approach using difference between voter rank and AP rank.
- bias0-mean: naive bias measure approach using difference between voter rank and mean rank of corresponding team.
- n: number of times team is ranked by voter.

### `voter_team_biases.png`

Visulization capturing high and low end cases of voter-team biases using `voter_team_biases.csv` weighted bias measures. 

### `voter_team_biases_nc.png`

Visualization capturing high and low end cases of voter-team biases using `voter_team_biases.csv` naive bias measures. 

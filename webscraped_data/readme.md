# Original Datasets README
## This folder contains the following CSV files:

- `college_football_polls_original`
- `college_basketball_polls_original`
- `pollsters_2014_2024.csv`


### `college_football_polls_original.csv`

<b>Columns:</b>

- Pollster: voter name

- Season: records year in which season took place

- week: AP poll week number in the season

- 1, ..., 25 : columns 1 - 25 respresent the given rank by the corresponding voter for a given week, and records the approriate name of the team in a 'team-mascot' format.

### `college_basketball_polls_original.csv`

<b>Columns:</b>

- Pollster: voter name

- Season: records year in which season took place

- week: AP poll week number in the season

- 1, ..., 25 : columns 1 - 25 respresent the given rank by the corresponding voter for a given week, and records the approriate name of the team in a 'team-mascot' format.
  
These two datasets are the original files were provided to us at the start of this project and were used to make a lot of the reference files, visualizations, and analysis done for this project.  

---

### `pollsters_2014_2024.csv`

<b>Columns:</b>

- pollster_name: voter name.

- affiliation: newspaper/journal they work at at and/or for.

- city: city that they are based in.

- state: state that they are based in. 

- year: year that corresponds to their affiliation, city and state in which they participated in the AP polls

This dataset is meant to serve as a foundation for our analysis in to whether or not voter location/affiliation has an impact on voter biases. 
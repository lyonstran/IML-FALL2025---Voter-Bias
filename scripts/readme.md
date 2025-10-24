# README for Scripts

# create_auxiliary.py

Functions for generating aggregated bias CSV files:

- **`create_voter_team_biases(csv_path)`**  
   Biases per voter/team pair (averaged over seasons).

- **`create_voter_season_biases(csv_path)`**  
   Biases per voter/season pair (averaged over teams).

- **`create_season_voter_conference_biases(average_biases_csv, cfb_csv)`**  
   Biases per voter/conference/season combinations (averaged over teams in conference).

- **`create_voter_conference_biases(average_biases_csv, cfb_csv)`**  
   Biases per voter/conference combinations (averaged over seasons and teams).

- **`create_percentile_graph(input_csv):`**  
   AP Rank, Mean, and Median bias by percentile. 

- **`create_svc_graph(input_csv: str):`**  
   Bar graph of each conference and their total bias
   
- **`create_voterteam_pair(input_csv: str)::`**  
   Biases for top/bottom 10 ap rank biases for all voter-team pairs.

- **`create_seasonteam_pair(input_csv: str):`**  
   Biases for top/bottom 10 ap rank biases for all season-team pairs.

# create_conf_aff_cbb.py

Functions for generating College Basketball conference affiliation files

- **`process_poll_data_cbb(df, year):`**
   Inputs are original poll data and year. Reads HTML from corresponding college basketball season/year from sportsreference.com to map teams to respective conferences. Returns dataframe of teams with corresponding conferences for that specific season.

- **`normalize_school(school):`**
   Normalizes names of schools to fit our school naming convention in the files.

- **`def process_all_years_cbb(df):`**
   Script using `process_poll_data_cbb` to loop through all the years in poll data and return dataframe with all the years/seasons of teams with their respective conferences.

# create_conf_aff_cfb.py

Functions for generating College Basketball conference affiliation files

- **`standardize_conference_name(conf: str):`**
   Standardize imported conference names to match naming convention in files.

- **`process_poll_data_cfb(df, year):`**
   Inputs are original poll data and year. Reads HTML from corresponding college football season/year from sportsreference.com to map teams to respective conferences. Returns dataframe of teams with corresponding conferences for that specific season.

- **`process_all_years_cfb(df):`**
   Script using `process_poll_data_cfb` to loop through all the years in poll data and return dataframe with all the years/seasons of teams with their respective conferences.

# create_master_bias.csv.py

Script using `college_football_polls_original.csv` and `cfb_cam_output.csv` to make `cfb_master_bias.csv`, (WIP) Using `college_basketball_polls_original.csv` and `cbb_cam_output.csv` to make `cbb_master_bias.csv`.

# create_percentile_biases.py

Script using `cfb_master_bias.csv` to convert bias measures to make `cfb_percentile_biases.csv`. (WIP): Scipt using `cbb_master_bias.csv` to convert bias measures to make `cbb_percentile_biases.csv`.

# create_teams_voters_summary.py

Script using `cfb_master_bias.csv` to make `cfb_teams_summary.csv` and `cfb_voter_summary.csv`. (WIP): Script using `cbb_master_bias.csv` to make `cbb_teams_summary.csv` and `cbb_voter_summary.csv`. 

# create_master_relative_percentage_bias.py

Script using `college_football_polls_original.csv` and `cfb_cam_output.csv` to make `cfb_master_relative_percentage_bias.csv`. (WIP) Using `college_basketball_polls_original.csv` and `cbb_cam_output.csv` to make `cbb_master_relative_percentage_bias.csv`.
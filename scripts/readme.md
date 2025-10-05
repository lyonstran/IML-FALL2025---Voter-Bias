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

   
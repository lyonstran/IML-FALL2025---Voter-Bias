import pandas as pd

df = pd.read_csv(r"C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cfb\cfb_master_bias_file.csv")
df_filtered = df[df["ap_rank"].notnull()]
team_summary = (df_filtered.groupby("Team (t)", as_index = False).
                agg(appearances_AP25 = ("ap_rank", "count"), avg_rank = ("ap_rank", "mean")).
                rename(columns = {"Team (t)": "Team"}))
team_summary.to_csv('cfb_teams_summary.csv')

df = pd.read_csv(r"C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cfb\cfb_master_bias_file.csv")
df_filtered = df[df["ap_rank"].notnull()]
voter_summary = (df_filtered.groupby("Pollster (v)", as_index = False).
                 agg(appearances = ("ap_rank", "count")).
                 rename(columns = {"Pollster (v)": "Voter"}))
voter_summary.to_csv('cfb_voter_summary.csv')
import pandas as pd
from collections import defaultdict
import statistics

# input - (Pollster,Season,Week,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
# output - (team,year,week,ap_rank,average,median)
# given scraped data, finds ap_rank/average/median rank for each team in each week
def create_cam_rankings(csv_path: str): # for every team in a year/week, 
    df_cam = pd.DataFrame(columns=["team", "year", "week", "ap_rank", "average", "median"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 
    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') # to order numbers
    df_scraped['Week'] = pd.to_numeric(df_scraped['Week'], errors='coerce') # to order numbers

    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # go through by each week/year
        team_ranks = defaultdict(list) # map, (team -> all AP ranks for that week/year)
        for _, row in group.iterrows():
            for rank in range(1, 26):
                team_name = row.iloc[rank] 
                if pd.notna(team_name) and team_name != "":
                    team_ranks[team_name].append(rank)
                else:
                    team_ranks[team_name].append(26)
        
        team_points = {}
        for team, ranks in team_ranks.items():
            total_points = 0
            for rank in ranks:
                points = 26 - rank
                total_points += points
            team_points[team] = total_points
        
        filtered_team_points = {team: points for team, points in team_points.items() if isinstance(team, str) and team.strip() != "" and not team.isdigit()} # gets rid of week and year in DF
        sorted_teams = sorted(filtered_team_points.items(), key=lambda x: x[1], reverse=True) # from first to last, get summary statistics
        for ap_rank, (team, points) in enumerate(sorted_teams, 1):
            ranks = team_ranks[team]
            mean_rank = statistics.mean(ranks)
            mean_rank = round(mean_rank, 3)
            median_rank = statistics.median(ranks)
            
            new_row = {
                'team': team,
                'year': int(season),
                'week': int(week),
                'ap_rank': ap_rank if ap_rank <= 25 else 26,
                #'ap_rank': ap_rank, <- leave no cap on, which I'd assume would extend the ranks (if we want to go past 26) 
                #'points' : points, #<- would it be helpful to keep track of total points? 
                # ^^^^ the commented code I think would make sense if we want to try and extend beyond top 25, otherwise
                #           we could always set non ranked teams to 0; whichever makes most sense for our goals
                # I'm leaning towards maybe cutting out the non ranked teams? (you mentioned the average and median need to 
                # be determined) 
                'average': mean_rank, 
                'median': median_rank,  
            }
            
            df_cam.loc[len(df_cam)] = new_row
    df_cam.to_csv("cam_output.csv", index=False)
    return df_cam

# output - (year,week,voters)
# outputs all the voters for a given week
def create_voters(csv_path: str): # df of all voters in a certain week/year
    df_voters = pd.DataFrame(columns=["year", "week", "voters"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 

    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') 
    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # sort by week/year
        voters = set() # set of all voters
        for _, row in group.iterrows():
            voters.add(row["Pollster"]) # add all the voters into the set
        new_row = {
                'year': int(season),
                'week': int(week),
                'voters': tuple(voters), 
            }   # make the new row
        df_voters.loc[len(df_voters)] = new_row
    df_voters = df_voters.sort_values(['year', 'week']).reset_index(drop=True)   # organize df by week/year  
    df_voters.to_csv("create_voters_output.csv", index=False)
    return df_voters

# output - (year,week,teams)
# outputs all the teams for a given week
def create_teams(csv_path: str): # df of all teams in a certain week/year
    df_teams = pd.DataFrame(columns=["year", "week", "teams"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 

    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') 
    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # sort by week/year
        teams = set() # set of all teams
        for _, row in group.iterrows():
            for i in range (1, 26):
                teams.add(row[str(i)]) # add all the teams into the set
        new_row = {
                'year': int(season),
                'week': int(week),
                'teams': tuple(teams), 
            }   # make the new row
        df_teams.loc[len(df_teams)] = new_row
    df_teams = df_teams.sort_values(['year', 'week']).reset_index(drop=True)   # organize df by week/year  
    df_teams.to_csv("create_teams_output.csv", index=False)
    return df_teams

"""
Season, Voter, Team, avg bias over full season, avg bias of 1st half season, avg bias over 2nd half season.

bias(whole season/1st half of season/2nd half of season)-(concensus bias/average bias/median bias)

    bias1-a -> AP rank bias for full season
    bias2-a -> average bias for full season
    bias3-a -> median bias for full season
    bias1-b -> AP rank bias for first-half of the season
    bias2-b -> average bias for first-half of the season
    bias3-b -> median bias for first-half of the season
    bias1-c -> AP rank bias for second-half of the season
    bias2-c -> average bias for second-half of the season
    bias3-c -> median bias for second-half of the season
 


    EXAMPLE INPUT 

      Pollster (v)  Season  Week  Rank                 Team (t)  ap_rank  average  median  bias1(v, t)  bias2(v, t)  bias3(v, t)
0        adam-jude    2014     1     1  florida-state-seminoles      1.0    3.067     3.0     0.000000    -2.067000    -2.000000
60       adam-jude    2014     2     1  florida-state-seminoles      1.0    3.322     3.0     0.000000    -2.322000    -2.000000
119      adam-jude    2014     3     1  florida-state-seminoles      1.0    3.617     3.0     0.000000    -2.617000    -2.000000
179      adam-jude    2014     4     1  florida-state-seminoles      1.0    3.567     3.0     0.000000    -2.567000    -2.000000
239      adam-jude    2014     5     1  florida-state-seminoles      1.0    4.017     3.0     0.000000    -3.017000    -2.000000
299      adam-jude    2014     6     1  florida-state-seminoles      1.0    4.400     4.0     0.000000    -3.400000    -3.000000
359      adam-jude    2014     7     1  florida-state-seminoles      1.0    3.650     3.0     0.000000    -2.650000    -2.000000
10677    adam-jude    2014     8     2  florida-state-seminoles      2.0    4.417     5.0     0.000000    -1.208500    -1.500000
10737    adam-jude    2014     9     2  florida-state-seminoles      2.0    4.117     4.0     0.000000    -1.058500    -1.000000
10797    adam-jude    2014    10     2  florida-state-seminoles      2.0    3.783     4.0     0.000000    -0.891500    -1.000000
10857    adam-jude    2014    11     2  florida-state-seminoles      2.0    3.800     4.0     0.000000    -0.900000    -1.000000
10917    adam-jude    2014    12     2  florida-state-seminoles      2.0    3.898     4.0     0.000000    -0.949000    -1.000000
21234    adam-jude    2014    13     3  florida-state-seminoles      1.0    3.407     3.0     2.000000    -0.135667     0.000000
21293    adam-jude    2014    14     3  florida-state-seminoles      1.0    3.712     3.0     2.000000    -0.237333     0.000000
21352    adam-jude    2014    15     3  florida-state-seminoles      2.0    3.897     4.0     0.500000    -0.299000    -0.333333
21410    adam-jude    2014    16     3  florida-state-seminoles      2.0    4.068     4.0     0.500000    -0.356000    -0.333333
62501    adam-jude    2014    17     7  florida-state-seminoles      6.0    7.466     7.0     0.166667    -0.066571     0.000000

RESULT 
    season      voter      team                     bias1-a       bias1-b bias1-c   bias2-a   bias2-b   bias2-c  bias3-a    bias3-b  bias3-c
    2014        adam-jude  florida-state-seminoles  0.303922      0.0     0.574074  -1.455416 -2.481063 -0.54373 -1.245098  -2.0625  -0.518519

"""

def create_vt_biases(csv_path: str):
    df_biases = pd.DataFrame(columns=["season", "voter", "team", "bias1-a", "bias1-b", "bias1-c", "bias2-a", "bias2-b", "bias2-c", "bias3-a", "bias3-b", "bias3-c", "bias0-ap", "bias0-mean", "n"])
    df_input = pd.read_csv(csv_path)

    season_length = df_input['Week'].max() # find season length by max week
    half_way = int(season_length / 2) # find half-way point of season
    df_input = df_input.sort_values(['Season', 'Rank', 'Pollster (v)'])
    
    for (season, pollster, team), group in df_input.groupby(['Season', 'Pollster (v)', 'Team (t)'], sort=False):
        bias1_a = bias1_b = bias1_c = bias2_a = bias2_b = bias2_c = bias3_a = bias3_b = bias3_c = bias0_mean = bias0_ap = 0
        fh_rank_counter = 0
        sh_rank_counter = 0
        
        for i in range(1, half_way + 1): # iterate by first half of the season 
            week_data = group[group["Week"] == i]
            if len(week_data) > 0:  # if there is data for that team for that week, add it to the sum 
                fh_rank_counter += 1
                bias0_ap += week_data["Rank"].iloc[0] - week_data["ap_rank"].iloc[0]
                bias0_mean += week_data["Rank"].iloc[0] - week_data["average"].iloc[0]
                bias1_a += week_data["bias1(v, t)"].sum()
                bias2_a += week_data["bias2(v, t)"].sum()
                bias3_a += week_data["bias3(v, t)"].sum()
                bias1_b += week_data["bias1(v, t)"].sum()
                bias2_b += week_data["bias2(v, t)"].sum()
                bias3_b += week_data["bias3(v, t)"].sum()
        
        for i in range(half_way + 1, season_length + 1):
            week_data = group[group["Week"] == i]
            if len(week_data) > 0:  
                sh_rank_counter += 1 # if there is data for that team for that week, add it to the sum
                bias0_ap += week_data["Rank"].iloc[0] - week_data["ap_rank"].iloc[0]
                bias0_mean += week_data["Rank"].iloc[0] - week_data["average"].iloc[0]
                bias1_a += week_data["bias1(v, t)"].sum()
                bias2_a += week_data["bias2(v, t)"].sum()
                bias3_a += week_data["bias3(v, t)"].sum()
                bias1_c += week_data["bias1(v, t)"].sum()
                bias2_c += week_data["bias2(v, t)"].sum()
                bias3_c += week_data["bias3(v, t)"].sum()
        
        n = fh_rank_counter + sh_rank_counter
        # find averages of each bias counter
        if (fh_rank_counter + sh_rank_counter) > 0:
            bias1_a = bias1_a / (fh_rank_counter + sh_rank_counter)
            bias2_a = bias2_a / (fh_rank_counter + sh_rank_counter)
            bias3_a = bias3_a / (fh_rank_counter + sh_rank_counter)
        
        if fh_rank_counter > 0:
            bias1_b = bias1_b / fh_rank_counter
            bias2_b = bias2_b / fh_rank_counter
            bias3_b = bias3_b / fh_rank_counter
        
        if sh_rank_counter > 0:
            bias1_c = bias1_c / sh_rank_counter
            bias2_c = bias2_c / sh_rank_counter
            bias3_c = bias3_c / sh_rank_counter
        
        new_row = {
            'season': int(season),
            'voter': pollster,
            'team': team,
            'bias1-a': bias1_a,
            'bias2-a': bias2_a,
            'bias3-a': bias3_a,
            'bias1-b': bias1_b,
            'bias2-b': bias2_b,
            'bias3-b': bias3_b,
            'bias1-c': bias1_c,
            'bias2-c': bias2_c,
            'bias3-c': bias3_c,
            'bias0-ap': bias0_ap,
            'bias0-mean': bias0_mean,
            'n': n,
        }
        df_biases.loc[len(df_biases)] = new_row    

    df_biases = df_biases.sort_values(['season', 'voter']).reset_index(drop=True)
    numeric_columns = ['bias1-a', 'bias1-b', 'bias1-c', 'bias2-a', 'bias2-b', 'bias2-c', 'bias3-a', 'bias3-b', 'bias3-c', 'bias0-ap', 'bias0-mean', 'n'] # round
    df_biases[numeric_columns] = df_biases[numeric_columns].round(4)
    df_biases.to_csv("average_biases.csv", index=False)
    return df_biases

# output - season,week,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std
# calculates mean/std of bias for a given week of each season
def biases_summary_by_week(csv_path: str):
    df_biases = pd.DataFrame(columns=["season", "week", "bias1_mean", "bias1_std", "bias2_mean", "bias2_std", "bias3_mean", "bias3_std", 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std'])
    df_input = pd.read_csv(csv_path)
    for (season, week), group in df_input.groupby(['Season', 'Week'], sort=False):
        mean_1 = group["bias1(v, t)"].mean()
        std_1 = group["bias1(v, t)"].std()
        mean_2 = group["bias2(v, t)"].mean()
        std_2 = group["bias2(v, t)"].std()
        mean_3 = group["bias3(v, t)"].mean()
        std_3 = group["bias3(v, t)"].std()
        mean_0_ap = group["bias0(v, t)_ap"].mean()
        std_0_ap = group["bias0(v, t)_ap"].std()
        mean_0_mean = group["bias0(v, t)_mean"].mean()
        std_0_mean = group["bias0(v, t)_mean"].std()

        new_row = {
            'season': int(season),
            'week': week,
            'bias1_mean': mean_1,    
            'bias1_std': std_1,
            'bias2_mean': mean_2,
            'bias2_std': std_2,
            'bias3_mean': mean_3,
            'bias3_std': std_3,
            'bias0_ap_mean': mean_0_ap,
            'bias0_ap_std': std_0_ap,
            'bias0_mean_mean': mean_0_mean,
            'bias0_mean_std': std_0_mean,
        }
        df_biases.loc[len(df_biases)] = new_row   
    numeric_columns = ['bias1_mean', 'bias1_std', 'bias2_mean', 'bias2_std', 'bias3_mean', 'bias3_std', 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std'] # round
    df_biases[numeric_columns] = df_biases[numeric_columns].round(4)
    df_biases.to_csv("summary_stats_by_week.csv", index=False)
    df_biases = df_biases.sort_values(['season', 'week']).reset_index(drop=True)
    return df_biases

# output - season,team,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std
# calculates mean/std of bias for a given team of each season

def biases_summary_by_team(csv_path: str):
    df_biases = pd.DataFrame(columns=["season", "team", "bias1_mean", "bias1_std", "bias2_mean", "bias2_std", "bias3_mean", "bias3_std", 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std', 'n'])
    df_input = pd.read_csv(csv_path)
    df_input = df_input.sort_values(['Season', 'Team (t)'])
    for (season, team), group in df_input.groupby(['Season', 'Team (t)'], sort=False):
        mean_1 = group["bias1(v, t)"].mean()
        std_1 = group["bias1(v, t)"].std()
        mean_2 = group["bias2(v, t)"].mean()
        std_2 = group["bias2(v, t)"].std()
        mean_3 = group["bias3(v, t)"].mean()
        std_3 = group["bias3(v, t)"].std()
        mean_0_ap = group["bias0(v, t)_ap"].mean()
        std_0_ap = group["bias0(v, t)_ap"].std()
        mean_0_mean = group["bias0(v, t)_mean"].mean()
        std_0_mean = group["bias0(v, t)_mean"].std()
        n = len(group)

        new_row = {
            'season': int(season),
            'team': team,
            'bias1_mean': mean_1,    
            'bias1_std': std_1,
            'bias2_mean': mean_2,
            'bias2_std': std_2,
            'bias3_mean': mean_3,
            'bias3_std': std_3,
            'bias0_ap_mean': mean_0_ap,
            'bias0_ap_std': std_0_ap,
            'bias0_mean_mean': mean_0_mean,
            'bias0_mean_std': std_0_mean,
            'n': n,
        }
        df_biases.loc[len(df_biases)] = new_row
    numeric_columns = ['bias1_mean', 'bias1_std', 'bias2_mean', 'bias2_std', 'bias3_mean', 'bias3_std', 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std', 'n'] # round
    df_biases[numeric_columns] = df_biases[numeric_columns].round(4)   
    df_biases.to_csv("ss_team.csv", index=False)
    df_biases = df_biases.sort_values(['season', 'team']).reset_index(drop=True)
    return df_biases

# output - season,voter,bias1_mean,bias1_std,bias2_mean,bias2_std,bias3_mean,bias3_std
# calculates mean/std of bias for a given voter of each season
def biases_summary_by_voter(csv_path: str):
    df_biases = pd.DataFrame(columns=["season", "voter", "bias1_mean", "bias1_std", "bias2_mean", "bias2_std", "bias3_mean", "bias3_std", 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std', 'n'])
    df_input = pd.read_csv(csv_path)
    df_input = df_input.sort_values(['Season', 'Pollster (v)'])
    for (season, voter), group in df_input.groupby(['Season', 'Pollster (v)'], sort=False):
        mean_1 = group["bias1(v, t)"].mean()
        std_1 = group["bias1(v, t)"].std()
        mean_2 = group["bias2(v, t)"].mean()
        std_2 = group["bias2(v, t)"].std()
        mean_3 = group["bias3(v, t)"].mean()
        std_3 = group["bias3(v, t)"].std()
        mean_0_ap = group["bias0(v, t)_ap"].mean()
        std_0_ap = group["bias0(v, t)_ap"].std()
        mean_0_mean = group["bias0(v, t)_mean"].mean()
        std_0_mean = group["bias0(v, t)_mean"].std()
        n = len(group)

        new_row = {
            'season': int(season),
            'voter': voter,
            'bias1_mean': mean_1,    
            'bias1_std': std_1,
            'bias2_mean': mean_2,
            'bias2_std': std_2,
            'bias3_mean': mean_3,
            'bias3_std': std_3,
            'bias0_ap_mean': mean_0_ap,
            'bias0_ap_std': std_0_ap,
            'bias0_mean_mean': mean_0_mean,
            'bias0_mean_std': std_0_mean,
            'n': n,
        }
        df_biases.loc[len(df_biases)] = new_row   
    numeric_columns = ['bias1_mean', 'bias1_std', 'bias2_mean', 'bias2_std', 'bias3_mean', 'bias3_std', 'bias0_ap_mean', 'bias0_ap_std', 'bias0_mean_mean', 'bias0_mean_std', 'n'] # round
    df_biases[numeric_columns] = df_biases[numeric_columns].round(4)
    df_biases.to_csv("ss_voter.csv", index=False)
    df_biases = df_biases.sort_values(['season', 'voter']).reset_index(drop=True)
    return df_biases

# def create_voter_team_biases(csv_path: str):
#     df_input = pd.read_csv(csv_path)
#     counts = df_input.groupby(['voter', 'team'], sort=False).size().reset_index(name='n')
#     df_input = df_input.groupby(['voter', 'team'], sort=False).agg({'bias1-a': 'mean', 'bias1-b': 'mean', 'bias1-c': 'mean', 'bias2-a': 'mean', 'bias2-b': 'mean', 'bias2-c': 'mean', 'bias3-a': 'mean', 'bias3-b': 'mean', 'bias3-c': 'mean', 'bias0-ap': 'mean', 'bias0-mean': 'mean'}).reset_index()
#     df_input = df_input.merge(counts, on=['voter', 'team'])
#     df_input.to_csv("voter_team_biases.csv", index=False)
#     return df_input

# ^^^^^old^^^^^
#\/\/\/\corrected (right number of rows) /\/\/\/

# def create_voter_team(csv_path: str):  # <- uses msater_bias.csv to do this
#     df_input = pd.read_csv(csv_path)
#     df_input = df_input.sort_values(['Pollster (v)', 'Team (t)'])
    
#     df_summary = pd.DataFrame(columns=[
#         "voter", "team",
#         "bias1", "bias2", "bias3",
#         "bias0_ap", "bias0_mean", "n"
#     ])
    
#     for (voter, team), group in df_input.groupby(['Pollster (v)', 'Team (t)'], sort=False):
#         new_row = {
#             'voter': voter,
#             'team': team,
#             'bias1': group["bias1(v, t)"].mean(),
#             'bias2': group["bias2(v, t)"].mean(),
#             'bias3': group["bias3(v, t)"].mean(),
#             'bias0_ap': group["bias0(v, t)_ap"].mean(),
#             'bias0_mean': group["bias0(v, t)_mean"].mean(),
#             'n': len(group)
#         }
#         df_summary.loc[len(df_summary)] = new_row
    
#     numeric_cols = ['bias1', 'bias2', 'bias3', 'bias0_ap', 'bias0_mean']
#     df_summary[numeric_cols] = df_summary[numeric_cols].astype(float)
    
#     df_summary = df_summary.sort_values(['voter', 'team']).reset_index(drop = True)
#     df_summary.to_csv("voter_team.csv", index = False)
#     return df_summary

##\/\/\/\/newest\/\/\/\/\/
def create_voter_team(csv_path: str):
    df = pd.read_csv(csv_path)
    df = df.sort_values(['voter', 'team'])

    grouped = df.groupby(['voter', 'team'], sort = False)

    df_summary = grouped.agg({
        'bias1-a': 'mean',
        'bias1-b': 'mean',
        'bias1-c': 'mean',
        'bias2-a': 'mean',
        'bias2-b': 'mean',
        'bias2-c': 'mean',
        'bias3-a': 'mean',
        'bias3-b': 'mean',
        'bias3-c': 'mean',
        'bias0-ap': 'mean',
        'bias0-mean': 'mean'
    }).reset_index()

    df_summary['n'] = grouped.size().values
    # df_summary.rename(columns = {
    #     'Pollster (v)': 'voter',
    #     'Team (t)': 'team'
    # }, inplace = True)

    df_summary.to_csv("voter_team.csv", index=False)
    return df_summary




def create_season_team_biases(csv_path: str):
    df_input = pd.read_csv(csv_path)
    counts = df_input.groupby(['season', 'team'], sort=False).size().reset_index(name='n')
    df_input = df_input.groupby(['season', 'team'], sort=False).agg({'bias1-a': 'mean', 'bias1-b': 'mean', 'bias1-c': 'mean', 'bias2-a': 'mean', 'bias2-b': 'mean', 'bias2-c': 'mean', 'bias3-a': 'mean', 'bias3-b': 'mean', 'bias3-c': 'mean', 'bias0-ap': 'mean', 'bias0-mean': 'mean'}).reset_index()
    df_input = df_input.merge(counts, on=['season', 'team'])
    df_input.to_csv("season_team_biases.csv", index=False)
    return df_input

def create_season_voter_conference_biases(average_biases_csv, cfb_csv: str):
    df_ab = pd.read_csv(average_biases_csv)
    df_c = pd.read_csv(cfb_csv)
    df_ab = df_ab.merge(
        df_c[['Season', 'Team', 'Conference']], 
        left_on=['season', 'team'], 
        right_on=['Season', 'Team'], 
        how='left'
    )
    df_ab = df_ab.drop(columns=['Season', 'Team'])
    df_ab = df_ab.groupby(['voter','season', 'Conference'], sort=False).agg({'bias1-a': 'mean', 'bias1-b': 'mean', 'bias1-c': 'mean', 'bias2-a': 'mean', 'bias2-b': 'mean', 'bias2-c': 'mean', 'bias3-a': 'mean', 'bias3-b': 'mean', 'bias3-c': 'mean', 'bias0-ap': 'mean', 'bias0-mean': 'mean', 'team': 'size'}).reset_index()

    df_ab = df_ab.rename(columns={'team': 'n'})
    df_ab.to_csv("season_voter_conference_biases.csv", index=False)
    return df_ab

def create_voter_conference_biases(average_biases_csv, cfb_csv: str):
    print("PRINT", average_biases_csv)
    df_ab = pd.read_csv(average_biases_csv)
    df_c = pd.read_csv(cfb_csv)
    df_ab = df_ab.merge(
        df_c[['Season', 'Team', 'Conference']], 
        left_on=['season', 'team'], 
        right_on=['Season', 'Team'], 
        how='left'
    )
    df_ab = df_ab.drop(columns=['Season', 'Team'])
    df_ab = df_ab.groupby(['voter','Conference'], sort=False).agg({'bias1-a': 'mean', 'bias1-b': 'mean', 'bias1-c': 'mean', 'bias2-a': 'mean', 'bias2-b': 'mean', 'bias2-c': 'mean', 'bias3-a': 'mean', 'bias3-b': 'mean', 'bias3-c': 'mean', 'bias0-ap': 'mean', 'bias0-mean': 'mean', 'team': 'size'}).reset_index()

    df_ab = df_ab.rename(columns={'team': 'n'})
    df_ab.to_csv("voter_conference_biases.csv", index=False)
    return df_ab
    


if __name__ == "__main__":
    #df_rankings = create_cam_rankings("original_data/college_basketball_polls_original.csv")
    #df_voters = create_teams("/Users/albertbogdan/IML-FALL2025---Voter-Bias/original_data/college_basketball_polls_original.csv")
    #create_voter_conference_biases("/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/output_data/season_voter_relative.csv", "/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/original_data/conference_affiliation.csv")
    #create_vt_biases("results/cfb/original_data/master_bias.csv")
    #create_season_team_biases("output_data/cfb/original/average_biases.csv")
    #biases_summary_by_team("output_data/cfb/relative/cfb_master_relative_percentage_bias.csv")
    #biases_summary_by_voter("results/cfb/original_data/master_bias.csv")
    create_voter_team(r'C:\Users\Lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\results\cfb\output_data\season_voter_team.csv')          
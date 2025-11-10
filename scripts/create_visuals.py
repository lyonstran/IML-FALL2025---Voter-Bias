import pandas as pd
import matplotlib.pyplot as plt

def graph_weekly_bias(input_csv: str): # get weekly bias visuals for mean and std
    graph_weekly_bias_mean(input_csv)
    graph_weekly_bias_std(input_csv)

def graph_weekly_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df = df.groupby('week').agg({'bias1-mean': 'mean', 'bias1-std': 'mean', 'bias2-mean': 'mean', 'bias2-std': 'mean', 'bias3-mean': 'mean', 'bias3-std': 'mean', 'bias0-ap-mean' : 'mean', 'bias0-ap-std' : 'mean', 'bias0-mean-mean' : 'mean', 'bias0-mean-std' : 'mean'}).reset_index()
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    scale_factor = 0.1
    df['bias0-ap-mean'] *= 0.1
    df['bias0-mean-mean'] *= 0.1
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias0-ap-mean'], 'o-', label='AP', linewidth=4, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias0-mean-mean'], 's-', label='Mean', linewidth=4, markersize=3)
    plt.plot(df['plot_index'], df['bias1-mean'], '^-', label='Spearman AP', linewidth=4, markersize=3)
    plt.plot(df['plot_index'], df['bias2-mean'], 'o-', label='Spearman Mean', linewidth=4, markersize=3)
   
    plt.xticks(fontsize=23) 
    plt.yticks(fontsize=14) 
    plt.xlabel('Week', fontsize=23)
    plt.ylabel('Average of Bias (Without Correction)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_week_mean.png') 

def graph_weekly_bias_std(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df = df.groupby('week').agg({'bias1-mean': 'std', 'bias1-std': 'mean', 'bias2-mean': 'mean', 'bias2-std': 'mean', 'bias3-mean': 'mean', 'bias3-std': 'mean', 'bias0-ap-mean' : 'mean', 'bias0-ap-std' : 'mean', 'bias0-mean-mean' : 'mean', 'bias0-mean-std' : 'mean'}).reset_index()
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    scale_factor = 0.1
    df['bias0-ap-mean'] *= 0.1
    df['bias0-mean-mean'] *= 0.1
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias0-ap-std'], 'o-', label='AP', linewidth=4, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias0-mean-std'], 's-', label='Mean', linewidth=4, markersize=3)
    plt.plot(df['plot_index'], df['bias1-std'], '^-', label='Spearman AP', linewidth=4, markersize=3)
    plt.plot(df['plot_index'], df['bias2-std'], 'o-', label='Spearman Mean', linewidth=4, markersize=3)
   
    #plt.plot(df['plot_index'], df['bias1_std'], 'o-', linewidth=4, markersize=3) # set up the lines
    # plt.plot(df['plot_index'], df['bias2_std'], 's-', label='Mean', linewidth=2, markersize=3)
    # plt.plot(df['plot_index'], df['bias3_std'], '^-', label='Median', linewidth=2, markersize=3)
   
    plt.xticks(df['plot_index'], df['week'])  
    plt.xlabel('Week', fontsize=12) 
    
    plt.xticks(fontsize=23) 
    plt.yticks(fontsize=14) 
    plt.xlabel('Week', fontsize=23)
    plt.ylabel('Standard Deviation of Bias (Without Correction)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_week_std.png')

def graph_team_bias(input_csv: str): # runs team bias
    graph_team_bias_ap(input_csv)
    graph_team_bias_mean(input_csv)

def graph_team_bias_ap(input_csv: str):
    df = pd.read_csv(input_csv)
    team_avg_bias = df.groupby('team')['bias1_mean'].mean().sort_values() # group by year so each row is a different team 
    first_10 = team_avg_bias.head(10)
    last_10 = team_avg_bias.tail(10)
    team_avg_bias = pd.concat([first_10, last_10])

    plt.figure(figsize=(20, 8))  
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=10, ha='center')  
    plt.yticks(fontsize=12)
    plt.ylabel("Average AP Rank Bias", fontsize=14)
    plt.title("Average Bias per Team", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.subplots_adjust(bottom=0.25)  
    plt.tight_layout()
    plt.savefig('cfb_ss_team_visual_ap.png')

def graph_team_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)

    team_avg_bias = df.groupby('team')['bias2_mean'].mean().sort_values()
    first_10 = team_avg_bias.head(10)
    last_10 = team_avg_bias.tail(10)
    team_avg_bias = pd.concat([first_10, last_10])

    plt.figure(figsize=(20, 8))  
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=10, ha='center')  
    plt.yticks(fontsize=12)
    plt.ylabel("Average Mean Bias", fontsize=14)
    plt.title("Average Bias per Team", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.subplots_adjust(bottom=0.25)  
    plt.tight_layout()
    plt.savefig('cfb_ss_team_visual_mean.png')

def graph_voter_bias(input_csv: str): # runs voter bias
    graph_voter_bias_ap(input_csv)
    graph_voter_bias_mean(input_csv)

def graph_voter_bias_ap(input_csv: str):
    df = pd.read_csv(input_csv)
    team_avg_bias = df.groupby('voter')['bias1_mean'].mean().sort_values() # group by year so each row is a different team 
    first_10 = team_avg_bias.head(10)
    last_10 = team_avg_bias.tail(10)
    team_avg_bias = pd.concat([first_10, last_10])

    plt.figure(figsize=(20, 8))  
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=10, ha='center')  
    plt.yticks(fontsize=12)
    plt.ylabel("Average AP Rank Bias", fontsize=14)
    plt.title("Average Bias per Voter", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.subplots_adjust(bottom=0.25)  
    plt.tight_layout()
    plt.savefig('cfb_ss_voter_visual_ap.png')

def graph_voter_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)
    team_avg_bias = df.groupby('voter')['bias2_mean'].mean().sort_values()
    first_10 = team_avg_bias.head(10)
    last_10 = team_avg_bias.tail(10)
    team_avg_bias = pd.concat([first_10, last_10])

    plt.figure(figsize=(20, 8))  
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=10, ha='center')  
    plt.yticks(fontsize=12)
    plt.ylabel("Average Mean Bias", fontsize=14)
    plt.title("Average Bias per Voter", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.subplots_adjust(bottom=0.25)  
    plt.tight_layout()
    plt.savefig('cfb_ss_voter_visual_mean.png')

def create_percentile_graph(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.reset_index(drop=True)
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias1(p)'], 'o-', label='AP Rank', linewidth=2, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias2(p)'], 's-', label='Mean', linewidth=2, markersize=3)
    plt.plot(df['plot_index'], df['bias3(p)'], '^-', label='Median', linewidth=2, markersize=3)
   
    tick_positions = [i for i in range(len(df)) if df.loc[i, 'Percentile'] in [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]]
    tick_labels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]
    plt.xticks(tick_positions, tick_labels)
    
    plt.title('Voter Bias Measurements', fontsize=16, fontweight='bold')
    plt.xlabel('Percentile', fontsize=12)
    plt.ylabel('Bias (mean)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('avg_percentile.png') 

def create_svc_graph(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.reset_index(drop=True)
    
    df_grouped = df.groupby('conference').agg({'bias1-a': 'mean'}).reset_index()
    # df_grouped["Conference" == 'SEC'] = df_grouped[df_grouped["Conference"] == 'sec']
    # df_grouped['BIG 10'] = df_grouped[df_grouped["Conference"] == 'big-ten']
    # df_grouped['MAC'] = df_grouped[df_grouped["Conference"] == 'mac']
    # df_grouped['ACC'] = df_grouped['acc']
    # df_grouped['BIG 12'] = df_grouped['big-12']
    # df_grouped['PAC 12'] = df_grouped['pac-12']
    # df_grouped['CUSA'] = df_grouped['cusa']
    # df_grouped['AMERICAN'] = df_grouped['american']
    # df_grouped['MWC'] = df_grouped['mwc']
    # df_grouped['SUN BELT'] = df_grouped['sun-belt']

    df_grouped = df_grouped.sort_values('bias1-a')  # sort by bias value
    # df_grouped = df_grouped[df_grouped['conference'] != "mvfc" & df_grouped['Conference'] != "sec" & df_grouped['Conference'] != "big-ten" & df_grouped['Conference'] != "mac" & df_grouped['Conference'] != "acc" & df_grouped['Conference'] != "big-12" & df_grouped['Conference'] != "pac-12" & df_grouped['Conference'] != "cusa" & df_grouped['Conference'] != "american" & df_grouped['Conference'] != "mwc" & df_grouped['Conference'] != "sun-belt"] 
    df_grouped = df_grouped[df_grouped['conference'] != "mvfc"]
    print(df_grouped)
    y_ticks = ['SEC', 'BIG 10', 'MAC', 'ACC', 'BIG 12', 'PAC 12', 'CUSA', 'AMERICAN', 'MWC', 'SUN BELT']
    values = [9, 8, 7, 6, 5, 4, 3 ,2, 1, 0]
    df_grouped['bias1-a'] = df_grouped['bias1-a'] * 2 - 1
    
    plt.figure(figsize=(14, 8))
    
    bars = plt.barh(df_grouped['conference'], df_grouped['bias1-a'], 
                   color='steelblue', edgecolor='black', linewidth=1.2)
    
    for i, bar in enumerate(bars):
        if df_grouped.iloc[i]['bias1-a'] < 0:
            bar.set_color('indianred')
        else:
            bar.set_color('mediumseagreen')
    
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)

    plt.xticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1], fontsize=21) 
    plt.xlim(-0.5, 0.5)
    plt.yticks(values, y_ticks, fontsize=21) 
    plt.ylabel('Conference', fontsize=21)
    plt.xlabel('Bias', fontsize=21)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('conference_bias.png')

def create_voterteam_pair(input_csv: str, master_csv: str, min_votes: int = 500):
    analysis_df = pd.read_csv(master_csv)
    voter_vote_counts = analysis_df.groupby('Pollster (v)').size().reset_index()
    voter_vote_counts.columns = ['voter', 'total_votes']
    # add the total votes as a column 
    
    df = pd.read_csv(input_csv)
    df = df.merge(voter_vote_counts, on='voter')
    
    df = df[df['total_votes'] >= min_votes]
    
    df = df.sort_values('bias1-a')
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    df_plot = pd.concat([bottom_5, top_5])
    df_plot['label'] = df_plot['voter'] + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    bars = plt.barh(df_plot['label'], df_plot['bias1-a'], edgecolor='black', linewidth=1)
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias1-a']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('Bias', fontsize=21)
    plt.ylabel('Voter/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('voterteam_bias.png')

def create_seasonteam_pair_old(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.sort_values('bias1-a')
    
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    df_plot = pd.concat([bottom_5, top_5])
    
    df_plot['label'] = df_plot['season'].astype(str) + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    
    bars = plt.barh(df_plot['label'], df_plot['bias1-a'], edgecolor='black', linewidth=1)
    
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias1-a']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('Bias', fontsize=21)
    plt.ylabel('Season/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('seasonteam_bias.png')

import numpy as np
def graph_weekly_ap_bias_boxplot(input_csv: str):
    df = pd.read_csv(input_csv)
    fig, axes = plt.subplots(1, 1, figsize=(20, 6))
    
    weeks = sorted(df['week'].unique())
    bias1_data = [df[df['week'] == week]['bias1_mean'].dropna().values for week in weeks]
    
    bp1 = axes.boxplot(bias1_data, labels=weeks, patch_artist=True)
    axes.set_title('AP Rank Bias', fontsize=14, fontweight='bold')
    axes.set_xlabel('Week', fontsize=12)
    axes.set_ylabel('Bias', fontsize=12)
    axes.grid(True, alpha=0.3)

    for patch in bp1['boxes']:
        patch.set_facecolor('lightblue')
    
    plt.tight_layout()
    plt.savefig('ap_weekly_boxplot.png')
    plt.close()

def graph_weekly_mean_bias_boxplot(input_csv: str):
    df = pd.read_csv(input_csv)
    fig, axes = plt.subplots(1, 1, figsize=(20, 6))
    
    weeks = sorted(df['week'].unique())
    bias1_data = [df[df['week'] == week]['bias2_mean'].dropna().values for week in weeks]
    
    bp1 = axes.boxplot(bias1_data, labels=weeks, patch_artist=True)
    axes.set_title('Mean Bias', fontsize=14, fontweight='bold')
    axes.set_xlabel('Week', fontsize=12)
    axes.set_ylabel('Bias', fontsize=12)
    axes.grid(True, alpha=0.3)

    for patch in bp1['boxes']:
        patch.set_facecolor('lightblue')
    
    plt.tight_layout()
    plt.savefig('mean_weekly_boxplot.png')
    plt.close()

def create_svc_graph_uncorrected(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.reset_index(drop=True)
    
    df_grouped = df.groupby('Conference').agg({'bias0-ap': 'mean'}).reset_index()
    # df_grouped["Conference" == 'SEC'] = df_grouped[df_grouped["Conference"] == 'sec']
    # df_grouped['BIG 10'] = df_grouped[df_grouped["Conference"] == 'big-ten']
    # df_grouped['MAC'] = df_grouped[df_grouped["Conference"] == 'mac']
    # df_grouped['ACC'] = df_grouped['acc']
    # df_grouped['BIG 12'] = df_grouped['big-12']
    # df_grouped['PAC 12'] = df_grouped['pac-12']
    # df_grouped['CUSA'] = df_grouped['cusa']
    # df_grouped['AMERICAN'] = df_grouped['american']
    # df_grouped['MWC'] = df_grouped['mwc']
    # df_grouped['SUN BELT'] = df_grouped['sun-belt']

    df_grouped = df_grouped.sort_values('bias0-ap')  # sort by bias value
    df_grouped['bias0-ap'] *= 0.1
    # df_grouped = df_grouped[df_grouped['Conference'] != "mvfc" & df_grouped['Conference'] != "sec" & df_grouped['Conference'] != "big-ten" & df_grouped['Conference'] != "mac" & df_grouped['Conference'] != "acc" & df_grouped['Conference'] != "big-12" & df_grouped['Conference'] != "pac-12" & df_grouped['Conference'] != "cusa" & df_grouped['Conference'] != "american" & df_grouped['Conference'] != "mwc" & df_grouped['Conference'] != "sun-belt"] 
    df_grouped = df_grouped[df_grouped['Conference'] != "mvfc"]
    print(df_grouped)
    y_ticks = ['SEC', 'BIG 10', 'MAC', 'ACC', 'BIG 12', 'PAC 12', 'CUSA', 'AMERICAN', 'MWC', 'SUN BELT']
    values = [9, 8, 7, 6, 5, 4, 3 ,2, 1, 0]
    
    plt.figure(figsize=(14, 8))
    
    bars = plt.barh(df_grouped['Conference'], df_grouped['bias0-ap'], 
                   color='steelblue', edgecolor='black', linewidth=1.2)
    
    for i, bar in enumerate(bars):
        if df_grouped.iloc[i]['bias0-ap'] < 0:
            bar.set_color('indianred')
        else:
            bar.set_color('mediumseagreen')
    
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)

    plt.xticks(fontsize=21) 
    plt.yticks(values, y_ticks, fontsize=21) 
    plt.ylabel('Conference', fontsize=21)
    plt.xlabel('Bias (uncorrected)', fontsize=21)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('conference_bias.png')

def create_voterteam_pair(input_csv: str, master_csv: str, min_votes: int = 0):
    analysis_df = pd.read_csv(master_csv)
    voter_vote_counts = analysis_df.groupby('pollster (v)').size().reset_index()
    voter_vote_counts.columns = ['voter', 'total_votes']
    # add the total votes as a column 
    
    df = pd.read_csv(input_csv)
    df = df.merge(voter_vote_counts, on='voter')
    
    df = df[df['total_votes'] >= min_votes]
    
    df = df.sort_values('bias1-a')
    df['bias1-a'] = df['bias1-a'] * 2 - 1
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    df_plot = pd.concat([bottom_5, top_5])
    df_plot['label'] = df_plot['voter'] + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    bars = plt.barh(df_plot['label'], df_plot['bias1-a'], edgecolor='black', linewidth=1)
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias1-a']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('Bias', fontsize=21)
    plt.ylabel('Voter/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('voterteam_bias.png')

def create_seasonteam_pair(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.groupby(['season', 'team']).agg({'bias1-a': 'mean'}).reset_index()
    df = df.sort_values('bias1-a')
    df['bias1-a'] = df['bias1-a'] * 2 - 1
    print(df)
    
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    print("TOP", top_5)
    print("BOTTOM 5", bottom_5)
    df_plot = pd.concat([bottom_5, top_5])
    
    df_plot['label'] = df_plot['season'].astype(str) + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    
    bars = plt.barh(df_plot['label'], df_plot['bias1-a'], edgecolor='black', linewidth=1)
    
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias1-a']]
    for bar, color in zip(bars, colors):
        print(bar)
        bar.set_color(color)
    
    plt.xticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1], fontsize=21) 
    plt.xlim(-1, 1)
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('Bias', fontsize=21)
    plt.ylabel('Season/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('seasonteam_bias.png')

def create_voterteam_pair_nc(input_csv: str, master_csv: str, min_votes: int = 500):
    analysis_df = pd.read_csv(master_csv)
    voter_vote_counts = analysis_df.groupby('Pollster (v)').size().reset_index()
    voter_vote_counts.columns = ['voter', 'total_votes']
    # add the total votes as a column 
    
    df = pd.read_csv(input_csv)
    df = df.merge(voter_vote_counts, on='voter')
    
    df = df[df['total_votes'] >= min_votes]
    
    df = df.sort_values('bias0-ap')
    df["bias0-ap"] *= 0.1
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    df_plot = pd.concat([bottom_5, top_5])
    df_plot['label'] = df_plot['voter'] + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    bars = plt.barh(df_plot['label'], df_plot['bias0-ap'], edgecolor='black', linewidth=1)
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias0-ap']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('AP Bias (no correction), scaled by 0.1', fontsize=21)
    plt.ylabel('Voter/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('voterteam_bias.png')

def create_seasonteam_pair_nc(input_csv: str):
    df = pd.read_csv(input_csv)
    df = df.sort_values('bias0-ap')
    df["bias0-ap"] *= 0.1
    
    bottom_5 = df.head(5)
    top_5 = df.tail(5)
    df_plot = pd.concat([bottom_5, top_5])
    
    df_plot['label'] = df_plot['season'].astype(str) + ' - ' + df_plot['team']
    
    plt.figure(figsize=(14, 10))
    
    bars = plt.barh(df_plot['label'], df_plot['bias0-ap'], edgecolor='black', linewidth=1)
    
    colors = ['indianred' if x < 0 else 'mediumseagreen' for x in df_plot['bias0-ap']]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.xticks(fontsize=21) 
    plt.yticks(fontsize=14) 
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.xlabel('Bias', fontsize=21)
    plt.ylabel('Season/Team', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig('seasonteam_bias.png')

if __name__ == "__main__":
    #graph_weekly_bias("/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/output_data/season_week_relative.csv")
    #create_svc_graph("results/cfb/output_data/conference_bias_relative.csv")
    # create_voterteam_pair_nc("output_data/cfb/average_biases/average_biases.csv", "output_data/cfb/cfb_master_bias.csv")
    create_voterteam_pair("/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/output_data/voter_team_relative.csv", "/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/original_data/master_bias_relative.csv")
    #create_seasonteam_pair("/Users/albertbogdan/IML-FALL2025---Voter-Bias/results/cfb/output_data/season_voter_team_relative.csv")
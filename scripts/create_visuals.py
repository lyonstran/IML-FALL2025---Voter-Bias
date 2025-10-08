import pandas as pd
import matplotlib.pyplot as plt

def graph_weekly_bias(input_csv: str): # get weekly bias visuals for mean and std
    graph_weekly_bias_mean(input_csv)
    graph_weekly_bias_std(input_csv)

def graph_weekly_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df = df.groupby('week').agg({'bias1_mean': 'mean', 'bias1_std': 'mean', 'bias2_mean': 'mean', 'bias2_std': 'mean', 'bias3_mean': 'mean', 'bias3_std': 'mean'}).reset_index()
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias1_mean'], 'o-', label='AP Rank', linewidth=2, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias2_mean'], 's-', label='Mean', linewidth=2, markersize=3)
    plt.plot(df['plot_index'], df['bias3_mean'], '^-', label='Median', linewidth=2, markersize=3)
   
    plt.xticks(df['plot_index'], df['week'])  
    plt.xlabel('Week', fontsize=12) 
    
    plt.title('Voter Bias Measurements', fontsize=16, fontweight='bold')
    plt.xlabel('Week', fontsize=12)
    plt.ylabel('Bias (mean)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_week_mean.png') 

def graph_weekly_bias_std(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df = df.groupby('week').agg({'bias1_mean': 'mean', 'bias1_std': 'mean', 'bias2_mean': 'mean', 'bias2_std': 'mean', 'bias3_mean': 'mean', 'bias3_std': 'mean'}).reset_index()
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias1_std'], 'o-', linewidth=4, markersize=3) # set up the lines
    # plt.plot(df['plot_index'], df['bias2_std'], 's-', label='Mean', linewidth=2, markersize=3)
    # plt.plot(df['plot_index'], df['bias3_std'], '^-', label='Median', linewidth=2, markersize=3)
   
    plt.xticks(df['plot_index'], df['week'])  
    plt.xlabel('Week', fontsize=12) 
    
    plt.xticks(fontsize=23) 
    plt.yticks(fontsize=14) 
    plt.xlabel('Week', fontsize=23)
    plt.ylabel('Standard Deviation of Bias', fontsize=14)
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
    
    df_grouped = df.groupby('Conference').agg({'bias1-a': 'mean'}).reset_index()
    df_grouped = df_grouped.sort_values('bias1-a')  # sort by bias value
    
    plt.figure(figsize=(14, 8))
    
    bars = plt.barh(df_grouped['Conference'], df_grouped['bias1-a'], 
                   color='steelblue', edgecolor='black', linewidth=1.2)
    
    for i, bar in enumerate(bars):
        if df_grouped.iloc[i]['bias1-a'] < 0:
            bar.set_color('indianred')
        else:
            bar.set_color('mediumseagreen')
    
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    
    plt.xticks(fontsize=18) 
    plt.yticks(fontsize=11) 
    plt.xlabel('Conference', fontsize=21)
    plt.ylabel('Bias (mean)', fontsize=14)
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

def create_seasonteam_pair(input_csv: str):
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

if __name__ == "__main__":
    #graph_weekly_bias_std("/Users/albertbogdan/IML-FALL2025---Voter-Bias/output_data/cfb/summary_stats/cfb_ss_week.csv")
    create_svc_graph("/Users/albertbogdan/IML-FALL2025---Voter-Bias/voter_conference_biases.csv")
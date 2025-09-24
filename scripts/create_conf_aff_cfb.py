import pandas as pd
import time

def standardize_conference_name(conf: str) -> str:
    if pd.isna(conf):
        return None
    conf = (
        conf.lower()
        .replace(" ", "-")
        .replace("&", "and")
        .replace("(", "")
        .replace(")", "")
        .replace(".", "")
        .replace("'", "")
    )
    for suffix in ["-east", "-west", "-north", "-south"]:
        if conf.endswith(suffix):
            conf = conf.replace(suffix, "")
    return conf

def process_poll_data_cfb(df, year):
    season_df = df[df["Season"] == str(year)]
    long_df = season_df.melt(
        id_vars=['Season', 'Week', 'Pollster'],
        value_vars=[str(i) for i in range(1, 26)],
        var_name='Rank',
        value_name='Team'
    ).dropna(subset=['Team'])
    rank_points = {str(i): 26 - i for i in range(1, 26)}
    long_df['Points'] = long_df['Rank'].map(rank_points)
    poll_df = long_df.groupby(['Season', 'Week', 'Team'], as_index=False)['Points'].sum()
    poll_df = poll_df.rename(columns={'Points': 'Total_Points'})
    url = f'https://www.sports-reference.com/cfb/years/{year}-standings.html' # <- link is different for cbb
    table = pd.read_html(url)[0]
    team_df = table.rename(columns={'Unnamed: 1_level_0': 'School', 'Unnamed: 2_level_0': 'Conf'})
    team_df = team_df[['School', 'Conf']]
    team_df.columns = team_df.columns.get_level_values(0)
    team_df = team_df.dropna()
    team_df = team_df[team_df.School != 'School']
    team_df.School = (
        team_df.School.str.lower()
        .str.replace(" ", "-", regex=False)
        .str.replace("&", "and", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace("'", "", regex=False)
    )

    team_df['Conf'] = team_df['Conf'].apply(standardize_conference_name)
    
    school_to_mascot = poll_df['Team'].unique().tolist()
    schools = team_df.School.unique().tolist()
    map_school_to_mascot = {}
    for school in schools:
        matches = [t for t in school_to_mascot if t.startswith(school)]
        if matches:
            map_school_to_mascot[school] = matches[0]
    team_df['updated_school'] = team_df['School'].map(map_school_to_mascot)
    team_df = team_df.dropna()
    conf_map = dict(zip(team_df['updated_school'], team_df['Conf']))
    poll_df['Conference'] = poll_df['Team'].map(conf_map)
    poll_df = poll_df[['Season', 'Week', 'Team', 'Conference', 'Total_Points']]
    return poll_df

def process_all_years_cfb(df):
    all_dfs = []
    for year in sorted(df.Season.unique()):
        try:
            season_df = process_poll_data_cfb(df, year)
            all_dfs.append(season_df)
            print(f"Processed {year}")
            time.sleep(5)#
        except Exception as e:
            print(f"Skipped {year} due to error: {e}")
    all_years_df = pd.concat(all_dfs, ignore_index = True)
    return all_years_df

#example:
# ret1 = process_all_years_cfb(df)
# ret1.to_csv('cfb_conf_aff.csv', index = False)
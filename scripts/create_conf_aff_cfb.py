import pandas as pd
import time

def standardize_conference_name(conf: str):
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

### manual data cleaning and entry:

df = pd.read_csv(r'C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cfb\cfb_conf_aff.csv')

tmc_2014 = df[df["Season"] == 2014][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2015 = df[df["Season"] == 2015][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2016 = df[df["Season"] == 2016][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2017 = df[df["Season"] == 2017][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2018 = df[df["Season"] == 2018][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2019 = df[df["Season"] == 2019][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2020 = df[df["Season"] == 2020][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2021 = df[df["Season"] == 2021][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2022 = df[df["Season"] == 2022][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2023 = df[df["Season"] == 2023][df["Conference"].isna()]["Team"].unique().tolist()
tmc_2024 = df[df["Season"] == 2024][df["Conference"].isna()]["Team"].unique().tolist() 

mtm_2014 = {
    'michigan-wolverines' : 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'arizona-wildcats' : 'pac-12',
    'north-dakota-state-bison' : 'mvfc',
    'utah-utes' : 'pac-12',
    'virginia-cavaliers' : 'acc'
}

mtm_2015 = {
    'arizona-wildcats' : 'pac-12',
    'michigan-wolverines' : 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'north-carolina-tar-heels' : 'acc'
}

mtm_2016 = {
    'michigan-wolverines' : 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'north-dakota-state-bison' : 'mvfc',
    'southern-methodist-mustangs' : 'american' 
}

mtm_2017 = {
    'michigan-wolverines': 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'iowa-hawkeyes' : 'big-ten',
    'virginia-cavaliers' : 'acc'
}

mtm_2018 = {
    'florida-gators' : 'sec',
    'michigan-wolverines' : 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'virginia-cavaliers' : 'acc'
}

mtm_2019 = {
    'arizona-wildcats' : 'pac-12',
    'michigan-wolverines' : 'big-ten',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'utah-utes' : 'pac-12',
    'north-dakota-state-bison' : 'mvfc',
    'southern-methodist-mustangs' : 'american',
    'louisiana-lafayette-ragin-cajuns' : 'sbc'
}

mtm_2020 = {
    'southern-methodist-mustangs' : 'american',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'north-dakota-state-bison' : 'mvfc',
    'arkansas-razorbacks' : 'sec'
}

mtm_2021 = {
    'north-carolina-tar-heels' : 'acc',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'southern-methodist-mustangs' : 'american',
    'virginia-cavaliers' : 'acc'
}

mtm_2022 = {
    'michigan-wolverines' : 'big-ten',
    'north-carolina-tar-heels' : 'acc',
    'texas-longhorns' : 'big-12',
    'utah-utes' : 'pac-12',
    'tcu-horned-frogs' : 'big-12',
    'kansas-jayhawks' : 'big-12',
    'ohio-bobcats' : 'mac'
}

mtm_2023 = {
    'north-carolina-tar-heels' : 'acc',
    'tcu-horned-frogs' : 'big-12',
    'texas-longhorns' : 'big-12',
    'kansas-jayhawks' : 'big-12',
    'southern-methodist-mustangs' : 'american',
    'unlv-rebels' : 'mwc',
    'ohio-bobcats' : 'mac'
}

mtm_2024 = {
    'southern-methodist-mustangs' : 'acc',
    'texas-longhorns' : 'sec',
    'north-carolina-tar-heels' : 'acc',
    'unlv-rebels' : 'mwc',
    'tcu-horned-frogs' : 'big-12'
}

manual_maps = {
    2014: mtm_2014, 
    2015: mtm_2015, 
    2016: mtm_2016, 
    2017: mtm_2017,
    2018: mtm_2018, 
    2019: mtm_2019, 
    2020: mtm_2020, 
    2021: mtm_2021,
    2022: mtm_2022, 
    2023: mtm_2023, 
    2024: mtm_2024
}
for year, mapping in manual_maps.items():
    mask = (df["Season"] == year) & (df["Conference"].isna())
    df.loc[mask, "Conference"] = df.loc[mask, "Team"].map(mapping)

df = df[df["Conference"] != "ind"]
df["Conference"] = df["Conference"].replace({
    "mwc-mountain": "mwc",
    "acc-atlantic": "acc",
    "acc-coastal": "acc"
})

#df.to_csv('cfb_conf_aff.csv')

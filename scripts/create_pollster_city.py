from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

base_url = "https://collegepolltracker.com/football/pollsters/{}"

all_pollsters = []

for year in range(2014, 2025):
    url = base_url.format(year)
    print(f"Scraping {year}")

    resp = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})  # https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python
    if resp.status_code != 200:  # good status code is 200 
        print(f"Failed to get {year} -> status {resp.status_code}")
        continue

    soup = BeautifulSoup(resp.text, "html.parser")

    pollster_blocks = soup.find_all("div", class_ = "ballotBoxRankItem")   
    print(f"{len(pollster_blocks)} pollsters in {year}, check with actual number")

    for block in pollster_blocks:
        values = {}
        for class_name, key in [("pollsterRankName", "pollster_name"), ("pollsterRankCompany", "city_state")]:
            tag = block.find("span", class_ = class_name) # block is one pollster’s div class ballotBoxRankItem (check inspected elememts for url)
            values[key] = tag.get_text(strip = True) if tag else None

        if values["pollster_name"] and values["city_state"]:
            values["year"] = year
            all_pollsters.append(values)

    time.sleep(3)

df = pd.DataFrame(all_pollsters)
df["affiliation"] = df["city_state"].str.split(" (", n = 1, expand = True, regex = False)[0].str.strip() # expand = true: The Seattle Times (Seattle, WA) -> ['The Seattle Times', 'Seattle, WA)'] (same column)

df["location"] = (df["city_state"]
    .str.split(" (", n = 1, expand = True, regex = False)[1]     # take second part after '('
    .str.replace(")", "", regex = False)        # remove trailing ')'
    .str.strip()                              # clean whitespace
)

city_state_split = df["location"].str.split(",", n = 1, expand = True)
df["city"] = city_state_split[0].str.strip()
df["state"] = city_state_split[1].str.strip()


df = df.drop(columns=["city_state", "location"])
df = df[["pollster_name", "affiliation", "city", "state", "year"]]
df.to_csv("pollsters_2014_2024.csv", index = False)

print("Saved to: 'pollsters_2014_2024.csv'")
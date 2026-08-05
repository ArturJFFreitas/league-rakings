import pandas as pd

URL = "https://dataviz.theanalyst.com/opta-power-rankings/league-meta.json"

def scrape_opta_league_rankings():
    df = pd.read_json(URL)
    df = df.sort_values("globalRank").reset_index(drop=True)
    return df

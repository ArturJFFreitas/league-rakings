import requests
import pandas as pd

URL = "https://dataviz.theanalyst.com/opta-power-rankings/league-meta.json"

KEEP_COLUMNS = ["globalRank",
                "leagueName",
                "countryName",
                "confederationName",
                "seasonAverageRating",
                "top10Rating",
                "top5Rating",
                "leagueSize",
                "countrySize",
                "confederationRank",
                "lastWeekGlobalRank",
                "endDate"]


def scrape_opta_league_rankings():

    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    missing = set(KEEP_COLUMNS) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return (
        df[KEEP_COLUMNS]
        .sort_values("globalRank")
        .reset_index(drop=True)
    )

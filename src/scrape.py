import pandas as pd
from datetime import datetime
from utils import create_or_update_club_rankings_release, add_timestamp_cols
from opta import scrape_opta_club_rankings
from urllib.error import HTTPError

current_time = datetime.now()
opta_df = scrape_opta_club_rankings()
opta_df = add_timestamp_cols(opta_df, current_time)

create_or_update_club_rankings_release(df=opta_df, file_name="opta-club-rankings.csv")

clubelo_date_str = datetime.strftime(datetime.today(), "%Y-%m-%d")
clubelo_url = f"http://api.clubelo.com/{clubelo_date_str}"
clubelo_df = None
try:
    clubelo_df = pd.read_csv(clubelo_url)
except HTTPError as e:
    print(f'ClubElo unavailable({e.code}). Skipping')
except Exception as e:
    print(f'Could not download ClubElo data: {e}')
if clubelo_df is not None:
    clubelo_df = add_timestamp_cols(clubelo_df, current_time)
    create_or_update_club_rankings_release(
        df=clubelo_df, file_name="clubelo-club-rankings.csv"
    )

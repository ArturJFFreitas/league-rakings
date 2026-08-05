from datetime import datetime
from opta import scrape_opta_league_rankings
from utils import (add_timestamp_cols, create_or_update_club_rankings_release)

current_time = datetime.now()

df = scrape_opta_league_rankings()
df = add_timestamp_cols(df, current_time)

create_or_update_club_rankings_release(df=df,file_name="opta-league-rankings.csv")

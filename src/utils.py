from gh import create_or_update_release as gh_create_or_update_release

REPO_NAME = 'league-rankings'
RELEASE_TAG = 'league-rankings'
RELEASE_DESCRIPTION = 'Opta Global League Rankings'
GITHUB_ACCESS_TOKEN_ENV_VAR_NAME = 'CLUB_RANKINGS_TOKEN'

def create_or_update_release(
  df, 
  file_name,
  repo_name=REPO_NAME,
  env_var_name=GITHUB_ACCESS_TOKEN_ENV_VAR_NAME, 
  tag=RELEASE_TAG,
  description=RELEASE_DESCRIPTION
):
  gh_create_or_update_release(
    df=df,
    file_name=file_name,
    repo_name=repo_name,
    env_var_name=env_var_name,
    tag=tag,
    description=description
  )

def add_timestamp_cols(df, timestamp):
  today = timestamp.strftime('%Y-%m-%d')
  formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
  df['date'] = today
  df['updated_at'] = formatted_timestamp
  return(df)

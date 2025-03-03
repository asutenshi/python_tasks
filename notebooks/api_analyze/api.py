#%%
import requests

URL = 'https://api.opendota.com/api/leagues'
params = {}

leagues = requests.get(URL, params=params)

leagues.content

leagues_dict = leagues.json()

import re
pattern = r'The International \d{4}$'

# int means International - name of the main dota 2 tournament
int_leagues_ids = {item['leagueid'] : item['name'] for item in leagues_dict if re.match(pattern, item['name'])}
sort_tourn_items = sorted(int_leagues_ids.items(), key=lambda x:x[1])

int_matches_data = {}
for leag_id, _ in sort_tourn_items:
    int_matches_data[leag_id] = requests.get(f'https://api.opendota.com/api/leagues/{leag_id}/matches').json()

int_matches_list = [list(item.values()) for leag in int_matches_data.values() for item in leag]
columns = tuple(int_matches_data.popitem()[1][0].keys())

import pandas as pd

int_matches_df = pd.DataFrame(int_matches_list, columns=columns)
int_matches_df['tour_name'] = int_matches_df['leagueid'].map(int_leagues_ids)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.boxplot(x='tour_name', y='duration', data=int_matches_df, palette='pastel')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%

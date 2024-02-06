import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

import sys
from pathlib import Path

# Get the absolute path of the directory where the script is located
current_script_directory = Path(__file__).resolve().parent

# go back one directory
current_script_directory = current_script_directory.parent


# Define the directory name you want to add to sys.path
#directory_name = 'reds_pitching_hackathon_team_mendoza_line'

# Construct the absolute path to the directory
directory_path = current_script_directory #/ directory_name

# Check if the directory exists before adding it to sys.path
if not directory_path.is_dir():
    raise FileNotFoundError(f"The directory {directory_path} does not exist.")

# Add the directory to sys.path
sys.path.append(str(directory_path))


from src.const import *
from src.funcs import *
from src.paths import *

# Load All Means
elite_mean_df = pd.read_csv(MEAN_CATEGORIES_DIR / 'elite_and_strong_mean.csv')
suboptimal_mean_df = pd.read_csv(MEAN_CATEGORIES_DIR / 'suboptimal_mean.csv')
elite_mean_by_role = pd.read_csv(MEAN_CATEGORIES_DIR / 'elite_means_by_role.csv')
suboptimal_mean_by_role = pd.read_csv(MEAN_CATEGORIES_DIR / 'suboptimal_means_by_role.csv')

# Load Suboptimal Players
suboptimal_df = pd.read_csv(PLAYER_CATEGORIES_DIR / 'suboptimal_players.csv')
elite_and_strong_players_df = pd.read_csv(PLAYER_CATEGORIES_DIR / 'elite_and_strong_players.csv')

# Load Suggested Data
suggested_roles_df = pd.read_csv(SUGGESTED_CHANGES_DIR / 'suggested_changes.csv')

# Load Chosen Player
chosen_player = pd.read_csv(STREAMLIT_DIR / 'chosen_players.csv')

# Rename columns
# rename Unnamed: 0 to Stat
elite_mean_by_role.rename(columns={'Unnamed: 0': 'Stat'}, inplace=True)
suboptimal_mean_by_role.rename(columns={'Unnamed: 0': 'Stat'}, inplace=True)

# Images Path
reds_image_path = r'image.png'

# Print TItle
st.title('Pitcher Role Suggestions ⚾')

# Insert Image 
st.image(reds_image_path, caption='2024 Cincinnati Reds Hackathon', use_column_width=True)

# For each top pitcher, provide an explanation for the suggested role

#chosen_players = suboptimal_pitchers[suboptimal_pitchers['Name'].isin(['Daniel Lynch IV', 'Chase Silseth', 'Jovani Moran'])]
st.header('Our Top Three Chosen Players')
for index, player in chosen_player.iterrows():
    st.subheader(f"{player['Name']} (Player ID: {player['PlayerId']})")
    st.write(f"**Current Role:** {player['Current Role']}")
    st.write(f"**Suggested Role:** {player['Suggested Role']}")

    # Collect stats within one standard deviation
    pos_stats_within_str = player['Positive Stats Within One Std Dev of Elite Mean']
    neg_stats_within_str = player['Negative Stats Within One Std Dev of Elite Mean']
    combined_within_str = (pos_stats_within_str or '') + ',' + (neg_stats_within_str or '')

    # Collect stats beyond one standard deviation
    pos_stats_beyond_str = player['Positive Stats Beyond One Std Dev of Elite Mean']  # Assuming you have this column
    neg_stats_beyond_str = player['Negative Stats Beyond One Std Dev of Elite Mean']  # Assuming you have this column
    combined_beyond_str = (pos_stats_beyond_str or '') + ',' + (neg_stats_beyond_str or '')

    # Combine all stats and visualize
    combined_stats_str = combined_within_str + ',' + combined_beyond_str
    if combined_stats_str:
        fig = parse_and_visualize_stats(combined_stats_str, player['Name'])
        st.plotly_chart(fig, use_container_width=True)

# Display the top pitchers and their suggested roles
st.header('Our Full List of Suboptimal Pitchers and Their Suggested Roles')

# Display the top suboptimal pitchers and their suggested roles
#top_suboptimal_pitchers = suggested_roles_df.head(10)
suboptimal_pitchers = suggested_roles_df 
st.write(suboptimal_pitchers)

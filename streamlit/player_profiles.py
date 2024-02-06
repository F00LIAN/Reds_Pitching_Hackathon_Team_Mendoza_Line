import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.append('\Projects\REDS_BASEBALL_PITCHING_PROJECT')

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
chase_silseth_image_path = r'chase_silseth.png'
daniel_lync_iv_image_path = r'daniel_lynch.jpg'
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

    # Parse and visualize positive stats
    pos_stats_str = player['Positive Stats Within One Std Dev of Elite Mean']
    if pos_stats_str:  # Check if the string is not empty
        pos_fig = parse_and_visualize_stats(pos_stats_str, player['Name'])
        st.plotly_chart(pos_fig, use_container_width=True)
    
    # Parse and visualize negative stats
    neg_stats_str = player['Negative Stats Within One Std Dev of Elite Mean']
    if neg_stats_str:  # Check if the string is not empty
        neg_fig = parse_and_visualize_stats(neg_stats_str, player['Name'])
        st.plotly_chart(neg_fig, use_container_width=True)


# Display the top pitchers and their suggested roles
st.header('Our Full List of Suboptimal Pitchers and Their Suggested Roles')

# Display the top suboptimal pitchers and their suggested roles
#top_suboptimal_pitchers = suggested_roles_df.head(10)
suboptimal_pitchers = suggested_roles_df 
st.write(suboptimal_pitchers)
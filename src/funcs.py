import pandas as pd
import os
import sys
# reference main directory in existing folder
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.const import *
from src.funcs import *
from scipy.spatial.distance import cosine
from sklearn.preprocessing import StandardScaler
import numpy as np
import re
import plotly.express as px
import plotly.graph_objects as go

# Use for streamlit dashboard
def profile_cluster_metrics(clustered_data, cluster_col, metrics_dict, cluster_label):
    """
    Profiles a specified cluster using selected metrics, excluding null values in calculations.

    :param clustered_data: DataFrame containing clustering results and player statistics
    :param cluster_col: str, name of the column in clustered_data that contains cluster labels
    :param metrics_dict: dict, dictionary where keys are metric names and values are descriptions
    :param cluster_label: int or str, the label of the cluster to profile
    :return: dict, profile of the specified cluster with the selected metrics
    """

    # Filter the DataFrame for the specified cluster
    cluster_data = clustered_data[clustered_data[cluster_col] == cluster_label]

    # Initialize the profile dictionary
    cluster_profile = {}

    # Loop through the metrics in the dictionary
    for metric in metrics_dict.keys():
        # Check if the metric is in the DataFrame
        if metric in cluster_data.columns:
            # Get the metric data (keeping NaN values)
            metric_data = cluster_data[metric]

            # Calculate the central tendencies and dispersion for the metric
            cluster_profile[metric] = {
                'mean': metric_data.mean(),
                'median': metric_data.median(),
                'range': metric_data.max() - metric_data.min(),  # Max and Min ignore NaN
                'interquartile_range': metric_data.quantile(0.75) - metric_data.quantile(0.25),  # Quantiles ignore NaN
                'description': metrics_dict[metric]
            }

    return cluster_profile

### Cosine Similarity & Role Changes Dashboard
# Function to calculate similarity to all elite role means
def calculate_similarity_to_all_roles(player_stats, role_means_df):
    """
    Calculate the similarity of a player's statistics to the mean statistics of elite players across all roles.
    """
    similarities = {}
    for role, mean_stats in role_means_df.items():
        similarity = 1 - cosine(player_stats, mean_stats)
        similarities[role] = similarity
    return similarities


def explain_suggested_role(player_stats, role_means, suggested_role):
    if suggested_role not in role_means.columns:
        return f"Role '{suggested_role}' not found in role means data."

    # Standardize the player's stats
    scaler = StandardScaler()
    scaler.fit(role_means.T)  # Fit the scaler on the transpose of role_means to standardize across features
    standardized_player_stats = scaler.transform(player_stats.values.reshape(1, -1)).flatten()

    # Get the standardized mean stats for the suggested role
    standardized_role_mean = scaler.transform(role_means[suggested_role].values.reshape(1, -1)).flatten()

    # Calculate the z-scores, which is the number of standard deviations from the mean
    z_scores = standardized_player_stats - standardized_role_mean

    # Identify the metrics within one standard deviation and those that are farther
    within_one_std = np.where((z_scores > -1) & (z_scores < 1))[0]
    beyond_one_std = np.where((z_scores <= -1) | (z_scores >= 1))[0]

    # Create explanations for metrics within one standard deviation
    close_metrics_explanations = [f"{player_stats.index[i]} (z-score: {z_scores[i]:.2f})" for i in within_one_std]
    # create explanations for positive and negative close metrics
    positive_close_metrics_explanations = [f"{player_stats.index[i]} (z-score: {z_scores[i]:.2f})" for i in within_one_std if z_scores[i] > 0]
    negative_close_metrics_explanations = [f"{player_stats.index[i]} (z-score: {z_scores[i]:.2f})" for i in within_one_std if z_scores[i] < 0]

    # Create explanations for metrics beyond one standard deviation
    far_metrics_explanations = [f"{player_stats.index[i]} (z-score: {z_scores[i]:.2f})" for i in beyond_one_std]

    # Construct the final explanation
    explanation = f"The player's statistics within one standard deviation for the {suggested_role} are: {', '.join(close_metrics_explanations)}."
    if far_metrics_explanations:
        explanation += f" Statistics beyond one standard deviation are: {', '.join(far_metrics_explanations)}."

    return explanation, close_metrics_explanations, far_metrics_explanations, positive_close_metrics_explanations, negative_close_metrics_explanations


def suggest_role_changes(suboptimal_players, elite_means_df, numeric_columns):
    """
    This function suggests role changes for players who are considered suboptimal in their current roles.
    It compares each player's statistics to the mean statistics of elite players' performance in various roles.
    The "Elite mean" refers to the average statistics of players who are top-performing (elite) in a specific role.
    
    The function calculates the similarity of each suboptimal player's stats to the elite means of all possible roles
    and suggests a change to the role where the player's stats are most similar to the elite means.
    It also identifies which stats are within one standard deviation above (positive) or below (negative)
    the elite mean of the suggested role.
    
    Parameters:
    - suboptimal_players (pd.DataFrame): DataFrame containing statistics for players considered suboptimal.
    - elite_means_df (pd.DataFrame): DataFrame containing the mean statistics of elite players by role.
    - numeric_columns (list): List of column names in suboptimal_players that contain numeric statistics to be considered.
    
    Returns:
    - suggested_changes (pd.DataFrame): DataFrame with suggested role changes and similarity scores,
      including detailed metrics comparison within one standard deviation of the elite means for the suggested role.
    """

    suggested_changes = pd.DataFrame(columns=[
        'Name', 'PlayerId', 'Team', 'Current Role', 
        'Suggested Role', 'Similarity Score', 'Positive Stats Within One Std Dev of Elite Mean', 
        'Negative Stats Within One Std Dev of Elite Mean'
    ])

    for index, player in suboptimal_players.iterrows():
        
        player_stats = player[numeric_columns]  # Select numeric columns for the player
        actual_role = player['classified_role']
        
        # Calculate similarities to all elite roles
        similarities = calculate_similarity_to_all_roles(player_stats, elite_means_df)

        # Find the role with the highest similarity score
        suggested_role = max(similarities, key=similarities.get)
        max_similarity_score = similarities[suggested_role]
        
        # Get the detailed explanation and metrics
        explanation, within_one_std_explanations, beyond_one_std_explanations, positive_close_metrics_explanations, negative_close_metrics_explanations = explain_suggested_role(player_stats, elite_means_df, suggested_role)

        # Construct the new row with additional columns
        row_to_add = {
            'Name': player['Name'],
            'PlayerId': player['PlayerId'],
            'Team': player['Team'],
            'Current Role': actual_role,
            'Suggested Role': suggested_role,
            'Similarity Score': max_similarity_score,
            'Positive Stats Within One Std Dev of Elite Mean': ', '.join(positive_close_metrics_explanations),
            'Negative Stats Within One Std Dev of Elite Mean': ', '.join(negative_close_metrics_explanations)
        }
        
        # Use concat to add the new row
        suggested_changes = pd.concat([suggested_changes, pd.DataFrame([row_to_add])], ignore_index=True)

    return suggested_changes

## Streamlit Dashboard

def parse_stats_column(stats_str):
    """
    Parses a string of stats and z-scores and returns a list of tuples with metric names and z-scores.
    
    :param stats_str: String containing stats and z-scores in the format 'metric (z-score: value)'
    :return: List of tuples [(metric1, z_score1), (metric2, z_score2), ...]
    """
    # Regular expression pattern to match the metric names and z-scores
    pattern = r'(\w+)\s\(z-score:\s([-\d.]+)\)'
    return re.findall(pattern, stats_str)

def parse_and_visualize_stats(combined_stats_str, player_name):
    """
    Visualizes the stats and z-scores using a bar chart, including stats within and beyond one standard deviation.
    
    :param combined_stats_str: String containing stats and z-scores both within and beyond one std dev in the format 'metric (z-score: value)'
    :param player_name: Name of the player to be used in the chart title
    """
    # Parse the combined stats string to get metrics and their z-scores
    stats = parse_stats_column(combined_stats_str)
    metrics, z_scores = zip(*stats) if stats else ([], [])
    z_scores = [float(z) for z in z_scores]  # Convert string z-scores to float
    
    # Assign colors based on z-scores magnitude and sign
    colors = ['lightgreen' if z >= 0 and abs(z) < 1 else 'darkgreen' if z >= 0 else 'lightcoral' if abs(z) < 1 else 'darkred' for z in z_scores]

    # Create a DataFrame from the parsed metrics and z-scores
    df = pd.DataFrame({'Metric': metrics, 'Z-Score': z_scores, 'Color': colors})

    # Create the bar chart using Plotly Graph Objects for more customization
    fig = go.Figure(data=[
        go.Bar(
            x=df['Metric'],
            y=df['Z-Score'],
            marker_color=df['Color']
        )
    ])

    # Update chart layout
    fig.update_layout(
        title=f'{player_name} Distribution of Stats around the Elite Pitching Mean',
        xaxis_title='Metrics',
        yaxis_title='Z-Score'
    )

    return fig


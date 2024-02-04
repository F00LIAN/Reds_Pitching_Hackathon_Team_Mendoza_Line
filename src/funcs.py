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

### Cosine Similarity

# Define a function to calculate similarity to successful role means
def calculate_similarity_to_roles(player_stats, role_means):
    """
    Calculate the similarity of a player's statistics to the mean statistics of successful players in each role.

    Parameters:
    - player_stats (pd.Series): A Pandas Series containing the player's statistics.
    - role_means (pd.DataFrame): A Pandas DataFrame where the index represents the role and the columns are the mean statistics for that role.

    Returns:
    - similarities (dict): A dictionary with roles as keys and similarity scores as values.
    """
    similarities = {}
    for role, mean_stats in role_means.iterrows():
        # Calculate the cosine similarity (or any other similarity measure)
        similarity = 1 - cosine(player_stats.values, mean_stats.values)
        similarities[role] = similarity
    return similarities
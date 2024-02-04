import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.append('\Projects\REDS_BASEBALL_PITCHING_PROJECT')

from src.const import *
from src.funcs import *
from src.paths import *

# Load your data
merged_df = pd.read_csv(CLEANED_DATA_DIR / 'fangraphs_merged_2.csv')
cluster_image_path = r'Kmeans Cluster.png'
# Streamlit UI
st.title('K Means Cluster Metrics Profiler part 2')

st.image(cluster_image_path, caption='K Means Cluster Plot', use_column_width=True)

# Allow users to select a dictionary of metrics
combined_metrics = {
    "pitcher_performance_metric": pitcher_performance_metric,
    "pitching_metrics": pitching_metrics,
    "advanced_pitching_metrics": advanced_pitching_metrics,
    "pitching_metrics_plus": pitching_metrics_plus,
    "weighted_pitch_type_runs_statcast": weighted_pitch_type_runs_statcast,
    "pitch_movement_statcast": pitch_movement_statcast,
    "pitch_type_speed_statcast": pitch_type_speed_statcast,
    "pitch_type_percentages_statcast": pitch_type_percentages_statcast,
    "pitch_control": pitch_control,
    "contact_metrics": contact_metrics,
    "hitter_performance_metrics": hitter_performance_metrics,
    "hitter_performance_metrics_statcast": hitter_performance_metrics_statcast,
    "exit_velocity_metrics": exit_velocity_metrics,
    "hitter_performance_metrics_plus": hitter_performance_metrics_plus,
    "pitch_timing_metrics": pitch_timing_metrics,
    "wins_above_replacement": wins_above_replacement,
    "catcher_framing": catcher_framing,
    "clutch_factor": clutch_factor,
    "leverage_index": leverage_index,
    "quadrant1_feature_loadings": quadrant1_feature_loadings,
    "quadrant2_feature_loadings": quadrant2_feature_loadings,
    "quadrant3_feature_loadings": quadrant3_feature_loadings,
    "quadrant4_feature_loadings": quadrant4_feature_loadings
}

metric_dict_options = combined_metrics

selected_dict = st.selectbox('Select a Metric Dictionary', list(metric_dict_options.keys()))

# Get all metrics from the selected dictionary
all_metrics = list(metric_dict_options[selected_dict].keys())
#selected_metric = st.selectbox('Select a Metric', all_metrics, key='metric_select')
selected_cluster = st.selectbox('Select a Cluster', merged_df['KMeans_Cluster'].unique(), key='cluster_select')

# Process Data
cluster_profile = profile_cluster_metrics(
    clustered_data=merged_df,
    cluster_col='KMeans_Cluster',
    metrics_dict=metric_dict_options[selected_dict],
    cluster_label=selected_cluster
)

# Create DataFrame for visualization
metrics_df = pd.DataFrame(columns=['Cluster Value', 'Dataset Average', 'Above/Below Average'])
for metric in all_metrics:
    dataset_avg = merged_df[metric].mean() if metric in merged_df.columns else None
    cluster_value = cluster_profile[metric]['mean'] if metric in cluster_profile else None
    if dataset_avg is not None and cluster_value is not None:
        comparison = 'Above Average' if cluster_value > dataset_avg else 'Below Average'
        metrics_df.loc[metric] = [cluster_value, dataset_avg, comparison]

# Function to apply color coding
def color_code(val):
    color = 'green' if val == 'Above Average' else 'red' if val == 'Below Average' else 'black'
    return f'color: {color}'

# Apply styling and display DataFrame
st.dataframe(metrics_df.style.applymap(color_code, subset=['Above/Below Average']))

# Optional: Display additional metric details
for metric in metrics_df.index:
    st.write(f"{metric}:")
    st.write(f"Cluster {selected_cluster} Value: {metrics_df.loc[metric, 'Cluster Value']}")
    st.write(f"Dataset Average: {metrics_df.loc[metric, 'Dataset Average']}")

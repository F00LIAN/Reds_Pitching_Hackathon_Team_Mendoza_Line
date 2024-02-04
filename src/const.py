# Metrics to be saved in a dictionary for easy use in notebooks and streamlit app
general_player_info = {
    "PlayerId": "General Player Information",
    "MLBAMID": "General Player Information",
    "Name": "General Player Information",
    "NameASCII": "General Player Information",
    "Throws": "General Player Information",
    "Season": "General Player Information",
    "Age": "General Player Information",
    "Team": "General Player Information",
    "Role": "General Player Information",
    "player_name": 'General Player Information',
    "pitcher_role": 'General Player Information'
}


### Pitching Metrics
pitcher_performance_metric= {
    "G": "General Pitcher Performance Metric",
    "GS": "General Pitcher Performance Metric",
    "IP": "General Pitcher Performance Metric",
    "TBF": "General Pitcher Performance Metric",
    "W": "General Pitcher Performance Metric",
    "L": "General Pitcher Performance Metric",
    "CG": "General Pitcher Performance Metric",
    "ShO": "General Pitcher Performance Metric",
    "SV": "General Pitcher Performance Metric",
    "BS": "General Pitcher Performance Metric",
    "HLD": "General Pitcher Performance Metric",
    "SD": "General Pitcher Performance Metric",
    "MD": "General Pitcher Performance Metric",
    "Pulls": "General Pitcher Performance Metric",
    "ERA": "General Pitcher Performance Metric",
    "WHIP": "General Pitcher Performance Metric",
    "R": "General Pitcher Performance Metric",
    "ER": "General Pitcher Performance Metric",
    "H": "General Pitcher Performance Metric",
    "HR": "General Pitcher Performance Metric",
    "SO": "General Pitcher Performance Metric",
    "BB": "General Pitcher Performance Metric",
    "IBB": "General Pitcher Performance Metric",
    "HBP": "General Pitcher Performance Metric",
    "WP": "General Pitcher Performance Metric",
    "BK": "General Pitcher Performance Metric",
    "Events": "General Pitcher Performance Metric",
}


pitching_metrics = {
    "botERA": "Pitching Metrics",
    "botOvr_CH": "Pitching Metrics",
    "botStf_CH": "Pitching Metrics",
    "botCmd_CH": "Pitching Metrics",
    "botOvr_CU": "Pitching Metrics",
    "botStf_CU": "Pitching Metrics",
    "botCmd_CU": "Pitching Metrics",
    "botOvr_FA": "Pitching Metrics",
    "botStf_FA": "Pitching Metrics",
    "botCmd_FA": "Pitching Metrics",
    "botOvr_SI": "Pitching Metrics",
    "botStf_SI": "Pitching Metrics",
    "botCmd_SI": "Pitching Metrics",
    "botOvr_SL": "Pitching Metrics",
    "botStf_SL": "Pitching Metrics",
    "botCmd_SL": "Pitching Metrics",
    "botOvr_KC": "Pitching Metrics",
    "botStf_KC": "Pitching Metrics",
    "botCmd_KC": "Pitching Metrics",
    "botOvr_FC": "Pitching Metrics",
    "botStf_FC": "Pitching Metrics",
    "botCmd_FC": "Pitching Metrics",
    "botOvr_FS": "Pitching Metrics",
    "botStf_FS": "Pitching Metrics",
    "botCmd_FS": "Pitching Metrics",
    "botOvr": "Pitching Metrics",
    "botStf": "Pitching Metrics",
    "botCmd": "Pitching Metrics",
    "botxRV100": "Pitching Metrics",
}

advanced_pitching_metrics = {

    "FIP": "Advanced Pitching Metrics",  # Fielding Independent Pitching, measures the outcomes that dont involve fielders. HR, BB, HBP, SO focus. Lower the better. 

    "xFIP": "Advanced Pitching Metrics", # Expected Fielding Independent Pitching, same as FIP but uses a constant HR/FB rate.

    "SIERA": "Advanced Pitching Metrics",# This metric provides a more comprehensive view of a pitchers performance than ERA. 
                                         # It takes into account strikeouts, walks, groundballs, and flyballs.
    
    "tERA": "Advanced Pitching Metrics", # True Earned Run Average, a more accurate measure of a pitchers performance than ERA. 

    "kwERA": "Advanced Pitching Metrics", # Focuses on a pitcher's strikeout and walk rates. It can be useful to identify pitchers with good command and control.

    "E_minus_F": "Advanced Pitching Metrics", # The difference between a pitcher's ERA and FIP. A positive number indicates that the pitcher has been lucky, while a negative number indicates that the pitcher has been unlucky.

    "RAR": "Advanced Pitching Metrics", # This measures the number of runs a pitcher prevents compared to a replacement-level player. It's useful for determining a pitcher's overall contribution to the team.

    "WAR": "Advanced Pitching Metrics", # Similar to RAR but scaled to wins. It assesses a player's total contribution to their team in terms of wins. A high WAR indicates a very valuable pitcher.
    
    "Dollars": "Advanced Pitching Metrics", # This typically refers to the value of a player's performance in terms of salary. It can be used to compare a player's on-field value to their actual salary, identifying potentially undervalued players.
    
    "WPA": "Advanced Pitching Metrics", # Win Probability Added, measures the change in win expectancy between each plate appearance. It can be used to determine how much a pitcher contributed to their team's win or loss.
    
    "RE24": "Advanced Pitching Metrics", # This measures a pitcher's impact on changing the expected runs given the situation when they enter the game. It's great for evaluating pitchers in specific scenarios.

    "REW": "Advanced Pitching Metrics", #(Run Expectancy Wins) Similar to RE24, it quantifies a pitcher's contribution in terms of wins based on run expectancy.
}


pitching_metrics_plus = {
    "Stf_plus_CH": "Pitching Metrics Plus",
    "Loc_plus_CH": "Pitching Metrics Plus",
    "Pit_plus_CH": "Pitching Metrics Plus",
    "Stf_plus_CU": "Pitching Metrics Plus",
    "Loc_plus_CU": "Pitching Metrics Plus",
    "Pit_plus_CU": "Pitching Metrics Plus",
    "Stf_plus_FA": "Pitching Metrics Plus",
    "Loc_plus_FA": "Pitching Metrics Plus",
    "Pit_plus_FA": "Pitching Metrics Plus",
    "Stf_plus_SI": "Pitching Metrics Plus",
    "Loc_plus_SI": "Pitching Metrics Plus",
    "Pit_plus_SI": "Pitching Metrics Plus",
    "Stf_plus_SL": "Pitching Metrics Plus",
    "Loc_plus_SL": "Pitching Metrics Plus",
    "Pit_plus_SL": "Pitching Metrics Plus",
    "Stf_plus_KC": "Pitching Metrics Plus",
    "Loc_plus_KC": "Pitching Metrics Plus",
    "Pit_plus_KC": "Pitching Metrics Plus",
    "Stf_plus_FC": "Pitching Metrics Plus",
    "Loc_plus_FC": "Pitching Metrics Plus",
    "Pit_plus_FC": "Pitching Metrics Plus",
    "Stf_plus_FS": "Pitching Metrics Plus",
    "Loc_plus_FS": "Pitching Metrics Plus",
    "Pit_plus_FS": "Pitching Metrics Plus",
    "Stf_plus_FO": "Pitching Metrics Plus",
    "Loc_plus_FO": "Pitching Metrics Plus",
    "Pit_plus_FO": "Pitching Metrics Plus",
    "Stuff_plus": "Pitching Metrics Plus",
    "Location_plus": "Pitching Metrics Plus",
    "Pitching_plus": "Pitching Metrics Plus",
}

weighted_pitch_type_runs_statcast = {
    "wFB": "Weighted Pitch Type Runs (Statcast)",
    "wSL": "Weighted Pitch Type Runs (Statcast)",
    "wCT": "Weighted Pitch Type Runs (Statcast)",
    "wCB": "Weighted Pitch Type Runs (Statcast)",
    "wCH": "Weighted Pitch Type Runs (Statcast)",
    "wSF": "Weighted Pitch Type Runs (Statcast)",
    "wKN": "Weighted Pitch Type Runs (Statcast)",
    "wFB_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wSL_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wCT_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wCB_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wCH_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wSF_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
    "wKN_per_c": "Weighted Pitch Type Runs per 100 Pitches (Statcast)",
}

pitch_movement_statcast = {
    "FA_X_sc": "Pitch Movement (Statcast)",
    "FC_X_sc": "Pitch Movement (Statcast)",
    "FS_X_sc": "Pitch Movement (Statcast)",
    "FO_X_sc": "Pitch Movement (Statcast)",
    "SI_X_sc": "Pitch Movement (Statcast)",
    "SL_X_sc": "Pitch Movement (Statcast)",
    "CU_X_sc": "Pitch Movement (Statcast)",
    "KC_X_sc": "Pitch Movement (Statcast)",
    "EP_X_sc": "Pitch Movement (Statcast)",
    "CH_X_sc": "Pitch Movement (Statcast)",
    "SC_X_sc": "Pitch Movement (Statcast)",
    "KN_X_sc": "Pitch Movement (Statcast)",
    "FA_Z_sc": "Pitch Movement (Statcast)",
    "FC_Z_sc": "Pitch Movement (Statcast)",
    "FS_Z_sc": "Pitch Movement (Statcast)",
    "FO_Z_sc": "Pitch Movement (Statcast)",
    "SI_Z_sc": "Pitch Movement (Statcast)",
    "SL_Z_sc": "Pitch Movement (Statcast)",
    "CU_Z_sc": "Pitch Movement (Statcast)",
    "KC_Z_sc": "Pitch Movement (Statcast)",
    "EP_Z_sc": "Pitch Movement (Statcast)",
    "CH_Z_sc": "Pitch Movement (Statcast)",
    "SC_Z_sc": "Pitch Movement (Statcast)",
    "KN_Z_sc": "Pitch Movement (Statcast)",
}

pitch_type_speed_statcast = {
    "FAv": "Pitch Type Speed (Statcast)",
    "SLv": "Pitch Type Speed (Statcast)",
    "CTv": "Pitch Type Speed (Statcast)",
    "CBv": "Pitch Type Speed (Statcast)",
    "CHv": "Pitch Type Speed (Statcast)",
    "SFv": "Pitch Type Speed (Statcast)",
    "KNv": "Pitch Type Speed (Statcast)",
    "vFA_sc": "Pitch Type Speed (Statcast)",
    "vFC_sc": "Pitch Type Speed (Statcast)",
    "vFS_sc": "Pitch Type Speed (Statcast)",
    "vFO_sc": "Pitch Type Speed (Statcast)",
    "vSI_sc": "Pitch Type Speed (Statcast)",
    "vSL_sc": "Pitch Type Speed (Statcast)",
    "vCU_sc": "Pitch Type Speed (Statcast)",
    "vKC_sc": "Pitch Type Speed (Statcast)",
    "vEP_sc": "Pitch Type Speed (Statcast)",
    "vCH_sc": "Pitch Type Speed (Statcast)",
    "vSC_sc": "Pitch Type Speed (Statcast)",
    "vKN_sc": "Pitch Type Speed (Statcast)",
}

pitch_type_percentages_statcast = {
    "FA_pct": "Pitch Type Percentages (Statcast)",
    "SL_pct": "Pitch Type Percentages (Statcast)",
    "CT_pct": "Pitch Type Percentages (Statcast)",
    "CB_pct": "Pitch Type Percentages (Statcast)",
    "CH_pct": "Pitch Type Percentages (Statcast)",
    "SF_pct": "Pitch Type Percentages (Statcast)",
    "KN_pct": "Pitch Type Percentages (Statcast)",
    "XX_pct": "Pitch Type Percentages (Statcast)",
    "PO_pct": "Pitch Type Percentages (Statcast)",
    "FA_pct_sc": "Pitch Type Percentages (Statcast)",
    "FC_pct_sc": "Pitch Type Percentages (Statcast)",
    "FS_pct_sc": "Pitch Type Percentages (Statcast)",
    "FO_pct_sc": "Pitch Type Percentages (Statcast)",
    "SI_pct_sc": "Pitch Type Percentages (Statcast)",
    "SL_pct_sc": "Pitch Type Percentages (Statcast)",
    "CU_pct_sc": "Pitch Type Percentages (Statcast)",
    "KC_pct_sc": "Pitch Type Percentages (Statcast)",
    "EP_pct_sc": "Pitch Type Percentages (Statcast)",
    "CH_pct_sc": "Pitch Type Percentages (Statcast)",
    "SC_pct_sc": "Pitch Type Percentages (Statcast)",
    "KN_pct_sc": "Pitch Type Percentages (Statcast)",
    "UN_pct_sc": "Pitch Type Percentages (Statcast)",
}

pitch_control = {
    "Balls": "Pitch Control",
    "Strikes": "Pitch Control",
    "Pitches": "Pitch Control",
}



### Hitter Performance Metrics

contact_metrics = {
    "GB_pct": "Contact Metrics",
    "LD_pct": "Contact Metrics",
    "FB_pct": "Contact Metrics",
    "IFFB_pct": "Contact Metrics",
    "BUH_pct": "Contact Metrics",
    "IFH_pct": "Contact Metrics"
}


hitter_performance_metrics = {
    "RS": "Hitter Performance Metrics",
    "RS_per_9": "Hitter Performance Metrics",
    "K_pct": "Hitter Performance Metrics",
    "BB_pct": "Hitter Performance Metrics",
    "K_minus_BB_pct": "Hitter Performance Metrics",
    "K_per_9": "Hitter Performance Metrics",
    "BB_per_9": "Hitter Performance Metrics",
    "K_to_BB": "Hitter Performance Metrics",
    "H_per_9": "Hitter Performance Metrics",
    "HR_per_9": "Hitter Performance Metrics",
    "AVG": "Hitter Performance Metrics",
    "WHIP": "Hitter Performance Metrics",
    "BABIP": "Hitter Performance Metrics",
    "LOB_pct": "Hitter Performance Metrics",
    "GB_pct": "Hitter Performance Metrics",
    "LD_pct": "Hitter Performance Metrics",
    "FB_pct": "Hitter Performance Metrics",
    "IFFB_pct": "Hitter Performance Metrics",
    "GB_to_FB": "Hitter Performance Metrics",
    "HR_to_FB": "Hitter Performance Metrics",
    "IFH_pct": "Hitter Performance Metrics",
    "BUH_pct": "Hitter Performance Metrics",
    "OSwing_pct": "Hitter Performance Metrics",
    "ZSwing_pct": "Hitter Performance Metrics",
    "Swing_pct": "Hitter Performance Metrics",
    "OContact_pct": "Hitter Performance Metrics",
    "ZContact_pct": "Hitter Performance Metrics",
    "Contact_pct": "Hitter Performance Metrics",
    "Zone_pct": "Hitter Performance Metrics",
    "FStrike_pct": "Hitter Performance Metrics",
    "SwStr_pct": "Hitter Performance Metrics",
    "CStr_pct": "Hitter Performance Metrics",
    "CSW_pct": "Hitter Performance Metrics",
}

hitter_performance_metrics_statcast = {
    "OSwing_pct_sc": "Hitter Performance Metrics (Statcast)",
    "ZSwing_pct_sc": "Hitter Performance Metrics (Statcast)",
    "Swing_pct_sc": "Hitter Performance Metrics (Statcast)",
    "OContact_pct_sc": "Hitter Performance Metrics (Statcast)",
    "ZContact_pct_sc": "Hitter Performance Metrics (Statcast)",
    "Contact_pct_sc": "Hitter Performance Metrics (Statcast)",
    "Zone_pct_sc": "Hitter Performance Metrics (Statcast)",
}

exit_velocity_metrics = {
    "EV": "Exit Velocity Metrics",
    "LA": "Launch Angle Metrics",
    "Barrels": "Exit Velocity Metrics",
    "Barrel_pct": "Exit Velocity Metrics",
    "maxEV": "Exit Velocity Metrics",
    "HardHit": "Exit Velocity Metrics",
    "HardHit_pct": "Exit Velocity Metrics",
}

hitter_performance_metrics_plus = {
    "K_pct_plus": "Hitter Performance Metrics Plus",
    "BB_pct_plus": "Hitter Performance Metrics Plus",
    "K_per_9_plus": "Hitter Performance Metrics Plus",
    "BB_per_9_plus": "Hitter Performance Metrics Plus",
    "K_to_BB_plus": "Hitter Performance Metrics Plus",
    "H_per_9_plus": "Hitter Performance Metrics Plus",
    "HR_per_9_plus": "Hitter Performance Metrics Plus",
    "AVG_plus": "Hitter Performance Metrics Plus",
    "WHIP_plus": "Hitter Performance Metrics Plus",
    "BABIP_plus": "Hitter Performance Metrics Plus",
    "LOB_pct_plus": "Hitter Performance Metrics Plus",
    "GB_pct_plus": "Hitter Performance Metrics Plus",
    "LD_pct_plus": "Hitter Performance Metrics Plus",
    "FB_pct_plus": "Hitter Performance Metrics Plus",
    "HR_to_FB_pct_plus": "Hitter Performance Metrics Plus",
    "Pull_pct_plus": "Hitter Performance Metrics Plus",
    "Cent_pct_plus": "Hitter Performance Metrics Plus",
    "Oppo_pct_plus": "Hitter Performance Metrics Plus",
    "Med_pct_plus": "Hitter Performance Metrics Plus",
    "Hard_pct_plus": "Hitter Performance Metrics Plus",
}

### Miscellaneous Metrics
pitch_timing_metrics = {
    "Pace": "Pitch Timing Metrics",
}

wins_above_replacement = {
    "RA9_WAR": "Wins Above Replacement",
}

catcher_framing = {
    "FRM": "Catcher Framing",
}

clutch_factor = {
    "Clutch": "Clutch Factor",
}

leverage_index = {
    "pLI": "Leverage Index",
    "inLI": "Leverage Index",
    "gmLI": "Leverage Index",
    "exLI": "Leverage Index",
    "WPA_to_LI": "Situational Wins",
}

## PCA Quadrant Feature Loadings

quadrant1_weights =  {
    'xFIP_minus': -1, 'xFIP': -1, 'WHIP': -1, 'WHIP_plus': 1,
    'SIERA': -1, 'kwERA': -1, 'AVG': -1, 'AVG_plus': 1,
    'FIP': -1, 'FIP_minus': -1, 'tERA': -1, 'ERA': -1,
    'ERA_minus': -1, 'H_per_9': -1, 'H_per_9_plus': 1,
    'botxRV100': 0, 'botERA': -1, 
    'Contact_pct': 1, 'Contact_pct_sc': 1, 
    'HR_per_9_plus': -1, 'HR_per_9': -1,
    'BB_per_9': -1, 'BB_per_9_plus': -1,
    'ZContact_pct_sc': 1, 'ZContact_pct': 1,
    'OContact_pct': 1, 'BABIP': -1, 'BABIP_plus': 1,
    'Hard_pct': -1, 'BB_pct': -1, 'Hard_pct_plus': -1,
    'BB_pct_plus': -1, 'E_minus_F': 0,
    'HR_to_FB_pct_plus': -1, 'HR_to_FB': -1,
    'EV': -1, 'HardHit_pct': -1,
    'Barrel_pct': -1, 'OContact_pct_sc': 1,
    'LD_pct': -1, 'LD_pct_plus': -1,
    'Pull_pct_plus': 0, 'Pull_pct': 0,
    'ZSwing_pct': 0, 'ZSwing_pct_sc': 0,
    'IFH_pct': -1
}

quadrant2_weights = {
    'H': -1, 'HardHit': -1, 'Events': 0, 'ER': -1,
    'R': -1, 'LD': -1, 'TBF': 1, 'Pitches': 0,
    'Strikes': 1, 'IP': 5, 'Balls': -1, 'Barrels': -1,
    'FB': -1, 'GS': 1, 'GB': 1, 'RS': 1,
    'HR': -1, 'SO': 1, 'BB': -1, 'L': -1,
    'IFH': -1, 'W': 1, 'IFFB': 1, 'RAR': 1,
    'Dollars': 1, 'WAR': 1, 'BU': -1, 'RA9_WAR': 1,
    'HBP': -1, 'BUH': -1, 'WP': -1, 'maxEV': -.3,
    'average_innings_pitched_per_appearance_SP': 1, 'average_batters_faced_per_appearance_SP': 1,
    'CG': 1, 'ShO': 1, 'BUH_pct': -1, 'BK': -1,
    'LOB_Wins': 1, 'Clutch': 1
}

quadrant3_weights = {
    'K_minus_BB_pct': 1, 'K_pct_plus': 1, 'K_pct': 1, 'Pitching_plus': 1,
    'CSW_pct': 1, 'SwStr_pct': 1, 'botOvr': 1, 'REW': 1,
    'RE24': 1, 'K_to_BB': 1, 'WPA_to_LI': 1, 'Pulls': -1,
    'Stuff_plus': 1, 'botStf': 1, 'SD': 1, 'G': 1,
    'wFB_per_c': 1, 'K_per_9_plus': 1, 'K_per_9': 1, 'WPA': 1,
    'LOB_pct': 1, 'LOB_pct_plus': 1, 'wFB': 1, 'Location_plus': 1,
    'inLI': 1, 'HLD': 1, 'OSwing_pct_sc': 1, 'gmLI': 1,
    'OSwing_pct': 1, 'BS': -1, 'MD': -1, 'botCmd': 1,
    'pLI': 1, 'SV': 1, 'FAv': 1, 'exLI': 1,
    'TTO_pct': 0, 'Swing_pct_sc': 1, 'Swing_pct': 1, 'BIP_Wins': 1,
    'IBB': -1, 'Soft_pct': 1, 'FStrike_pct': 1, 'Med_pct': 0,
    'Med_pct_plus': 1, 'FDP_Wins': 1, 'CStr_pct': 1, 'GB_pct_plus': 1,
    'GB_pct': 1, 'Zone_pct_sc': 1, 'Pace': 0, 'Zone_pct': 1,
    'Oppo_pct': 0, 'Oppo_pct_plus': 0, 'IFFB_pct': 1, 'GB_to_FB': 0,
    'FRM': 1, 'RS_per_9': 1, 'Cent_pct_plus': 1, 'Cent_pct': 1
}

quadrant4_weights = {
    'average_batters_faced_per_appearance_RP': 0,
    'average_innings_pitched_per_appearance_RP': 0,
    'FB_pct_plus': 0,  # Context-dependent
    'FB_pct': 0,       # Context-dependent
    'FA_pct': 1,       # Style indicator, context-dependent
    'LA': 0           # Depends on the value and context
}

combined_weights = {
    "quadrant1_weights": quadrant1_weights,
    "quadrant2_weights": quadrant2_weights,
    "quadrant3_weights": quadrant3_weights,
    "quadrant4_weights": quadrant4_weights
}

quadrant1_feature_loadings = {
    'xFIP_minus': 'Q1',
    'xFIP': 'Q1',
    'WHIP': 'Q1',
    'WHIP_plus': 'Q1',
    'SIERA': 'Q1',
    'kwERA': 'Q1',
    'AVG': 'Q1',
    'AVG_plus': 'Q1',
    'FIP': 'Q1',
    'FIP_minus': 'Q1',
    'tERA': 'Q1',
    'ERA': 'Q1',
    'ERA_minus': 'Q1',
    'H_per_9': 'Q1',
    'H_per_9_plus': 'Q1',
    'botxRV100': 'Q1',
    'botERA': 'Q1',
    'Contact_pct': 'Q1',
    'Contact_pct_sc': 'Q1',
    'HR_per_9_plus': 'Q1',
    'HR_per_9': 'Q1',
    'BB_per_9': 'Q1',
    'BB_per_9_plus': 'Q1',
    'ZContact_pct_sc': 'Q1',
    'ZContact_pct': 'Q1',
    'OContact_pct': 'Q1',
    'BABIP': 'Q1',
    'BABIP_plus': 'Q1',
    'Hard_pct': 'Q1',
    'BB_pct': 'Q1',
    'Hard_pct_plus': 'Q1',
    'BB_pct_plus': 'Q1',
    'E_minus_F': 'Q1',
    'HR_to_FB_pct_plus': 'Q1',
    'HR_to_FB': 'Q1',
    'EV': 'Q1',
    'HardHit_pct': 'Q1',
    'Barrel_pct': 'Q1',
    'OContact_pct_sc': 'Q1',
    'LD_pct': 'Q1',
    'LD_pct_plus': 'Q1',
    'Pull_pct_plus': 'Q1',
    'Pull_pct': 'Q1',
    'ZSwing_pct': 'Q1',
    'ZSwing_pct_sc': 'Q1',
    'IFH_pct': 'Q1'
}

quadrant2_feature_loadings = {
    'H': 'Q2',
    'HardHit': 'Q2',
    'Events': 'Q2',
    'ER': 'Q2',
    'R': 'Q2',
    'LD': 'Q2',
    'TBF': 'Q2',
    'Pitches': 'Q2',
    'Strikes': 'Q2',
    'IP': 'Q2',
    'Balls': 'Q2',
    'Barrels': 'Q2',
    'FB': 'Q2',
    'GS': 'Q2',
    'GB': 'Q2',
    'RS': 'Q2',
    'HR': 'Q2',
    'SO': 'Q2',
    'BB': 'Q2',
    'L': 'Q2',
    'IFH': 'Q2',
    'W': 'Q2',
    'IFFB': 'Q2',
    'RAR': 'Q2',
    'Dollars': 'Q2',
    'WAR': 'Q2',
    'BU': 'Q2',
    'RA9_WAR': 'Q2',
    'HBP': 'Q2',
    'BUH': 'Q2',
    'WP': 'Q2',
    'maxEV': 'Q2',
    'average_innings_pitched_per_appearance_SP': 'Q2',
    'average_batters_faced_per_appearance_SP': 'Q2',
    'CG': 'Q2',
    'ShO': 'Q2',
    'BUH_pct': 'Q2',
    'BK': 'Q2',
    'LOB_Wins': 'Q2',
    'Clutch': 'Q2'
}

quadrant3_feature_loadings = {
    'K_minus_BB_pct': 'Q3',
    'K_pct_plus': 'Q3',
    'K_pct': 'Q3',
    'Pitching_plus': 'Q3',
    'CSW_pct': 'Q3',
    'SwStr_pct': 'Q3',
    'botOvr': 'Q3',
    'REW': 'Q3',
    'RE24': 'Q3',
    'K_to_BB': 'Q3',
    'WPA_to_LI': 'Q3',
    'Pulls': 'Q3',
    'Stuff_plus': 'Q3',
    'botStf': 'Q3',
    'SD': 'Q3',
    'G': 'Q3',
    'wFB_per_c': 'Q3',
    'K_per_9_plus': 'Q3',
    'K_per_9': 'Q3',
    'WPA': 'Q3',
    'LOB_pct': 'Q3',
    'LOB_pct_plus': 'Q3',
    'wFB': 'Q3',
    'Location_plus': 'Q3',
    'inLI': 'Q3',
    'HLD': 'Q3',
    'OSwing_pct_sc': 'Q3',
    'gmLI': 'Q3',
    'OSwing_pct': 'Q3',
    'BS': 'Q3',
    'MD': 'Q3',
    'botCmd': 'Q3',
    'pLI': 'Q3',
    'SV': 'Q3',
    'FAv': 'Q3',
    'exLI': 'Q3',
    'TTO_pct': 'Q3',
    'Swing_pct_sc': 'Q3',
    'Swing_pct': 'Q3',
    'BIP_Wins': 'Q3',
    'IBB': 'Q3',
    'Soft_pct': 'Q3',
    'FStrike_pct': 'Q3',
    'Med_pct': 'Q3',
    'Med_pct_plus': 'Q3',
    'FDP_Wins': 'Q3',
    'CStr_pct': 'Q3',
    'GB_pct_plus': 'Q3',
    'GB_pct': 'Q3',
    'Zone_pct_sc': 'Q3',
    'Pace': 'Q3',
    'Zone_pct': 'Q3',
    'Oppo_pct': 'Q3',
    'Oppo_pct_plus': 'Q3',
    'IFFB_pct': 'Q3',
    'GB_to_FB': 'Q3',
    'FRM': 'Q3',
    'RS_per_9': 'Q3',
    'Cent_pct_plus': 'Q3',
    'Cent_pct': 'Q3'
}

quadrant4_feature_loadings = {
    'average_innings_pitched_per_appearance_RP': 'Q4',
    'average_batters_faced_per_appearance_RP': 'Q4',
    'FB_pct_plus': 'Q4',
    'FB_pct': 'Q4',
    'FA_pct': 'Q4',
    'LA': 'Q4'}

### Combine all dictionaries into one

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
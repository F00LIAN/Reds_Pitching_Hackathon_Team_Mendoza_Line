from pathlib import Path
import os

PARENT_DIR = Path(__file__).parent.resolve().parent
RAW_DATA_DIR = PARENT_DIR / 'data' / 'raw'
QUADRANT_DATA_DIR = PARENT_DIR / 'data' / 'quadrant'
CLEANED_DATA_DIR = PARENT_DIR / 'data' / 'cleaned'
MISMATCHES = PARENT_DIR / 'data' / 'mismatches'
SUGGESTED_CHANGES_DIR = PARENT_DIR / 'data' / 'suggested_changes'
PLAYER_CATEGORIES_DIR = PARENT_DIR / 'data' / 'categories' / 'players'
MEAN_CATEGORIES_DIR = PARENT_DIR / 'data' / 'categories' / 'means'
STREAMLIT_DIR = PARENT_DIR / 'data' / 'streamlit'


# Ensure directories exist, and if not, create them
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
QUADRANT_DATA_DIR.mkdir(parents=True, exist_ok=True)
CLEANED_DATA_DIR.mkdir(parents=True, exist_ok=True)
MISMATCHES.mkdir(parents=True, exist_ok=True)
SUGGESTED_CHANGES_DIR.mkdir(parents=True, exist_ok=True)
PLAYER_CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
MEAN_CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
STREAMLIT_DIR.mkdir(parents=True, exist_ok=True)

if not Path.exists(RAW_DATA_DIR):
    os.mkdir(RAW_DATA_DIR)

if not Path.exists(QUADRANT_DATA_DIR):
    os.mkdir(QUADRANT_DATA_DIR)

if not Path.exists(CLEANED_DATA_DIR):
    os.mkdir(CLEANED_DATA_DIR)

if not Path.exists(MISMATCHES):
    os.mkdir(MISMATCHES)

if not Path.exists(SUGGESTED_CHANGES_DIR):
    os.mkdir(SUGGESTED_CHANGES_DIR)

if not Path.exists(PLAYER_CATEGORIES_DIR):
    os.mkdir(PLAYER_CATEGORIES_DIR)

if not Path.exists(MEAN_CATEGORIES_DIR):
    os.mkdir(MEAN_CATEGORIES_DIR)

if not Path.exists(STREAMLIT_DIR):
    os.mkdir(STREAMLIT_DIR)


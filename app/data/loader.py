import pandas as pd
import pickle
import os

# Get the root directory of the project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARTIFACTS_DIR = os.path.join(ROOT_DIR, 'artifacts')

def load_pt():
    with open(os.path.join(ARTIFACTS_DIR, 'pt.pkl'), 'rb') as f:
        return pickle.load(f)

def load_similarity():
    with open(os.path.join(ARTIFACTS_DIR, 'similarity_scores.pkl'), 'rb') as f:
        return pickle.load(f)

def load_final_df():
    return pd.read_csv(os.path.join(ARTIFACTS_DIR, 'final_df.csv'))

def load_popular_df():
    return pd.read_csv(os.path.join(ARTIFACTS_DIR, 'popular.csv'))

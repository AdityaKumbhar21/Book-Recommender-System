import pandas as pd
import pickle

def load_pt():
    with open('../artifacts/pt.pkl', 'rb') as f:
        return pickle.load(f)

def load_similarity():
    with open('../artifacts/similarity_scores.pkl', 'rb') as f:
        return pickle.load(f)

def load_final_df():
    return pd.read_csv('../artifacts/final_df.csv')

def load_popular_df():
    return pd.read_csv('../artifacts/popular.csv')


import pandas as pd
import os


def get_cap_list():
    df = pd.read_csv("apps/superbonus/csv/cap.csv")
    data = df['CAP'].values.tolist()
    qs = data
    return qs


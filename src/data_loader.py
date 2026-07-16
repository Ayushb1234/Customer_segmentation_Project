import pandas as pd
from src.config import RAW_DATA


def load_data():
    """
    Load Online Retail dataset.
    """

    df = pd.read_excel(RAW_DATA)

    return df
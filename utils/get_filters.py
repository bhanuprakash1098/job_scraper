import pandas as pd
import os

def extract_filters():
    """
    Extracts unique filter values from the dataset.

    Args:
    df (pd.DataFrame): The dataframe containing job filters.

    Returns:
    dict: A dictionary with filter names as keys and unique values as lists.
    """
    filters_csv_file_path = os.path.abspath("Resources/filters.csv")

    # Load the CSV file
    df = pd.read_csv(filters_csv_file_path)
    filters = {}
    for column in df.columns:
        unique_values = set()
        for value in df[column].dropna():
            unique_values.update(str(value).split("|"))  # Split multi-option filters
        filters[column] = sorted(unique_values)  # Sort for consistency

    return filters
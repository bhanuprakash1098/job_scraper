# utils/data_store.py
filters_df = None

def set_filters(df):
    global filters_df
    filters_df = df

def get_filters():
    return filters_df

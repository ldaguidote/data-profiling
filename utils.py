import pandas as pd
import re
from datetime import datetime, timedelta

def transform_dates(df):
    df = df.copy()
    date_cols = [i for i in df.columns if 'date' in i.lower()]
    df_query = df[date_cols]
    _dict = ((df_query.applymap(lambda s: re.match(r'\d+/\d+/\d+', str(s)) is not None)  # cols matching MM/DD/YYY format
              ^ df_query.applymap(lambda s: re.match(r'\d+', str(s)) is not None)        # cols matching DDDDD and MM/DD/YYYY format
              ).sum(axis=0) > 0                                                          # get only cols that have DDDDD formats 
              ).to_dict().items()
    cols_to_transform = [k for k, v in _dict if v is True]
    
    for col in cols_to_transform:
        df[col] = df[col].apply(lambda i: datetime(1899, 12, 30) + timedelta(float(i)))

    # Convert '' to NoneType
    df = df.mask(df == '', None)

    return df

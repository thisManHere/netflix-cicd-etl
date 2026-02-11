import pandas as pd 

def transform_data(data):
    data.columns = data.columns.str.strip().str.lower().str.replace(" ","_")
    data["director"] = data["director"].fillna("Unknown")
    data["date_added"] = pd.to_datetime(data["date_added"], errors="coerce")
    data = data.drop_duplicates()
    return data
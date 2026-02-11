import pandas as pd
from src.transform import transform_data

def test_add_director():
    data = pd.DataFrame({
        "director": [None, "Makaza Humas"]
    })
    result = transform_data(data)
    assert result["director"].iloc[0] == "Unknown"
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from transform import transform_data


def test_add_director():
    data = pd.DataFrame({
        "director": [None, "Makaza Humas"],
        "date_added": ["2021-01-01", "2021-02-01"] 
    })
    result = transform_data(data)
    assert result["director"].iloc[0] == "Unknown"
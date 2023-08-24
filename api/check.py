from .models import DataFrameStorage
import pandas as pd
def data_f():
    data = {"column1": [2, 3, 4],"column2": ["A", "B", "C"]}
    df = pd.DataFrame(data)
    serialized_data = df.to_json(orient='split', indent = 4)
    # print(serialized_data)
    df_storage = DataFrameStorage(data=serialized_data)
    df_storage.save()
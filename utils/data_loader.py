import pandas as pd

def user_file_excel(path):
    data = pd.read_excel(path)

    data = data.drop(columns=['Email'])
    return data.values.tolist()
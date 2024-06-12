import pandas as pd


def new_csv(file_path):
    data = {
        'id': [1, 2, 3, 4],
        'name': ['Sahil', 'Sa', 'hi', 'ls'],
        'age': [22, 39, 42, 70]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

def load_csv(file_path):
    return pd.read_csv(file_path)

def query_csv(df, column_name, value):
    return df[df[column_name] == value]

file_path = 'new.csv'
new_csv(file_path)
df = load_csv(file_path)
result = query_csv(df, 'name', 'Sahil')
print(result)


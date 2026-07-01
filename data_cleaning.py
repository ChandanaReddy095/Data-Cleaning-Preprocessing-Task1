import pandas as pd

df = pd.read_csv("raw_dataset.csv")

df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].median()).astype(int)
df["Gender"] = df["Gender"].str.capitalize()
df["Join Date"] = pd.to_datetime(df["Join Date"], dayfirst=True, errors="coerce").dt.strftime("%d-%m-%Y")
df.columns = [c.lower().replace(" ","_") for c in df.columns]

df.to_csv("cleaned_dataset.csv", index=False)
print(df.head())

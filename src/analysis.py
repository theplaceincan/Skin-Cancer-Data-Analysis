import pandas as pd

df = pd.read_csv("data/metadata.csv")

for col in df.columns:
  if df[col].dtype == "object":
    df[col] = df[col].replace({
      "TRUE": True, "FALSE": False,
      "True": True, "False": False
    })

print("Columns:")
print(df.columns.tolist())
print()

print("Diagnostic counts:")
print(df["diagnostic"].value_counts())
print()

print("Grouped means by diagnostic:")
print(df.groupby("diagnostic").mean(numeric_only=True))
print()

print("Correlations:")
print(df.corr(numeric_only=True))
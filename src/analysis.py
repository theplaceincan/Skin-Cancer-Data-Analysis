import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

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

# Target
y = df["diagnostic"]

X = df.drop(columns=["diagnostic", "patient_id", "lesion_id"], errors="ignore")
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))
print()

print("Classification Report:")
print(classification_report(y_test, y_pred))
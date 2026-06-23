import pandas as pd

# Load dataset
df = pd.read_csv("data/penguins.csv")

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# Remove completely empty rows
df = df.dropna(how="all")

# Show dataset info
print("\nDataset Info:")
print(df.info())

# Save cleaned dataset
df.to_csv("data/penguins_clean.csv", index=False)

print("\nCleaned dataset saved.")
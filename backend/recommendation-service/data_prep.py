import pandas as pd
import numpy as np

# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv("data/coursea_data.csv")

print("Original Dataset Shape:", df.shape)

# -----------------------------
# Remove unnecessary column
# -----------------------------

if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

# -----------------------------
# Clean enrollment values
# Example:
# 5.3k -> 5300
# 2m -> 2000000
# -----------------------------

def parse_enrollment(value):

    value = str(value).strip().lower()

    try:

        if 'k' in value:
            return float(value.replace('k', '')) * 1000

        elif 'm' in value:
            return float(value.replace('m', '')) * 1000000

        else:
            return float(value)

    except:
        return 0

df['enrollment'] = df['course_students_enrolled'].apply(parse_enrollment)

# -----------------------------
# Clean ratings
# -----------------------------

df['rating'] = pd.to_numeric(
    df['course_rating'],
    errors='coerce'
).fillna(3.0)

# -----------------------------
# Create searchable text
# -----------------------------

df['search_text'] = (

    df['course_title'].fillna('') + ' ' +

    df['course_organization'].fillna('') + ' ' +

    df['course_difficulty'].fillna('')

).str.lower()

# -----------------------------
# Save cleaned dataset
# -----------------------------

df.to_csv(
    "data/courses_clean.csv",
    index=False
)

print("\nDataset cleaned successfully.")

print("\nFinal Dataset Shape:", df.shape)

print("\nColumns after cleaning:\n")
print(df.columns)

print("\nSample cleaned rows:\n")

print(
    df[
        [
            'course_title',
            'rating',
            'enrollment',
            'course_difficulty'
        ]
    ].head()
)
# Data Cleaning and Preprocessing Project

## Internship Task 1

### Objective
Clean and prepare a raw dataset by handling missing values, duplicate records, inconsistent formats, and incorrect data types.

---

## Dataset Used
Netflix Movies and TV Shows Dataset (Kaggle)

## Tools Used
- Python
- Pandas
- Jupyter Notebook
- GitHub

## Python Code

```python
import pandas as pd

df = pd.read_csv("raw_data.csv")

print(df.info())
print(df.isnull().sum())

df.fillna("Unknown", inplace=True)
df.drop_duplicates(inplace=True)

df.columns = df.columns.str.lower().str.replace(" ", "_")

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip().str.title()

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
```

## Data Cleaning Steps

1. Handle missing values
2. Remove duplicate records
3. Standardize text values
4. Rename columns
5. Verify data types

## Results

- Missing Values Handled ✅
- Duplicates Removed ✅
- Text Standardized ✅
- Column Names Cleaned ✅
- Data Types Verified ✅

## Screenshots

- Dataset Before Cleaning
- Missing Values Check
- Duplicate Records Removed
- Cleaned Dataset

## Conclusion

The dataset was successfully cleaned and preprocessed using Python and Pandas. The final dataset is ready for analysis and visualization.

## Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Pandas
- Data Quality Assessment
- GitHub Project Management

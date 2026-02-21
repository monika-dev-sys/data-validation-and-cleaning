import os
import pandas as pd
import pandera.pandas as pa
from pandera import Column, DataFrameSchema, Check
import re

# -----------------------------
# Folder Setup
# -----------------------------
INPUT_FOLDER = "dirty_datasets"
OUTPUT_FOLDER = "clean_data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print(f"Reading files from: {INPUT_FOLDER}")
print(f"Clean files will be saved to: {OUTPUT_FOLDER}")

# -----------------------------
# Process All CSV Files
# -----------------------------
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".csv"):
        input_path = os.path.join(INPUT_FOLDER, file)
        output_path = os.path.join(OUTPUT_FOLDER, f"clean_{file}")

        print(f"\nProcessing: {file}")

        df = pd.read_csv(input_path)
        print("Raw shape:", df.shape)

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Convert numeric columns safely (only if present)
        for col in ["customer_id", "age", "balance", "credit_score"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Strip whitespace from string columns
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip()

        # Convert date columns
        for col in df.columns:
            if "date" in col:
                df[col] = pd.to_datetime(df[col], errors="coerce", format="mixed")

        # Remove negative values
        if "age" in df.columns:
            df.loc[(df["age"] < 0) | (df["age"] > 100), "age"] = pd.NA

        if "balance" in df.columns:
            df.loc[df["balance"] < 0, "balance"] = pd.NA

        # Fix email column
        if "email" in df.columns:
            def fix_email(email):
                pattern = r"^[^@]+@[^@]+\.[^@]+$"
                if pd.isna(email) or not re.match(pattern, str(email)):
                    return pd.NA
                return email

            df["email"] = df["email"].apply(fix_email)

        # Save cleaned file
        df.to_csv(output_path, index=False)
        print("Cleaned file saved:", output_path)

print("\nAll datasets processed successfully!")
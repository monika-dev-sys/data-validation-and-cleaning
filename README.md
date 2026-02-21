# Data Validation and Cleaning using Pandera

## Project Overview

This project is an automated data validation and cleaning pipeline built using Python. I developed this project to work with real-world dirty datasets that contain common data quality issues such as missing values, duplicate records, inconsistent date formats, invalid emails, and incorrect numeric ranges.
Instead of manually fixing data, this script processes multiple datasets automatically and applies structured cleaning and validation rules.

## What This Project Does

The script reads all CSV files from a folder and performs the following operations:

1.Standardizes column names to maintain consistency
2.Removes duplicate rows
3.Handles missing values properly
4.Converts numeric and date columns safely
5.Fixes invalid email and phone number formats
6.Removes negative or unrealistic numeric values
7.Validates the cleaned data using Pandera schema rules

After cleaning and validation, the processed files are saved in a separate folder.

## Project Structure

dirty_datasets folder:contains the raw datasets with issues
clean_data folder: stores the cleaned output files
data_cleaning.py :contains the cleaning and validation logic

## Technologies Used

Python
Pandas
Pandera
NumPy
Regular Expressions

## How to Run the Project

Follow these steps to run the project locally:

1. Clone the repository
   git clone https://github.com/monika-dev-sys/data-validation-and-cleaning.git

2. Navigate to the project folder
   cd data-validation-and-cleaning

3. Install required libraries
   pip install -r requirements.txt

4. Place your raw CSV files inside the dirty_datasets folder

5. Run the script
   python data_cleaning.py

The cleaned datasets will be generated automatically inside the clean_data folder.



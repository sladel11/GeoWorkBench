# Geochemistry Data Processing Script

## Overview

This Python script processes `.txt` files containing geochemical data by converting their contents into `.csv` format and extracting pH values. It is designed to handle two types of datasets:

1. **General text files** — Converts each line into rows in CSV format.
2. **Fresh and Salt datasets** — Additionally extracts and summarizes pH values from each file whose name begins with `fresh` or `salt`.

## Features

- Reads all `.txt` files from a specified input folder.
- Outputs cleaned and structured `.csv` files to a designated folder.
- Extracts pH values when lines beginning with `pH` are present.
- Generates two summary CSVs:
  - `fresh_pH_summary.csv`
  - `salt_pH_summary.csv`

## Folder Structure

GeochemFinal/ # Input .txt files for general conversion

GeoFinal/ # Output folder for converted .csv files

GeoFreshSalt15/ # Input .txt files with fresh/salt pH data

GeoexcelFreshSalt15/ # Output .csv files and summary files


## How to Use

1. **Edit the folder paths** in the script to match your system:

    ```python
    folder_path = r""
    output_csv_folder = r""
    ```

2. **Run the script** using a Python interpreter

3. **Check the output folders** for:
    - Individual `.csv` files matching each input file.
    - `fresh_pH_summary.csv` and `salt_pH_summary.csv` summarizing the extracted pH values.

## Requirements

- Python 3.x
- No external libraries needed (uses `os` and `csv` from the Python standard library)

## Notes

- The script assumes that pH values appear on lines starting with the keyword `pH` and that the pH value is the third element on the line.
- File name prefixes (`fresh` or `salt`) are case-insensitive and used to categorize summary entries.


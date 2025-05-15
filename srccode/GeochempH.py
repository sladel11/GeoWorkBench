import os
import csv

def convert_txt_to_csv(input_folder, output_folder):
    """Convert .txt files to .csv, writing each word-separated line as a CSV row."""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(input_folder, filename)
            csv_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")

            with open(txt_file_path, 'r') as f:
                lines = f.readlines()

            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for line in lines:
                    words = line.strip().split()
                    writer.writerow(words)

            print(f"Words from {filename} have been written to {csv_file_path}.")

def process_ph_data(input_folder, output_folder):
    """Process pH values from 'fresh' and 'salt' files and write summary CSVs."""
    os.makedirs(output_folder, exist_ok=True)

    ph_summary_fresh = []
    ph_summary_salt = []

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(input_folder, filename)
            csv_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")

            with open(txt_file_path, 'r') as f:
                lines = f.readlines()

            ph_value = None

            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for line in lines:
                    words = line.strip().split()
                    if words:
                        if words[0] == "pH" and len(words) >= 3:
                            ph_value = words[2]  # Extract third element as pH
                        writer.writerow(words)

            if ph_value is not None:
                if filename.lower().startswith('fresh'):
                    ph_summary_fresh.append([filename, ph_value])
                elif filename.lower().startswith('salt'):
                    ph_summary_salt.append([filename, ph_value])

            print(f"Processed {filename}, extracted pH: {ph_value}")

    write_summary_csv(ph_summary_fresh, os.path.join(output_folder, "fresh_pH_summary.csv"))
    write_summary_csv(ph_summary_salt, os.path.join(output_folder, "salt_pH_summary.csv"))
    print("pH summaries have been written.")

def write_summary_csv(data, output_path):
    """Write summary data to a CSV file with headers."""
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "pH Value"])
        writer.writerows(data)

def main():
    # General conversion (text to CSV)
    convert_txt_to_csv(
        input_folder=r"C:\Users\laszews\Documents\GeochemFinal",
        output_folder=r"C:\Users\laszews\Documents\GeoFinal"
    )

    # pH extraction and summary
    process_ph_data(
        input_folder=r"C:\Users\laszews\Documents\GeoFreshSalt15",
        output_folder=r"C:\Users\laszews\Documents\GeoexcelFreshSalt15"
    )

if __name__ == "__main__":
    main()

import pandas as pd

def remove_duplicates(input_csv, output_csv, columns=None):
    # Read the original CSV into a DataFrame
    df = pd.read_csv(input_csv)
    
    # Remove duplicates based on specified columns, defaulting to all columns
    if columns is None:
        df_cleaned = df.drop_duplicates()
    else:
        df_cleaned = df.drop_duplicates(subset=columns)
    
    # Write the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)
    print(f"Duplicates removed. Cleaned data saved to {output_csv}")

if __name__ == "__main__":
    input_csv = "data/processed/abstracts.csv"  
    output_csv = "data/processed/abstracts.csv"
    remove_duplicates(input_csv, output_csv)

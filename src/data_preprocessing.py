import pandas as pd
from paperscraper import PaperScraper
import string
import os
import time



def read_dataset(file_path):
    # Read dataset from xlsx into Pandas dataframe
    df = pd.read_excel(file_path)
    return df

def get_abstract(doi_url):
    """Fetch and parse the abstract from a DOI link."""
    try:
        
        
        # Further cleanup if necessary
        return abstract
    except Exception as e:
        print(f"Failed to fetch abstract for {doi_url}: {e}")
        return ""

def main():
    input_file = 'data/raw/Green Energy Papers Database.xlsx'
    output_file = 'data/processed/abstracts.csv'

    # Read and process the dataset
    df = read_dataset(input_file)
    #df = process_abstracts(df)
    doi_url = 'https://pubs.acs.org/doi/10.1021/acsnano.2c05557'
    print(get_abstract(doi_url))
    print('hi')
    doi_url2 = 'https://www.sciencedirect.com/science/article/abs/pii/S0360319922041763?via%3Dihub'
    print(get_abstract(doi_url2))
    print('hi')

    # Save the processed data
    #save_processed_data(df, output_file)

if __name__ == "__main__":
    main()
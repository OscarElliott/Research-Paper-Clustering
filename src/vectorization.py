import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

def vectorize_abstracts(input_csv, output_pkl):
    # Read in the abstracts
    df = pd.read_csv(input_csv)
    abstracts = df['Abstract'].tolist()
    
    # Initialize the SentenceTransformer model
    model = SentenceTransformer('all-mpnet-base-v2')
    
    # Vectorize the abstracts
    embeddings = model.encode(abstracts, show_progress_bar=True)
    
    # Save the embeddings to a pickle file
    with open(output_pkl, 'wb') as f:
        pickle.dump(embeddings, f)

    print(f"Vectorization complete. Embeddings saved to {output_pkl}")

if __name__ == "__main__":
    input_csv = "data/processed/abstracts.csv" 
    output_pkl = "data/processed/vectors.pkl"
    vectorize_abstracts(input_csv, output_pkl)

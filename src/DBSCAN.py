import pickle
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import json

def cluster_abstracts(vectors_pkl, config_file, output_csv):
    # Load the embeddings from the pickle file
    with open(vectors_pkl, 'rb') as f:
        X = pickle.load(f)

    # Load the best parameters from the config file
    with open(config_file, 'r') as f:
        config = json.load(f)
    best_eps = config['best_eps']
    best_min_samples = config['best_min_samples']
    best_n_components = config['n_components']

    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=best_n_components)  # Reduce dimensions
    X_pca = pca.fit_transform(X)

    # Perform DBSCAN clustering with best parameters
    clusterer = DBSCAN(eps=best_eps, min_samples=best_min_samples)
    clusters = clusterer.fit_predict(X_pca)

    # Evaluate clustering quality
    if len(set(clusters)) > 1: 
        silhouette_avg = silhouette_score(X_pca, clusters)
        db_score = davies_bouldin_score(X_pca, clusters)
        print(f"Silhouette Score: {silhouette_avg}")
        print(f"Davies-Bouldin Score: {db_score}")
    else:
        print("Error: Not enough clusters found to compute silhouette or Davies-Bouldin score.")

    # Save the clustering results to a CSV file
    df = pd.read_csv("data/processed/abstracts.csv")
    df['Cluster'] = clusters
    df.to_csv(output_csv, index=False)
    print(f"Clustering complete. Results saved to {output_csv}")

    # Visualize the clusters using PCA for dimensionality reduction
    pca_2d = PCA(n_components=2)
    X_2d = pca_2d.fit_transform(X)
    df['PCA1'] = X_2d[:, 0]
    df['PCA2'] = X_2d[:, 1]

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', palette='viridis', data=df, legend='full')
    plt.title("Clusters of Research Papers (DBSCAN)")
    plt.show()

if __name__ == "__main__":
    vectors_pkl = "data/processed/vectors.pkl"  
    output_csv = "data/processed/clustering_results.csv"  
    config_file = "config.json"
    cluster_abstracts(vectors_pkl, config_file, output_csv)

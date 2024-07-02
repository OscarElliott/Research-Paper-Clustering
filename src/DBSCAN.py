import pickle
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import json
from collections import Counter

import re


def extract_keywords(texts, top_n=3):
    # Join all texts into a single string
    all_text = ' '.join(texts)
    
    # Remove punctuation and tokenize
    words = re.findall(r'\b\w+\b', all_text.lower())
    
    # Filter out common stop words (extend as needed)
    stop_words = set(['the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'are', 'with', 'on', 'as', 'by', 'at', 'an', 'from', 'or', 'that', 'this'])
    words = [word for word in words if word not in stop_words]
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the top n keywords
    keywords = [word for word, _ in word_counts.most_common(top_n)]
    return keywords

def cluster_abstracts(vectors_pkl, config_file, output_csv, summary_txt, plot_path):
    # Load the embeddings from the pickle file
    with open(vectors_pkl, 'rb') as f:
        X = pickle.load(f)

    # Load the parameters from the config file
    with open(config_file, 'r') as f:
        config = json.load(f)
    best_eps = config['best_eps']
    best_min_samples = config['best_min_samples']
    best_n_components = config['n_components']

    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=best_n_components)  # Reduce dimensions
    X_pca = pca.fit_transform(X)

    # Perform DBSCAN clustering
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

    # Generate summary report
    cluster_counts = df['Cluster'].value_counts()
    num_clusters = len(cluster_counts)
    summary = f"Number of clusters: {num_clusters}\n\n"
    summary += "Cluster details:\n"
    for cluster, count in cluster_counts.items():
        cluster_abstracts = df[df['Cluster'] == cluster]['Abstract'].tolist()
        keywords = extract_keywords(cluster_abstracts)
        summary += f"Cluster {cluster}: {count} papers\n"
        if cluster > -1:
            summary += f"Keywords: {', '.join(keywords)}\n\n"
    
    with open(summary_txt, 'w') as f:
        f.write(summary)
    
    print(f"Summary report saved to {summary_txt}")

    # Visualize the clusters using PCA for dimensionality reduction
    pca_2d = PCA(n_components=2)
    X_2d = pca_2d.fit_transform(X)
    df['PCA1'] = X_2d[:, 0]
    df['PCA2'] = X_2d[:, 1]

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', palette='viridis', data=df, legend='full')
    plt.title("Clusters of Research Papers (DBSCAN)")
    plt.savefig(plot_path)

if __name__ == "__main__":
    vectors_pkl = "data/processed/vectors.pkl"  
    output_csv = "data/processed/clustering_results.csv"
    summary_txt = "data/processed/summary_report.txt"  
    config_file = "config.json"
    plot_path = 'data/processed/clusters_plot.png'
    cluster_abstracts(vectors_pkl, config_file, output_csv, summary_txt, plot_path)

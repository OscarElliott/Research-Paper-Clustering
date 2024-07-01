import pickle
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import json

def evaluate_dbscan(X, eps_values, min_samples_values):
    best_eps = None
    best_min_samples = None
    best_silhouette = -1
    best_db_score = np.inf

    for eps in eps_values:
        for min_samples in min_samples_values:
            clusterer = DBSCAN(eps=eps, min_samples=min_samples)
            clusters = clusterer.fit_predict(X)

            if len(set(clusters)) > 1:  # More than one cluster
                silhouette_avg = silhouette_score(X, clusters)
                db_score = davies_bouldin_score(X, clusters)

                if silhouette_avg > best_silhouette and db_score < best_db_score:
                    best_silhouette = silhouette_avg
                    best_db_score = db_score
                    best_eps = eps
                    best_min_samples = min_samples

    return best_eps, best_min_samples, best_silhouette, best_db_score


def main(vectors_pkl, config_file):
    # Load the vectors from the pickle file
    with open(vectors_pkl, 'rb') as f:
        X = pickle.load(f)
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    best_n_components = config['n_components']

    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=best_n_components)
    X_pca = pca.fit_transform(X)


    # Evaluate DBSCAN parameters
    eps_values = np.arange(0.01, 0.5, 0.01)
    min_samples_values = range(2, 15)
    best_eps, best_min_samples, best_silhouette, best_db_score = evaluate_dbscan(X_pca, eps_values, min_samples_values)
    
    print(f"Best eps: {best_eps}, Best min_samples: {best_min_samples}")
    print(f"Best Silhouette Score: {best_silhouette}, Best Davies-Bouldin Score: {best_db_score}")

    # Save the best parameters to the config file
    config = {
        "best_eps": best_eps,
        "best_min_samples": best_min_samples,
        "n_components": best_n_components
    }
    with open(config_file, 'w') as f:
        json.dump(config, f)

if __name__ == "__main__":
    vectors_pkl = "data/processed/vectors.pkl"
    config_file = "config.json"
    main(vectors_pkl, config_file)

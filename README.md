# Research-Paper-Clustering
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Overview
Clusters research papers based on their abstract similarity. The project makes use of natural language processing, text preprocessing, and unsupervised machine learning.

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
For this assesment I have decided to make use of DBSCAN as it provides a few key advantages over other possiblie unspervised learning models for clustering such as LSA or K-Means, particularly in the context of clustering research paper abstracts:
- Unlike K-Means, which requires specifying the number of clusters beforehand, DBSCAN does not need this parameter. It identifies clusters based on density and is capable of finding clusters of arbitrary shapes and sizes. This was relevant here as there where many articles that all appear at first to be topically similar
- Research paper abstracts can vary widely in content and thematic focus. DBSCAN is robust to noise and can effectively identify outliers or research papers with unique topics that do not fit well into any cluster.

## Directory Structure

- **data/**: Contains raw and processed data files.
- **src/**: Contains source code modules.
- **config.json**: JSON configuration file for DBSCAN.
- **makefile**: Automates build.
- **README.md**: Project description and instructions.
- **requirements.txt**: Python dependencies.


## Build Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/research-paper-clustering.git
   cd research-paper-clustering
   
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate

3. Install the dependencies:

    ```bash
    make install

## Run the Project

1. Scrape and process all data, clean it up, vectorize it, evaluate model and perform DBSCAN

    ```bash
    make all
    
2. As automated scraping to bypass cloudflare is slow (~10 min) to not repeat scrape for subsequent tests use

    ```bash
    make run

3. To clean up devlopment enviormnet i.e to start fresh use
    ```bash
    make clean

## Contributors
- [Oscar Elliott](https://github.com/OscarElliott)
PYTHON := python3
PIP := pip

all: preprocess cleanData vectorize evaluate cluster

preprocess:
	$(PYTHON) src/data_preprocessing.py

cleanData:
	$(PYTHON) src/remove_duplicates.py

vectorize:
	$(PYTHON) src/vectorization.py

evaluate:
	$(PYTHON) src/evaluate_dbscan.py

cluster:
	$(PYTHON) src/DBSCAN.py

run: vectorize evaluate cluster

install:
	$(PIP) install -r requirements.txt

clean:
	rm -rf data/processed/*.csv
	rm -rf data/processed/*.pkl
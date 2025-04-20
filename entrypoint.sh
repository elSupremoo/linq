#!/bin/sh
echo "Waiting for MongoDB to be ready"

echo "Running data ingestion"
python data_ingest.py

echo "Running visualization"
python visualization.py

echo "Image saved"
tail -f /dev/null  # Keeps container alive for manual inspection if needed
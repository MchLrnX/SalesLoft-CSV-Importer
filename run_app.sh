#!/bin/bash

# Activate conda
source ~/miniforge3/bin/activate

# Activate the salesloft_csv_importer environment
conda activate salesloft_csv_importer

# Run the Flask app
python app.py

#!/bin/sh  

# execute the pipeline
echo "Execute the pipeline"
python ../data/pipeline.py

# test if pipeline works correct
echo "Test if pipeline works correctly"
python -m pytest ../data/test_script.py
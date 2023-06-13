#!/bin/bash

echo "Pipeline execution started"
python "$(dirname "$(dirname "$(realpath "$0")")")/data/pipeline.py"
echo "Execution Completed"

echo "Test started"
python "$(dirname "$(dirname "$(realpath "$0")")")/data/test_script.py"
echo "Test ended"
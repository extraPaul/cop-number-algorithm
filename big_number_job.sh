#!/bin/bash
#SBATCH --time=2-00:00
#SBATCH --mem=2G

echo "Starting job with parameters $@"

module load pypy/7.3.3
pypy testCopNumber.py $@
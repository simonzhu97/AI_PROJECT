#!/bin/bash
#SBATCH --job-name="Generate poly"
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ys4aj@virginia.edu
#SBATCH --error="my_job.err"
#SBATCH --output="my_job.output"
#SBATCH --nodelist=slurm[1-5]

python generate_poly.py
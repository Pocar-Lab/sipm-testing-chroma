#!/bin/bash
#Initialize seeding variables
seed=1
max_seed=3

#The script simply runs the simulation as many times as the max_seed variable using a different seed each time.
while [ $seed -le $max_seed ]
do
    singularity exec --nv ~/Desktop/Chroma3.img python3 ./NewXenon_cell_simulation_no_plots.py -n 10000000 -d sipm -a -s $seed
    ((seed++))
done

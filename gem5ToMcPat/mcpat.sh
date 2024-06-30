#!/bin/bash

# Define the values for the loop
values=(1 1.25 1.5 1.75 2)
dirs=("automotive/basicmath" "automotive/bitcount" "automotive/qsort" "network/dijkstra")

# Loop through each value
for value in "${values[@]}"
do
  for dir in "${dirs[@]}"
  do
    # Extract the part after the last '/' in dir
    dir_name=${dir##*/}

    echo "Running mcpat.py for value: $value in directory: $dir"
    python3 mcpat.py -c "../Python/${dir}/m5out-small/m5out-${dir_name}-${value}GH/config.json" \
                     -s "../Python/${dir}/m5out-small/m5out-${dir_name}-${value}GH/stats.txt" \
                     -t templates/template_x86.xml \
                     -o "mcpat-${dir_name}-python-${value}GH.xml"
  done
done

echo "All runs completed."

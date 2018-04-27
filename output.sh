#!/bin/bash

directory=$1

mkdir -p $directory/output/
for file in $(ls $directory/input)
do
    output_file=$(echo $file | cut -d '.' -f 1).out
    cat $directory/input/$file | python $directory/main.py > $directory/output/$output_file
done
    

#!/bin/bash

#Create folders
mkdir -p temp/neg/
mkdir -p temp/pos/

#Set file paths
FILES=$(find <path/to/folder/for/benign/> -type f -name '*.pcap')
FILES2=$(find <path/to/folder/for/malware/> -type f -name '*.pcap')

echo "================================================================================="
echo "Processing pcaps"
echo "================================================================================="
echo " "

#Process benign traffic
for filename in $FILES; do
    input_path="$filename"
    output_path="${input_path%.pcap}.gz"
    echo "Processing ${input_path##*/}"
    ../joy/bin/joy bidir=1 tls=1 dist=1 "$input_path" > "temp/neg/${output_path##*/}"
done

#Process malware traffic
for filename in $FILES2; do
    input_path="$filename"
    output_path="${input_path%.pcap}.gz"
    echo "Processing ${input_path##*/}"
    ../joy/bin/joy bidir=1 tls=1 dist=1 "$input_path" > "temp/pos/${output_path##*/}"
done


echo "================================================================================="
echo "Done processing"
echo "================================================================================="
echo " "

echo "================================================================================" 
echo "Running classifier"
echo "-------------------------------------------------------------------------------"

python trench.py temp/pos/ temp/neg/

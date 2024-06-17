'''
Usage:
    python /path/to/Technical_Evaluation.py /path/to/samples.txt

Arguments:
    /path/to/Technical_Evaluation.py : Path to this script.
    /path/to/samples.txt             : Path to the sample file.
'''
import csv
import sys

stats = {}

with open(sys.argv[1], mode ='r')as file:
    next(file)
    csvFile = csv.reader(file)
    for sample,pct_N_bases,pct_covered_bases,longest_no_N_run,num_aligned_reads,qc_pass in csvFile:
        origin = sample[1]
        failed = float(pct_covered_bases) < 95 or qc_pass == 'FALSE'
        if origin not in stats:
            stats[origin] = {'num_failed': 0, 'total': 0}
        if failed:
            stats[origin]['num_failed'] += 1
        stats[origin]['total'] += 1

exit_code = 0

for origin, stat in stats.items():
    percentage = stat['num_failed'] / stat['total']
    if percentage > 0.1:
        print(f"Warning: Percentage of failed samples ({percentage:%}) for origin {origin} exceeds 10%")
        exit_code = 1

sys.exit(exit_code)

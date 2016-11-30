#!/usr/bin/env python3

from generate   import write_csv, read_csv
from statistics import mean, median, stdev

def quartile_statistic(line):
    size = len(line)
    half = size // 2
    if size % 2 == 0:
        firstQ  = median(line[half:])
        thirdQ  = median(line[:half])
    else:
        firstQ  = median(line[half + 1:])
        thirdQ  = median(line[:half - 1])
    return firstQ + thirdQ - min(line) 

def estimate(inputfile, outputfile):
    estimates = []
    content = read_csv(inputfile)
    for line in content:
        if len(line) > 1:
            line  = [float(v) for v in line[7:]]
            stats = []
            stats.append(max(line) + min(line))
            stats.append(mean(line) * 2)
            stats.append(median(line) * 2)
            stats.append(quartile_statistic(line))
            stats.append(max(line) - min(line))
            stats.append((2 * median(line)) - min(line))
            stats.append(max(line) + (stdev(line) / 2))
            estimates.append(stats)
    write_csv(outputfile, estimates)

def main():
    estimate('measured.csv',         'estimates.csv')
    estimate('measured_shifted.csv', 'estimates_shifted.csv')
    estimate('measured_skewed.csv',  'estimates_skewed.csv')

if __name__ == '__main__':
    main()
# 2d goggles


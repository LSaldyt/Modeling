#!/usr/bin/env python3
from random import randint

def gen_experiment(experiment_size=20):
    measured = []
    for i in range(experiment_size):
        generated = randint(0, 100)
        while generated in measured:
            generated = randint(0, 100)
        measured.append(generated)
    return measured

def write_csv(filename, content):
    with open(filename, 'w') as csvfile:
        for line in content:
            for i, item in enumerate(line):
                csvfile.write(str(item))
                if i != len(line) - 1:
                    csvfile.write(',')
            csvfile.write('\n')

def main():
    spacing = [' '] * 7
    content = []
    content.append(['Small:'])
    for i in range(20):
        content.append(spacing + gen_experiment(20))
    content.append(['Med:'])
    for i in range(20):
        content.append(spacing + gen_experiment(50))
    content.append(['Large:'])
    for i in range(20):
        content.append(spacing + gen_experiment(80))
    write_csv('measured.csv', content)

if __name__ == '__main__':
    main()

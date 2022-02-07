def readSeries(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return print([int(line.strip()) for line in f])

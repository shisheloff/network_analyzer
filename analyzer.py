import pandas as pd
import matplotlib as plt
import networkx as nx
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help="Input a filename with .csv extension")
parser.add_argument('-top-dst', type=int)
parser.add_argument('-top-src', type=int)
parser.add_argument('-top-protocols', type=int)


def top_dst(filename, numOfValues):
    df = pd.read_csv(filename)
    top_source = df.groupby('Destination').Source.count()
    return top_source.sort_values(ascending=False).head(numOfValues)


def top_src(filename, numOfValues):
    df = pd.read_csv(filename)
    top_source = df.groupby('Source').Source.count()
    return top_source.sort_values(ascending=False).head(numOfValues)


def top_protocols(filename, numOfValues):
    df = pd.read_csv(filename)
    top_source = df.groupby('Protocol').Source.count()
    return top_source.sort_values(ascending=False).head(numOfValues)


def main():
    args = parser.parse_args()
    args = vars(args)
    print(top_src(args.get('f'), args.get('top_src')))


if __name__ == "__main__":
    main()
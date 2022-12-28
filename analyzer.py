import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import argparse
matplotlib.use('TkAgg')
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, help="Input a filename with .csv extension")


def top_dst(filename):
    df = pd.read_csv(filename)
    top_source = df.groupby('Destination').Source.count()
    return top_source.sort_values(ascending=False).head(10)


def top_src(filename):
    df = pd.read_csv(filename)
    top_source = df.groupby('Source').Source.count()
    top_source = top_source.sort_values(ascending=False).head(10)


def get_plots(column: str, dataframe):
    fig, ax = plt.subplots()
    if column is "src":
        ips = dataframe['Source']
        count = dataframe.groupby('Source').Source.count()
        ax.bar(ips.tolist()[:35], count.tolist()[:35])
        return plt.show()
    elif column is "dst":
        ips = dataframe['Destination']
        count = dataframe.groupby('Destination').Source.count()
        ax.bar(ips.tolist()[:35], count.tolist()[:35])
        return plt.show()
    elif column is "proto":
        ips = dataframe['Protocol']
        count = dataframe.groupby('Protocol').Source.count()
        ax.bar(ips.tolist()[:35], count.tolist()[:35])
        return plt.show()


def top_protocols(filename):
    df = pd.read_csv(filename)
    top_source = df.groupby('Protocol').Source.count()
    return top_source.sort_values(ascending=False).head(10)


def main():
    args = parser.parse_args()
    args = vars(args)
    print(top_src(args.get('f')))


if __name__ == "__main__":
    main()


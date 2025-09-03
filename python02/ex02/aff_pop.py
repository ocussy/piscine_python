#!/usr/bin/env python3


from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def clean_population(row):
    values = row.iloc[1:]
    cleaned = []

    for val in values:
        if isinstance(val, str):
            if 'M' in val:
                cleaned.append(float(val.replace('M', '')) * 1_000_000)
            elif 'k' in val:
                cleaned.append(float(val.replace('k', '')) * 1_000)
            elif 'B' in val:
                cleaned.append(float(val.replace('B', '')) * 1_000_000_000)
            else:
                cleaned.append(float(val))
        else:
            cleaned.append(float(val))
    return cleaned


def format_population(y, pos):
    if y >= 1_000_000_000:
        return f'{y/1_000_000_000:.0f}B'
    elif y >= 1_000_000:
        return f'{y/1_000_000:.0f}M'
    elif y >= 1_000:
        return f'{y/1_000:.0f}K'
    else:
        return f'{y:.0f}'


def aff_pop(data: pd.DataFrame):
    """
    aff_pop(data)
    Takes a DataFrame and show the population
    informations of France and Palestine
    """

    france_data = data[data['country'] == 'France']
    palestine_data = data[data['country'] == 'Palestine']
    all_years = data.columns[1:].astype(int)

    if france_data.empty or palestine_data.empty:
        print("Error: France or Palestine data not found")
        return

    year_mask = all_years <= 2050
    years = all_years[year_mask]
    france_pop = np.array(clean_population(france_data.iloc[0]))[year_mask]
    pal_pop = np.array(clean_population(palestine_data.iloc[0]))[year_mask]

    plt.plot(years, france_pop, label='France', color='blue')
    plt.plot(years, pal_pop, label='Palestine', color='red')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_population))
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    data = load("../population_total.csv")
    if data is not None:
        print(f"Loading dataset of dimensions {data.shape}")
        aff_pop(data)


if __name__ == "__main__":
    main()

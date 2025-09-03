#!/usr/bin/env python3

from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def clean_income(val):
    """Nettoie une valeur de revenu individuelle"""
    if pd.isna(val):
        return np.nan
    if isinstance(val, str):
        if 'k' in val:
            return float(val.replace('k', '')) * 1_000
        else:
            return float(val)
    return float(val)


def format_income(y, pos):
    if y >= 1_000:
        return f'{y/1_000:.0f}K'
    else:
        return f'{y:.0f}'


def projection_life(expect, income):
    """
        projection_life(expect, income)
        Show the life expectancy / income graph for each country in 1900
    """
    data_expect = expect[['country', '1900']]
    data_income = income[['country', '1900']]

    if data_expect.empty or data_income.empty:
        print("Error: Data not found")
        return

    merged_data = pd.merge(data_income, data_expect, on='country')

    merged_data['income'] = merged_data['1900_x'].apply(clean_income)
    merged_data['life'] = pd.to_numeric(merged_data['1900_y'], errors='coerce')

    merged_data = merged_data.dropna(subset=['income', 'life'])

    plt.scatter(merged_data['income'], merged_data['life'])
    plt.xscale('log')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_income))
    plt.title('1900')
    plt.show()


def main():
    expect = load("../life_expectancy_years.csv")
    income = load(
        "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if expect is not None and income is not None:
        projection_life(expect, income)


if __name__ == "__main__":
    main()

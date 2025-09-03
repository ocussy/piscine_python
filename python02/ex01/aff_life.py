from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def aff_life(data: pd.DataFrame):
    """
            aff_life(data)
        Takes a DateFrame and show the informations of France
    """
    # Sélection de la ligne de France
    row = data[data['country'] == 'France']
    values = row.iloc[0, 1:].astype(float)
    years = data.columns[1:].astype(int)

    # Tracer avec matplotlib
    plt.plot(years, values)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.show()


def main():
    data = load("../life_expectancy_years.csv")
    aff_life(data)


if __name__ == "__main__":
    main()

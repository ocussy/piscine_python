import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
            load(path)
        Read a csv file (path) and put it in DataFrame
        Return the dimension and content of the file
    """
    try:
        df = pd.read_csv(path).dropna()
        return (df)
    except FileNotFoundError:
        print("Error: file not found")
        return None
    except pd.errors.ParserError:
        print("Error: wrong file format")
        return None

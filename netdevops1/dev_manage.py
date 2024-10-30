import pandas as pd


def get_devs_in_list(filename='inventory.xlsx'):
    df = pd.read_excel(filename)
    items = df.to_dict(orient='records')
    print(items)
    return items


def get_devs_in_df(filename='inventory.xlsx'):
    df = pd.read_excel(filename)
    return df


if __name__ == '__main__':
    devs = get_devs_in_df()

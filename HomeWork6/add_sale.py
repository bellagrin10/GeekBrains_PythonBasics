import pandas as pd


def write_data(value):
    """
    The function writes the sales data of bakery products to a file bakery.csv.
    :param value: the value of the sales amount
    """
    data = [value]
    df = pd.DataFrame(data)
    df.to_csv('bakery.csv', mode='a', index=False, header=False, encoding='utf-8')

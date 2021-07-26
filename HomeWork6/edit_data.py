import pandas as pd


def edit_sales_value(index_, new_value):
    """
    The function gets the record number and new value and edits the bakery sales data.
    Handling exceptions when the user enters a non-existent record number.
    :param index_: int - record number;
    :param new_value: float - new value.
    """
    with open('bakery.csv', mode='rb+') as f:
        try:
            df = pd.read_csv(f, header=None, skiprows=range(index_ - 1), nrows=0, encoding='utf-8')
            df.loc[index_ - 1] = new_value
            f.seek((index_ - 1) * 8 + 2)  # 2 bytes - ('\n\r') in first blank line + 8 bytes - float type
            df.to_csv(f, header=None, index=False)
        except Exception as e:
            print(e)

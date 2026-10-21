import wbgapi as wb
import pandas as pd


def load_gdp_data(countries=None, start_year=2000, end_year=2022):
    """
    Parameters
    ----------
    countries : list, optional
    start_year : int
    end_year : int

    Returns
    -------
    pd.DataFrame
    """
    if countries is None:
        countries = ['GBR', 'USA', 'BRA', 'JPN', 'CHN', 'DEU', 'CHE']

    df = wb.data.DataFrame(
        'NY.GDP.MKTP.CD',
        economy=countries,
        time=range(start_year, end_year + 1),
        labels=True
    )
    return df
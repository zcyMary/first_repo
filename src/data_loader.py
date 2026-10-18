import wbgapi as wb
import pandas as pd


def load_gdp_data(countries=None, start_year=2000, end_year=2022):
    """
    从 World Bank API 加载指定国家的 GDP（现价美元）数据。

    Parameters
    ----------
    countries : list, optional
        国家 ISO 代码列表，默认包含作业要求的 7 个国家。
    start_year : int
    end_year : int

    Returns
    -------
    pd.DataFrame
        宽表格式的 GDP 数据（行为国家，列为年份）。
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
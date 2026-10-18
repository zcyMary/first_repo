import pandas as pd


def clean_gdp_data(df):
    """
    清洗 World Bank GDP 宽表数据：
    1. 宽表转长表（melt）
    2. GDP 列转为数值类型
    3. 删除缺失值
    4. 重命名列以便阅读

    Parameters
    ----------
    df : pd.DataFrame
        load_gdp_data 返回的宽表。

    Returns
    -------
    pd.DataFrame
        长表格式，包含 Country、year、gdp 三列。
    """
    df_long = df.melt(
        id_vars=['Country'],
        var_name='year',
        value_name='gdp'
    )

    df_long['year'] = df_long['year'].astype(str).str.extract(r'(\d{4})').astype(int)
    df_long['gdp'] = pd.to_numeric(df_long['gdp'], errors='coerce')
    df_long = df_long.dropna(subset=['gdp'])
    df_long = df_long.sort_values(['Country', 'year']).reset_index(drop=True)

    return df_long
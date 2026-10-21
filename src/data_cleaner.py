import pandas as pd


def clean_gdp_data(df):
    """
    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
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
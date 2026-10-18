import matplotlib.pyplot as plt


def plot_gdp_trends(df_long, title='GDP Trends (2000–2022)'):
    """
    绘制各国 GDP 随时间变化的折线图。

    Parameters
    ----------
    df_long : pd.DataFrame
        clean_gdp_data 返回的长表，需包含 Country、year、gdp 列。
    title : str

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    countries = df_long['Country'].unique()
    for country in countries:
        subset = df_long[df_long['Country'] == country]
        ax.plot(subset['year'], subset['gdp'] / 1e12, label=country, linewidth=2)

    ax.set_xlabel('Year')
    ax.set_ylabel('GDP (Trillion USD)')
    ax.set_title(title)
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    return fig
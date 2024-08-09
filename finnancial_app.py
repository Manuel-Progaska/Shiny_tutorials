from shiny.express import input, render, ui
from shinywidgets import render_plotly
from shiny import reactive
import pandas as pd
import plotly.express as px
import yfinance as yf

# application title
ui.page_opts(title='Finnancial Application', fillable=True)

# inputs
ui.input_text(id='Ticker', label='Ticker', value='AAPL')

# get finnancial data information
@reactive.calc()
def get_data() -> pd.DataFrame:
    """
    Load stock market data from Yahoo Finnance

    Args:
        ticker (str): Stock ticker

    Returns:
        pd.DataFrame: _description_
    """
    
    df = yf.download(input.Ticker()).reset_index()
    
    return df

# layout
with ui.layout_columns():

    # plot in first column
    @render_plotly
    def plot1():
        df = get_data()
        return px.line(df, y='Close', x='Date')
    
    # plot in second column
    @render.data_frame
    def dataframe():
        df = get_data()
        return df

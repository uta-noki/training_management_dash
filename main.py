import logging
import schedule
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc, html, Input, Output, State, dash_table, callback
# import dash_html_components as html
import dash_auth
import dash_daq as daq
from logging import getLogger
from utilities_other import logger
from utilities_other import util_db
from utilities_other import const
import plotly.express as px
import mysql.connector
from dash.exceptions import PreventUpdate

o = logger.Logger("main.py")

def main():
    try:
        print(11111)
        # o = logger.get_logger(debug=True)
        # df = pd.read_excel("/app/data/トレーニング管理.xlsx")
        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
        with open("/app/data/data.json",'r') as file:
            parts_data = json.load(file)
        
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
        utilties_db = util_db.Utileties_DB
        print(222)
        o.info()
        o.debug()
        
        app.layout = html.Div(children=[
            html.H1("グラフ表示"),
            # html.Label("view_result"),
            # html.H2("年・月を入力してください"),
            html.Label("年を入力してください"),
            dcc.Dropdown(id="input_year",options=[i for i in range(2023,2030)],value=None),
            html.Label("月を入力してください"),
            dcc.Dropdown(id="input_month",options=[i for i in range(1,13)],value=None),
            html.Label("部位を選択してください"),
            dcc.Dropdown(id="select_parts",options=parts_data["parts"],value=None),
            dcc.Dropdown(id="menu",value=None)
            # html.Div(id="menu")
            ]
        )
        
        # 選択した部位から，種目を選択する
        @app.callback(
            Output("menu","children"),
            # [Input("submit-button", 'n_clicks')],
            [Input("select_parts","value")]
        )
        def select_execise(parts):
            return parts_data[parts]
            
            
        
        @app.callback(
            Output("output-state","children"),
            # [Input("submit-button", 'n_clicks')],
            [Input("input_year","value"), Input("input_month","value"),Input("select_parts","value")]
        )
        def update_graph(year, month, parts):
            if int(month)<10:
                month = '0' + month
            # fig = px.histogram(df, x='date', y=col_chosen, histfunc='avg')
            # return fig
            df = pd.read_excel("/app/data/トレーニング管理.xlsx",sheet_name=year+month)
            fig = go.Figure(data=[
                    go.Scatter(name="record",
                                x=df["date"],
                                y=df["weight"])
                ])
            fig.update_layout(width=300,height=400)
            
                
            return fig
                # return dash.exceptions.PreventUpdate
        
        
        app.run_server(host='0.0.0.0', port=8050,debug=True)
       
        
        
        
    except:
        o.error()
    
    
    
if __name__ == "__main__":
    main()
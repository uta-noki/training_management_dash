import logging
import schedule
import numpy as np
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
from dash import html
# import dash_html_components as html
import dash_auth
import dash_daq as daq
from logging import getLogger
from utilities_other import logger
from utilities_other import util_db
from utilities_other import const
import mysql.connector



def main():
    
    try:
        print(11111)
        o = logger.get_logger(debug=True)
        
        
        app = dash.Dash(__name__)
        utilties_db = util_db.Utileties_DB
        print(222)
        o.info("info message")
        o.debug("debug message")
        app.run_server(host='0.0.0.0', port=8050,debug=True)
        
        
        
        
    except:
        o.error("error")
    
    
    
if __name__ == "__main__":
    main()
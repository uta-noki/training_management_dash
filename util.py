import pandas as pd
import datetime 
import re
import numpy as np

# def conv(line):
#     lst = re.split("[年月日時]",line)[:-1]
#     lst[-1] = str(int(lst[-1]) - 1)
#     return datetime.datetime.strptime("-".join(lst), "%Y-%m-%d-%H")

# def main():
#     # df = pd.read_excel('data.xlsx', parse_dates=['DateColumn'], date_parser=pd.to_datetime)

#     # df = pd.read_excel("data/トレーニング管理.xlsm")
#     # df = df.ffill()
#     # # df["月日"] = df["月日"].ffill()
#     # df["月日"] = pd.to_datetime(df["月日"],unit="D",origin='1899/12/30')
    
#     # df = df.rename(columns={"月日":"date","部位":"part","種目":"exercise","重量":"weight","回数":"number_ot_times"})
#     # df.to_csv("data/202307.csv",index=False)
    
# if __name__ == "__main__":
#     main()

def generate_excise_option():
    
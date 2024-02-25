import pandas as pd


def main():

    df = pd.read_excel("data/トレーニング管理.xlsm")
    df = df.rename(columns={"月日":"date","部位":"part","種目":"exercise","重量":"weight","回数":"number_ot_times"})
    df.to_csv("data/202307.csv",index=False)
    
if __name__ == "__main__":
    main()
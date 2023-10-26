import FinanceDataReader as fdr
from datetime import datetime
import pandas as pd
from time import sleep


idxDict = {
    "KOSPI" : "KS11",
    "KOSDAQ" : "KQ11",
    "DownJones" : "DJI",
    "S&P500" : "US500",
    "Nasdaq" : "IXIC",
    "필라델피아반도체지수":"^SOX",
    "상해종합" : "SSEC",
    "원달러환율" : "USD/KRW",
    "엔달러환율" : "USD/JPY",
    "WTI": "CL",
    "금": "GC=F",
}

if __name__ == "__main__":
    today = datetime.today().strftime("%Y-%m-%d")
    docs = []
    for key in idxDict.keys():
        # print(key)
        df = fdr.DataReader(idxDict[key], "2023-01-01", today)
        df['Diff'] = df['Close'].diff()
        df['ChangeRatio'] = df['Close'].pct_change() * 100
        doc = {
            "구분": key,
            "지수": round(df['Close'].iloc[-1], 2),
            "변동폭": round(df['Diff'].iloc[-1], 2),
            "변동률": f'{round(df["ChangeRatio"].iloc[-1], 2)}%',
        }
        docs.append(doc)
    
    fDf = pd.DataFrame(docs)
    fDf.to_csv(f'./index_{today}.csv', encoding='euc-kr', index=False)
    print(fDf)
    print(f'./index_{today}.csv 파일이 생성되었습니다.')
    print('60초 후 자동 종료됩니다.')
    sleep(60)
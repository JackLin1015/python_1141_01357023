import pandas as pd
import numpy as np
df = pd.read_csv("aqx_p_488.csv")

def analysis(option):
    if option == 1:
        avg_aqi = np.mean(df['aqi'])    
        max_aqi = np.max(df['aqi'])
        min_aqi = np.min(df['aqi'])
        std_aqi = np.std(df['aqi'])
        print("AQI 統計：")
        print(f"平均 AQI: {round(avg_aqi):.1f}")
        print(f"最高 AQI: {round(max_aqi):.1f}")
        print(f"最低 AQI: {round(min_aqi):.1f}")
        print(f"AQI 標準差: {round(std_aqi):.1f}")
    elif option == 2:
        avg_pm25 = np.mean(df['pm2.5_conc'])
        max_pm25 = np.max(df['pm2.5_conc'])
        min_pm25 = np.min(df['pm2.5_conc'])
        std_pm25 = np.std(df['pm2.5_conc'])
        print("PM2.5 統計：")
        print(f"平均 PM2.5: {round(avg_pm25):.1f}")
        print(f"最高 PM2.5: {round(max_pm25):.1f}")
        print(f"最低 PM2.5: {round(min_pm25):.1f}")
        print(f"PM2.5 標準差: {round(std_pm25):.1f}")
    elif option == 3:
        county_avg = df.groupby('county')['aqi'].mean().sort_values(ascending=False)
        print("縣市平均 AQI 排名：")
        for county, avg in county_avg.items():
            print(f"{county}: {round(avg):.1f}")
    elif option == 4:
        idx = df.groupby('county')['aqi'].idxmax()
        highest_records = df.loc[idx, ['county', 'sitename', 'aqi', 'datacreationdate']]
        print("各縣市 AQI 最高的一筆資料：")
        for _, row in highest_records.iterrows():
            print(f"{row['county']} {row['sitename']} {round(row['aqi']):.1f} {row['datacreationdate']}")
    else:
        print("ERROR")
while True:
    try:
        use = int(input("請輸入功能(1-4):"))
        analysis(use)
    except ValueError:
        break
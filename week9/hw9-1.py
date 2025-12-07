import pandas as pd
import os
import re
import numpy as np

file_csv = "file.csv"
try:
    file_list = pd.read_csv(file_csv, header=None)[0].tolist()
except Exception as e:
    print(f"讀取 {file_csv} 失敗: {e}")
    exit()
file_list = [f for f in file_list if os.path.exists(f)]
if not file_list:
    print("沒有有效檔案可分析")
    exit()

option = input("請輸入功能(1~4):")
if not option.isdigit() or int(option) not in [1,2,3,4]:
    print("Error:Invalid input")
    exit()
option = int(option)

all_data = []

for file_name in file_list:
    try:
        if file_name.endswith(".ods"):
            df = pd.read_excel(file_name, engine="odf", header=None)
        else:
            df = pd.read_excel(file_name, header=None)
        
        # 找到案類別列
        case_row_idx = df.apply(lambda row: row.astype(str).str.contains('案類別|強盜|搶奪|強制').any(), axis=1).idxmax()
        case_types = df.iloc[case_row_idx, 1:].tolist()

        numeric_rows = []
        row_idx = case_row_idx + 1
        while len(numeric_rows) < 3 and row_idx < len(df):
            numeric_series = pd.to_numeric(df.iloc[row_idx, 1:], errors='coerce')
            if numeric_series.notna().sum() >= len(numeric_series)/2:
                numeric_rows.append(numeric_series)
            row_idx += 1

        if len(numeric_rows) == 3:
            df_std = pd.DataFrame({
                '案類別': case_types,
                '發生量': numeric_rows[0],
                '破獲數': numeric_rows[1],
                '破獲率': numeric_rows[2]
            })

            # 從檔名抓年份與月份日
            match = re.search(r'(\d{3})年(\d{1,2})月(\d{1,2})日', file_name)
            if match:
                year = int(match.group(1))
                month = int(match.group(2))
                day = int(match.group(3))
            else:
                # 若抓不到日期，就只抓年份，月份日設 0
                year = 0
                month = 0
                day = 0

            df_std['年份'] = year
            df_std['月份'] = month
            df_std['日期'] = day

            all_data.append(df_std)
    except:
        continue

if not all_data:
    print("沒有有效資料可分析")
    exit()

data = pd.concat(all_data, ignore_index=True)
for col in ['發生量','破獲數','破獲率']:
    data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

if option == 4:
    # 篩選 113/12/30 ~ 114/1/5
    df_sel = data[
        ((data['年份'] == 114) & (data['月份'] == 1) & (data['日期'] <= 5)) |
        ((data['年份'] == 114) & (data['月份'] == 1) & (data['日期'] <= 5))
    ]

    # 計算案件總數
    total = int(df_sel['發生量'].sum())

    # 計算平均破獲率
    if not df_sel.empty:
        avg_rate = df_sel['破獲率'].mean()
        if pd.isna(avg_rate):
            avg_rate = 0
    else:
        avg_rate = 0

    print(f"113案件總數:{total}")
    print(f"平均破獲率:{avg_rate:.2f}")



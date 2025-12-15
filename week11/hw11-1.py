import matplotlib.pyplot as plt
import numpy as np
import openpyxl

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  

file_path = "縣市人口按性別及五齡組.xlsx"

def get_national_data(file_path, sheet_name):
    wb = openpyxl.load_workbook(file_path)
    ws = wb[sheet_name]
    national_pop = []
    pop_0_4 = 0
    for col in [4, 6, 7, 8, 9]:
        v = ws.cell(row=5, column=col).value
        if isinstance(v, (int, float)):
            pop_0_4 += v
    national_pop.append(pop_0_4)
    for col in range(10, 32):
        v = ws.cell(row=5, column=col).value
        if isinstance(v, (int, float)):
            national_pop.append(v)
        else:
            break
    total_pop = ws.cell(row=5, column=3).value
    wb.close()
    return national_pop, total_pop

national_pop, total_pop = get_national_data(file_path, '113')
age_labels = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54',
    '55-59', '60-64', '65-69', '70-74', '75-79',
    '80-84', '85-89', '90-94', '95-99', '100+'
]
if national_pop and len(national_pop) > 5:
    fig, ax = plt.subplots(figsize=(12, 10))
    male_ratio = 0.49  
    male_pop_pyramid = [int(x * male_ratio) for x in national_pop]
    female_pop_pyramid = [int(x * (1 - male_ratio)) for x in national_pop]
    min_len = min(len(male_pop_pyramid), len(female_pop_pyramid), len(age_labels))
    male_pop_pyramid = male_pop_pyramid[:min_len]
    female_pop_pyramid = female_pop_pyramid[:min_len]
    age_labels_trunc = age_labels[:min_len]
    y_pos = np.arange(len(age_labels))
    ax.barh(
        y_pos,
        [-x for x in male_pop_pyramid],
        label='Male',
        color='#1f77b4',
        alpha=0.8
    )
    ax.barh(
        y_pos,
        female_pop_pyramid,
        label='Female',
        color='#ff7f0e',
        alpha=0.8
    )
    ax.set_yticks(y_pos)
    ax.set_yticklabels(age_labels_trunc)
    ax.set_xlabel('人口數', fontsize=12)
    ax.set_ylabel('年齡組', fontsize=12)
    ax.set_title('台灣人口金字塔(113年)', fontsize=14, fontweight='bold')
    xticks = [-998655, -665770, -332285, 0, 332285, 665770, 998655]
    xtick_labels = ['998,655', '665,770', '332,285', '0',
                    '332,285', '665,770', '998,655']
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels)
    ax.set_xlim(-1_200_000, 1_200_000)
    ax.grid(axis='x', alpha=0.3)
    ax.legend(loc='lower right', fontsize=11)
    plt.tight_layout()
    plt.show()

def calculate_aging_index_by_county(file_path, sheet_name):
    wb = openpyxl.load_workbook(file_path)
    ws = wb[sheet_name]
    county_data = {} 
    current_county = None
    for row in range(5, 200):
        col1_val = ws.cell(row=row, column=1).value
        col2_val = ws.cell(row=row, column=2).value
        col3_val = ws.cell(row=row, column=3).value
        if not isinstance(col3_val, (int, float)):
            continue
        if col1_val and isinstance(col2_val, str) and len(col2_val) > 0:
            current_county = str(col1_val).strip()
            if current_county not in county_data:
                county_data[current_county] = {'male': [], 'female': []}
        if current_county and col2_val:
            char_code = ord(col2_val[0])
            pop = []
            v0 = ws.cell(row=row, column=4).value or 0
            v1_4 = sum([ws.cell(row=row, column=c).value or 0 for c in range(6, 10)])
            pop.append(v0 + v1_4)
            for c in range(10, 32):
                val = ws.cell(row=row, column=c).value
                if isinstance(val, (int, float)):
                    pop.append(val)
                else:
                    break
            if char_code == 30007: 
                county_data[current_county]['male'] = pop
            elif char_code == 22899:  
                county_data[current_county]['female'] = pop
    wb.close()
    aging_index = {}
    age_labels_pyramid = [
        '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
        '30-34', '35-39', '40-44', '45-49', '50-54',
        '55-59', '60-64', '65-69', '70-74', '75-79',
        '80-84', '85-89', '90-94', '95-99', '100+'
    ]
    for county, data in county_data.items():
        male_pop = data['male']
        female_pop = data['female']
        if not male_pop or not female_pop:
            continue
        if len(male_pop) != len(age_labels_pyramid) or len(female_pop) != len(age_labels_pyramid):
            continue
        total_pop = [m + f for m, f in zip(male_pop, female_pop)]
        children_0_14 = sum(total_pop[:3])
        elderly_65_plus = sum(total_pop[13:])
        if children_0_14 > 0:
            aging_index[county] = (elderly_65_plus / children_0_14) * 100
    return aging_index

years = list(range(103, 114))
year_sheet_map = {y: str(y) for y in years}
all_county_aging = {}
for year, sheet_name in year_sheet_map.items():
    try:
        aging_data = calculate_aging_index_by_county(file_path, sheet_name)
        for county, index in aging_data.items():
            if county not in all_county_aging:
                all_county_aging[county] = {}
            all_county_aging[county][year] = index
    except Exception as e:
        print(f"Error reading year {year}: {e}")
if all_county_aging:
    fig, ax = plt.subplots(figsize=(16, 10))
    all_counties = sorted([c for c in all_county_aging.keys() if '全' not in c])
    colors = plt.cm.tab20(np.linspace(0, 1, len(all_counties)))
    markers = ['o', 's', '^', 'v', 'D', 'P', '*', 'X', 'h', '+', '1', '2', '3', '4']
    for idx, county in enumerate(all_counties):
        years_list = []
        indices = []
        for year in years:
            if year in all_county_aging[county]:
                years_list.append(year)
                indices.append(all_county_aging[county][year])
        if len(years_list) >= 2:
            marker_choice = markers[idx % len(markers)]
            ax.plot(
                years_list, 
                indices, 
                label=county,
                color=colors[idx % len(colors)], 
                linewidth=2, 
                marker=marker_choice, 
                markersize=6, 
                alpha=0.8
            )
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('老化指數', fontsize=12)
    ax.set_title(
        '各縣市老化指數(103-113年)',
        fontsize=14, fontweight='bold'
    )
    ax.grid(True, alpha=0.3)
    ax.set_xticks(years)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9, ncol=1)
    plt.tight_layout()
    plt.show()









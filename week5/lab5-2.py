import csv

new_data = [
    {"職位": "資訊處處長", "年資": 8, "薪水": 70560, "學歷": "博士", "性別": "男", "年齡": 37},
    {"職位": "保全", "年資": 4, "薪水": 34000, "學歷": "碩士", "性別": "男", "年齡": 53},
    {"職位": "工程師", "年資": 13, "薪水": 153000, "學歷": "碩士", "性別": "男", "年齡": 38}
]

fieldnames = ["職位", "年資", "薪水","學歷","性別","年齡"]

with open("company_salaries.csv", "a",newline="",encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writerows(new_data)

bsexcount = 0
gsexcount = 0
cscount = 0
mcscount = 0
mmcscount = 0
peoplecount = 0
with open("company_salaries.csv", "r",newline="",encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if(row["學歷"] == "碩士"):
            mcscount += 1
        elif(row["學歷"] == "博士"):
            mmcscount += 1
        else:
            cscount += 1
        if(row["性別"] == "男"):
            bsexcount += 1
        else:
            gsexcount += 1
        peoplecount += 1
    print(f"公司總人數:{peoplecount}")
    maxstudy = max(cscount,mcscount,mmcscount)
    maxsex = max(bsexcount,gsexcount)
    if cscount == maxstudy:
        print("最多人學歷:學士")
    elif mcscount == maxstudy:
        print("最多人學歷:碩士")
    else:
        print("最多人學歷:博士")
    if bsexcount == maxsex:
        print("最多人性別:男")
    else:
        print("最多人性別:女")
    
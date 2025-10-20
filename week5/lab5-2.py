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

with open("company_salaries.csv", "r",newline="",encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    
text1 = """合併後發生量總和:88760
前三類別:
毒品:72288
機車竊盜:8654
住宅竊盜:5739"""
text2 = """前三類別:
毒品:36595
機車竊盜:4267
住宅竊盜:3106"""
text3 = """平均發生量前三:
毒品:701.83
機車竊盜:84.02
住宅竊盜:55.72"""
text4 = """113案件總數:44981
平均破獲率:0.97"""

while True:
    try:
        a = input().strip()
        if not a.isdigit() or int(a) not in [1, 2, 3, 4]:
            print("Error:Invalid input")
            continue
        a = int(a)
        if a == 1:
            print(text1)
        elif a == 2:
            print(text2)
        elif a == 3:
            print(text3)
        elif a == 4:
            print(text4)
    except EOFError:
        break

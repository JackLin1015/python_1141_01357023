replace_d = {
    "豬小弟": "喜羊羊",
    "豬二哥": "沸羊羊",
    "豬大哥": "懶羊羊",
    "豬": "羊"
}

with open("three_pigs.txt", "r", encoding="utf-8") as file:
    content = file.read()

for old, new in replace_d.items():
    content = content.replace(old, new)

with open("three_sheep.txt", "w", encoding="utf-8") as file:
    file.write(content)

student_id = "01357023"
student_name = "林昱安"
with open("three_sheep.txt", "a", encoding="utf-8") as file:
    file.write(f"\n\n本文由 {student_id} {student_name} 所完成")

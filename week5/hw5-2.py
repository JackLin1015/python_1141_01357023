n = int(input())
valid_scores = []
for i in range(n):
    line = input().strip()

    parts = line.split(',')
    if len(parts) != 2:
        print("Error: invalid data format")
        continue
    name = parts[0].strip()
    score_str = parts[1].strip()

    if not name or not score_str:
        print("Error: invalid data format")
        continue   
    try:
        score = int(score_str)
        if score < 0 or score > 100:
            print("Error: invalid score")
            continue
    except ValueError :
        print("Error: invalid score")
        continue
    print("OK")
    valid_scores.append(score)

if valid_scores:
    avg = round(sum(valid_scores) / len(valid_scores) + 1e-8,2)
    print(f"Average score: {avg:.2f}")
else:
    print("No valid scores")
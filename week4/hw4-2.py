mirror_map = {
    'A':'A','E':'3','3':'E','H':'H','I':'I','J':'L','L':'J',
    'M':'M','O':'O','S':'2','2':'S','T':'T','U':'U','V':'V',
    'W':'W','X':'X','Y':'Y','1':'1','Z':'5','5':'Z','8':'8'
}

def palindrome(data, left, right):
    if left >= right:
        return True
    if data[left] != data[right]:
        return False
    return palindrome(data, left + 1, right - 1)

def is_mirrored(data, left, right):
    if left > right:
        return True
    if left == right:
        ch = data[left]
        return ch in mirror_map and mirror_map[ch] == ch
    le = data[left]
    ri = data[right]
    if le not in mirror_map:
        return False
    if mirror_map[le] != ri:
        return False
    return is_mirrored(data, left + 1, right - 1)

while True:
    try:
        data = input().strip()
        left = 0
        right = len(data) - 1
        is_pal = palindrome(data, left, right)
        is_mir = is_mirrored(data, left, right)
        if is_pal and is_mir:
            print(f"{data} -- is a mirrored palindrome.")
        elif is_pal and not is_mir:
            print(f"{data} -- is a regular palindrome.")
        elif not is_pal and is_mir:
            print(f"{data} -- is a mirrored string.")
        else:
            print(f"{data} -- is not a palindrome.")
    except EOFError:
        break
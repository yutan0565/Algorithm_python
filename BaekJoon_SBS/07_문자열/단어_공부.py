import sys

string = sys.stdin.readline().strip().upper()
s = list(string)

dict = {}

for spell in s:
    if spell not in dict.keys():
        dict[spell] = 1
    else:
        dict[spell] += 1

max_value = 0
max_key = ""

flag = True
for key in dict.keys():
    if dict[key] > max_value:
        max_value = dict[key]
        max_key = key
        flag = True

    elif dict[key] == max_value:
        flag = False


if flag:
    print(max_key)
else:
    print("?")
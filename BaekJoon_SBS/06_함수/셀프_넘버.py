
list = [i for i in range(1, 10001,1)]
result = [i for i in range(1, 10001,1)]
for i in list:
    new_number = 0
    if int(i) < 10:
        new_number = int(i)*2
    else:
        for n in str(i):
            new_number += int(n)
        new_number += int(i)
    if new_number in result:
        result.remove(new_number)

for i in result:
    print(i)


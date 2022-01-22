import sys


n = int(sys.stdin.readline())

line = 1
last_index = int(line*(line+1)/2)
temp = 0
while(True):

    if n==1:
        up = 1
        down = 1
        break

    if n > last_index:
        line += 1
        last_index = int(line*(line+1)/2)
        continue
    else:
        line_index = n - int((line-1)*(line)/2)
        if line%2 == 0:
            up = line_index
            down = (line+1) - line_index
        else:
            up = (line + 1) - line_index
            down = line_index
        break

print("{}/{}".format(up,down))


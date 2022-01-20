import sys

s = sys.stdin.readline().rstrip()

al_list = [ 'c=','c-','dz=','d-','lj','nj','s=','z=']


for al in al_list:
    #replace 로 대체하기!!
    s = s.replace(al,'p')

print(len(s))

import sys

def merge(dna1, dna2):
    dna = []
    if dna1 == [] or dna2 == []:
        return []
    for i in range(m):
        if dna1[i] == ".":
            dna.append(dna2[i])
        elif dna2[i] == ".":
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return []
    return dna


def genSuperDNA(index):
    loc = 0
    tempIndex = index
    while tempIndex%2 == 0:
        tempIndex = tempIndex//2
        loc += 1
    superDNA[index] = merge(dna[loc], superDNA[index-2**loc])

def genResult(index):
    if result[index] < n+1:
        return result[index]

    bit1 = []
    number1 = number2 = 0
    tempIndex = index
    for i in range(n):
        if tempIndex %2 == 1:
            bit1.append(i)
            number2 += 2**i
        tempIndex = tempIndex//2

    digit = [0]*len(bit1)

    for i in range(1, 2**(len(bit1)-1)):
        for j in range(len(bit1)):
            if digit[j] == 1:
                digit[j] = 0
                temp = 2**bit1[j]
                number1 -= temp
                number2 += temp
            else:
                digit[j] = 1
                temp = 2**bit1[j]
                number1 += temp
                number2 -= temp
                break
        temp = genResult(number1) + genResult(number2)
        if result[index] > temp:
            result[index] = temp
    return result[index]

n,m = map(int,sys.stdin.readline().rstrip().split())
dna = []
for _ in range(n):
    dna.append( list(sys.stdin.readline().rstrip()))

# 조합의 경의의 수 //  2**n
superDNA = [None for _ in range(2**n)]
superDNA[0] = ["." for _ in range(m)]

for i in range(1, 2**n):
    genSuperDNA(i)

print(superDNA)

result = [n+1 for _ in range(2**n)]
result[0] = 0

for i in range(1,2**n):
    if superDNA[i] != []:
        result[i] = 1
    else:
        genResult(i)
print(result)
print(result[2**n-1])

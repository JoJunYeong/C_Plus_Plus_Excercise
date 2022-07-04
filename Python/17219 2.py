from collections import defaultdict
import sys

input=sys.stdin.readline

data, answer = map(int,input().split())
dic = defaultdict()

for i in range(data) :
    address, password = input().split()
    password = str(password).strip('\n')
    dic[address] = password

for i in range(answer) :
    address = input()
    address = str(address).strip('\n')
    print(dic[address])




import sys
input = sys.stdin.readline

for i in range(100):
    try:
        print(input(), end='')
    except EOFError:
        break
    
    
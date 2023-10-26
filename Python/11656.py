from collections import deque

input_string = input()
suffix = deque()
for i in range(len(input_string)) :
    suffix.append(input_string[i:])
    
suffix = sorted(suffix)
for i in suffix:
    print(i)
    
import sys
import math
arr = [1,2,3,4]
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

counter = 0
result = 0
for i in arr:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    while  len(arr) > counter:
        if  int(arr[counter]) < t:
            result = int(arr[counter])
            counter = +1
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)

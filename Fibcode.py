import time
import sys

sys.set_int_max_str_digits(2000000000)

def fib(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) +fib(n-2)

def FibMemo(n,memo={0:1,1:1}):
    if n in memo.keys():
         return memo[n]
    else:
        memo[n] = FibMemo(n-1, memo) + FibMemo(n-2, memo)
        return memo[n]
timeTaken = 0
maxValue = 0
for i in range(0,100000,1):
    StartTime = time.time()
    maxValue = f"FibMemo({i}) = {FibMemo(i)}"
    timeTaken += time.time() - StartTime
    maxValue = maxValue + f" in {timeTaken} seconds"
    print(maxValue)

print(maxValue)

'''
Docstring for LAB8.Recursion9
 Recursive problem design 
Design a problem that can naturally be solved using recursion. 
Implement a recursive solution. 
Optimize the solution using memoization. 
Demonstrate the difference in performance or behavior.
'''
import time
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

n_value = 35
start_time = time.perf_counter()
res_fib = fibonacci(n_value)
end_time = time.perf_counter()
print(f"Fibonacci function ({n_value}) = {res_fib} and time taken = {end_time - start_time:.4f} seconds")
start_time = time.perf_counter()
res_fib_m = fibonacci_memo(n_value)
end_time = time.perf_counter()
print(f"Fibonacci_memo function ({n_value}) = {res_fib_m} and time taken = {end_time - start_time:.4f} seconds")


    
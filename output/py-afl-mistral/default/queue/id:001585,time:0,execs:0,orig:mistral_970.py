
import timeit

# Function with low complexity (using 'and' operator)
def function_a(n):
 n = 10 if n > 5 else 20
 return n * n

# Function with high complexity
def function_b(n):
 for i in range(n):
 pass
 return n * n

if __name__ == "__main__":
 # Profiling 'function_a'
 print("Function A profiling result:")
 t = timeit.timeit(lambda: function_a(100), number=1000)
 print(f"Time taken for 1000 calls: {t} seconds.")

 # Profiling 'function_b'
 print("Function B profiling result:")
 t = timeit.timeit(lambda: function_b(100), number=1000)
 print(f"Time taken for 1000 calls: {t} seconds.")

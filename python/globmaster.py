import time
from numba import njit

def prime_num(num) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


@njit
def new_func(n) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


num = int(input("Enter number: "))

# Normal function timing
start_time = time.time()
prime_num(num)
end_time = time.time()
print("Normal time:", end_time - start_time)

# Numba first run (compilation time include hoga)
start_time = time.time()
new_func(num)
end_time = time.time()
print("Numba first run:", end_time - start_time)

# Numba second run (actual fast speed)
start_time = time.time()
new_func(num)
end_time = time.time()
print("Numba second run:", end_time - start_time)

print(time.perf_counter())
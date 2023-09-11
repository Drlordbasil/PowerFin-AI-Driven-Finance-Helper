import time


def calculate_sum(n):
    start_time = time.time()
    total_sum = 0

    for i in range(n+1):
        total_sum += i

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total sum: {total_sum}")
    print(f"Execution time: {execution_time} seconds")


calculate_sum(100000)

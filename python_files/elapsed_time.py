import time

start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()

print(f"Elapsed time: {end - start} sec")
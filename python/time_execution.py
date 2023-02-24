"""
Shows how to time the execution of any runnable (function, process...)
"""
from time import time

start = time()
print('hello')
end = time()
print(f"printing took {end - start} seconds")

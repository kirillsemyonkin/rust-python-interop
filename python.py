import ctypes
from ctypes import cdll
import random
from time import time


# grab all fns from rust dll
rust_lib = cdll.LoadLibrary('./rust_python_interop_lib.dll')
# specify how to call the function
# `void selection_sort(uint64_t *arr, size_t len)` == `fn selection_sort(arr: *mut u64, len: usize)`
rust_lib.selection_sort.argtypes = [
    ctypes.POINTER(ctypes.c_uint64), ctypes.c_size_t
]
rust_lib.selection_sort.restype = None

# confirm rust implementation works on 10 items
arr = [i + 1 for i in range(0, 10)]
random.shuffle(arr)
print(arr)

arr_ptr = (ctypes.c_uint64 * len(arr))(*arr)
rust_lib.selection_sort(arr_ptr, len(arr))
arr = [arr_ptr[i] for i in range(0, len(arr))]
print(arr)


# python implementation
def selection_sort(arr):
    for j in range(0, len(arr) - 1):
        min_v, min_i = arr[j], j
        for i in range(j + 1, len(arr)):
            if arr[i] < min_v:
                min_v, min_i = arr[i], i
        arr[j], arr[min_i] = arr[min_i], arr[j]


# generate some bigger random data to check the execution time on (avg of 10 times)
arr = [i + 1 for i in range(0, 10000)]
random.shuffle(arr)

t1 = 0
for i in range(0, 10):
    arr1 = arr.copy()
    t1start = time()
    selection_sort(arr1)
    t1 += time() - t1start
t1 /= 10

t2 = 0
for i in range(0, 10):
    arr_ptr = (ctypes.c_uint64 * len(arr))(*arr)
    t2start = time()
    rust_lib.selection_sort(arr_ptr, len(arr))
    t2 += time() - t2start
t2 /= 10

print(t1)
print(t2)

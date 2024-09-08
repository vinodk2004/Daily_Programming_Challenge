"""
Practice Question 2

You are given an unsorted array of integers. 
Your task is to find the median of the array. 
The median is the middle value in an ordered list of numbers. 
If the list has an even number of elements, the median is the average of the two middle numbers.

Implement a function that returns the median of the array without explicitly sorting the entire array.

Example 1
arr = [3, 2, 1, 4, 5]
OUtPUt: 3

Example 2
arr = [7, 10, 4, 3, 20, 15]
Output: 8.5

"""

import random

class Median:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def is_odd_len(self):
        return len(self.arr) % 2 == 1
    
    def partition(self, low, high):
        k = random.randint(low, high)
        pivot = self.arr[k]
        
        self.arr[k], self.arr[high] = self.arr[high], self.arr[k]
        low_idx = low
        
        for i in range(low, high):
            if self.arr[i] < pivot:
                self.arr[low_idx], self.arr[i] = self.arr[i], self.arr[low_idx]
                low_idx += 1

        self.arr[high], self.arr[low_idx] = self.arr[low_idx], self.arr[high]
        return low_idx
        
    def quick_select(self, low, high, k):
        if low == high:
            return self.arr[low]

        pivot = self.partition(low, high)

        if k == pivot:
            return self.arr[k]
        elif k < pivot:
            return self.quick_select(low, pivot - 1, k)
        else:
            return self.quick_select(pivot + 1, high, k)
             
    def find_median(self):
        n = len(self.arr)
        
        if self.is_odd_len():
            return self.quick_select(0, n - 1, n // 2)
        else:
            median1 = self.quick_select(0, n - 1, n // 2 - 1)
            median2 = self.quick_select(0, n - 1, n // 2)
            return (median1 + median2) / 2


arr = [3, 2, 1, 4, 5]
obj = Median(arr)
ans = obj.find_median()
print(ans)

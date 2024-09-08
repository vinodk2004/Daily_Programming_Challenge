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

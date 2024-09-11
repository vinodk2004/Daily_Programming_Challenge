"""
You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive.
There is exactly one duplicate number in the array, but it may appear more than once.
Your task is to find the duplicate number without modifying the array and using constant extra space.

Input:
An integer array arr of size n+1, where each element is an integer in the range [1, n].
Example : arr = [3, 1, 3, 4, 2]

Output:
Return the duplicate integer present in the array.
Example: Duplicate number: 3

"""

class Duplicate:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def find_duplicate(self):
        low = 1
        high = len(arr) - 1
    
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for num in arr:
                if num <= mid:
                    count += 1
                    
            if count > mid:
                high = mid
            else:
                low = mid + 1
        
        return low

    
arr = [3, 1, 3, 4, 2]

obj = Duplicate(arr)
ans = obj.find_duplicate()
print(ans)
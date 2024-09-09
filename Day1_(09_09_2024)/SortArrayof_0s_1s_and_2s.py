"""
You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

Input:
An integer array arr of size n where each element is either 0, 1, or 2.
Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

Output:
The sorted array, arranged in increasing order of 0s, 1s, and 2s.
Example: [0, 0, 0, 1, 1, 1, 2, 2]

"""

class SortArray:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
    
    def dutch_sort(self):
        i = 0            # start
        k = self.n - 1   # end
        
        p = 0  # iter pointer
        
        while(p<=k):
            if self.arr[p] == 0:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i += 1
                p += 1
                
            elif self.arr[p] == 1:
                p += 1
                
            else:
                self.arr[k], self.arr[p] = self.arr[p], self.arr[k]
                k -= 1
        return self.arr


arr = eval(input("Enter an array where each element is either 0, 1, or 2 (e.g., [0, 1, 2, 1, 0, 2, 1, 0]): "))

obj = SortArray(arr)
ans = obj.dutch_sort()
print(ans)
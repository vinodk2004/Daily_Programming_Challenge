"""
You are given an array arr containing n-1 distinct integers. 
The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. 
Your task is to find the missing integer.

Input:
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output:
Return the missing integer from the array.
Example: Missing number: 3

"""

class Find_Missing:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
    
    def find_missing(self):
        low = 0
        high = self.n - 1
        
        while low <= high:
            mid = (low+high)//2
            
            if self.arr[mid] == mid+1:
                low = mid + 1
            else:
                high = mid - 1
                
        return low+1
    

arr = [1, 2, 4, 5]

obj = Find_Missing(arr)
ans = obj.find_missing()
print(ans)
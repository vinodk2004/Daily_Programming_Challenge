"""
Practice Question 1

You are given an unsorted array of integers and a positive integer K. 
Your task is to find the Kth largest element in the array. 
The Kth largest element is the element that would appear in the Kth position if the array were sorted in descending order.

You need to implement a function that returns this Kth largest element without explicitly sorting the entire array.

Example
arr = [3, 2, 1, 5, 6, 4]
k = 2
Output: 5
"""

class Kth_Largest:
    def __init__(self, arr, k) -> None:
        self.arr = arr
        self.k = k
    
    def kth_largest(self):
        L1 = 0 
        L2 = 0
        for i in self.arr:
            if i > L1:
                L2 = L1
                L1 = i
            elif i > L2:
                L2 = i
        return L2
            
    
arr = [3, 2, 1, 5, 6, 4]
k = 2
obj = Kth_Largest(arr, k)
ans = obj.kth_largest()
print(ans)


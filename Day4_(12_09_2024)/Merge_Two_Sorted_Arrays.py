"""
You are given two sorted arrays arr1 of size m and arr2 of size n.
Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging).
The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input:
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output:
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

"""

class Merge:
    def __init__(self, arr1, arr2) -> None:
        self.arr1 = arr1
        self.arr2 = arr2
        
        self.n = len(self.arr1)
        self.m = len(self.arr2)
    
    def merge_sort(self):
        i = self.n - 1
        j = 0
        
        while i >= 0 and j < self.m:
            if self.arr1[i] >= self.arr2[j]:
                self.arr1[i], self.arr2[j] = self.arr2[j], self.arr1[i]
            i -= 1
            j += 1
        
        self.arr1.sort()
        self.arr2.sort()
        
        return self.arr1, self.arr2
 
    
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

obj = Merge(arr1, arr2)
ans1, ans2 = obj.merge_sort()
print(ans1)
print(ans2)
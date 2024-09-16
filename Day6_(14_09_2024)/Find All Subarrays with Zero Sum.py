"""
You are given an integer array arr of size n. 
Your task is to find all the subarrays whose elements sum up to zero.
A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

Input:
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output:
Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. 
The ending index (0-based) of the subarray.
The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.

Example
Output: [(0, 2), (2, 3)]

"""

class SubArraySum0:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def find_subarray(self):
        map = {}
        cum_sum = 0
        ans = []

        for i in range(len(arr)):
            cum_sum += arr[i]

            if cum_sum == 0:
                ans.append((0, i))

            if cum_sum in map:
                for j in map[cum_sum]:
                    ans.append((j + 1, i))

            if cum_sum in map:
                map[cum_sum].append(i)
            else:
                map[cum_sum] = [i]

        return ans

    
arr = [1, 2, -3, 3, -1, 2]

obj = SubArraySum0(arr)
ans = obj.find_subarray()
print(ans)

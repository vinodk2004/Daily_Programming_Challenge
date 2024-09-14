"""
You are given an integer array arr of size n.
An element is considered a leader if it is greater than all the elements to its right.
Your task is to find all such leader elements in the array.

Input:
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output:
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]

"""

class Leader:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
        self.ans = []
    
    def find_leader(self):
        for i in range(self.n):
            flag = True
            
            for j in range(i+1, self.n):
                if self.arr[i] < self.arr[j]:
                    flag = False
                    break
                
            if flag:
                self.ans.append(self.arr[i])
                
        return self.ans
                
    
arr = [16, 17, 4, 3, 5, 2]

obj = Leader(arr)
ans = obj.find_leader()
print(ans)
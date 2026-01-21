class Solution:
    def getAlternates(self, arr):
        for i in range(0, len(arr), 2):
            print(arr[i], end = '')
sol = Solution()
li =  input("Enter elements: ").split()
sol.getAlternates(li)          
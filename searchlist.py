class Search:
    def search_list(self, lst, value):
        for i, item in enumerate(lst):
            if item == value:
                return i
        return -1
sol = Search()
lst = [10, 20, 30, 40, 50]
print(sol.search_list(lst, 30))


# class Solution:
#     def search(self, arr, x):
#            if x in arr:
#                return arr.index(x)
#            else:
#                 return -1
            
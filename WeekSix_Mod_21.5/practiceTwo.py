# Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
            #   [ 0    1   2   3  4  5  6  7 ]
# Output : [[-10, 2, 8], [-7, -3, 10]]


class FindThreeElemSumToZero:
    def __init__(self,nums:list) -> None:
        self.nums = nums

    def threeSumToZero(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                for k in range(j+1,len(self.nums)):
                    tESum = self.nums[i]+self.nums[j]+self.nums[k]
                    if tESum == 0:
                        result.append([self.nums[i],self.nums[j],self.nums[k]])
        return result
    

lst = [-25, -10, -7, -3, 2, 4, 8, 10]
res = FindThreeElemSumToZero(lst).threeSumToZero()
print(res)
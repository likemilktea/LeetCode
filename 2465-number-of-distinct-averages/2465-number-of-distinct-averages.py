class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgList=[]
        nums.sort()
        print(nums)
        while(len(nums)!=0):
            num1=nums.pop(0)
            num2=nums.pop(-1)
            avgList.append((num1+num2)/2)
            print(num1,num2)
        print(avgList)
        return len(set(avgList))
        
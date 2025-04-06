class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        longest=0
        numb=set(nums)
        for num in numb:
            l=dic.get(num-1,0)
            r=dic.get(num+1,0)
            curr_len=l+r+1
            dic[num-l]=curr_len
            dic[num+r]=curr_len
            longest=max(longest,curr_len)
        return longest

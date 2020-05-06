class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        majorityEle = len(nums)//2
        frequency_dict = {}
        for i in nums:
            if i in frequency_dict:
                frequency_dict[i] += 1
            else:
                frequency_dict[i] = 1
        
        for key,value in frequency_dict.items():
            if(value > majorityEle):
                return key
            
        

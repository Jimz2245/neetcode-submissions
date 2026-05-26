class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix #sets each value in res to the prefix of itself
            prefix *= nums[i] #increments prefix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #goes from end to beginning
                       #start, stop, step
            res[i] *= postfix #increments each idx by its postfix
            postfix *= nums[i] #increments postfix
        return res


        
            
            
                

            



        
            

        
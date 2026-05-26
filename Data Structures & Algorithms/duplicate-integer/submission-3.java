class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        boolean dups = false;
        for(int i = 0; i<nums.length - 1; i++)
        {
            for(int j = i + 1; j<nums.length; j++)
            {
                if(nums[i] == nums[j])
                {
                    dups = true;
                }
            }
        }
        return dups;
    }
}
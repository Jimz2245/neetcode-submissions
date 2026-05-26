class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        if(nums.length <2)
        {
            return false;
        }
        Arrays.sort(nums);
        int previous = nums[0];
        for(int i = 1; i< nums.length; i++)
        {
            if(previous == nums[i])
            {
                return true;
            }
            previous = nums[i];
        }
        return false;
    }
}
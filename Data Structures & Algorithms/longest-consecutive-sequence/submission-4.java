class Solution 
{
    public int longestConsecutive(int[] nums) 
    {
        if(nums.length < 2)
        {
            return nums.length;
        }
        int len = 1;
        int maxLen = 1;
        Arrays.sort(nums);
        int previous = nums[0];
        for(int i =1; i<nums.length ; i++)
        {
            if(nums[i] == previous)
            {
                continue;
            }
            if(nums[i] == (previous+1))
            {
                len++;
            }
            else
            {
                len = 1;
            }
            previous = nums[i];
            maxLen = Math.max(maxLen, len);

        }
        return maxLen;

    }
}

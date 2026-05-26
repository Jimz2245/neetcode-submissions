class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        for(int i = 0; i<nums.length - 1; i++)
        {
            int a = nums[i];
            for(int j = i + 1 ; j< nums.length; j++)
            {
                int b = nums[j];
                if(a + b == target)
                {
                    int[] solution = {i, j};
                    return solution;
                }
            }
        }
        int[] solution = {0, 0};
        return solution;
    }
}

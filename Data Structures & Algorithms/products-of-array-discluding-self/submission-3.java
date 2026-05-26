class Solution {
    public int[] productExceptSelf(int[] nums) 
    {
        int[] products = new int[nums.length];
        
        Arrays.fill(products, 1);

        int curr = 1;

        for(int i = 0; i<nums.length; i++)
        {
            products[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;

        for(int i = nums.length-1; i>=0; i--)
        {
            products[i] *= curr;
            curr *= nums[i];
        }

        return products;
        
    }
}  

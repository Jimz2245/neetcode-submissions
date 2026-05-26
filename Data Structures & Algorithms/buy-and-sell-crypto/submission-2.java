class Solution
{
    public int maxProfit(int[] prices) 
    {
        int profit = 0;
        int previous = 0;
        for(int i = prices.length - 1; i>0; i--)
        {
            int sell = prices[i];
            if(sell > previous)
            {
                previous = sell;
                for(int j = i - 1; j>=0; j--)
                {
                    int buy = prices[j];
                    if(sell - buy > profit)
                    {
                        profit = sell - buy;
                    }
                }
            }
        }
        return profit;
    }
}
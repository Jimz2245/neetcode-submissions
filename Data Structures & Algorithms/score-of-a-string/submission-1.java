class Solution 
{
    public int scoreOfString(String s) 
    {
        char[] chars = s.toCharArray();

        int previous = chars[0];
        int sum =  0;

        for(int i = 1; i < chars.length; i++)
        {
            sum += Math.abs(chars[i] - previous);
            previous = chars[i];
        }
        return sum;
    }
}
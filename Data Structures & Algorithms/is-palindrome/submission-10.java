class Solution 
{
    public boolean isPalindrome(String s) 
    {
        boolean pal = true;
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        String temp = "";
        for(int i = 0; i<s.length(); i++)
        {
            String a = s.substring(i, i+1);
            if(!(a.equals(" ")))
            {
                temp += a;
                System.out.println(temp);
            }
        }
        for(int j = 0; j< temp.length()/2; j++)
        {
            if(temp.charAt(j) != temp.charAt(temp.length() - 1 - j))
            {
                pal = false;
            }
        }
        return pal;
    }
}

public class Solution 
{
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        Map<String, List<String>> res = new HashMap<>(); //Hashmap to store arrays, key will be sorted Strings
        for (String s : strs) //goes through each string in the array
        {
            char[] charArray = s.toCharArray(); 
            Arrays.sort(charArray);
            String sortedS = new String(charArray); //makes the key for the string (sortedS)
            res.putIfAbsent(sortedS, new ArrayList<>()); //if the key doesnt exist, it makes a new arraylist
            res.get(sortedS).add(s); //adds the original String to the key array (sortedS)
        }
        return new ArrayList<>(res.values());
    }
}

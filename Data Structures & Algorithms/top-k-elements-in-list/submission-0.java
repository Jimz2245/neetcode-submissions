public class Solution 
{
    public int[] topKFrequent(int[] nums, int k) 
    {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) 
        {
            count.put(num, count.getOrDefault(num, 0) + 1);
            //puts the number and its count into the hashmap (key, value)
            //count.getOrDefault(num, 0) + 1) if num(key) exists in 
            //the map already we add a number to that value, if not
            //we return 0 and add 1 to it (updates the count for the number)
        }

        List<int[]> arr = new ArrayList<>(); //makes arraylist of integer arrays
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) 
        {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
            //adds a new int array for every hashmap entry [value, num], [count, number]
        }
        arr.sort((a, b) -> b[0] - a[0]);
        //looks at the frequency of 2 elements in the arraylist
        //b[0] - a[0] sorts by greater numbers, most freq. first]

        int[] res = new int[k];
        //makes array to get the k most freq numbers
        for (int i = 0; i < k; i++) 
        {
            res[i] = arr.get(i)[1];
            //puts the number only into the array, not its count
        }
        return res;
    }
}

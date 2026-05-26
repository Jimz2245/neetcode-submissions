public class Solution {

    public String encode(List<String> strs) {
        if (strs.isEmpty()) return ""; 
        StringBuilder res = new StringBuilder(); 
        List<Integer> sizes = new ArrayList<>(); //ArrayList to hold string length
        for (String str : strs) {
            sizes.add(str.length()); //add string lengths to sizes
        }
        for (int size : sizes) {
            res.append(size).append(','); //adds the size with a comma
        }
        res.append('#');
        for (String str : strs) {
            res.append(str);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        if (str.length() == 0) {
            return new ArrayList<>();
        }
        List<String> res = new ArrayList<>();
        List<Integer> sizes = new ArrayList<>();
        int i = 0;
        while (str.charAt(i) != '#') {
            StringBuilder cur = new StringBuilder();
            while (str.charAt(i) != ',') {
                cur.append(str.charAt(i));
                i++;
            }
            sizes.add(Integer.parseInt(cur.toString()));
            i++;
        }
        i++;
        for (int sz : sizes) {
            res.add(str.substring(i, i + sz));
            i += sz;
        }
        return res;
    }
}

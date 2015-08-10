public class Solution {

    public int compareVersion(String version1, String version2) {
    	int temp1 = 0, temp2 =0; 
    	int len1 = version1.length();
    	int len2 = version2.length();
    	int i = 0, j = 0;

    	while (i < len1 || j < len2) {
    		temp1 = 0;
    		temp2 = 0;

    		while (i < len1 && version1.charAt(i) != '.') {
    			temp1 = temp1 * 10 + version1.charAt(i++)-'0';
    		}
    		while (j < len2 && version2.charAt(j) != '.') {
    			temp2 = temp2 * 10 + version2.charAt(j++)-'0';
    		}

    		if (temp1 > temp2) {
    			return 1;
    		} else if (temp1 < temp2) {
    			return -1;
    		} else {
    			i++;
    			j++;
    		}
    	}
    	return 0;
    }

    public static void main(String[] args) {
    	String v1 = "1";
    	String v2 = "0";
    	Solution sol = new Solution();
    	int rs = sol.compareVersion(v1, v2);
    	System.out.println(rs);
    }
}
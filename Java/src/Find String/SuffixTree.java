import java.util.*;

public class SuffixTree {
	SuffixTreeNode root = new SuffixTreeNode();

	public SuffixTree(String s) {
		// insert to form a tree
		for (int i = 0; i < s.length(); i++) {
			String suffix = s.substring(i);
			root.insertString(suffix, i);
		}
	}

	// get the indexes of string, starting from root
	public ArrayList<Integer> getIndexes(String s) {
		return root.getIndexes(s);
	}
}